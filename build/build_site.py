"""Builds index.html from the project/career data below.

Run: python3 build/build_site.py   (from the repo root)
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EMAIL = "bora_9203@naver.com"

# (n, category key, category label, stack, title, [문제, 방법, 결과],
#  hero (value, label) or None, [(label, value)...], screenshot or None,
#  [how-it-ran steps], background, extra detail html, search keywords)
PROJECTS = [
    (1, "crm", "BI · 확산", "SQL · Power BI", "반복 자료 요청을 Power BI 셀프 조회로 전환",
     ["1인 CRM에 반복 추출 요청이 집중", "지표 기준 정리 + Power BI 조회 화면 구축", "현업이 직접 조회, 분석·자동화에 쓸 시간 확보"],
     ("6개", "현업이 고르는 조회 필터"), [("대상 중복·누락", "0건"), ("연결 DB", "SQL Server")],
     ("powerbi-self-service.jpg", "Power BI CRM 셀프 조회 화면. 연도·월·브랜드·유통·지역·매장코드 필터와 매출 차트", 1100, 627, "수치·매장명 모자이크"),
     ["반복 요청 지표와 집계 기준 정리", "SQL Server에 연결한 Power BI 조회 화면 구축", "브랜드·지역·매장별 필터와 사용 기준을 현업에 공유"],
     "CRM 팀장 퇴사 후 전사 CRM을 혼자 맡았습니다. 회원·매출 자료를 매번 엑셀로 집계하면 분석과 캠페인 기획에 쓸 시간이 줄었습니다.",
     "", "셀프 조회 power bi sql 반복 요청 필터 대시보드"),
    (2, "crm", "고객 분석", "Python · Streamlit", "RFM · 코호트 기반 고객 분석 화면 구축",
     ["재구매·이탈을 볼 기준이 없음", "RFM · 코호트 · LTV 화면 직접 구축", "분석 결과로 캠페인 타깃 바로 추출"],
     ("5개", "직접 구축한 분석 화면"), [("데이터", "새벽 배치 · Azure SQL"), ("수정", "외부 개발 없이 직접")],
     ("cohort-retention.jpg", "첫 구매월 기준 코호트 리텐션 히트맵 화면", 773, 560, "수치 모자이크"),
     ["POS·ERP·CRM 원천 데이터를 새벽 배치로 Azure SQL에 적재", "같은 데이터를 Power BI와 Python·Streamlit 분석에 사용", "실제 첫 구매월 기준으로 코호트 정의"],
     "재구매와 이탈을 판단할 공통 기준이 없어, 원천 데이터부터 분석 화면까지 직접 연결했습니다.",
     '<h4>분석 범위</h4><div class="pf-chips"><span class="pf-chip">RFM</span><span class="pf-chip">재구매</span><span class="pf-chip">코호트 리텐션</span><span class="pf-chip">관측 LTV</span></div>'
     '<p class="pf-note">새벽 배치 기준이며 실시간이 아니고, LTV는 예측값이 아닌 누적 구매액 기반 관측값입니다.</p>',
     "고객 분석 rfm 코호트 리텐션 ltv python streamlit azure sql 배치 재구매"),
    (3, "crm", "CRM 캠페인", "SQL · 문자 · 카카오", "CRM 타깃 선정부터 구매 성과 확인까지 연결",
     ["매번 반복되는 CRM 타깃 추출", "대상 기준 SQL화 + 쿠폰·구매 데이터 매칭", "재사용 SQL로 타깃 추출 표준화"],
     None, [("대상 기준", "구매 이력 · 수신동의"), ("채널", "문자 · 카카오 · 쿠폰"), ("성과 확인", "쿠폰 사용 ↔ 구매·매출")], None,
     ["구매 이력·수신동의 조건을 SQL로 반영", "문자·카카오로 쿠폰 혜택 발송", "쿠폰 사용과 구매·매출 데이터 매칭", "타깃·혜택 조건을 다음 캠페인에 반영"],
     "발송으로 끝내지 않고, 쿠폰 사용과 구매 데이터를 연결해 다음 캠페인 조건을 정했습니다.",
     "<h4>온·오프라인 연계 멤버십 이벤트</h4><ul><li>홈페이지 참여 회원의 CRM 대상 조건을 정하고 매장 사용 데이터와 연결</li><li>CRM 대행사·홈페이지 유지보수사·전산팀 일정과 데이터 기준 조율</li></ul>",
     "crm 캠페인 타깃 문자 카카오 쿠폰 멤버십 이벤트 sql 성과"),
    (4, "crm", "요구사항 → 정책", "PM", "전사 마일리지 소멸 정책 수립과 첫 시행",
     ["규정만 있고 시스템이 없어 부채 누적", "기준 정의, 재무·전산·대행사 조율", "첫 소멸 실행 + 고객 조회 페이지 오픈"],
     ("14만+ 명", "첫 소멸 대상"), [("소멸 처리 잔액", "약 2.5억 원"), ("협업", "재무 · 전산 · 대행사")], None,
     ["요구사항 정의 (CRM)", "정책 합의 (재무)", "시스템 구현 (전산)", "안내 발송 (대행사)", "테스트·검증 (CRM)", "고객 조회 페이지 (전산)"],
     "통합 멤버십 도입 후 실행되지 않던 마일리지 소멸을 운영 과제로 정리하고, CRM이 PM을 맡아 첫 시행까지 이끌었습니다. 대상자와 소멸액은 사전 시뮬레이션으로 검증했습니다.",
     '<p class="pf-note">약 2.5억 원은 소멸 처리된 마일리지 잔액이며, 비용 절감액이나 영업이익이 아닙니다.</p>',
     "마일리지 소멸 정책 pm 재무 전산 대행사 멤버십 요구사항"),
    (5, "crm", "분석 → 운영 기준", "SQL", "어뷰징 고객 선별 기준과 점검 프로세스 수립",
     ["혜택 대상에 이상 계정이 섞임", "구매 패턴 4단계 분류 + 영업·매장 확인", "반복 관리 가능한 운영 기준 수립"],
     ("828명", "확인 후 비활성화"), [("데이터로 선별", "1,080명"), ("분류", "고위험 · 의심 · 관찰 · 정상")], None,
     ["CRM 추출", "영업 검토", "매장 소명", "계정 조치", "후속 관리"],
     "구매 패턴만으로 바로 정지하지 않고, 영업부와 매장 확인을 거쳐 오판을 줄였습니다.",
     "<h4>분석 기준</h4><ul><li>전화번호당 계정 수</li><li>고객별 연간 전표와 매출</li><li>구매 매장과 반복 구매 패턴</li></ul>"
     "<h4>함께 운영</h4><ul><li>구매 실적 기준 월별 VIP 대상을 추출해 매장에 공유</li></ul>",
     "어뷰징 이상계정 비활성화 vip 매장 영업 sql 운영 기준"),
    (6, "crm", "개인 프로젝트", "Python · Streamlit · OpenAI API", "리테일 CRM 정책 벤치마크 DB 구축",
     ["경쟁사 정책 조사가 매번 일회성", "공식 출처 수집 + 공통 기준 표준화", "변경 이력까지 추적하는 대시보드"],
     ("72건", "검증한 CRM 사례"), [("공식 출처", "49개"), ("비교 기업", "8개")],
     ("crm-intelligence.jpg", "Retail CRM Intelligence 대시보드. CRM Insight, Company Intelligence, Change Radar 탭", 1363, 936, "공식 공개 자료 기반"),
     ["Notion DB에 사례 수집", "Python·Pandas로 공통 기준 표준화", "Streamlit으로 기업별 비교", "Change Log로 변경 모니터링"],
     "OpenAI API 요약 결과는 원문과 대조해 검증했습니다.",
     '<p class="pf-note">공개 프로토타입이며 내부 CRM 데이터와 분리되어 있습니다.</p>',
     "retail crm intelligence 벤치마크 openai api streamlit 개인 프로젝트"),
    (7, "crm", "외부 데이터 수집", "Python · Playwright", "경쟁 브랜드 SNS 크롤링 분석",
     ["경쟁 브랜드 SNS 운영을 비교할 데이터가 없음", "웹 크롤링으로 게시물·캠페인 이미지 수집", "게시 빈도·콘텐츠 형식 비교해 개선안 전달"],
     ("90일", "최근 게시물 수집 기간"), [("수집 대상", "게시물 · 캠페인 이미지"), ("비교 기준", "게시 빈도 · 형식")], None,
     ["Python·Playwright로 게시물과 이미지 수집", "브랜드별 게시 빈도와 콘텐츠 형식 비교", "자사 계정 운영 개선안을 PR 담당자에게 전달"],
     "공개 자료 조사를 매번 새로 하지 않도록, 비교 가능한 데이터로 만들었습니다.",
     "", "경쟁사 sns 크롤링 playwright python 게시물 캠페인 이미지 pr 콘텐츠"),
    (8, "mkt", "캠페인 성과 분석", "메가존 · GA · UTM", "쌤소나이트 캠페인 UTM · GA 분석과 A/B 테스트",
     ["프로모션·소재별 성과를 나눠 보기 어려움", "프로모션별 UTM 설정 + GA 분석 + A/B 테스트", "F1 광고 ROAS 467% → 645%"],
     ("645%", "F1 광고 ROAS (기존 467%)"), [("첫 구매 전환율", "51% 증가"), ("오픈한 기획전", "35건+")], None,
     ["프로모션별 UTM 설정", "GA 기반 유입·전환 분석", "광고 소재·랜딩페이지 A/B 테스트", "개선안 제안과 정기 리포트"],
     "종합광고대행사 AE로 Demandware 기반 쌤소나이트 공식몰과 DMC미디어 페이스북 광고 솔루션(F1)을 운영했습니다.",
     "", "메가존 쌤소나이트 ga utm a/b 테스트 f1 페이스북 광고 roas 전환율 demandware 기획전 ae"),
    (9, "md", "채널 · 물류 구축", "체리부로 · ERP · WMS", "온라인 채널 확장과 풀필먼트 체계 구축",
     ["채널이 늘며 주문·출고·재고 관리 부담 증가", "자사몰 런칭, 쿠팡 로켓배송·파스토 3PL 도입", "주문·출고·재고·정산 데이터가 연결된 운영 체계"],
     ("약 60억 원", "연간 온라인 매출 운영"), [("신규 채널", "자사몰 · 쿠팡 로켓배송"), ("물류", "네이버 파스토 3PL")], None,
     ["컬리·정육각 B2B 직매입, 오픈마켓 운영", "자사몰 런칭과 쿠팡 로켓배송 입점", "네이버 파스토 3PL 연계", "ERP·사방넷·3PL·WMS 데이터 연계"],
     "B2B 직매입과 B2C 채널을 함께 운영하며, 채널 확장에 맞춰 물류와 데이터 연계를 정비했습니다.",
     "", "체리부로 쿠팡 로켓배송 자사몰 파스토 3pl 풀필먼트 erp 사방넷 wms 컬리 정육각 b2b 온라인 md"),
    (10, "md", "판매 예측 · 프로모션", "체리부로 · 판매 데이터", "판매량 예측으로 시즌 프로모션 일정 조정",
     ["시즌 프로모션 시점을 감으로 정함", "판매량 예측 기반으로 프로모션 일정 조정", "평균 대비 3배 최대 월매출 달성"],
     ("3배", "평균 대비 최대 월매출"), [("쿠팡 광고 ROAS", "697% → 965%"), ("조정 근거", "판매량 예측")], None,
     ["판매 데이터로 수요 시점 예측", "시즌 프로모션 일정 조정", "쿠팡 광고 효율 개선"],
     "판매 데이터로 수요가 몰리는 시점을 예측하고, 프로모션 일정을 그에 맞췄습니다.",
     "", "체리부로 판매량 예측 시즌 프로모션 월매출 쿠팡 광고 roas"),
]

CATS = [("all", "전체"), ("crm", "CRM · 데이터"), ("md", "커머스 · MD"), ("mkt", "마케팅 · 광고")]

JOBS = [
    ("NOW", "2024.01 – 현재", "㈜인디에프 · 광고홍보팀 CRM 대리", "코스피 상장 패션기업 · 멤버십 22만 명, 300개 매장",
     ["Power BI 기반 <strong>현업 셀프 조회 체계</strong> 구축", "전사 마일리지 첫 소멸 <strong>14만+ 명 · 약 2.5억 원</strong>", "어뷰징 의심 1,080명 선별 → <strong>828명 비활성화</strong>"]),
    ("ONLINE MD", "2022.01 – 2023.05", "㈜체리부로 · 온라인팀 대리", "코스닥 상장 육계기업 · B2B 직매입과 B2C 채널",
     ["연간 약 <strong>60억 원</strong> 온라인 매출 운영, 자사몰 런칭·쿠팡 로켓배송 입점", "쿠팡 광고 ROAS <strong>697% → 965%</strong>", "판매량 예측으로 평균 대비 <strong>3배</strong> 최대 월매출"]),
    ("MD · MARKETING", "2019.03 – 2022.01", "㈜웅진투투럽 · 마케팅팀", "웅진 H&amp;B 계열사 · 수입 브랜드, 자사몰과 20개+ 채널",
     ["재포장·반품 위기 재고 <strong>1억 원 규모 전량 소진</strong>", "Meta 광고 최대 ROAS <strong>1,734%</strong>", "올리브영·LF몰 등 주요 유통채널 추가 입점"]),
    ("AE", "2018.03 – 2018.10", "㈜메가존 · 펜타클 광고사업부 AE", "종합광고대행사 · 쌤소나이트 공식몰과 캠페인",
     ["기획전 <strong>35건+</strong> 오픈", "F1 광고 ROAS <strong>467% → 645%</strong>, 첫 구매 전환율 <strong>51% 증가</strong>"]),
    ("MARKETING", "2017.05 – 2018.01", "㈜문정아중국어연구소 · 마케팅팀", "교육 전문기업 · SNS 콘텐츠, PR, 검색광고", []),
]

HIGHLIGHTS = [(4, "마일리지 첫 소멸", "14만+ 명"), (5, "어뷰징 계정 비활성화", "828명"), (8, "F1 광고 ROAS", "645%"),
              (10, "평균 대비 최대 월매출", "3배"), (6, "검증한 CRM 사례", "72건")]
CAREER_RAIL = [("인디에프", "CRM 데이터", "2024 –"), ("체리부로", "온라인 MD", "2022 – 23"), ("웅진투투럽", "MD · 마케팅", "2019 – 22"),
               ("메가존", "광고 AE", "2018"), ("문정아중국어", "마케팅", "2017")]

ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="i-home" viewBox="0 0 24 24"><path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z"/></symbol>
  <symbol id="i-projects" viewBox="0 0 24 24"><path d="M12 3 2 8l10 5 10-5z"/><path d="m2 13 10 5 10-5"/></symbol>
  <symbol id="i-career" viewBox="0 0 24 24"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/></symbol>
  <symbol id="i-skills" viewBox="0 0 24 24"><rect x="3" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="1.5"/></symbol>
  <symbol id="i-mail" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></symbol>
  <symbol id="i-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></symbol>
  <symbol id="i-chevron" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></symbol>
</svg>"""


