---
title: "C15. 승인 모델"
parent: "개념 3. 승인과 실행 기록"
nav_order: 15
concept:
  id: C15
  grade: A
  used_in: "Lab 3 ② 승인 요청 · ③ 결과 분기 · ⑥ 반려 — 의견 회신 · ⑦ 승인 경로 테스트 · ⑧ 반려 경로 테스트"
  tokens: ["승인 시작 및 대기", "승인 형식", "body/responses", "Approve", "승인/거부"]
  sample: false
---

# C15. 승인 모델

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안. 샘플 없음.
     문서 대조: get-started-approvals 영어판 · 한국어판 모두 「four approval types」라고 쓰고 표에 다섯 행을 둔다.
     set-up-sequential-approvals 가 Sequential Approval 을 승인 유형으로 고르게 하므로 이 페이지는 다섯 행으로 적었다. all-assigned-must-approve 표는 순차 없이 네 행이다.
     ⚠️ 실측할 것: 승인 형식 드롭다운에 순차 승인이 보이는지와 나머지 라벨(실측한 것은 「승인/거부 - 첫 번째로 응답」뿐),
     승인 시작 및 대기의 실제 출력 키(커넥터 참조는 이 작업의 출력을 동적이라 적어, 키 목록은 텍스트 승인의 출력 정의에서 옮겼다),
     모두가 승인해야 함의 outcome 모양(커넥터 정의는 string, all-assigned-must-approve 팁은 array of Approve or Reject),
     사용자 지정 응답의 outcome 값, 조건 왼쪽에 응답 쪽 값을 고를 때의 동작(자습서 modern-approvals 는 Responses Approver response 를 고르고, Lab 3 은 결과를 고른다), Power Automate 승인 센터 라벨(한국어판 수신, Teams 실측 받음), 의견을 비운 거부에서 comments 가 null 인지 빈 문자열인지,
     Teams 응답에서 메모를 비웠을 때 표시.
     강사 메모: 첫 실행 프로비저닝은 강사가 전날 한 번 돌린다. 교육 환경은 보안 그룹으로 접근을 제어하므로 그룹 밖 승인자에게 역할이 자동으로 붙지 않는다.
     승인 확인용 계정은 그 그룹에 넣는다 -->

> **다루는 것**: 승인 작업 셋과 유형, 응답 경로, 첫 실행 프로비저닝, 승인 결과 출력의 구조
>
> **쓰는 곳**: Lab 3 `승인 시작 및 대기` · `승인/거부 - 첫 번째로 응답` · `결과` 다음과 같음 `Approve` · `first(outputs('승인_시작_및_대기')?['body/responses'])?['comments']`

---

## 승인 작업 셋

승인 커넥터의 등급은 표준입니다. Power Automate와 표준 커넥터를 쓸 수 있는 라이선스면 승인 흐름을 만들 수 있습니다.[^start]

| 작업 | 영문 · 작업 ID | 흐름의 동작 | 응답 · 의견 출력 |
|---|---|---|---|
| 승인 시작 및 대기 | Start and wait for an approval · `StartAndWaitForAnApproval` | 요청을 만들고 응답이 끝날 때까지 다음 작업을 실행하지 않음 | 있음 |
| 승인 만들기 | Create an approval · `CreateAnApproval` | 요청을 만들고 바로 다음 작업을 실행 | 없음 |
| 승인 대기 | Wait for an approval · `WaitForAnApproval` | 승인 ID를 받아 완료될 때까지 다음 작업을 실행하지 않음 | 있음 |

승인 시작 및 대기와 승인 만들기는 Dataverse에 기록을 만들고 메일과 모바일 앱 알림을 보냅니다.[^diff]

| 고르는 기준 | 작업 |
|---|---|
| 요청과 결과 처리를 한 흐름에 둠 | 승인 시작 및 대기 |
| 요청 정보를 다른 시스템에 먼저 기록함 | 승인 만들기 → 기록 → 승인 대기[^diff] |
| Teams에 적응형 카드를 직접 게시함 | 승인 만들기 → 카드 게시 → 승인 대기[^diff] |
| 30일을 넘길 수 있음 | 승인 만들기로 요청하는 흐름과 응답을 처리하는 흐름 둘[^modern] |

