---
title: "C1. Power Automate 지도"
parent: "개념 1. 흐름의 구성"
nav_order: 1
concept:
  id: C1
  grade: A
  used_in: "Lab 1 ② 인스턴트 흐름 · Lab 4 ① 시작"
  tokens: ["클라우드 흐름", "Desktop 흐름"]
  sample: false
---

# C1. Power Automate 지도

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안. 샘플 없음.
     ⚠️ 개념_후보.md 는 세 유형을 클라우드 · 데스크톱 · 비즈니스 프로세스 흐름으로 적었다. 현재 flow-types 문서는 영어판 · 한국어판 모두 클라우드 · 데스크톱 · 생성 작업(미리 보기)이다. 비즈니스 프로세스 흐름은 별도 문서이므로 절을 나눴다.
     ⚠️ 실측할 것: 왼쪽 메뉴 라벨(문서는 「더보기」 · 「학습」, Lab 1 실측은 「+ 만들기」), 교육 계정의 라이선스(설정 › 내 라이선스 보기), 생성 작업이 교육 환경의 작업 추가 창에 보이는지 -->

> **다루는 것**: Power Automate 가 제공하는 흐름의 유형, 만드는 곳과 다루는 대상, 포털 메뉴와 환경, 라이선스별 기능
>
> **쓰는 곳**: 1일차 Lab 1~3 은 클라우드 흐름, 2일차 Lab 4~7 은 데스크톱 흐름 · Lab 1 9~11번 Power Automate 홈과 환경 · Lab 4 ① 콘솔

---

## 흐름의 유형

Power Automate 문서는 흐름을 세 유형으로 나눕니다. 유형마다 따로 쓸 수 있고 함께 쓸 수도 있습니다.[^types]

| 유형 | 자동화하는 것 | 시작 방법 |
|---|---|---|
| 클라우드 흐름 | 앱과 서비스를 잇는 작업 | 이벤트 · 단추 · 일정 |
| 데스크톱 흐름 | 웹과 PC 프로그램의 화면 조작, 파일과 폴더 | 콘솔 · 디자이너 · 클라우드 흐름의 호출 |
| 생성 작업(미리 보기) | 의도만 적으면 AI 가 작업과 순서를 고르는 작업 | 클라우드 흐름 안의 작업으로 실행 |

생성 작업은 미리 보기 기능이며 운영 용도로 제공되지 않습니다. 입력은 텍스트만 받고 쓸 수 있는 커넥터도 정해져 있습니다.[^gen]

---

## 클라우드 흐름과 데스크톱 흐름

두 유형은 만드는 곳과 다루는 대상이 다릅니다.[^desktop]

| 항목 | 클라우드 흐름 | 데스크톱 흐름 |
|---|---|---|
| 이 과정의 표기 | Cloud Flow · DPA | PAD · RPA |
| 만드는 곳 | 웹 포털의 디자이너 | PC에 설치한 Power Automate 앱의 디자이너 |
| 다루는 대상 | 커넥터가 있는 앱과 서비스 | 웹 앱 · 데스크톱 앱 · 터미널 에뮬레이터 같은 구형 앱 · Excel 파일 · 폴더 |
| 대상에 닿는 방법 | 커넥터의 트리거와 작업, 계정 연결 | UI 요소 · 이미지 · 좌표 |
| 시작 | 트리거 | 사람의 실행 또는 클라우드 흐름의 호출 |
| 실행 위치 | Power Automate 클라우드 서비스 | 데스크톱 컴퓨터 |

클라우드 흐름은 **Run a flow built with Power Automate for desktop** 작업으로 데스크톱 흐름을 실행합니다.[^arch] 이 작업이 속한 Desktop flows 커넥터는 프리미엄 등급입니다.[^premium] 자세한 조건은 [P24](p24-from-cloud.html)에서 다룹니다.

---

## 비즈니스 프로세스 흐름

문서의 흐름 유형 목록과 별도로 비즈니스 프로세스 흐름이 있습니다. 사람이 앱에서 데이터를 입력할 때 따라갈 단계를 안내하는 기능입니다.[^bpf]

