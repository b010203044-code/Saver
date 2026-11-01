import os, re, html
OUT=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(OUT,'gen.py'),encoding='utf-8').read()
ns={'__file__':os.path.join(OUT,'gen.py')}
exec(src.split('e = html.escape')[0],ns)
data=ns['data']; e=html.escape
H=lambda t,css:f'<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{t}</title><style>{css}</style></head><body>'
font='font-family:"PingFang TC","Noto Sans TC","Microsoft JhengHei",sans-serif'

# 1 大字版 A4 / A5（一頁一分類，超過自動換頁）
for size,pt in (("A4",60),("A5",40)):
    css=f'''@page{{size:{size};margin:12mm}}*{{box-sizing:border-box}}body{{margin:0;background:#fff;color:#000;{font}}}
section{{page-break-after:always;padding:4mm}}h2{{font-size:14pt;color:#c2410c;margin:0 0 8mm}}
.w{{display:flex;flex-wrap:wrap;gap:4mm 10mm}}.w span{{font-size:{pt}pt;font-weight:700;line-height:1.25;white-space:nowrap}}
@media screen{{section{{border-bottom:1px dashed #aaa;margin-bottom:8px}}body{{padding:8px}}}}'''
    o=H(f"POP 大字版 {size}",css)
    for t,ws in data:
        o+=f'<section><h2>{e(t)}</h2><div class="w">'+''.join(f'<span>{e(w)}</span>' for w in ws)+'</div></section>'
    open(os.path.join(OUT,f'POP大字版_{size}.html'),'w',encoding='utf-8').write(o+'</body></html>')

# 2 貨架價格卡：A4 直式，8 張 (A7 橫式 105x74mm)，可改 CSS 變數 --cw --ch
css=f'''@page{{size:A4;margin:0}}*{{box-sizing:border-box}}:root{{--cw:105mm;--ch:74mm}}
body{{margin:0;background:#fff;color:#000;{font}}}
.sheet{{width:210mm;height:297mm;display:grid;grid-template-columns:repeat(2,var(--cw));grid-auto-rows:var(--ch);justify-content:center;align-content:start;page-break-after:always}}
.card{{border:.3mm dashed #888;padding:4mm 5mm;display:grid;grid-template-rows:1fr 1.5fr .5fr;position:relative}}
.card .z{{border-bottom:.2mm solid #e5e5e5;font-size:7pt;color:#bbb}}
.card .name{{}} .card .price{{}} .card .unit{{text-align:right;border:0}}
.sample .name{{font-size:26pt;font-weight:700;color:#000;border-bottom:.2mm solid #e5e5e5}}
.sample .price{{font-size:54pt;font-weight:800;color:#c2410c;line-height:1}} .sample .unit{{font-size:14pt;color:#000}}
@media screen{{body{{padding:8px;background:#eee}}.sheet{{background:#fff;margin:0 auto 12px}}}}'''
def blank(n):
    return ''.join('<div class="card"><div class="z name">品名（中字）</div><div class="z price">價格（最大）</div><div class="z unit">單位／備註（小字）</div></div>' for _ in range(n))
sample='<div class="card sample"><div class="z name">高麗菜</div><div class="z price">$40</div><div class="z unit">一顆　當季</div></div>'
o=H("POP 貨架價格卡",css)+'<div class="sheet">'+sample+blank(7)+'</div><div class="sheet">'+blank(8)+'</div></body></html>'
open(os.path.join(OUT,'POP貨架價格卡_A4.html'),'w',encoding='utf-8').write(o)

# 3 練習方格紙 A4 / A5（4cm 方格，十字輔助線）
for size,cols,rows in (("A4",5,7),("A5",3,5)):
    cell=lambda:'<div class="c"></div>'
    css=f'''@page{{size:{size};margin:0}}*{{box-sizing:border-box}}body{{margin:0;background:#fff}}
.sheet{{width:{ 210 if size=="A4" else 148}mm;height:{297 if size=="A4" else 210}mm;display:grid;grid-template-columns:repeat({cols},40mm);grid-auto-rows:40mm;justify-content:center;align-content:center;page-break-after:always}}
.c{{border:.3mm solid #999;background:linear-gradient(#ddd,#ddd) center/100% .2mm no-repeat,linear-gradient(#ddd,#ddd) center/.2mm 100% no-repeat}}
@media screen{{body{{padding:8px;background:#eee}}.sheet{{background:#fff;margin:0 auto 12px}}}}'''
    open(os.path.join(OUT,f'POP練習方格紙_{size}.html'),'w',encoding='utf-8').write(H(f"POP 練習方格紙 {size}",css)+'<div class="sheet">'+cell()*(cols*rows)+'</div></body></html>')