이름이 비슷한 **텍스트 승인 시작 및 대기**(`StartAndWaitForATextSuggestionApproval`)가 있습니다. 승인자가 제안 텍스트를 검토하거나 고치고, 출력에 `acceptedText` 가 있습니다.[^connector] 사용 중단된 작업 둘은 `approvalSubscribe` · `approvalSubscribeV2` 입니다.[^connector]

---

## 승인 유형

| 승인 형식 | 영문 | 승인자의 선택지 | 다음 작업이 실행되는 때 |
|---|---|---|---|
| 승인/거부 - 모두가 승인해야 함 | Approve/Reject - Everyone must approve | 승인 · 거부 | 전원 승인 또는 거부 한 건 |
| 승인/거부 - 첫 번째로 응답 | Approve/Reject - First to respond | 승인 · 거부 | 한 명이 승인 또는 거부 |
| 사용자 지정 응답 - 모든 응답을 기다립니다 | Custom Responses - Wait for all responses | 흐름 작성자가 정함 | 전원 응답 |
| 사용자 지정 응답 - 하나의 응답을 기다립니다 | Custom Responses - Wait for one response | 흐름 작성자가 정함 | 한 명 응답 |
| 순차 승인 | Sequential approval | 차례마다 응답 | 정한 순서의 전원 응답 |

순차 승인은 할당 대상 칸을 단계마다 하나씩 두고, 같은 승인자를 다른 단계에 넣을 수 없습니다.[^sequential] 사용자 지정 응답과 순차 · 병렬 구성은 [C27](c27-approval-variants.html)에서 다룹니다.

---

## 승인 시작 및 대기의 칸

| 칸 | 내용 |
|---|---|
| 승인 형식 | 위 표에서 고름. 필수 |
| 제목 | 승인 요청의 제목. 필수 |
| 할당 대상 | 승인자. 필수 |
| 세부 정보 | 요청 설명. Markdown 지원 |
| 항목 링크 · 항목 링크 설명 | 승인 대상으로 가는 링크와 그 표시 글자 |

할당 대상은 메일 주소 · UPN · Microsoft Entra 사용자 ID를 받습니다. 여러 명은 세미콜론으로 나눕니다.[^connector]

```
jsmith@contoso.com;3b3ba145-7da5-414d-b84f-a9835eb71f3b;jane.doe@contoso.com
```

---

## 응답 경로

| 경로 | 찾는 곳 | 응답 | 조건 |
|---|---|---|---|
| Teams 승인 앱 | 활동 알림 · 앱 막대 **승인**의 받음 탭 | 설명 입력 후 승인 · 거부. 확인 단계 없음 | 없음 |
| Outlook 메일 | 받은 승인 메일 | 승인 · 거부 → 메모 → 확인 | 표준 메일 계정에서 보낸 메일만 응답 가능. 게스트 제외 |
| Power Automate 승인 센터 | 왼쪽 메뉴 **작업 항목 › 승인** | 승인 · 거부 → 메모 → 확인 | 받은 요청은 수신 탭 |
| Power Automate 모바일 앱 | 메일의 승인 | 승인 · 거부 → 확인 | 앱이 설치된 기기 |

Teams 행은 실측이고 나머지 행은 문서에서 옮겼습니다.[^respond] 흐름에서 직접 보낸 메일에 승인 링크를 넣을 수는 있지만, 그 메일 안에서는 승인 · 거부를 누를 수 없습니다.[^connector] 응답에는 Power Automate 라이선스 또는 Power Automate 기능이 포함된 Office 365 · Dynamics 365 라이선스가 필요합니다.[^start]

| 동작 | 내용 |
|---|---|
| 요청 취소 | 보낸 사람이 승인 센터 보냄 탭에서 **취소**[^modern] |
| 흐름 작성자 표시 | 승인 세부 정보에 항상 표시됨. 발신자 위장 방지[^connector] |
| 승인 시각 | 항상 UTC로 표시[^connector] |
| 요청 언어 | 받는 사람의 Power Automate 포털 언어 → Office 포털 언어 → 호출자 전달 언어 → 작성자 언어[^respond] |
| 언어 변경 | 톱니바퀴 › **Power Automate 설정 모두 보기**. 반영까지 최대 24시간[^respond] |

