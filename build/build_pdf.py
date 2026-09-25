"""Builds portfolio.pdf: a 16:9 PDF with clickable navigation, from the same data as the site.

Run from the repo root:
  python3 build/build_pdf.py <fonts-dir>     # writes build/pdf.html
  node build/render_pdf.js                    # writes portfolio.pdf

<fonts-dir> must hold NotoSansKR-400/500/700/800.ttf (Google Fonts, OFL).
"""
import base64
import sys
from pathlib import Path

import build_site as S

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "build" / "fonts"
CAT_NAMES = dict(S.CATS)


def img(f):
    return "data:image/jpeg;base64," + base64.b64encode((ROOT / "assets" / f).read_bytes()).decode()


def font_faces():
    out = []
    for w in (400, 500, 700, 800):
        p = FONT_DIR / f"NotoSansKR-{w}.ttf"
        out.append(f"@font-face{{font-family:'PF Sans';font-weight:{w};src:url('file://{p}') format('truetype');}}")
    return "\n".join(out)


def sidebar(current):
    items = [("overview", "개요"), ("career", "경력"), ("skills", "역량")]
    nav = "".join(
        f'<a class="sb-link{" is-on" if current == k else ""}" href="#{k}">{v}</a>' for k, v in items[:1])
    proj = "".join(
        f'<a class="sb-proj{" is-on" if current == f"p{p[0]:02d}" else ""}" href="#p{p[0]:02d}"><span>{p[0]:02d}</span>{p[4]}</a>'
        for p in S.PROJECTS)
    rest = "".join(
        f'<a class="sb-link{" is-on" if current == k else ""}" href="#{k}">{v}</a>' for k, v in items[1:])
    return f"""<aside class="sb">
      <a class="sb-name" href="#overview"><b>임보라</b><span>CRM 데이터 포트폴리오</span></a>
      <nav>{nav}<div class="sb-group">프로젝트</div>{proj}{rest}</nav>
      <div class="sb-foot">{S.EMAIL}</div>
    </aside>"""


def page(pid, inner, current=None):
    return f'<section class="page" id="{pid}">{sidebar(current or pid)}<div class="main">{inner}</div></section>'


def overview():
    hl = "".join(f'<a class="hl" href="#p{n:02d}"><span>{t}</span><b>{v}</b></a>' for n, t, v in S.HIGHLIGHTS)
    groups = ""
    for k, name in S.CATS[1:]:
        rows = "".join(
            f'<a class="ix" href="#p{p[0]:02d}"><span class="ix-n">{p[0]:02d}</span><span class="ix-t">{p[4]}</span><span class="ix-go">보기 →</span></a>'
            for p in S.PROJECTS if p[1] == k)
        groups += f'<div class="ix-group">{name}</div>{rows}'
    return page("overview", f"""
      <div class="ov-top">
        <div class="tag"><i></i>CJ올리브영 데이터 사업 담당자 지원</div>
        <h1>임보라 <small>CRM 데이터 담당 · ㈜인디에프</small></h1>
        <p class="bio">마케팅 현장의 문제를 데이터 분석과 시스템으로 해결해 왔습니다. 분석을 리포트로 끝내지 않고, 현업이 직접 쓰는 조회 화면과 운영 기준으로 바꿉니다.</p>
        <ul class="stats"><li><b>9년</b><span>리테일 · 커머스</span></li><li><b>22만</b><span>멤버십 회원 분석</span></li><li><b>300개</b><span>매장 데이터</span></li><li><b>20+</b><span>온·오프라인 채널</span></li></ul>
      </div>
      <div class="ov-cols">
        <div><h2>핵심 성과</h2>{hl}</div>
        <div><h2>프로젝트 <span class="hint">제목을 누르면 해당 페이지로 이동합니다</span></h2><div class="ix-list">{groups}</div></div>
      </div>""")


