---
title: "C25. 제한과 스로틀링"
parent: "더 읽을거리 · Cloud Flow"
nav_order: 25
concept:
  id: C25
  grade: C
  used_in: "랩에서 쓰지 않음"
  tokens: []
  sample: false
---

# C25. 제한과 스로틀링

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안. 샘플 없음.
     ⚠️ 실측할 것: 교육 계정의 성능 프로필(설정 › 내 라이선스 보기), 흐름 세부 정보의 분석 메뉴 라벨
     ⚠️ 문서 사이 차이: 실행 기록 보관을 limits-and-config 는 30일, 화면과 문제 해결 문서는 28일로 적는다. 트리거 동시성 기본값은 C26 에 적었다.
     한국어판 limits-and-config 는 수치가 영어판과 같고 이름 번역이 어긋난다(Characters per expression → 식당 문자 수, Switch scope cases limit → 범위 케이스 제한 전환). -->

> **다루는 것**: 흐름에 걸리는 한도 가운데 흐름을 설계할 때 쓰는 값, 스로틀링이 왔을 때의 구분과 대응
>
> **쓰는 곳**: 랩에서 쓰지 않음

---

## 성능 프로필

흐름의 요청 한도는 성능 프로필로 정해집니다. 성능 프로필은 흐름 소유자의 플랜을 따릅니다.[^limits]

| 프로필 | 플랜 |
|---|---|
| 낮음 | 무료 · Microsoft 365 · Power Apps Plan 1 · Power Apps 앱당 · Power Automate Plan 1 · 모든 평가판 · Dynamics 365 Team Member · Power Apps for Developer |
| 중간 | Power Apps로 시작한 흐름 · 수동 흐름 · 하위 흐름 · Power Apps Plan 2 · Power Apps 사용자당 · Power Automate Plan 2 · Power Automate Premium · Dynamics 365 Enterprise · Professional |
| 높음 | Power Automate Process · 흐름당 플랜 |
| 무제한 연장 | 종량제 흐름 · 서비스 주체로 실행되는 Dynamics 컨텍스트 흐름 |

- 플랜이 여러 개면 높은 쪽 프로필을 씁니다.
- 원래 소유자가 조직을 떠나면 낮음으로 돌아갑니다.
- 본인 플랜은 제목 표시줄의 **설정**에서 **내 라이선스 보기**로 확인합니다.

---

## 일일 요청 한도

작업 하나를 실행할 때마다 Power Platform 요청 1건을 씁니다. 공식 한도와 현재 적용 중인 전환 기간 한도가 따로 있습니다.[^requests]

| 라이선스 | 공식 한도(24시간) | 전환 기간 한도(24시간) |
|---|---:|---:|
| Microsoft 365 · Power Automate 무료 · Dynamics 365 Team Member | 사용자당 6,000 | 흐름당 10,000 |
| Power Automate Premium · Power Apps Premium · Dynamics 365 Enterprise · Professional | 사용자당 40,000 | 흐름당 200,000 |
| Power Automate Process · Hosted Process · 흐름당 플랜 | 라이선스당 250,000 | 라이선스당 500,000 |

- 전환 기간이 끝나면 Premium과 기본 포함 라이선스는 사용자 단위 한도로 바뀝니다. 문서는 사용자 단위 한도에 맞춰 설계하라고 권장합니다.
- 5분당 한도는 라이선스와 관계없이 100,000건입니다.
- 24시간은 슬라이딩 창입니다. 남은 요청은 다음 날로 넘어가지 않습니다.
- 인스턴트 흐름은 시작한 사용자의 한도를, 예약 · 자동화 흐름은 소유자의 한도를 씁니다.
- 데스크톱 흐름 실행은 Power Platform 요청을 쓰지 않습니다.

---

## 요청으로 세는 것

| 대상 | 세는 방법 |
|---|---|
| 트리거와 작업 | 각 1건. 트리거 1개와 작업 1개인 흐름은 실행마다 2건 |
| 기본 제공 작업 | 변수 초기화 · 범위 · 작성 포함 |
| 성공 · 실패한 작업 | 셈 |
| 건너뛴 작업 | 세지 않음 |
| 각각에 적용 안의 작업 | 항목 수만큼 |
| 한 작업 안의 여러 식 | 1건 |
| 재시도 · 페이지 매김 요청 | 셈 |

흐름이 실제로 쓴 작업 수는 흐름 세부 정보의 **분석**에서 작업 탭으로 봅니다.[^guide]

---

## 흐름 정의 한도

흐름 하나를 만들 때 걸리는 한도입니다.[^limits]