---

## 첫 실행 프로비저닝

승인 기록은 Dataverse에 저장됩니다. 기본이 아닌 환경에서 승인 커넥터를 처음 쓰면 시스템이 데이터베이스를 자동으로 프로비저닝합니다.[^start]

| 항목 | 내용 |
|---|---|
| 걸리는 시간 | 몇 분. 첫 실행에서 지연이 보임 |
| 첫 실행자 권한 | 그 환경의 관리자 역할 |
| 이후 사용자 권한 | 상승된 권한 필요 없음 |
| 기본 환경 | 프로비저닝 필요 없음. 자동 생성 |

환경 밖 사용자에게 승인을 할당하면 그 사용자에게 **승인 사용자**(Approvals User) Dataverse 보안 역할이 자동으로 부여됩니다. 응답을 처리하고 승인 기록에 남기는 데 이 역할이 쓰입니다.[^start]

| 역할을 자동 부여하지 않는 구성 |
|---|
| Microsoft Entra의 AllowAdHocSubscriptions 설정이 꺼져 있음 |
| 보안 그룹으로 Dataverse 환경의 접근을 제어함 |
| Power Automate 미국 정부 요금제 |

---

## 승인 결과의 출력

승인 시작 및 대기가 끝나면 출력은 객체 하나입니다. 키는 커넥터 참조의 출력 정의에서 옮겼고, 값은 예입니다.[^connector]

```
{
  "title": "HGD 정기점검 보고서 승인 요청",
  "outcome": "Reject",
  "responseSummary": "...",
  "completionDate": "...",
  "responses": [
    {
      "responder": { "displayName": "교육", "email": "edu@2ktech.co.kr" },
      "requestDate": "...",
      "responseDate": "...",
      "approverResponse": "Reject",
      "comments": "서버랙 UPS 부하율 82 % 항목의 조치 계획을 보완해 주세요."
    }
  ]
}
```

| 키 | 모양 | 값 |
|---|---|---|
| `outcome` | 문자열 | 승인의 결과. 조건 카드의 **결과** |
| `responses` | 객체 배열 | 모든 응답 |
| `responses` 의 `approverResponse` | 문자열 | 그 승인자의 응답 |
| `responses` 의 `comments` | 문자열 | 그 승인자의 의견 |
| `responses` 의 `responder` | 객체 | 승인자의 ID · 이름 · 메일 · UPN |
| `responseSummary` | 문자열 | 응답 요약 |
| `completionDate` | 날짜 | 완료 날짜 |

승인/거부 유형의 응답 값은 `Approve` · `Reject` 이고 대소문자를 구분합니다.[^connector] 사용자 지정 응답은 `outcome` 에 고른 응답이 담깁니다.[^howto] 모두가 승인해야 함의 `outcome` 은 커넥터 정의가 문자열로, 그 유형의 자습서가 응답 수만큼의 배열로 적습니다.[^all] 이 유형을 쓸 때는 실행 기록의 출력으로 모양을 확인합니다.

---

## responses가 배열인 이유

한 요청을 여러 명에게 할당할 수 있고, 승인자마다 응답이 쌓입니다. 그래서 `responses` 는 언제나 배열이고, 응답이 한 건이어도 항목 하나인 배열입니다.[^connector]

배열 안의 값은 항목을 정해야 읽을 수 있습니다. 응답 의견을 동적 콘텐츠로 고르면 디자이너가 그 카드를 **For each**로 감쌉니다. 식으로 첫 항목을 지정하면 감싸지 않습니다.

```
first(outputs('승인_시작_및_대기')?['body/responses'])?['comments']
```

| 조각 | 읽는 값 |
|---|---|
| `outputs('승인_시작_및_대기')` | 카드 **승인 시작 및 대기**의 출력. 공백은 `_` |
| `?['body/responses']` | 출력의 본문에 있는 `responses` 배열 |
| `first(...)` | 배열의 첫 항목. 빈 배열이면 null[^cookbook] |
| `?['comments']` | 그 항목의 의견. 없으면 null |