def post(p, img_src=lambda f: "assets/" + f):
    n, cat, label, stack, title, psr, hero, rows, shot, steps, lead, extra, search = p
    nums = ""
    if hero:
        nums += f'<div class="pf-media__hero"><b>{hero[0]}</b><span>{hero[1]}</span></div>'
    nums += '<dl class="pf-media__rows">' + "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in rows) + "</dl>"
    shot_html = ""
    if shot:
        f, alt, w, h, cap = shot
        shot_html = f'<figure class="pf-media__shot"><img src="{img_src(f)}" alt="{alt}" width="{w}" height="{h}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
    flow = '<ol class="pf-flow">' + "".join(f"<li>{s}</li>" for s in steps) + "</ol>"
    return f"""
      <article class="pf-post" id="p{n:02d}" data-cat="{cat}" data-search="{search}">
        <div class="pf-post__eyebrow"><b>PROJECT {n:02d}</b><span>{label}</span><span>·</span><span>{stack}</span></div>
        <h2 class="pf-post__title">{title}</h2>
        <dl class="pf-post__psr">
          <dt>문제</dt><dd>{psr[0]}</dd>
          <dt class="is-how">방법</dt><dd>{psr[1]}</dd>
          <dt class="is-result">결과</dt><dd class="is-result">{psr[2]}</dd>
        </dl>
        <div class="pf-media{' has-shot' if shot else ''}">
          <div class="pf-media__nums">{nums}</div>{shot_html}
        </div>
        <details class="pf-detail">
          <summary>어떻게 진행했나 <svg class="pf-icon"><use href="#i-chevron"/></svg></summary>
          <div class="pf-detail__body">
            <p>{lead}</p>
            <h4>진행 순서</h4>{flow}{extra}
          </div>
        </details>
      </article>"""