| 항목 | 내용 |
|---|---|
| 하는 일 | 스테이지와 스텝을 양식 위쪽 컨트롤로 표시 |
| 스텝 | 데이터를 입력할 열 하나 |
| 다음 스테이지로 가는 조건 | 필수로 지정한 스텝이 채워져 있을 것 |
| 범위 | 테이블 하나 또는 최대 5개 |
| 한도 | 테이블당 활성 10개, 프로세스당 스테이지 30개 |
| 자동화 | 조건 논리와 자동화를 직접 제공하지 않음. 다른 프로세스와 함께 씀 |
| Office 365 라이선스 | 포함되지 않음 |

---

## 라이선스별 기능

Office 365 라이선스에는 자동화 · 예약 · 단추 클라우드 흐름이 포함됩니다.[^faq] 나머지 기능은 라이선스에 따라 다릅니다.[^faq][^licenses]

| 기능 | Office 365 | Windows | Power Automate Premium |
|---|---|---|---|
| 표준 커넥터 | 포함 | 없음 | 포함 |
| 프리미엄 커넥터 | Dataverse for Teams 환경에서만 | 없음 | 포함 |
| 사용자 지정 커넥터 | 없음 | 없음 | 포함 |
| 비즈니스 프로세스 흐름 | 없음 | 없음 | 포함 |
| 온-프레미스 게이트웨이 | 없음 | 없음 | 포함 |
| 유인 RPA | 없음 | 기본 환경에서만 | 유인 봇 1개 |
| 무인 RPA | 없음 | 없음 | 없음. Process 라이선스에 포함 |
| 하루 작업 수 | 6,000 | 해당 없음 | 40,000 |

본인의 라이선스는 포털 위쪽 톱니 단추의 **내 라이선스 보기**에서 확인합니다.[^home]

---

## 포털 메뉴

Power Automate 포털의 왼쪽 메뉴입니다.[^home]

| 메뉴 | 하는 일 |
|---|---|
| 홈 | Power Automate 시작 화면 |
| 만들기 | Copilot · 템플릿 · 처음부터 흐름 만들기 |
| 템플릿 | 흐름 템플릿 보기와 검색 |
| 학습 | 제품 문서로 이동 |
| 내 흐름 | 내가 만들었거나 공유받은 흐름 |
| 승인 · 솔루션 · 프로세스 마이닝 등 | 자주 쓰는 페이지. 고정과 해제 가능 |
| 더보기 | 테이블 · 클라우드 흐름 활동 · 연결 등. 항목별 고정 가능 |
| Power Platform | Power Apps · Power BI · 관리 센터 등으로 이동 |

위쪽에는 검색 칸, 환경 선택, 톱니(설정), 물음표(도움말)가 있습니다.

---

## 환경

환경은 작업 종류 사이에 경계를 만듭니다. 부서별로 나누거나 개발 중인 흐름과 사용할 흐름을 나눌 때 씁니다.[^home] 이 과정의 환경은 `{{ site.pa.environment }}` 입니다.

| 항목 | 내용 |
|---|---|
| 확인하는 곳 | 포털 위쪽 오른쪽의 환경 선택 |
| 목록의 구분 | 빌드 흐름 · 기타 환경 |
| 기타 환경 | 읽기 전용이고 승인에 접근할 수 있는 환경 |
| 환경 사이 이동 | 구성 요소를 쉽게 옮길 수 없음 |
| 흐름의 범위 | 한 환경에서 만든 흐름은 다른 환경에서 보이지 않음 |

흐름을 만들기 전에 환경을 확인합니다. 솔루션과 환경 변수는 [C23](c23-solutions.html)에서 다룹니다.

---

## 흐름을 만드는 방법

클라우드 흐름은 Copilot 으로 만들거나 처음부터 만듭니다.[^cloud]

