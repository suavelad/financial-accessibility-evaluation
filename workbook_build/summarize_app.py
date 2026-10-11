
import sys,re,collections,glob,os
sys.path.insert(0,os.path.dirname(__file__))
from parse import parse
dirs=sys.argv[1:]
it=parse(dirs)
print('SCREENS',sum(len(glob.glob(d+'/report*.txt')) for d in dirs),'ITEMS',len(it))
print(collections.Counter(i['cat'] for i in it))
dims=[]
web=0
for i in it:
    if i['cat']!='Touch target': continue
    m=i['msg']
    if 'web content' in m: web+=1
    a=re.search(r"size is (\d+)dp x (\d+)dp",m); h=re.search(r"height is (\d+)dp",m); w=re.search(r"width is (\d+)dp",m)
    if a: dims.append(min(int(a.group(1)),int(a.group(2))))
    elif h: dims.append(int(h.group(1)))
    elif w: dims.append(int(w.group(1)))
print('TT n',len(dims),'webcontent',web,'<24:',sum(d<24 for d in dims),'24-43:',sum(24<=d<44 for d in dims),'>=44:',sum(d>=44 for d in dims), collections.Counter(dims).most_common(12))
for cat in ['Text contrast','Image contrast']:
    rs=[];cols=collections.Counter()
    for i in it:
        if i['cat']!=cat: continue
        m=re.search(r"contrast ratio is ([\d.]+?)\.?(?:\s|$)",i['msg'])
        if m: rs.append(float(m.group(1)))
        c=re.findall(r"#[0-9A-Fa-f]{6}",i['msg']); 
        if c: cols[tuple(c[:2])]+=1
    if rs: print(cat,'n',len(rs),'min',min(rs),'<3:',sum(r<3 for r in rs),'<2:',sum(r<2 for r in rs),'lowest',sorted(rs)[:6],'top colours',cols.most_common(4))
lab=collections.Counter(i['el'] for i in it if i['cat']=='Item label')
print('LABEL els',lab.most_common(25))
for c in ['Unexposed Text','Clickable items','Item descriptions','Text scaling','Traversal order','Clickable links','Editable item label']:
    xs=[i for i in it if i['cat']==c]
    if xs:
        print('==',c,len(xs))
        for x in xs[:40]: print('  ',x['file'],'|',x['el'][:50],'|',x['msg'][:160])
others=set(i['cat'] for i in it)-{'Touch target','Item label','Text contrast','Image contrast','Unexposed Text','Clickable items','Item descriptions'}
for c in others:
    xs=[i for i in it if i['cat']==c]; print('== OTHER',c,len(xs))
    for x in xs[:15]: print('  ',x['file'],'|',x['el'][:50],'|',x['msg'][:200])