def job(j):
    tag, period, title, desc, wins = j
    w = ('<ul class="pf-job__wins">' + "".join(f"<li>{x}</li>" for x in wins) + "</ul>") if wins else ""
    return f"""
      <article class="pf-job">
        <div class="pf-job__period"><b>{tag}</b>{period}</div>
        <h2 class="pf-job__title">{title}</h2>
        <p class="pf-job__desc">{desc}</p>{w}
      </article>"""


def chips(items, brand=()):
    return '<div class="pf-chips">' + "".join(
        f'<span class="pf-chip{" pf-chip--brand" if i in brand else ""}">{i}</span>' for i in items) + "</div>"


def body(img_src=lambda f: "assets/" + f):
    counts = {k: sum(1 for p in PROJECTS if k == "all" or p[1] == k) for k, _ in CATS}
    filt = "".join(
        f'<button class="pf-filter__btn" aria-pressed="{"true" if k == "all" else "false"}" data-cat="{k}">{v} <span>{counts[k]}</span></button>'
        for k, v in CATS)
    posts = "".join(post(p, img_src) for p in PROJECTS)
    jobs = "".join(job(j) for j in JOBS)
    hl = "".join(f'<a class="pf-row" href="#p{n:02d}" data-jump="p{n:02d}"><span class="pf-row__title">{t}</span><span class="pf-row__value">{v}</span></a>' for n, t, v in HIGHLIGHTS)
    cr = "".join(f'<div class="pf-row" style="cursor:default"><span class="pf-row__title"><b style="color:var(--ink)">{a}</b> · {b}</span><span class="pf-row__meta">{c}</span></div>' for a, b, c in CAREER_RAIL)
    return f"""{ICONS}
<div class="pf-shell">
  <header class="pf-shell__nav">
    <nav class="pf-nav" aria-label="주요 메뉴">
      <a class="pf-nav__brand" href="#top"><b>임보라</b><span>CRM 데이터 · 9년</span></a>
      <ul class="pf-nav__list">
        <li><a class="pf-nav__item" href="#top" data-tab="projects" aria-current="page"><svg class="pf-icon"><use href="#i-home"/></svg><span class="pf-nav__label">홈</span></a></li>
        <li><a class="pf-nav__item" href="#tabs" data-tab="projects"><svg class="pf-icon"><use href="#i-projects"/></svg><span class="pf-nav__label">프로젝트</span></a></li>
        <li><a class="pf-nav__item" href="#tabs" data-tab="career"><svg class="pf-icon"><use href="#i-career"/></svg><span class="pf-nav__label">경력</span></a></li>
        <li><a class="pf-nav__item" href="#tabs" data-tab="skills"><svg class="pf-icon"><use href="#i-skills"/></svg><span class="pf-nav__label">역량</span></a></li>
        <li><a class="pf-nav__item" href="mailto:{EMAIL}"><svg class="pf-icon"><use href="#i-mail"/></svg><span class="pf-nav__label">연락하기</span></a></li>
      </ul>
      <div class="pf-nav__contact">이메일<a href="mailto:{EMAIL}">{EMAIL}</a></div>
    </nav>
  </header>

  <main class="pf-shell__feed" id="top">
    <section class="pf-intro" aria-label="소개">
      <div class="pf-intro__tag"><span class="pf-dot"></span>CJ올리브영 데이터 사업 담당자 지원</div>
      <h1 class="pf-intro__name">임보라<small>CRM 데이터 담당 · ㈜인디에프</small></h1>
      <p class="pf-intro__bio">마케팅 현장의 문제를 데이터 분석과 시스템으로 해결해 왔습니다. 분석을 리포트로 끝내지 않고, 현업이 직접 쓰는 조회 화면과 운영 기준으로 바꿉니다.</p>
      <ul class="pf-intro__stats">
        <li><b>9년</b><span>리테일 · 커머스</span></li>
        <li><b>22만</b><span>멤버십 회원 분석</span></li>
        <li><b>300개</b><span>매장 데이터</span></li>
        <li><b>20+</b><span>온·오프라인 채널</span></li>
      </ul>
    </section>

    <div class="pf-tabs" role="tablist" id="tabs" aria-label="포트폴리오 섹션">
      <button class="pf-tab" role="tab" id="tab-projects" aria-controls="panel-projects" aria-selected="true">프로젝트</button>
      <button class="pf-tab" role="tab" id="tab-career" aria-controls="panel-career" aria-selected="false" tabindex="-1">경력</button>
      <button class="pf-tab" role="tab" id="tab-skills" aria-controls="panel-skills" aria-selected="false" tabindex="-1">역량</button>
    </div>

    <section class="pf-panel" role="tabpanel" id="panel-projects" aria-labelledby="tab-projects">
      <div class="pf-filter" role="group" aria-label="분야 필터">{filt}</div>{posts}
      <div class="pf-empty" id="empty" hidden>조건에 맞는 프로젝트가 없습니다.</div>
    </section>

    <section class="pf-panel" role="tabpanel" id="panel-career" aria-labelledby="tab-career" hidden>{jobs}
    </section>

    <section class="pf-panel" role="tabpanel" id="panel-skills" aria-labelledby="tab-skills" hidden>
      <div class="pf-block">
        <h2 class="pf-block__title">직무와 연결되는 경험</h2>
        <ul class="pf-fit">
          <li><b>마케팅 데이터 해석</b><span>CRM 캠페인과 구매·매출 성과를 연결해 후속 운영 방향을 정했습니다.</span></li>
          <li><b>SQL · Python · BI</b><span>Azure SQL 데이터를 Power BI와 Streamlit으로 분석하고 조회 화면을 만들었습니다.</span></li>
          <li><b>요구사항 구조화</b><span>서비스 화면과 멤버십 운영에 필요한 데이터 기준과 예외 조건을 정했습니다.</span></li>
          <li><b>문서화와 협업</b><span>전산팀·외부 개발사·대행사와 구현 결과를 확인했습니다.</span></li>
        </ul>
      </div>
      <div class="pf-block">
        <h2 class="pf-block__title">일하는 방식</h2>
        <ol class="pf-flow"><li>문제와 지표 정의</li><li>SQL · Python 분석</li><li>실행안 제안</li><li>기능 · 운영 기준 정리</li><li>가이드와 활용 확산</li></ol>
      </div>
      <div class="pf-block">
        <h2 class="pf-block__title">활용 도구</h2>
        <dl class="pf-tools">
          <dt>데이터 · CRM</dt><dd>{chips(["SQL", "Python / Pandas", "Azure SQL", "Dynamics 365"], ("SQL",))}</dd>
          <dt>분석 · 시각화</dt><dd>{chips(["Power BI", "Streamlit", "GA4", "GTM"], ("Power BI",))}</dd>
          <dt>자동화 · AI</dt><dd>{chips(["Playwright", "OpenAI API"])}</dd>
          <dt>커머스 · 광고</dt><dd>{chips(["SMS/LMS/MMS", "Kakao", "Meta Ads", "Naver SA", "Cafe24", "Demandware", "사방넷", "ERP", "WMS · 3PL"])}</dd>
          <dt>어학 · 자격</dt><dd>{chips(["新HSK 6급", "MOS Expert", "GTQ 1급"])}</dd>
        </dl>
      </div>
    </section>
  </main>

  <aside class="pf-shell__rail" aria-label="요약">
    <div class="pf-shell__rail-inner">
      <label class="pf-search pf-rail-search">
        <svg class="pf-icon"><use href="#i-search"/></svg>
        <span class="pf-visually-hidden">프로젝트 검색</span>
        <input type="search" id="q" placeholder="프로젝트 검색 (예: SQL, 쿠팡)">
      </label>
      <section class="pf-card">
        <h2 class="pf-card__title">핵심 성과</h2>{hl}
        <div class="pf-card__foot"></div>
      </section>
      <section class="pf-card">
        <h2 class="pf-card__title">경력</h2>{cr}
        <div class="pf-card__foot"></div>
      </section>
      <p class="pf-legal">화면 캡처의 수치·식별정보는 모자이크 처리했습니다. © 2026 임보라</p>
    </div>
  </aside>
</div>
"""


