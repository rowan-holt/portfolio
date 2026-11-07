#!/usr/bin/env python3
"""data/hotels.json → 정적 HTML.

zh-TW: 루트(/), ko: /ko/  (ko는 검토용, 검색엔진 색인 제외)
실행: python3 build.py
"""
import json
import shutil
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
DATA = json.loads((ROOT / "data/hotels.json").read_text(encoding="utf-8"))
SITE_URL = "https://rowan-holt.github.io/portfolio/"

T = {
    "zh": {
        "html_lang": "zh-Hant-TW",
        "site": "首爾飯店判定",
        "tagline": "負評是個案，還是結構性問題？由前飯店等級評鑑委員逐條判定。",
        "home_title": "明洞飯店 5 選｜首爾飯店判定",
        "home_desc": "明洞5間飯店的出口、機場巴士、房間坪數、浴缸、禁菸、櫃檯資訊，每一項都附官方出處與確認日期。負評由前飯店等級評鑑委員判定是個案還是結構性問題。",
        "nav_home": "飯店列表",
        "nav_about": "判定的人與方法",
        "other_lang": "한국어",
        "col_hotel": "飯店",
        "col_station": "最近車站出口",
        "col_tub": "浴缸",
        "col_smoke": "禁菸",
        "see": "看判定與事實",
        "facts_title": "事實確認表",
        "facts_note": "每一項都附出處與確認日期。官方沒有寫、我們也沒能確認的，標示為「未確認」，不用猜的填。",
        "rooms_title": "房型・面積・浴室",
        "room": "房型",
        "size": "面積（㎡）",
        "tub": "浴缸",
        "sep": "淋浴／馬桶分開",
        "note": "備註",
        "verdict_title": "負評判定",
        "verdict_pending": "這間飯店的負評判定正在撰寫中。",
        "verdict_labels": {"isolated": "個案", "structural": "結構性問題", "mixed": "看房型・時段"},
        "booking_title": "訂房",
        "booking_pending": "訂房連結準備中。",
        "official": "官方網站",
        "source": "出處",
        "checked": "確認日",
        "unverified": "未確認",
        "checkin": "入住／退房",
        "address": "地址",
        "yes": "有", "no": "無", "unlisted": "官方設備清單未列",
        "fact_labels": {
            "station": "車站出口・步行時間",
            "exit_elevator": "出口電梯",
            "airport_bus": "機場巴士",
            "smoking": "吸菸規定",
            "front_24h": "24小時櫃檯",
            "self_checkin": "自助入住",
            "languages": "日語・中文服務",
            "luggage": "行李寄放",
            "payment": "付款",
            "min_age": "入住年齡",
        },
        "disclosure": "本站部分訂房連結為聯盟連結，透過連結訂房時本站可能獲得佣金，您支付的價格不變。判定內容不受佣金影響。",
        "updated": "資料確認日",
        "about_title": "判定的人與方法｜首爾飯店判定",
        "about_h1": "判定的人與方法",
        "about_who_h": "誰在判定",
        "about_who": [
            "大學主修觀光經營",
            "曾任職飯店",
            "韓國觀光口譯導遊（관광통역안내사）國家證照",
            "曾任韓國飯店等級評鑑委員",
        ],
        "about_how_h": "怎麼判定",
        "about_how": [
            "事實與判定分開。事實表只放官方或公開資料能確認的內容，每一項都附出處網址與確認日期。",
            "確認不了的就寫「未確認」，不用推測補上。",
            "負評先看是不是多次、不同時間、不同房型都出現。同一件事只出現一次、而且有明確原因的，判為「個案」；和建築結構、營運方式、人力配置有關，換一天也會發生的，判為「結構性問題」。",
            "判定一定附上依據。",
        ],
        "about_money_h": "本站怎麼賺錢",
    },
    "ko": {
        "html_lang": "ko",
        "site": "서울 호텔 판정",
        "tagline": "부정적 리뷰는 일부 사례일까, 구조적 문제일까? 전 호텔등급심사 평가위원이 하나씩 판정합니다.",
        "home_title": "명동 호텔 5곳｜서울 호텔 판정 (검토용)",
        "home_desc": "명동 호텔 5곳의 출구, 공항버스, 객실 면적, 욕조, 금연, 프런트 정보. 항목마다 출처와 확인 날짜.",
        "nav_home": "호텔 목록",
        "nav_about": "판정하는 사람과 방법",
        "other_lang": "繁體中文",
        "col_hotel": "호텔",
        "col_station": "가까운 역 출구",
        "col_tub": "욕조",
        "col_smoke": "금연",
        "see": "판정과 사실 보기",
        "facts_title": "사실 확인표",
        "facts_note": "항목마다 출처와 확인 날짜를 적었습니다. 공식 자료에 없고 확인하지 못한 항목은 추측하지 않고 '미확인'으로 둡니다.",
        "rooms_title": "객실 타입·면적·욕실",
        "room": "객실",
        "size": "면적(㎡)",
        "tub": "욕조",
        "sep": "샤워·변기 분리",
        "note": "비고",
        "verdict_title": "부정적 리뷰 판정",
        "verdict_pending": "이 호텔의 리뷰 판정은 작성 중입니다.",
        "verdict_labels": {"isolated": "일부 사례", "structural": "구조적 문제", "mixed": "객실·시기에 따라 다름"},
        "booking_title": "예약",
        "booking_pending": "예약 링크 준비 중입니다.",
        "official": "공식 사이트",
        "source": "출처",
        "checked": "확인일",
        "unverified": "미확인",
        "checkin": "체크인 / 체크아웃",
        "address": "주소",
        "yes": "있음", "no": "없음", "unlisted": "공식 설비 목록에 없음",
        "fact_labels": {
            "station": "역 출구·도보 시간",
            "exit_elevator": "출구 엘리베이터",
            "airport_bus": "공항버스",
            "smoking": "흡연 정책",
            "front_24h": "24시간 프런트",
            "self_checkin": "셀프 체크인",
            "languages": "일본어·중국어 응대",
            "luggage": "짐 보관",
            "payment": "결제",
            "min_age": "체크인 나이",
        },
        "disclosure": "이 사이트의 일부 예약 링크는 제휴 링크입니다. 링크로 예약하면 사이트가 수수료를 받을 수 있으며 결제 금액은 같습니다. 판정 내용은 수수료와 관계없습니다.",
        "updated": "자료 확인일",
        "about_title": "판정하는 사람과 방법｜서울 호텔 판정",
        "about_h1": "판정하는 사람과 방법",
        "about_who_h": "누가 판정하나",
        "about_who": [
            "관광경영 전공",
            "호텔 근무 경력",
            "관광통역안내사 자격",
            "호텔등급심사 평가위원 경력",
        ],
        "about_how_h": "어떻게 판정하나",
        "about_how": [
            "사실과 판정을 나눕니다. 사실 확인표에는 공식·공개 자료로 확인한 내용만 넣고, 항목마다 출처 URL과 확인 날짜를 적습니다.",
            "확인하지 못한 항목은 추측하지 않고 '미확인'으로 둡니다.",
            "부정적 리뷰는 여러 번, 다른 시기, 다른 객실에서 반복되는지 먼저 봅니다. 한 번 나왔고 원인이 분명하면 '일부 사례', 건물 구조·운영 방식·인력 배치와 연결돼 다른 날에도 생길 일이면 '구조적 문제'로 판정합니다.",
            "판정에는 반드시 근거를 붙입니다.",
        ],
        "about_money_h": "이 사이트의 수익 구조",
    },
}

