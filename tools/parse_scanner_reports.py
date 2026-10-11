"""Tally Google Accessibility Scanner findings for one app (Methodology, Section 8, Step 2).

Usage:
    python3 parse_scanner_reports.py "<session folder or .zip>" ["<another session>" ...]

Each session is an exported results_<App>_<timestamp> folder (or its .zip) containing
reportN.txt / screenN.png pairs. All sessions passed are pooled into one app total.
Standard library only - no installs needed.
"""
import collections
import glob
import os
import re
import sys
import tempfile
import zipfile

# Scanner category -> scorecard success criteria it feeds
SC_MAP = {
    'Item label': '1.1.1, 2.4.4, 4.1.2',
    'Unexposed Text': '1.1.1, 2.5.3',
    'Clickable items': '4.1.2, 1.3.1',
    'Item descriptions': '4.1.2, 1.3.1',
    'Text contrast': '1.4.3',
    'Image contrast': '1.4.11',
    'Touch target': '2.5.8, 2.5.5',
    'Text Scaling': '1.4.4',
    'Unsupported item type': '4.1.2',
    'Item type label': '4.1.2',  # label repeats the role (e.g. "... button")
}


def session_dirs(paths):
    for p in paths:
        if p.endswith('.zip'):
            out = tempfile.mkdtemp(prefix='scan_')
            zipfile.ZipFile(p).extractall(out)
            yield from {os.path.dirname(f) for f in glob.glob(out + '/**/report*.txt', recursive=True)}
        else:
            yield p


def report_number(path):
    return int(re.findall(r'\d+', os.path.basename(path))[0])


def parse(dirs):
    items, screens, seen = [], 0, set()
    for d in dirs:
        reports = sorted(glob.glob(os.path.join(d, 'report*.txt')), key=report_number)
        screens += len(reports)
        for f in reports:
            txt = open(f, encoding='utf-8', errors='ignore').read()
            seen.add(txt)
            blocks = [b.strip().split('\n') for b in re.split(r'\n\s*\n', txt) if b.strip()]
            for b in blocks[1:]:  # block 0 is the report preamble
                items.append(dict(screen=f'{os.path.basename(d)}/{os.path.basename(f)}',
                                  cat=b[0].strip(),
                                  el=b[1].strip() if len(b) > 1 else '',
                                  msg=' '.join(b[2:])))
    return items, screens, len(seen)


def target_size(msg):
    """Smallest dimension (dp) of a touch-target finding, or None."""
    m = re.search(r"size is (\d+)dp x (\d+)dp", msg)
    if m:
        return min(int(m.group(1)), int(m.group(2)))
    m = re.search(r"(?:height|width) is (\d+)dp", msg)
    return int(m.group(1)) if m else None


def main(paths):
    items, screens, unique = parse(list(session_dirs(paths)))
    counts = collections.Counter(i['cat'] for i in items)
    print(f'Screens: {screens}   Findings: {len(items)}')
    if unique < screens:
        print(f'  NOTE: only {unique} of {screens} reports are unique - the same screen was captured more than once,')
        print('  so the counts below include repeats of the same finding.')
    print()
    print(f'{"Category":20} {"Count":>6}  Feeds SC')
    for cat, n in counts.most_common():
        print(f'{cat:20} {n:>6}  {SC_MAP.get(cat, "(review manually)")}')

    sizes = [s for s in (target_size(i['msg']) for i in items if i['cat'] == 'Touch target') if s is not None]
    if sizes:
        web = sum('web content' in i['msg'] for i in items if i['cat'] == 'Touch target')
        print(f'\nTouch targets: <24dp {sum(s < 24 for s in sizes)} | 24-43dp {sum(24 <= s < 44 for s in sizes)} '
              f'| 44dp+ {sum(s >= 44 for s in sizes)} | share <24dp {100 * sum(s < 24 for s in sizes) / len(sizes):.0f}%'
              f' | from web content {web}')
        if web == len(sizes):
            print('  NOTE: all findings are web content - label checks (1.1.1/2.4.4/4.1.2) are likely not evaluable.')

    for cat in ('Text contrast', 'Image contrast'):
        ratios, pairs = [], collections.Counter()
        for i in items:
            if i['cat'] != cat:
                continue
            m = re.search(r"contrast ratio is ([\d.]+?)\.?(?:\s|$)", i['msg'])
            if m:
                ratios.append(float(m.group(1)))
            cols = re.findall(r"#[0-9A-Fa-f]{6}", i['msg'])
            if len(cols) >= 2:
                pairs[f'{cols[0]} on {cols[1]}'] += 1
        if ratios:
            print(f'\n{cat}: lowest {min(ratios)}:1 | <3:1 {sum(r < 3 for r in ratios)} | <2:1 {sum(r < 2 for r in ratios)}')
            print('  most frequent colour pairs: ' + '; '.join(f'{p} ({n})' for p, n in pairs.most_common(4)))

    for cat in ('Item label', 'Unexposed Text', 'Item descriptions', 'Clickable items'):
        els = collections.Counter(i['el'] for i in items if i['cat'] == cat)
        if els:
            print(f'\n{cat} - most frequent elements:')
            for el, n in els.most_common(10):
                print(f'  {n:>3}  {el}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