def project(i, p):
    n, cat, label, stack, title, psr, hero, rows, shot, steps, lead, extra, _ = p
    nums = f'<div class="hero"><b>{hero[0]}</b><span>{hero[1]}</span></div>' if hero else ""
    nums += '<dl class="rows">' + "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in rows) + "</dl>"
    shot_html = ""
    if shot:
        f, alt, w, h, cap = shot
        shot_html = f'<figure class="shot"><img src="{img(f)}" alt="{alt}"><figcaption>{cap}</figcaption></figure>'
    flow = '<ol class="flow">' + "".join(f"<li>{s}</li>" for s in steps) + "</ol>"
    prev_ = f'<a href="#p{S.PROJECTS[i-1][0]:02d}">← 이전 프로젝트</a>' if i > 0 else '<a href="#overview">← 개요</a>'
    next_ = f'<a href="#p{S.PROJECTS[i+1][0]:02d}">다음 프로젝트 →</a>' if i < len(S.PROJECTS) - 1 else '<a href="#career">경력 →</a>'
    return page(f"p{n:02d}", f"""
      <div class="eyebrow"><b>PROJECT {n:02d}</b>{CAT_NAMES[cat]} · {label} · {stack}</div>
      <h1 class="ptitle">{title}</h1>
      <div class="pgrid">
        <div class="pleft">
          <dl class="psr"><dt>문제</dt><dd>{psr[0]}</dd><dt class="how">방법</dt><dd>{psr[1]}</dd><dt class="res">결과</dt><dd class="res">{psr[2]}</dd></dl>
          <div class="nums">{nums}</div>
          {shot_html}
        </div>
        <div class="detail">
          <h3>어떻게 진행했나</h3>
          <p>{lead}</p>
          <h4>진행 순서</h4>{flow}{extra}
        </div>
      </div>
      <div class="pager">{prev_}<a href="#overview">목록</a>{next_}</div>""")


def career():
    jobs = ""
    for tag, period, title, desc, wins in S.JOBS:
        w = ("<ul>" + "".join(f"<li>{x}</li>" for x in wins) + "</ul>") if wins else ""
        jobs += f'<article class="job"><div class="jp"><b>{tag}</b>{period}</div><h3>{title}</h3><p>{desc}</p>{w}</article>'
    return page("career", f'<h1 class="ptitle">경력 <small>9년 · 5개 회사</small></h1><div class="jobs">{jobs}</div>')


def skills():
    tools = [("데이터 · CRM", ["SQL", "Python / Pandas", "Azure SQL", "Dynamics 365"]),
             ("분석 · 시각화", ["Power BI", "Streamlit", "GA4", "GTM"]),
             ("자동화 · AI", ["Playwright", "OpenAI API"]),
             ("커머스 · 광고", ["SMS/LMS/MMS", "Kakao", "Meta Ads", "Naver SA", "Cafe24", "Demandware", "사방넷", "ERP", "WMS · 3PL"]),
             ("어학 · 자격", ["新HSK 6급", "MOS Expert", "GTQ 1급"])]
    t = "".join(f"<dt>{a}</dt><dd>" + "".join(f'<span class="chip">{c}</span>' for c in cs) + "</dd>" for a, cs in tools)
    return page("skills", f"""<h1 class="ptitle">역량</h1>
      <div class="sk">
        <div><h2>직무와 연결되는 경험</h2>
          <ul class="fit">
            <li><b>마케팅 데이터 해석</b><span>CRM 캠페인과 구매·매출 성과를 연결해 후속 운영 방향을 정했습니다.</span></li>
            <li><b>SQL · Python · BI</b><span>Azure SQL 데이터를 Power BI와 Streamlit으로 분석하고 조회 화면을 만들었습니다.</span></li>
            <li><b>요구사항 구조화</b><span>서비스 화면과 멤버십 운영에 필요한 데이터 기준과 예외 조건을 정했습니다.</span></li>
            <li><b>문서화와 협업</b><span>전산팀·외부 개발사·대행사와 구현 결과를 확인했습니다.</span></li>
          </ul>
          <h2>일하는 방식</h2>
          <ol class="flow"><li>문제와 지표 정의</li><li>SQL · Python 분석</li><li>실행안 제안</li><li>기능 · 운영 기준 정리</li><li>가이드와 활용 확산</li></ol>
        </div>
        <div><h2>활용 도구</h2><dl class="tools">{t}</dl>
          <p class="contact">연락처 <b>{S.EMAIL}</b></p></div>
      </div>""")


