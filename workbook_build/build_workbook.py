# Copies the BK Mobile tabs as a template, writes ratings.py into new app tabs, and adds dashboard rows.
# Paths below are those used at the time; the project folder was then 'Digital accessiblity'.

import sys,copy,openpyxl
sys.path.insert(0,sys.argv[1])
from ratings import APPS, NT
from openpyxl.worksheet.datavalidation import DataValidation
F=sys.argv[2]
wb=openpyxl.load_workbook(F)
bk=wb['BK Mobile']; bkt=wb['BK Mobile - Transactions']
GENERIC='No fix to prescribe yet - conduct the manual test first to confirm actual status.'
extra_txn={
 'GTWorld NG':{'T7':('Not Tested',"No login screen captured; biometric option not observed.",NT),
               'T8':('Not Tested',"No fraud-alert, dispute or help path observed in the captured screens.",NT)},
}
region={'Equity Mobile RW':"Out of scope for this app-only scan. Material gap for East Africa: much mobile money usage is USSD/agent-based, not app-based, and this scorecard has not evaluated that channel at all.",
        'default':"Out of scope for this app-only scan. USSD banking is widely used in Nigeria, and this scorecard has not evaluated that channel at all."}
for name in APPS:
    for s in [name, name+' - Transactions']:
        if s in wb.sheetnames: del wb[s]
order=[]
for name,a in APPS.items():
    ws=wb.copy_worksheet(bk); ws.title=name
    ws['A1']='Accessibility Scorecard — '+a['title']
    seen=set()
    for r in range(5,40):
        sc=ws.cell(r,1).value
        if sc in a['wcag']:
            st,notes,inst,rec=a['wcag'][sc]; seen.add(sc)
            ws.cell(r,6).value=st; ws.cell(r,8).value=notes; ws.cell(r,9).value=inst; ws.cell(r,13).value=rec
        else:
            if bk.cell(r,6).value not in ('Not Tested','N/A'):
                raise SystemExit(f'{name}: scored BK row {sc} not overridden')
    assert seen==set(a['wcag']), (name,set(a['wcag'])-seen)
    ws.freeze_panes='A5'
    dv=DataValidation(type='list',formula1='"Pass,Partial,Fail,Not Tested,N/A"',allow_blank=True); ws.add_data_validation(dv); dv.add('F5:F39')
    wt=wb.copy_worksheet(bkt); wt.title=name+' - Transactions'
    wt['A1']='Financial Transaction Accessibility (Supplemental) '+a['title']
    txn=dict(a['txn']); txn.update(extra_txn.get(name,{}))
    txn.setdefault('T4',('Not Tested',"No statement or receipt export was captured in this session.",NT))
    txn['T6']=('Not Tested',region.get(name,region['default']),NT)
    for r in range(5,17):
        ref=wt.cell(r,1).value
        if ref in txn:
            st,notes,rec=txn[ref]
            wt.cell(r,5).value=st; wt.cell(r,7).value=notes; wt.cell(r,10).value=rec if rec else GENERIC
        elif ref not in ('T2','T3','T10'):
            raise SystemExit(f'{name}: {ref} would inherit BK-specific text')
    wt.freeze_panes='A5'
    dv=DataValidation(type='list',formula1='"Pass,Partial,Fail,Not Tested,N/A"',allow_blank=True); wt.add_data_validation(dv); dv.add('E5:E16')
    order+= [ws,wt]
# sheet order: after BK tabs, before App Template
sh=[s for s in wb._sheets if s not in order]
i=sh.index(wb['BK Mobile - Transactions'])+1
wb._sheets=sh[:i]+order+sh[i:]
# dashboard
d=wb['Comparison Dashboard']
for k,(name,a) in enumerate(APPS.items()):
    r=6+k; src=5 if r%2==1 else 6
    for c in range(1,10):
        cell=d.cell(r,c); s=d.cell(src,c) if src==5 else d.cell(6,c)
        ref=d.cell(5,c)
        cell.font=copy.copy(ref.font); cell.alignment=copy.copy(ref.alignment); cell.border=copy.copy(ref.border); cell.number_format=ref.number_format
        cell.fill=copy.copy(d.cell(5 if r%2==1 else 6,c).fill)
    q=f"'{name}'"; t=f"'{name} - Transactions'"
    vals=[a['title'],f"={q}!$E$44",f"={q}!$E$49",f"={q}!$E$45",f"={q}!$E$46",f"={t}!$D$21",f"={q}!$E$47",f"={q}!$E$48+{t}!$D$22",a['dash_note']]
    for c,v in enumerate(vals,1): d.cell(r,c).value=v
    d.row_dimensions[r].height=d.row_dimensions[5].height
d['A11']="Comparability caveat: scores reflect only the screens each scan captured, and differ in coverage (e.g. no login screen for GTWorld / AccessMore; no confirm step for Equity / Fidelity). Fidelity's WebView defeated automated label checks, so its WCAG score excludes 1.1.1 / 2.4.4 / 2.5.3 / 4.1.2 and is not directly comparable until manually audited."
d['A11'].alignment=openpyxl.styles.Alignment(wrap_text=True,vertical='top')
wb.calculation.fullCalcOnLoad=True
wb.save(F); print('saved',wb.sheetnames)