FACT_ORDER = ["station", "exit_elevator", "airport_bus", "smoking", "front_24h",
              "self_checkin", "languages", "luggage", "payment", "min_age"]

CSS = """
:root{color-scheme:light dark;--bg:#f7f6f3;--card:#fff;--text:#1d1c1a;--muted:#6a6862;--line:#e3e1db;
--accent:#1f5f8b;--warn-bg:#fbf1dc;--warn:#8a5a00;--ok:#1d6b3f;--gutter:16px;
font-family:"Noto Sans TC","Noto Sans KR",system-ui,-apple-system,"PingFang TC","Apple SD Gothic Neo",sans-serif}
@media (prefers-color-scheme:dark){:root{--bg:#151514;--card:#1e1e1c;--text:#ecebe7;--muted:#a3a19a;--line:#33322f;
--accent:#7db8e0;--warn-bg:#3a2d12;--warn:#f0c26a;--ok:#7fd3a0}}
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);line-height:1.7;word-break:keep-all;overflow-wrap:anywhere}
a{color:var(--accent)}
.wrap{max-width:960px;margin:0 auto;padding:0 var(--gutter)}
header.site{border-bottom:1px solid var(--line);background:var(--card)}
header.site .wrap{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:8px 20px;padding-top:14px;padding-bottom:14px}
.brand{font-weight:700;text-decoration:none;color:var(--text);font-size:1.05rem}
nav ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:4px 16px;font-size:.92rem}
nav a{color:var(--muted);text-decoration:none}nav a:hover,nav a[aria-current]{color:var(--text)}
main{padding:28px 0 48px}
h1{font-size:1.6rem;line-height:1.35;margin:0 0 8px}
h2{font-size:1.15rem;margin:40px 0 12px;padding-top:4px}
.lead{color:var(--muted);margin:0 0 24px}
.tablewrap{overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--card)}
table{border-collapse:collapse;width:100%;font-size:.93rem}
th,td{text-align:left;vertical-align:top;padding:10px 12px;border-bottom:1px solid var(--line)}
tr:last-child>*{border-bottom:0}
thead th{font-size:.8rem;color:var(--muted);font-weight:500;white-space:nowrap}
tbody th{font-weight:500;width:8.5em}
@media (max-width:480px){tbody th{width:6.5em;font-size:.85rem}}
.src{display:block;font-size:.78rem;color:var(--muted);margin-top:2px}
.src a{color:var(--muted)}
.tag{display:inline-block;font-size:.75rem;padding:1px 7px;border-radius:999px;background:var(--warn-bg);color:var(--warn);white-space:nowrap}
.yes{color:var(--ok);font-weight:500}
.cards{display:grid;gap:12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px}
.card h3{margin:0 0 6px;font-size:1.05rem}
.card h3 a{color:var(--text);text-decoration:none}
.card dl{display:grid;grid-template-columns:auto 1fr;gap:2px 12px;margin:8px 0 10px;font-size:.9rem}
.card dt{color:var(--muted)}.card dd{margin:0}
.meta{font-size:.88rem;color:var(--muted)}
.pending{background:var(--card);border:1px dashed var(--line);border-radius:10px;padding:16px;color:var(--muted)}
.verdict{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px;margin-bottom:12px}
.verdict .label{font-weight:700}
.verdict.structural .label{color:#b3261e}.verdict.isolated .label{color:var(--ok)}
.btns{display:flex;flex-wrap:wrap;gap:8px}
.btn{display:inline-block;padding:10px 16px;border-radius:8px;background:var(--accent);color:#fff;text-decoration:none;font-weight:500}
@media (prefers-color-scheme:dark){.btn{color:#111}}
footer.site{border-top:1px solid var(--line);padding:20px 0 32px;font-size:.82rem;color:var(--muted)}
ul.plain,ol.plain{padding-left:1.2em}
.rooms td{overflow-wrap:normal}
@media (max-width:600px){
.rooms thead{display:none}
.rooms tr{display:block;padding:10px 12px;border-bottom:1px solid var(--line)}
.rooms tr:last-child{border-bottom:0}
.rooms td{display:grid;grid-template-columns:7.5em 1fr;gap:8px;padding:2px 0;border:0}
.rooms td.rname{display:block;font-weight:700;padding-bottom:4px}
.rooms td.empty{display:none}
.rooms td>.tag,.rooms td>span{justify-self:start}
.rooms td[data-l]::before{content:attr(data-l);color:var(--muted);font-size:.85rem}
}
"""