| 항목 | 한도 |
|---|---:|
| 흐름당 작업 수 | 500 |
| 작업 중첩 깊이 | 8 |
| Switch 케이스 | 25 |
| 흐름당 변수 | 250 |
| 작업 · 트리거 이름 길이 | 80자 |
| 식 길이 | 8,192자 |
| 설명 길이 | 256자 |
| `concat()` · `base64()` · `string()` 결과 길이 | 131,072자 |
| 요청 URL 길이 | 16,384자 |
| 사용자당 소유 흐름 | 600개. 솔루션 흐름은 제외 |

작업이 500개보다 적어도 많으면 편집이 느려집니다. 중첩 깊이나 작업 수가 모자라면 [C30](c30-child-versions.html)의 하위 흐름으로 나눕니다.

---

## 실행 시간과 흐름 꺼짐

| 항목 | 한도 | 내용 |
|---|---:|---|
| 실행 시간 | 30일 | 시작 시각부터 계산. 승인 대기 포함. 30일 후 대기 단계는 시간 초과 |
| 실행 기록 보관 | 30일 | 흐름 세부 정보 화면은 28일 실행 기록 |
| 되풀이 간격 | 60초~500일 | 예약 트리거 |
| 연기 최소 간격 | 낮음 5초, 그 외 1초 | |
| 계속 실패하는 흐름 | 14일 | 트리거나 작업이 계속 실패하면 꺼짐 |
| 계속 스로틀되는 흐름 | 14일 | 꺼짐. 소유자에게 메일 통보 |
| 트리거가 없는 흐름 | 90일 | 꺼질 수 있음. 30일 전에 통보. 프리미엄 · 용량 라이선스 소유 흐름은 제외 |

꺼진 흐름은 다시 켤 수 있습니다. 한도를 계속 넘으면 다시 꺼집니다.[^guide]

흐름을 끄면 새 실행만 시작되지 않고 진행 중인 실행은 끝까지 돕니다. 흐름을 삭제하면 진행 중인 실행도 취소됩니다. 10분 넘게 도는 흐름을 테스트하면 시간 초과 메시지가 뜰 수 있으나 흐름은 뒤에서 계속 실행됩니다.[^limits]

---

## 반복과 동시 실행

| 항목 | 한도 | 내용 |
|---|---|---|
| 각각에 적용 항목 수 | 낮음 5,000, 그 외 100,000 | 넘으면 `WorkflowRunActionRepetitionQuotaExceeded` |
| 각각에 적용 동시 실행 | 기본 1, 최대 50 | [C18](c18-loops.html) |
| Until 반복 | 기본 60, 최대 5,000 | |
| 페이지 매김 항목 수 | 낮음 5,000, 그 외 100,000 | 작업별 기본값은 [C14](c14-limits.html) |
| 흐름 동시 실행 | 동시성 제어를 끄면 무제한, 켜면 1~100 | [C26](c26-trigger-conditions.html) |
| 대기 실행 | 켰을 때 10 + 병렬도 | 넘은 트리거는 재시도되거나 실패할 수 있음 |
| 분할(Split on) 항목 | 낮음 5,000, 그 외 100,000. 트리거 동시성을 켜면 100 | |

---

## 요청 크기와 시간

| 항목 | 한도 |
|---|---|
| 메시지 크기 | 100MB. 파일을 보낼 때는 페이로드 전체 기준 |
| 청크 분할 메시지 | 1GB. 청크를 지원하는 작업만 |
| 나가는 동기 요청 | 120초 |
| 나가는 비동기 요청 | 최대 30일까지 설정 |
| 들어오는 요청 | 120초 |

실패한 요청의 기본 재시도는 프로필마다 다릅니다.

| 프로필 | 기본 재시도 |
|---|---|
| 낮음 | 최대 2회. 간격을 지수로 늘림. 마지막 간격 약 10분 |
| 중간 · 높음 | 최대 12회. 7초부터 늘림. 마지막 간격 약 1시간 |

재시도 설정을 직접 바꿀 때의 한도는 최대 90회, 최소 지연 5초, 최대 지연 1일입니다. 재시도도 요청으로 셉니다.

---

## 커넥터별 호출 한도

커넥터 한도는 위 한도보다 먼저 닿는 경우가 많습니다.[^limits] 넘으면 HTTP 429와 `Rate limit is exceeded` 메시지가 옵니다.[^guide]