SCRIPT = """<script>
(function () {
  var tabs = [].slice.call(document.querySelectorAll('.pf-tab'));
  var navItems = [].slice.call(document.querySelectorAll('.pf-nav__item[data-tab]'));
  var posts = [].slice.call(document.querySelectorAll('#panel-projects .pf-post'));
  var q = document.getElementById('q'), empty = document.getElementById('empty'), cat = 'all';
  function select(name, focus) {
    tabs.forEach(function (t) {
      var on = t.id === 'tab-' + name;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
      if (on && focus) t.focus();
    });
    navItems.forEach(function (n, i) {
      var cur = n.getAttribute('data-tab') === name && (name !== 'projects' || i === 1);
      if (cur) n.setAttribute('aria-current', 'page'); else n.removeAttribute('aria-current');
    });
  }
  function filter() {
    var v = q.value.trim().toLowerCase(), shown = 0;
    posts.forEach(function (p) {
      var ok = (cat === 'all' || p.getAttribute('data-cat') === cat) &&
        (!v || (p.getAttribute('data-search') + ' ' + p.textContent).toLowerCase().indexOf(v) > -1);
      p.hidden = !ok; if (ok) shown++;
    });
    empty.hidden = shown > 0;
  }
  function setCat(c) {
    cat = c;
    document.querySelectorAll('.pf-filter__btn').forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-cat') === c ? 'true' : 'false'); });
    filter();
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { select(t.id.slice(4)); });
    t.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (d) { select(tabs[(i + d + tabs.length) % tabs.length].id.slice(4), true); e.preventDefault(); }
    });
  });
  navItems.forEach(function (a) { a.addEventListener('click', function () { select(a.getAttribute('data-tab')); }); });
  document.querySelectorAll('.pf-filter__btn').forEach(function (b) { b.addEventListener('click', function () { setCat(b.getAttribute('data-cat')); }); });
  document.querySelectorAll('[data-jump]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      e.preventDefault(); select('projects'); q.value = ''; setCat('all');
      document.getElementById(a.getAttribute('data-jump')).scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
  q.addEventListener('input', function () { select('projects'); filter(); });
})();
</script>"""

HEAD = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>임보라 · CRM 데이터 포트폴리오</title>
<meta name="description" content="온라인 MD·마케팅·CRM을 거친 9년 차 리테일 경력. 프로젝트 10건을 문제·방법·결과로 정리한 포트폴리오.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body class="pf-root">
"""

if __name__ == "__main__":
    (ROOT / "index.html").write_text(HEAD + body() + SCRIPT + "\n</body>\n</html>\n", encoding="utf-8")
    print("wrote index.html")
