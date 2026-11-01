import html, os
OUT = os.path.dirname(os.path.abspath(__file__))
S = lambda s: s.split("｜")
data = [
 ("促銷", S("特價｜限時特價｜買一送一｜第二件半價｜滿額折扣｜全面8折｜清倉｜最後一天｜優惠中｜免運｜加購價｜會員價｜限量｜售完為止")),
 ("商品", S("新品上市｜熱賣中｜人氣第一｜店長推薦｜今日特餐｜季節限定｜手工製作｜現做｜新鮮直送｜招牌｜本日精選")),
 ("店務告示", S("歡迎光臨｜營業中｜休息中｜今日公休｜請排隊｜小心地滑｜請勿拍照｜謝謝光臨｜洗手間｜請保持安靜｜自助取用｜需要協助請告知")),
 ("數字", S("0｜1｜2｜3｜4｜5｜6｜7｜8｜9｜$｜%｜.｜~｜+｜／｜零｜一｜二｜三｜四｜五｜六｜七｜八｜九｜十｜百｜千｜萬｜兩")),
 ("單位：價格", S("元｜塊｜NT$｜起｜折｜OFF｜免費｜FREE｜含稅｜未稅")),
 ("單位：數量", S("個｜件｜組｜份｜盒｜包｜袋｜瓶｜罐｜杯｜碗｜片｜條｜支｜張｜本｜套｜雙｜對｜箱｜打｜入")),
 ("單位：重量容量", S("公斤｜kg｜公克｜g｜斤｜兩｜公升｜L｜毫升｜ml｜cc")),
 ("單位：時間人數", S("分鐘｜小時｜天｜日｜週｜月｜年｜每日｜每週｜即日起｜至｜止｜到期｜人｜位｜名｜場｜額滿為止")),
 ("常用句型", S("每杯$50｜每份99元｜買3送1｜任選2件8折｜第2杯5折｜滿500折50｜全館85折｜限量100組｜剩3件｜即日起至12/31止")),
 ("葉菜", S("高麗菜｜小白菜｜青江菜｜空心菜｜菠菜｜地瓜葉｜A菜｜萵苣｜芥藍｜油菜｜茼蒿｜龍鬚菜｜九層塔｜香菜｜芹菜｜蔥｜韭菜｜白菜")),
 ("根莖瓜果", S("白蘿蔔｜紅蘿蔔｜馬鈴薯｜地瓜｜芋頭｜山藥｜洋蔥｜蒜頭｜薑｜竹筍｜玉米｜南瓜｜冬瓜｜絲瓜｜苦瓜｜小黃瓜｜茄子｜青椒｜辣椒｜蕃茄｜花椰菜｜青花菜｜四季豆｜毛豆｜香菇｜金針菇｜木耳｜豆芽菜")),
 ("水果", S("蘋果｜香蕉｜橘子｜柳丁｜檸檬｜葡萄｜西瓜｜香瓜｜哈密瓜｜芭樂｜鳳梨｜芒果｜木瓜｜奇異果｜草莓｜藍莓｜櫻桃｜水蜜桃｜李子｜梨子｜柿子｜柚子｜釋迦｜蓮霧｜荔枝｜龍眼｜火龍果｜百香果｜椰子｜甘蔗")),
 ("蔬果形容", S("新鮮｜當季｜產地直送｜有機｜無毒｜產銷履歷｜現採｜香甜｜多汁｜脆甜｜爆甜｜進口｜國產")),
]
e = html.escape
head = lambda t, css: f'<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{t}</title><style>{css}</style></head><body>'
base = ':root{--bg:#fff;--fg:#1b1b1b;--ac:#c2410c;--bd:#d6d3d1}@media(prefers-color-scheme:dark){:root{--bg:#171717;--fg:#f5f5f4;--ac:#fb923c;--bd:#44403c}}body{margin:0;background:var(--bg);color:var(--fg);font-family:"PingFang TC","Noto Sans TC","Microsoft JhengHei",sans-serif}'

# 小卡版
css = base + '''
h1{font-size:18px;margin:16px;} .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px;padding:0 16px 24px}
.card{border:1.5px dashed var(--bd);border-radius:8px;padding:10px 12px;break-inside:avoid}
.card h2{margin:0 0 6px;font-size:13px;color:var(--ac);letter-spacing:.1em}
.card p{margin:0;font-size:15px;line-height:1.8;word-break:keep-all}
.card span{display:inline-block;margin:0 8px 0 0;white-space:nowrap}
@media print{.grid{grid-template-columns:repeat(2,1fr);padding:0}h1{display:none}body{background:#fff;color:#000}}'''
o = head("POP 字小卡版", css) + '<h1>POP 字小卡版（列印後沿虛線剪開）</h1><div class="grid">'
for t, ws in data:
    o += f'<div class="card"><h2>{e(t)}</h2><p>' + "".join(f'<span>{e(w)}</span>' for w in ws) + '</p></div>'
o += '</div></body></html>'
open(os.path.join(OUT, "POP小卡版.html"), "w", encoding="utf-8").write(o)

# 大字版
css = base + '''
section{padding:24px 16px;border-bottom:2px solid var(--bd);min-height:90vh;box-sizing:border-box}
h2{font-size:20px;color:var(--ac);margin:0 0 16px}
.w{display:flex;flex-wrap:wrap;gap:12px 28px}
.w span{font-size:clamp(44px,9vw,96px);font-weight:700;line-height:1.2;white-space:nowrap}
@media print{section{page-break-after:always;border:0;min-height:0}body{background:#fff;color:#000}.w span{font-size:56pt}}'''
o = head("POP 字大字版", css)
for t, ws in data:
    o += f'<section><h2>{e(t)}</h2><div class="w">' + "".join(f'<span>{e(w)}</span>' for w in ws) + '</div></section>'
o += '</body></html>'
open(os.path.join(OUT, "POP大字版.html"), "w", encoding="utf-8").write(o)
