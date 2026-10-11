"""Recompute every score reported in the paper from the ratings workbook.

Usage:
    python3 evaluation_tools/reproduce_scores.py ["Mobile App Accessibility Evaluation.xlsx"]

Reads the Status (column F) and Relevance weight (column E) of each app tab and the
Transactions tabs, then prints:
  - Table "Scores per app": rated / Not Tested, Fail count, WCAG score, band, Level A %,
    Level AA %, transaction score (checks scored)
  - Table "Weighted and unweighted scores"
  - Table "Score bounds" (every Not Tested criterion passes / fails)
  - Table "Scanner-only scores" (criteria resting on the screenshot review alone left out)
  - BK Mobile's score with both authentication criteria treated as Not Tested
  - Table "Recurring barriers" (status and scanner instances), criteria Not Tested in all
    five apps, and Table "Transaction-level checks"
Standard library only - the .xlsx is read as a zip of XML files.
"""
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

APPS = ['BK Mobile', 'Equity Mobile RW', 'Fidelity NG', 'GTWorld NG', 'AccessMore NG']
STATUS = {'Pass': 1.0, 'Partial': 0.5, 'Fail': 0.0}

# The workbook numbers three WCAG 2.2 criteria one place off; names and levels are right.
# Map workbook number -> WCAG 2.2 number, so output matches the paper.
RENUMBER = {'3.3.9': '3.3.7', '3.3.7': '3.3.8', '3.3.8': '3.3.9'}

# Criteria rated from the screenshot review alone (WCAG 2.2 numbering), left out of the
# scanner-only score. 3.3.8 and 3.3.9 are the two Accessible Authentication criteria
# (workbook rows 3.3.7 and 3.3.8).
SCREENSHOT_ONLY = {'1.3.3', '2.4.6', '2.5.1', '3.3.4', '3.3.8', '3.3.9'}

# Rows of the paper's recurring-barriers table
RECURRING = ['1.1.1', '4.1.2', '2.4.4', '3.3.2', '3.3.1', '3.3.8', '3.3.4', '1.4.3', '1.4.11', '2.5.8', '2.5.5']

NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
REL = '{http://schemas.openxmlformats.org/package/2006/relationships}'


