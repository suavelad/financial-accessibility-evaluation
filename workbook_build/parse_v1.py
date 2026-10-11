
import sys,glob,re,os,collections,json
def parse(dirs):
    items=[]
    for d in dirs:
        for f in sorted(glob.glob(os.path.join(d,'report*.txt')), key=lambda x:int(re.findall(r'\d+',os.path.basename(x))[0])):
            txt=open(f,encoding='utf-8',errors='ignore').read()
            blocks=[b.strip().split('\n') for b in re.split(r'\n\s*\n',txt) if b.strip()]
            for b in blocks[1:]:
                items.append(dict(file=os.path.basename(d)+'/'+os.path.basename(f),cat=b[0].strip(),el=b[1].strip() if len(b)>1 else '',msg=' '.join(b[2:])))
    return items
if __name__=='__main__':
    dirs=sys.argv[1:]
    it=parse(dirs)
    nrep=sum(len(glob.glob(os.path.join(d,'report*.txt'))) for d in dirs)
    print('screens',nrep,'items',len(it))
    c=collections.Counter(i['cat'] for i in it); print(c)
    # subcategories
    sub=collections.Counter()
    for i in it:
        m=i['msg']
        if i['cat']=='Item label':
            k='label:'+('text-detected' if 'text' in m.lower() and 'detected' in m.lower() else m[:70])
        elif i['cat']=='Touch target':
            k='tt'
        else: k=i['cat']+':'+m[:60]
        sub[k]+=1
    for k,v in sub.most_common(): print(v,k)
    # touch target sizes
    sizes=[]
    for i in it:
        if i['cat']=='Touch target':
            m=re.search(r"size is (\d+)dp x (\d+)dp",i['msg'])
            if m: sizes.append((int(m.group(1)),int(m.group(2))))
    below24=sum(1 for w,h in sizes if min(w,h)<24); below44=sum(1 for w,h in sizes if min(w,h)<44)
    print('tt sizes',len(sizes),'min<24:',below24,'min<44:',below44, 'mins', sorted(set(min(s) for s in sizes))[:15])
    tr=[];ir=[]
    for i in it:
        m=re.search(r"contrast ratio is ([\d.]+)",i['msg'])
        if m:
            (tr if i['cat']=='Text contrast' else ir).append(float(m.group(1)))
    if tr: print('text contrast n',len(tr),'min',min(tr),'lowest',sorted(tr)[:8], 'lt3', sum(r<3 for r in tr))
    if ir: print('image contrast n',len(ir),'min',min(ir),sorted(ir)[:8])
    json.dump(it,open(os.environ.get('OUT','/dev/null'),'w'),indent=0)
