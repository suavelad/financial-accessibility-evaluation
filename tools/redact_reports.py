"""Make a shareable copy of scanner reports: text reports only, personal data removed.

Usage:
    python3 evaluation_tools/redact_reports.py <out_dir> --name "First Last" [--name ...] \
        -- "<session folder or .zip>" ["<another session>" ...]

Copies every reportN.txt (never the screenshots) into <out_dir>/<session name>/ and replaces
  - each --name given (case-insensitive) with [NAME]
  - every run of 8 or more digits (account numbers, BVNs, phone numbers) with [NUMBER]
  - the last four digits of an account shown as "From 1234" or "From •1234" with [NUMBER]
Finding blocks, categories and line breaks are untouched, so parse_scanner_reports.py gives
the same counts on the redacted copy as on the original.
Standard library only.
"""
import glob
import os
import re
import sys
import tempfile
import zipfile


def session_dirs(paths):
    for p in paths:
        if p.endswith('.zip'):
            out = tempfile.mkdtemp(prefix='scan_')
            zipfile.ZipFile(p).extractall(out)
            for d in sorted({os.path.dirname(f) for f in glob.glob(out + '/**/report*.txt', recursive=True)}):
                yield d, os.path.basename(p)[:-4]
        else:
            yield p, os.path.basename(p.rstrip('/'))


def main(argv):
    if '--' not in argv or len(argv) < 3:
        sys.exit(__doc__)
    split = argv.index('--')
    opts, sessions = argv[:split], argv[split + 1:]
    out_dir, names = opts[0], [opts[i + 1] for i, a in enumerate(opts) if a == '--name']
    patterns = [(re.compile(re.escape(n), re.I), '[NAME]') for n in names]
    patterns.append((re.compile(r'\d{8,}'), '[NUMBER]'))
    patterns.append((re.compile(r'(From\s*\W?)\d{4}\b'), r'\1[NUMBER]'))  # masked account ending
    total = changed = 0
    for src, label in session_dirs(sessions):
        dest = os.path.join(out_dir, label.replace(':', '-'))
        os.makedirs(dest, exist_ok=True)
        for f in glob.glob(os.path.join(src, 'report*.txt')):
            txt = open(f, encoding='utf-8', errors='ignore').read()
            new = txt
            for pat, repl in patterns:
                new = pat.sub(repl, new)
            total += 1
            changed += new != txt
            open(os.path.join(dest, os.path.basename(f)), 'w', encoding='utf-8').write(new)
    print(f'{total} reports copied to {out_dir}, {changed} redacted')


if __name__ == '__main__':
    main(sys.argv[1:])