def e(s):
    return escape(str(s), quote=True)


def page(lang, depth, path_here, title, desc, body, alt_path, noindex=False):
    t = T[lang]
    up = "../" * depth
    other = alt_path
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    canonical = f'<link rel="canonical" href="{SITE_URL}{path_here}">' if not noindex else ""
    return f"""<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{robots}{canonical}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&family=Noto+Sans+KR:wght@400;500;700&display=swap">
<link rel="stylesheet" href="{up}{'../' if lang == 'ko' else ''}style.css">
</head>
<body>
<header class="site"><div class="wrap">
<a class="brand" href="{up}index.html">{e(t['site'])}</a>
<nav aria-label="menu"><ul>
<li><a href="{up}index.html">{e(t['nav_home'])}</a></li>
<li><a href="{up}about.html">{e(t['nav_about'])}</a></li>
<li><a href="{e(other)}" hreflang="{'ko' if lang == 'zh' else 'zh-Hant-TW'}">{e(t['other_lang'])}</a></li>
</ul></nav>
</div></header>
<main><div class="wrap">
{body}
</div></main>
<footer class="site"><div class="wrap">
<p>{e(t['disclosure'])}</p>
<p>© {e(t['site'])}</p>
</div></footer>
</body>
</html>
"""


def src_html(lang, url, checked):
    t = T[lang]
    if url:
        host = url.split("/")[2].replace("www.", "")
        return (f'<span class="src">{e(t["source"])}: <a href="{e(url)}" rel="nofollow noopener" target="_blank">{e(host)}</a>'
                f' · {e(t["checked"])} {e(checked)}</span>')
    return f'<span class="src">{e(t["checked"])} {e(checked)}</span>'