CSS = """
@page { size: 1280px 720px; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; }
body { font-family: 'PF Sans', sans-serif; color: #161318; -webkit-print-color-adjust: exact; print-color-adjust: exact; word-break: keep-all; }
a { color: inherit; text-decoration: none; }
.page { width: 1280px; height: 720px; display: grid; grid-template-columns: 250px 1fr; overflow: hidden; page-break-after: always; break-after: page; }
.page:last-child { page-break-after: auto; }

/* sidebar: the clickable menu on every page */
.sb { display: flex; flex-direction: column; padding: 32px 18px 24px 26px; border-right: 1px solid #e7dbea; background: #f7f5f8; }
.sb-name b { display: block; font-size: 22px; line-height: 28px; font-weight: 800; }
.sb-name span { display: block; font-size: 12px; line-height: 16px; color: #6b656d; }
.sb nav { display: flex; flex-direction: column; gap: 1px; margin-top: 22px; }
.sb-link { padding: 6px 10px; border-radius: 8px; font-size: 14px; line-height: 20px; font-weight: 700; color: #3f3941; }
.sb-group { margin: 12px 0 4px; padding: 0 10px; font-size: 11px; font-weight: 800; letter-spacing: .06em; color: #6b656d; }
.sb-proj { display: flex; gap: 8px; padding: 4px 10px; border-radius: 8px; font-size: 12px; line-height: 17px; color: #3f3941; }
.sb-proj span { flex: none; font-weight: 800; color: #5a3a61; }
.sb-link.is-on, .sb-proj.is-on { background: #5a3a61; color: #fff; }
.sb-proj.is-on span { color: #fff; }
.sb-link:not(.is-on) + .sb-group { margin-top: 12px; }
.sb .sb-group ~ .sb-link { margin-top: 2px; }
.sb-foot { margin-top: auto; font-size: 11px; line-height: 16px; color: #6b656d; }

.main { position: relative; padding: 40px 52px 36px; }

/* overview */
.tag { display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 700; color: #5a3a61; }
.tag i { width: 9px; height: 9px; border-radius: 50%; background: #82de1b; }
.ov-top h1 { margin: 8px 0 0; font-size: 40px; line-height: 50px; font-weight: 800; }
h1 small { margin-left: 10px; font-size: 17px; font-weight: 500; color: #6b656d; }
.bio { margin: 8px 0 0; max-width: 46em; font-size: 16px; line-height: 26px; color: #3f3941; }
.stats { list-style: none; margin: 16px 0 0; padding: 0; display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }
.stats li { padding: 10px 16px; border-radius: 10px; background: #f5f0f6; }
.stats b { display: block; font-size: 26px; line-height: 32px; font-weight: 800; }
.stats span { font-size: 13px; color: #6b656d; }
.ov-cols { display: grid; grid-template-columns: 330px 1fr; gap: 40px; margin-top: 20px; }
h2 { margin: 0 0 8px; font-size: 18px; line-height: 26px; font-weight: 800; }
.hint { margin-left: 8px; font-size: 12px; font-weight: 500; color: #6b656d; }
.hl { display: flex; justify-content: space-between; align-items: baseline; padding: 7px 0; border-bottom: 1px solid #e7dbea; font-size: 14px; color: #3f3941; }
.hl b { font-size: 18px; font-weight: 800; color: #5a3a61; }
.ix-list { display: grid; grid-template-columns: 1fr; }
.ix-group { margin: 6px 0 2px; font-size: 12px; font-weight: 800; color: #6b656d; }
.ix { display: grid; grid-template-columns: 30px 1fr auto; gap: 8px; padding: 3px 0; font-size: 14px; line-height: 20px; border-bottom: 1px solid #f0e8f2; }
.ix-n { font-weight: 800; color: #5a3a61; }
.ix-t { font-weight: 700; }
.ix-go { font-size: 12px; color: #5a3a61; font-weight: 700; }

/* project page */
.eyebrow { font-size: 14px; color: #6b656d; }
.eyebrow b { margin-right: 10px; color: #5a3a61; font-weight: 800; letter-spacing: .04em; }
.ptitle { margin: 6px 0 0; font-size: 30px; line-height: 40px; font-weight: 800; letter-spacing: -.01em; }
.pgrid { display: grid; grid-template-columns: 470px 1fr; gap: 36px; margin-top: 22px; }
.psr { display: grid; grid-template-columns: 40px 1fr; gap: 6px 10px; margin: 0; }
.psr dt { font-size: 14px; line-height: 26px; font-weight: 700; color: #6b656d; }
.psr dt.how { color: #5a3a61; }
.psr dt.res { color: #161318; }
.psr dd { margin: 0; font-size: 17px; line-height: 26px; color: #3f3941; }
.psr dd.res { font-weight: 800; color: #161318; }
.nums { display: grid; grid-template-columns: auto 1fr; gap: 20px; align-items: center; margin-top: 18px; padding: 16px 18px; border: 1px solid #e7dbea; border-radius: 14px; }
.hero b { display: block; font-size: 40px; line-height: 46px; font-weight: 800; letter-spacing: -.02em; color: #5a3a61; white-space: nowrap; }
.hero span { font-size: 13px; color: #6b656d; }
.rows { display: grid; grid-template-columns: auto 1fr; gap: 4px 12px; margin: 0; font-size: 13px; line-height: 20px; }
.rows dt { color: #6b656d; }
.rows dd { margin: 0; text-align: right; font-weight: 700; }
.shot { margin: 14px 0 0; border: 1px solid #e7dbea; border-radius: 12px; overflow: hidden; background: #f7f5f8; }
.shot img { display: block; width: 100%; max-height: 215px; object-fit: contain; }
.shot figcaption { padding: 4px 12px; font-size: 11px; color: #6b656d; }
.detail { padding: 22px 26px; border-radius: 14px; background: #f7f5f8; font-size: 14px; line-height: 23px; color: #3f3941; align-self: start; }
.detail h3 { margin: 0 0 8px; font-size: 16px; font-weight: 800; color: #5a3a61; }
.detail p { margin: 0; }
.detail h4 { margin: 16px 0 6px; font-size: 13px; font-weight: 800; color: #161318; }
.detail ul { margin: 0; padding-left: 18px; }
.flow { list-style: none; counter-reset: f; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 4px; }
.flow li { counter-increment: f; display: flex; gap: 10px; font-size: 14px; line-height: 22px; }
.flow li::before { content: counter(f); flex: none; width: 21px; height: 21px; margin-top: 1px; border-radius: 50%; background: #5a3a61; color: #fff; font-size: 11px; line-height: 21px; font-weight: 800; text-align: center; }
.pf-chips { display: flex; flex-wrap: wrap; gap: 6px; }
.pf-chip, .chip { display: inline-block; padding: 2px 10px; border: 1px solid #d9cdd9; border-radius: 999px; background: #fff; font-size: 12px; line-height: 18px; margin: 0 4px 4px 0; }
.pf-note { margin-top: 12px !important; font-size: 12px; line-height: 18px; color: #6b656d; }
.pager { position: absolute; left: 52px; right: 52px; bottom: 26px; display: flex; justify-content: space-between; padding-top: 12px; border-top: 1px solid #e7dbea; font-size: 13px; font-weight: 700; color: #5a3a61; }

/* career + skills */
.jobs { display: grid; grid-template-columns: 1fr 1fr; gap: 14px 36px; margin-top: 18px; }
.job { padding-bottom: 12px; border-bottom: 1px solid #e7dbea; }
.jp { font-size: 12px; color: #6b656d; }
.jp b { margin-right: 8px; color: #5a3a61; font-weight: 800; }
.job h3 { margin: 2px 0 0; font-size: 17px; line-height: 24px; font-weight: 800; }
.job p { margin: 2px 0 0; font-size: 12px; line-height: 18px; color: #6b656d; }
.job ul { margin: 6px 0 0; padding-left: 16px; font-size: 13px; line-height: 20px; color: #3f3941; }
.job strong { color: #161318; font-weight: 800; }
.sk { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; margin-top: 22px; }
.fit { list-style: none; margin: 0 0 22px; padding: 0; display: grid; gap: 10px; }
.fit b { display: block; font-size: 15px; }
.fit span { font-size: 13px; line-height: 20px; color: #6b656d; }
.tools { display: grid; grid-template-columns: 110px 1fr; gap: 10px 12px; margin: 0; }
.tools dt { font-size: 13px; line-height: 26px; font-weight: 800; }
.tools dd { margin: 0; }
.contact { margin-top: 28px; font-size: 14px; color: #6b656d; }
.contact b { color: #161318; margin-left: 8px; }
"""

if __name__ == "__main__":
    pages = overview() + "".join(project(i, p) for i, p in enumerate(S.PROJECTS)) + career() + skills()
    html = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>임보라 CRM 데이터 포트폴리오</title><style>{font_faces()}{CSS}</style></head><body>{pages}</body></html>'
    (ROOT / "build" / "pdf.html").write_text(html, encoding="utf-8")
    print("wrote build/pdf.html")
