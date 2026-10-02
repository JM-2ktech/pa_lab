# Power Automate 업무 자동화 실습

Cloud Flow 기반 DPA(1일차)와 Power Automate Desktop 기반 RPA(2일차)를 다루는 **2일 핸즈온 교안**입니다.

배포: `https://jm-2ktech.github.io/pa_lab/`

## 무엇을 다루나

| 랩 | 분 | 내용 |
|---|---|---|
| Lab 1 | 75 | 첫 클라우드 흐름 — SharePoint 목록 · 조건 · Outlook · Teams · 예약 트리거와 식 |
| Lab 2 | 90 | 정기점검 보고서 — Excel 표 취합 · 배열 필터링 · HTML 보고서 파일 생성 |
| Lab 3 | 85 | 정기점검 보고서 — 승인 · 승인/반려 분기 · 공유 링크 배포 |
| Lab 4 | 80 | Desktop 흐름 기본 — 변수 · 조건 · 반복 · 파일과 폴더 · Excel |
| Lab 5 | 70 | 웹 자동화 — 입력 · 검색 · 여러 쪽 표 추출 · Excel 저장 |
| Lab 6 | 95 | 고객계약 발굴 — 키워드 반복 · 조건 거르기 · 예외 처리 · 결과 파일 |

**핸즈온 495분.** 표의 시간은 손을 움직이는 시간만입니다. 랩마다 개념 설명과 마무리로 10분 정도가 더 붙습니다.

## 준비물

- Microsoft 365 계정과 Power Platform 환경(Environment Maker)
- SharePoint 팀 사이트 하나 — 수강생 전원이 구성원
- 2일차: Power Automate Desktop과 Edge 확장

## 로컬에서 보기

```bash
bundle install
bundle exec jekyll serve --port 4002
```

`http://localhost:4002/pa_lab/` 에서 확인할 수 있습니다.

## 폴더 구조

```
pa_lab/
├── _config.yml                  Jekyll 설정
├── _sass/custom/custom.scss     커스텀 스타일 (정본 cs_lab)
├── .github/workflows/pages.yml  GitHub Pages 배포
├── index.md                     홈
├── docs/lab1.md ~ lab6.md       Lab 1~6
├── practice/bid/                Lab 5·6 웹 자동화 대상 — 모의 공고 사이트
└── assets/
    ├── lab1/ ~ lab6/            스텝 스크린샷
    └── download/                실습용 배포 파일
```

## 실습 자료

- `assets/download/점검기록.xlsx` — Lab 2·3
- `assets/download/PA실습.zip` — Lab 4~6
- `practice/bid/` — 모의 공고 사이트. 데이터는 `practice/bid/data.js`

> 회사·기관·공고·금액은 전부 **가상**입니다.

## 저작 규칙

- **랩 1개 = 1페이지.** 평평한 번호 시퀀스만 씁니다.
- **「예상 시간」은 순수 핸즈온 시간입니다.** 스텝 하나당 1.5분으로 잡습니다.
- **절을 여러 개로 쪼갤 때는 `{: start="N" }`** 을 붙입니다.