def tub_html(lang, v):
    t = T[lang]
    if v == "yes":
        return f'<span class="yes">{e(t["yes"])}</span>'
    if v == "no":
        return e(t["no"])
    if v == "unlisted":
        return e(t["unlisted"])
    return f'<span class="tag">{e(t["unverified"])}</span>'


def fact_value(lang, f):
    raw = f["value"][lang]
    tag = f'<span class="tag">{e(T[lang]["unverified"])}</span>'
    if raw == T[lang]["unverified"]:
        v = tag
    elif f["status"] != "ok":
        v = tag + " " + e(raw)
    else:
        v = e(raw)
    return v + src_html(lang, f.get("source", ""), f["checked"])


def tub_summary(lang, h):
    vals = {r["tub"] for r in h["rooms"]["list"]}
    t = T[lang]
    if vals == {"yes"}:
        return {"zh": "全房型都有", "ko": "전 객실 있음"}[lang]
    if "yes" in vals:
        return {"zh": "部分房型有", "ko": "일부 객실만"}[lang]
    return f'<span class="tag">{e(t["unverified"])}</span>'


def short_station(lang, h):
    f = h["facts"]["station"]
    if f["status"] != "ok" or "short" not in f:
        return f'<span class="tag">{e(T[lang]["unverified"])}</span>'
    return e(f["short"][lang])


def smoke_short(lang, h):
    f = h["facts"]["smoking"]
    if f["status"] != "ok":
        return f'<span class="tag">{e(T[lang]["unverified"])}</span>'
    return {"zh": "禁菸", "ko": "금연"}[lang]


def build_home(lang):
    t = T[lang]
    cards = []
    for h in DATA["hotels"]:
        cards.append(f"""<article class="card">
<h3><a href="hotels/{h['id']}.html">{e(h['name'][lang])}</a></h3>
<div class="meta">{e(h['name_en'])}</div>
<dl>
<dt>{e(t['col_station'])}</dt><dd>{short_station(lang, h)}</dd>
<dt>{e(t['col_tub'])}</dt><dd>{tub_summary(lang, h)}</dd>
<dt>{e(t['col_smoke'])}</dt><dd>{smoke_short(lang, h)}</dd>
</dl>
<a href="hotels/{h['id']}.html">{e(t['see'])} →</a>
</article>""")
    body = f"""<h1>{e(t['site'])}</h1>
<p class="lead">{e(t['tagline'])}</p>
<div class="cards">{''.join(cards)}</div>"""
    return body