| 커넥터 | 호출 | 갱신 주기 | 기준 |
|---|---:|---:|---|
| SharePoint[^sp] | 600 | 60초 | 연결당 |
| Office 365 Outlook[^outlook] | 300 | 60초 | 연결당 |
| Excel Online (Business)[^excel] | 100 | 60초 | 연결당 |
| Microsoft Teams[^teams] | 100 | 60초 | 연결당 |
| Microsoft Teams 흐름 봇 게시 등 조회 외 요청 | 25 | 300초 | 연결당 |
| Microsoft Teams 그 외 조회 외 요청 | 300 | 300초 | 연결당 |
| 표준 승인 승인 만들기[^approvals] | 50 | 60초 | 흐름당 |
| 표준 승인 그 외 요청 | 500 | 60초 | 흐름당 |
| 사용자 지정 커넥터 | 500 | 60초 | 연결당 |

한 사서함에 여러 흐름이 몰리면 커넥터 한도와 별개로 Exchange의 사서함 한도가 걸릴 수 있습니다.[^outlook]

---

## 스로틀링이 왔을 때

한도를 넘으면 흐름의 작업이 느려지고, 슬라이딩 창의 값이 한도 아래로 내려가면 원래 속도로 돌아옵니다. 한도는 흐름 정의 버전마다 계산하므로 흐름을 수정해 저장하면 계산을 새로 시작합니다.[^limits]

어떤 한도를 넘었는지는 증상으로 구분합니다.[^guide]

| 증상 | 넘은 한도 | 대응 |
|---|---|---|
| 흐름 전체의 작업이 늦어짐. 관리 센터 일일 작업 수가 높음 | 일일 작업 한도 | Process 라이선스 또는 요청 줄이기 |
| 한 커넥터에서 HTTP 429 | 커넥터 한도 | 호출을 시간에 나눔, 일괄 처리, 다른 연결 사용 |
| 부하가 클 때 Dataverse 호출 오류 | Dataverse 서비스 보호 한도 | 요청 속도 줄이기. Process 라이선스로 늘어나지 않음 |

요청을 줄이는 방법입니다.

| 방법 | 효과 | 다루는 페이지 |
|---|---|---|
| 트리거 조건 | 필요한 이벤트에서만 실행 | [C26](c26-trigger-conditions.html) |
| 데이터 원본에서 필터 쿼리 | 읽는 행과 반복 횟수 감소 | [C13](c13-filter.html) |
| 반복 대신 선택 · 배열 필터링 | 항목마다 드는 요청 제거 | [C12](c12-dataops.html) |
| 필요 없는 재시도 제거 | 재시도 요청 감소 | [C17](c17-error-handling.html) |
| 지연 작업 | 커넥터 호출을 시간에 나눔 | [C22](c22-error-codes.html) |

Process 라이선스는 흐름 자체에 배정합니다. 흐름이 솔루션에 있어야 합니다. 라이선스마다 24시간 250,000건이고 한 흐름에 최대 10개까지 쌓을 수 있습니다. 흐름 그룹에 배정하면 최대 25개 흐름이 250,000건을 나눠 씁니다. 플랜 변경은 흐름을 저장하면 바로 적용되고, 저장하지 않으면 일주일 안에 적용됩니다.[^guide]

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다.

- **문헌**: 제한과 구성[^limits] · 요청 한도와 할당[^requests] · 플랫폼 제한 이해[^guide] · SharePoint[^sp] · Office 365 Outlook[^outlook] · Excel Online (Business)[^excel] · Microsoft Teams[^teams] · 표준 승인[^approvals]

[^limits]: **Limits of automated, scheduled, and instant flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/limits-and-config> (2026-11-02 영어판 확인). 성능 프로필, 흐름 정의 · 실행 시간 · 보관 · 반복 · 요청 크기 · 재시도 한도, 끄기와 삭제의 차이.
[^requests]: **Requests limits and allocations** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-platform/admin/api-request-limits-allocations> (2026-11-02 영어판 확인). 공식 한도와 전환 기간 한도, 5분 한도, 슬라이딩 창, 누구의 한도를 쓰는지, 데스크톱 흐름 실행이 요청을 쓰지 않는다는 것.
[^guide]: **Understand platform limits and avoid throttling** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/understand-limits> (2026-11-02 영어판 확인). 요청으로 세는 것, 증상별 구분과 대응, Process 라이선스, 분석 화면.
[^sp]: **SharePoint** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/sharepointonline/> (2026-11-02 영어판 확인). Throttling Limits.
[^outlook]: **Office 365 Outlook** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/office365/> (2026-11-02 영어판 확인). Throttling Limits와 Office 쪽 사서함 한도.
[^excel]: **Excel Online (Business)** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/excelonlinebusiness/> (2026-11-02 영어판 확인). Throttling Limits.
[^teams]: **Microsoft Teams** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/teams/> (2026-11-02 영어판 확인). Throttling Limits.
[^approvals]: **Standard approvals** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/approvals/> (2026-11-02 영어판 확인). Throttling Limits.
