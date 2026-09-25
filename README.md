# 임보라 · CRM 데이터 포트폴리오

경력기술서의 핵심 사례를 **문제 · 방법 · 결과**로 정리한 포트폴리오 웹사이트입니다. X(Twitter)처럼 3단(내비게이션 · 피드 · 요약 레일)으로 구성되어 있습니다.

- `index.html` — 사이트 본문 (프로젝트 10건 · 경력 5곳 · 역량, `build/build_site.py`가 생성)
- `styles.css` — 디자인 시스템 토큰 + 컴포넌트 스타일 + 반응형 규칙
- `assets/` — 모자이크 처리된 화면 캡처

빌드 과정이 없는 정적 사이트라 `index.html`을 브라우저로 바로 열면 됩니다.

- `portfolio.pdf` — 같은 내용을 16:9 PDF로 정리한 버전. 왼쪽 메뉴·목록·이전/다음을 클릭하면 해당 페이지로 이동합니다.
- 다시 만들기: `python3 build/build_site.py` (웹), `python3 build/build_pdf.py <폰트 폴더> && node build/render_pdf.js` (PDF, Noto Sans KR TTF 필요)