def build_hotel(lang, h):
    t = T[lang]
    rows = []
    rows.append(f'<tr><th scope="row">{e(t["address"])}</th><td>{e(h["address"][lang])}</td></tr>')
    rows.append(f'<tr><th scope="row">{e(t["checkin"])}</th><td>{e(h["checkin"])}</td></tr>')
    for k in FACT_ORDER:
        if k in h["facts"]:
            rows.append(f'<tr><th scope="row">{e(t["fact_labels"][k])}</th><td>{fact_value(lang, h["facts"][k])}</td></tr>')

    r = h["rooms"]
    room_rows = []
    for rm in r["list"]:
        note = e(rm["note"][lang]) if rm.get("note") else ""
        src = rm.get("source", r["source"])
        room_rows.append(
            f'<tr><td class="rname">{e(rm["name"])}</td><td data-l="{e(t["size"])}">{e(rm["size"])}</td>'
            f'<td data-l="{e(t["tub"])}">{tub_html(lang, rm["tub"])}</td>'
            f'<td data-l="{e(t["sep"])}">{tub_html(lang, rm["sep"])}</td>'
            + (f'<td data-l="{e(t["note"])}">{note}</td>' if note else '<td class="empty"></td>') + '</tr>')
    all_note = f'<p>{e(r["all_note"][lang])}</p>' if r.get("all_note") else ""

    if h["verdicts"]:
        vs = []
        for v in h["verdicts"]:
            vs.append(f"""<div class="verdict {e(v['verdict'])}">
<div><span class="label">{e(t['verdict_labels'][v['verdict']])}</span> — {e(v['topic'][lang])}</div>
<p>{e(v['summary'][lang])}</p>
<p class="meta">{e(v.get('evidence', {}).get(lang, ''))} · {e(v.get('date', ''))}</p>
</div>""")
        verdict_html = "".join(vs)
    else:
        verdict_html = f'<div class="pending">{e(t["verdict_pending"])}</div>'

    links = [(k, u) for k, u in h["booking"].items() if u]
    names = {"agoda": "Agoda", "trip": "Trip.com", "klook": "Klook"}
    if links:
        booking_html = '<div class="btns">' + "".join(
            f'<a class="btn" href="{e(u)}" rel="sponsored nofollow noopener" target="_blank">{names[k]}</a>' for k, u in links) + "</div>"
    else:
        booking_html = f'<div class="pending">{e(t["booking_pending"])}</div>'

    return f"""<h1>{e(h['name'][lang])}</h1>
<p class="lead">{e(h['name_en'])} · <a href="{e(h['official'])}" rel="nofollow noopener" target="_blank">{e(t['official'])}</a></p>

<h2 id="verdict">{e(t['verdict_title'])}</h2>
{verdict_html}

<h2 id="facts">{e(t['facts_title'])}</h2>
<p class="meta">{e(t['facts_note'])}</p>
<div class="tablewrap"><table><tbody>{''.join(rows)}</tbody></table></div>

<h2 id="rooms">{e(t['rooms_title'])}</h2>
{all_note}
<div class="tablewrap rooms"><table>
<thead><tr><th>{e(t['room'])}</th><th>{e(t['size'])}</th><th>{e(t['tub'])}</th><th>{e(t['sep'])}</th><th>{e(t['note'])}</th></tr></thead>
<tbody>{''.join(room_rows)}</tbody></table></div>
{src_html(lang, r['source'], r['checked'])}

<h2 id="booking">{e(t['booking_title'])}</h2>
{booking_html}
"""


def build_about(lang):
    t = T[lang]
    who = "".join(f"<li>{e(x)}</li>" for x in t["about_who"])
    how = "".join(f"<li>{e(x)}</li>" for x in t["about_how"])
    return f"""<h1>{e(t['about_h1'])}</h1>
<h2>{e(t['about_who_h'])}</h2>
<ul class="plain">{who}</ul>
<h2>{e(t['about_how_h'])}</h2>
<ol class="plain">{how}</ol>
<h2>{e(t['about_money_h'])}</h2>
<p>{e(t['disclosure'])}</p>
"""


def write(path, html):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")


def main():
    for d in ["hotels", "ko"]:
        shutil.rmtree(ROOT / d, ignore_errors=True)
    (ROOT / "style.css").write_text(CSS.strip() + "\n", encoding="utf-8")

    for lang in ["zh", "ko"]:
        base = "" if lang == "zh" else "ko/"
        noindex = lang == "ko"
        t = T[lang]

        # 홈
        write(f"{base}index.html", page(lang, 0, f"{base}index.html", t["home_title"], t["home_desc"],
                                        build_home(lang), ("ko/index.html" if lang == "zh" else "../index.html"), noindex))
        # 소개
        write(f"{base}about.html", page(lang, 0, f"{base}about.html", t["about_title"], t["home_desc"],
                                        build_about(lang), ("ko/about.html" if lang == "zh" else "../about.html"), noindex))
        # 호텔
        for h in DATA["hotels"]:
            title = f"{h['name'][lang]}｜{t['facts_title']}・{t['verdict_title']}｜{t['site']}"
            desc = f"{h['name'][lang]}: " + " / ".join(
                f"{t['fact_labels'][k]} {h['facts'][k]['value'][lang]}" for k in ["station", "smoking"])
            alt = (f"../ko/hotels/{h['id']}.html" if lang == "zh" else f"../../hotels/{h['id']}.html")
            write(f"{base}hotels/{h['id']}.html",
                  page(lang, 1, f"{base}hotels/{h['id']}.html", title, desc, build_hotel(lang, h), alt, noindex))

    # sitemap (zh만)
    urls = ["index.html", "about.html"] + [f"hotels/{h['id']}.html" for h in DATA["hotels"]]
    sm = "\n".join(f"<url><loc>{SITE_URL}{u}</loc></url>" for u in urls)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}\n</urlset>\n')
    print("built", len(DATA["hotels"]), "hotels × 2 langs")


if __name__ == "__main__":
    main()