승인/거부 - 첫 번째로 응답은 응답 한 건으로 끝나므로 첫 항목이 그 응답입니다. 승인자가 여럿인 유형에서 의견을 전부 읽으려면 선택으로 `comments` 를 뽑고 조인으로 잇습니다. 표기는 [C8](c08-json.html), 작업은 [C12](c12-dataops.html)에서 다룹니다.

분기 조건에는 `outcome` 을 씁니다. 동적 콘텐츠 이름은 **결과**입니다.

---

## 대기 시간과 제한

| 항목 | 값 |
|---|---|
| 흐름 실행 기간 | 시작부터 30일. 승인처럼 대기 중인 단계 포함. 지나면 대기 단계가 시간 초과[^limits] |
| 승인을 만드는 요청 | 흐름당 60초에 50건[^connector] |
| 그 밖의 승인 요청 | 흐름당 60초에 500건[^connector] |
| 연결 | 계정당 1개[^connector] |
| 첨부 파일 | 한 승인 안에서 이름이 달라야 함[^connector] |
| 사용자 지정 응답 + 모두 응답 | 받는 사람이 많으면 결과 필드 크기 제한으로 실패할 수 있음[^connector] |

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. Teams 응답 경로와 작업 구별은 Lab 3 실측에서 옮겼습니다.

- **문헌**: 승인 시작하기[^start] · 승인 흐름 만들기와 테스트[^modern] · 승인 요청 관리[^respond] · 표준 승인 커넥터[^connector] · 승인 작업의 차이[^diff] · 순차 승인 설정[^sequential] · 전원 승인 흐름[^all] · 승인 사용 사례[^howto] · 흐름 제한[^limits] · 식 요리책[^cookbook]

[^start]: **Get started with approvals** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/get-started-approvals> (2026-11-02 확인). 승인 유형 표, Dataverse 프로비저닝과 권한, 라이선스, 승인 사용자 역할과 자동 부여가 되지 않는 구성, 응답 경로. 본문은 네 가지라고 적고 표는 다섯 행이다.
[^modern]: **Create and test an approval workflow with Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/modern-approvals> (2026-11-02 확인). 30일을 넘는 승인을 두 흐름으로 나누는 방법, 요청 취소.
[^respond]: **Manage approval requests in Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/approve-reject-requests> (2026-11-02 확인). 메일 · 승인 센터 · 모바일 앱의 승인과 거부, 승인 언어를 정하는 순서와 변경.
[^connector]: **Standard approvals** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/approvals/> (2026-11-02 확인). 작업 목록, 할당 대상 형식, 출력 정의, 알려진 제한과 호출 제한. 응답 값은 영어판의 `Approve` · `Reject` 를 따랐다. 한국어판은 값까지 「승인」「거부」로 옮겼다.
[^diff]: **Differences between flow approval actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/troubleshoot/power-platform/power-automate/approvals/differences-between-flow-approval-actions> (2026-11-02 확인). 승인 시작 및 대기 · 승인 만들기 · 승인 대기의 차이와 쓰는 예.
[^sequential]: **Set up sequential approvals** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/set-up-sequential-approvals> (2026-11-02 확인). 승인 유형 Sequential Approval, 단계 추가, 같은 승인자를 다른 단계에 넣을 수 없다는 제한.
[^all]: **Create an approval flow that requires everyone to approve** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/all-assigned-must-approve> (2026-11-02 확인). 유형별 동작, Outcome 이 응답 수만큼의 Approve · Reject 배열이라는 팁.
[^howto]: **How to - Top scenarios with approval flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/approvals-howto> (2026-11-02 확인). 사용자 지정 응답의 결과를 Outcome 출력으로 읽는다는 것.
[^limits]: **Limits of automated, scheduled, and instant flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/limits-and-config> (2026-11-02 확인). 실행 기간 30일에 대기 중인 승인 단계가 포함된다는 것.
[^cookbook]: **Expression cookbook for cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/expression-cookbook> (2026-11-02 확인). 14번 패턴. `first()` 는 빈 배열에서 null 을 돌려준다는 것.