| 방법 | 시작하는 곳 | 조건 |
|---|---|---|
| 처음부터 | 만들기 › 시작(처음부터) | 유형과 트리거를 직접 고름 |
| 템플릿 | 만들기 또는 템플릿 | 템플릿에서 시작해 디자이너에서 구성 |
| Copilot | 홈의 Copilot 입력 칸 | 새 디자이너에서만 지원. 관리자가 끌 수 있음. 프롬프트가 유형을 정함 |

이 과정의 랩은 처음부터 만듭니다. Copilot 은 [C29](c29-copilot.html)에서 다룹니다.

---

## 함께 쓰는 제품

| 제품 | Power Automate 와의 관계 |
|---|---|
| Azure Logic Apps | Power Automate 의 워크플로 엔진.[^connectors] 식 함수 참조 문서가 Logic Apps 문서 아래에 있고 두 제품에 함께 적용됨[^functions] |
| Power Apps | 연결을 공유함.[^connections] Power Apps 에서도 흐름을 만들고 관리함[^types] |
| Copilot Studio | 같은 커넥터를 씀[^connectors] |

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다.

- **문헌**: Power Automate란?[^types] · 클라우드 흐름 개요[^cloud] · 데스크톱 흐름 소개[^desktop] · Power Automate for desktop 아키텍처[^arch] · 생성 작업[^gen] · 비즈니스 프로세스 흐름[^bpf] · 라이선스 FAQ[^faq] · 라이선스 유형[^licenses] · 프리미엄 커넥터 목록[^premium] · 홈 페이지 살펴보기[^home] · 커넥터 개요[^connectors] · 연결 관리[^connections] · 식 함수 참조[^functions]

[^types]: **What is Power Automate?** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/flow-types> (2026-11-02 확인). 세 유형과 Power Apps 안에서 흐름을 만들고 관리하는 것.
[^cloud]: **Overview of cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/overview-cloud> (2026-11-02 확인). Copilot 과 처음부터 만들기의 차이, Copilot 이 새 디자이너에서만 된다는 것.
[^desktop]: **Introduction to desktop flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/introduction> (2026-11-02 확인). 대상 앱의 범위, UI 요소 · 이미지 · 좌표로 조작한다는 것, Windows 앱에 로그인해 쓴다는 것.
[^arch]: **Power Automate for desktop architecture** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/pad-architecture> (2026-11-02 확인). 데스크톱 컴퓨터에서 도는 서비스, 클라우드에서 실행할 때 쓰는 작업 이름.
[^gen]: **Use generative actions in cloud flows (preview)** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/generative-actions-overview> (2026-11-02 확인). 미리 보기 조건, 텍스트 입력, 커넥터 제한.
[^bpf]: **Business process flows overview** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/business-process-flows-overview> (2026-11-02 확인). 스테이지와 스텝, 한도, 자동화를 직접 제공하지 않는다는 것.
[^faq]: **Power Automate licensing FAQ** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-platform/admin/power-automate-licensing/faqs> (2026-11-02 확인). Office 365 · Windows 라이선스의 기능 표.
[^licenses]: **Types of Power Automate licenses** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-platform/admin/power-automate-licensing/types> (2026-11-02 확인). Premium · Process 라이선스의 기능 표.
[^premium]: **List of all Premium tier connectors** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/connectors/connector-reference/connector-reference-premium-connectors> (2026-11-02 확인). Desktop flows 커넥터의 등급.
[^home]: **Explore the Power Automate home page** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/getting-started> (2026-11-02 확인). 왼쪽 메뉴, 환경 선택, 환경의 범위, 설정 메뉴.
[^connectors]: **Connectors overview** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/connectors/overview> (2026-11-02 확인). 커넥터를 쓰는 제품들, Logic Apps 가 Power Automate 의 워크플로 엔진이라는 것.
[^connections]: **Manage connections in Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/add-manage-connections> (2026-11-02 확인). 연결이 Power Apps 와 공유된다는 것.
[^functions]: **Reference guide to functions in expressions for workflows in Azure Logic Apps and Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/workflow-definition-language-functions-reference> (2026-11-02 확인). 이 참조가 Logic Apps 문서에 있고 Power Automate 에도 적용된다는 것.