def read_sheets(path):
    """Return {sheet name: {cell ref: value}} with formulas' cached values ignored."""
    z = zipfile.ZipFile(path)
    shared = []
    if 'xl/sharedStrings.xml' in z.namelist():
        for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si', NS):
            shared.append(''.join(t.text or '' for t in si.iter('{%s}t' % NS['m'])))
    rels = {r.get('Id'): r.get('Target') for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels')).iter(REL + 'Relationship')}
    sheets = {}
    for s in ET.fromstring(z.read('xl/workbook.xml')).iter('{%s}sheet' % NS['m']):
        target = rels[s.get('{%s}id' % NS['r'])].lstrip('/')
        target = target if target.startswith('xl/') else 'xl/' + target
        cells = {}
        for c in ET.fromstring(z.read(target)).iter('{%s}c' % NS['m']):
            if c.find('m:f', NS) is not None:
                continue
            inline, v = c.find('m:is', NS), c.find('m:v', NS)
            if inline is not None:
                cells[c.get('r')] = ''.join(t.text or '' for t in inline.iter('{%s}t' % NS['m']))
            elif v is not None:
                cells[c.get('r')] = shared[int(v.text)] if c.get('t') == 's' else v.text
        sheets[s.get('name')] = cells
    return sheets


def wcag_rows(cells):
    rows = []
    for r in range(5, 40):
        sc = cells.get(f'A{r}')
        if not sc or not re.match(r'^\d\.\d+\.\d+$', sc):
            continue
        rows.append(dict(sc=RENUMBER.get(sc, sc), level=cells.get(f'C{r}'),
                         weight=float(cells.get(f'E{r}') or 0), status=cells.get(f'F{r}'),
                         inst=cells.get(f'I{r}')))
    return rows


def score(rows, levels=('A', 'AA', 'AAA'), weighted=True, fill=None, skip=()):
    """Weighted score over rated rows. fill = value given to Not Tested rows (bounds)."""
    num = den = 0.0
    for x in rows:
        if x['level'] not in levels or x['sc'] in skip or x['status'] == 'N/A':
            continue
        s = STATUS.get(x['status'], fill if x['status'] == 'Not Tested' else None)
        if s is None:
            continue
        w = x['weight'] if weighted else 1.0
        num += w * s
        den += w
    return 100 * num / den if den else 0.0


def band(x):
    return ('Level AA-aligned' if x >= 90 else 'Substantially accessible' if x >= 75 else
            'Partially accessible' if x >= 50 else 'Largely inaccessible' if x >= 25 else 'Inaccessible')


def main(path):
    sheets = read_sheets(path)
    print(f'{"App":18} {"Rated/NT":>9} {"Fail":>5} {"WCAG":>6}  {"Band":22} {"A %":>6} {"AA %":>6}  Txn (scored)')
    data = {}
    for app in APPS:
        rows = wcag_rows(sheets[app])
        tx = sheets[app + ' - Transactions']
        checks = [(float(tx.get(f'D{r}') or 0), tx.get(f'E{r}')) for r in range(5, 17)]
        scored = [(w, STATUS[s]) for w, s in checks if s in STATUS]
        txn = 100 * sum(w * s for w, s in scored) / sum(w for w, _ in scored) if scored else 0.0
        rated = sum(x['status'] in STATUS for x in rows)
        nt = sum(x['status'] == 'Not Tested' for x in rows)
        fails = sum(x['status'] == 'Fail' for x in rows)
        w = score(rows)
        data[app] = (rows, w, nt)
        print(f'{app:18} {f"{rated}/{nt}":>9} {fails:>5} {w:6.1f}  {band(w):22} {score(rows, ("A",)):6.1f} '
              f'{score(rows, ("A", "AA")):6.1f}  {txn:5.1f} ({len(scored)})')

    print(f'\n{"App":18} {"Weighted":>9} {"Unweighted":>11}')
    for app, (rows, w, _) in data.items():
        print(f'{app:18} {w:9.1f} {score(rows, weighted=False):11.1f}')

    print(f'\n{"App":18} {"Observed":>9} {"Worst":>7} {"Best":>7} {"Not Tested":>11}')
    for app, (rows, w, nt) in data.items():
        print(f'{app:18} {w:9.1f} {score(rows, fill=0.0):7.1f} {score(rows, fill=1.0):7.1f} {nt:11}')

    print(f'\n{"App":18} {"Reported":>9} {"Scanner-only":>13} {"Rated (all, scanner-only)":>27}')
    for app, (rows, w, _) in data.items():
        rated = sum(x['status'] in STATUS for x in rows)
        kept = sum(x['status'] in STATUS and x['sc'] not in SCREENSHOT_ONLY for x in rows)
        print(f'{app:18} {w:9.1f} {score(rows, skip=SCREENSHOT_ONLY):13.1f} {f"{rated}, {kept}":>27}')

    # BK Mobile with both Accessible Authentication criteria treated as Not Tested
    bk = [dict(x, status='Not Tested') if x['sc'] in ('3.3.8', '3.3.9') else x for x in data['BK Mobile'][0]]
    print(f'\nBK Mobile with 3.3.8 and 3.3.9 treated as Not Tested: {score(bk):.1f}')

    # Recurring barriers: status (instances) per criterion and app
    short = {a: a.split()[0] for a in APPS}
    print(f'\n{"Criterion":8} ' + ' '.join(f'{short[a]:>16}' for a in APPS))
    for sc in RECURRING:
        cells = []
        for app in APPS:
            x = next(r for r in data[app][0] if r['sc'] == sc)
            cells.append(f'{x["status"]}' + (f' ({x["inst"]})' if x['inst'] not in (None, '', '-') else ''))
        print(f'{sc:8} ' + ' '.join(f'{c:>16}' for c in cells))

    never = [x['sc'] for x in data['BK Mobile'][0]
             if all(next(r for r in data[a][0] if r['sc'] == x['sc'])['status'] == 'Not Tested' for a in APPS)]
    print(f'\nNot Tested in all five apps ({len(never)}): {", ".join(sorted(never, key=lambda s: [int(p) for p in s.split(".")]))}')

    # Transaction checks per app
    print(f'\n{"Check":6} ' + ' '.join(f'{short[a]:>11}' for a in APPS))
    for i, ref in enumerate([f'T{n}' for n in range(1, 13)]):
        print(f'{ref:6} ' + ' '.join(f'{sheets[a + " - Transactions"].get(f"E{5 + i}", ""):>11}' for a in APPS))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else "data/Mobile App Accessibility Evaluation.xlsx")
