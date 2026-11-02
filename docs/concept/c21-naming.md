---
title: "C21. 이름 규칙 · 메모 · 코드 보기"
parent: "개념 4. 공유와 이름"
nav_order: 21
concept:
  id: C21
  grade: B
  used_in: "Lab 2 ③ 12번 · ④ 22 · 24번 · ⑤ 28 · 32 · 35 · 38번 · ⑦ 47번 카드 이름 · ⑤ 31번 작업 복사 · Lab 1 ⑥ 49번 카드 이름과 식 · Lab 3 ② 9번 코드 보기"
  tokens: ["카드 이름", "코드 보기", "operationId", "작업 복사", "메모 추가"]
  sample: true
---

# C21. 이름 규칙 · 메모 · 코드 보기

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행.
     ⚠️ 실측할 것: ⋮ 메뉴의 메모 추가 라벨과 메모 기호 위치(ko-kr 문서 둘이 다르다 — flows-designer 는 카드 오른쪽 아래 기호, use-peekcode-addnotes 는 작업 이름 아래) · 메모가 코드 보기에 나타나는지(limits 의 description 256자와 같은 것인지) · 붙여넣은 카드에 메모가 따라오는지.
     ⚠️ 문서 대조: ① 코드 보기 — 영어판은 직접 고칠 수 없다고 적고, ko-kr use-peekcode-addnotes 는 코드를 편집할 수 있다고 적는다. 본문은 영어판을 따랐다.
        ② 붙여넣은 카드 이름 — flows-designer 는 끝에 -copy 가 붙는다고 적고, Lab 2 31~32번 실측은 끝에 「 1」이 붙는다. 본문은 실측을 따랐다.
        ③ 트리거 복사 — use-peekcode-addnotes 영어판은 복사할 수 없다고 적고, flows-designer 는 action (or trigger) 를 복사한다고 적는다. 본문은 앞 문서를 따랐다.
     ⚠️ error-reference 의 이름 바꾸기는 카드 ... 메뉴 › Rename(구 디자이너)이다. 본문은 Lab 2 실측인 구성 창 맨 위 이름을 따랐다.
     ★ 카드 이름과 식의 관계는 C9 가 소유한다. 여기는 이름 짓는 규칙만 둔다. -->

> **다루는 것**: 흐름 구성 요소의 이름 규칙, 카드에 메모 달기, 코드 보기로 카드 정의 읽기, 작업 복사와 붙여넣기
>
> **쓰는 곳**: Lab 2 카드 이름 `원본행` · `점검행` · `조치필요` · 31번 **작업 복사** · Lab 1 49번 `length(body('배열_필터링'))` · Lab 3 9번 **코드 보기**의 `operationId`

---

## 이름 규칙

문서가 권하는 규칙입니다.[^naming]

| 규칙 | 내용 | 예 |
|---|---|---|
| 뜻이 드러나게 | 일반적이거나 모호한 이름을 쓰지 않음 | `Trigger1` 대신 `New Email Received` |
| 단어 구분 | camelCase 또는 밑줄 | `sendEmailNotification` · `send_email_notification` |
| 접두사로 분류 | 종류나 기능을 앞에 표시 | `Trg_` 트리거 · `Act_` 작업 · `Var_` 변수 |
| 같은 규칙 유지 | 흐름 전체에 같은 방식 | — |
| 문서로 남기기 | 스타일 가이드나 SharePoint 사이트에 정리 | — |
| 메모 달기 | 복잡한 작업에 목적과 로직을 적음 | — |

---

## 이름의 제약

카드와 흐름 이름에 걸리는 제약입니다.[^limits][^errref][^designer]

| 대상 | 제약 | 바꾸는 곳 |
|---|---|---|
| 카드 이름 | 80자까지. 흐름 안에서 중복 불가. 공백은 식에서 `_` | 구성 창 맨 위의 이름 |
| 흐름 이름 | 언제든 고칠 수 있음 | 디자이너 왼쪽 위의 흐름 이름 › **저장** |
| 같은 이름의 카드를 추가 | 끝에 ` 1` 이 붙음 | 구성 창 맨 위의 이름 |

- 이름이 겹치면 `DuplicateActionName` 오류가 납니다. 조건이나 범위 안의 카드도 함께 찾습니다.[^errref]
- 식은 카드 이름으로 앞 작업을 찾습니다. 이름과 식의 관계는 [C9](c09-references.html)에서 다룹니다.

---

## 메모

메모(Note)는 카드의 목적과 로직을 적어 두는 글입니다. 코드의 주석과 같은 역할을 합니다.[^peek]

| 항목 | 내용 |
|---|---|
| 다는 곳 | 카드를 고르고 구성 창의 **⋮**(추가 명령) › **메모 추가** |
| 대상 | 작업과 트리거 |
| 보기 | 카드에 메모 기호가 나타남. 포인터를 올리면 내용이 보임 |
| 범위 카드 | 범위에도 달 수 있음. 묶음의 목적을 적음[^scope-guide] |

클래식 디자이너의 댓글과는 다른 기능입니다.[^multistep]

| 항목 | 메모 | 댓글(클래식 디자이너) |
|---|---|---|
| 새 디자이너 | 가능 | 불가 |
| 답글 · 해결 | 없음 | 있음 |
| @멘션 | 없음 | 있음. 멘션하면 메일이 감 |
| 조건 | 없음 | Dataverse 환경. 흐름을 한 번 저장한 뒤 |

---

## 코드 보기

코드 보기(Code view)는 카드 뒤에 있는 JSON 정의를 보여 줍니다. 카드를 고르고 구성 창의 **코드 보기** 탭을 엽니다. 읽기 전용입니다.[^peek]

| 읽을 수 있는 것 | 코드에서 찾는 값 |
|---|---|
| 작업 종류 | `type` |
| 입력 | `inputs` |
| 앞 작업과 허용 상태 | `runAfter`. [C17](c17-error-handling.html) |
| 같은 이름의 작업 구별 | `operationId` |
| 동적 콘텐츠가 저장된 식 | `inputs` 안의 `@...` |
| 트리거의 확인 주기 · 조건 | 트리거 카드의 코드 |
| 동적 콘텐츠의 스키마 | 카드의 코드 |

작성 카드의 코드 모양입니다.[^schema]

```
{
  "type": "Compose",
  "inputs": "@triggerBody()?['text']",
  "runAfter": {}
}
```

---

## 작업 복사와 붙여넣기

같은 작업을 다시 쓸 때 복사합니다.[^peek][^designer]

| 항목 | 내용 |
|---|---|
| 복사 | 카드를 마우스 오른쪽 단추로 눌러 **작업 복사**. 키보드는 Ctrl+C |
| 붙여넣기 | **+** 를 마우스 오른쪽 단추로 눌러 **작업 붙여넣기**. 키보드는 Ctrl+V |
| 대상 | 작업 하나 · 조건 전체 · 범위 전체 |
| 복사할 수 없는 것 | 트리거 |
| 복사 범위 | 같은 흐름 안 · 다른 흐름 |
| 복사되는 값 | 조건과 입력 값까지 |
| 붙여넣은 카드 이름 | 끝에 ` 1` 이 붙음. 이름을 부르는 식이 있으면 고침 |

---

## 샘플

흐름 `식 연습장_HGD` 를 씁니다. 없으면 [C7](c07-types.html)의 샘플로 만듭니다.

1. [Power Automate — {{ site.pa.environment }}]({{ site.pa.powerautomate_url }}){:target="_blank"}를 엽니다. 왼쪽 메뉴 **내 흐름**에서 `식 연습장_HGD` 를 열고 **편집**을 누릅니다.
2. **작성** 카드를 누릅니다. 구성 창의 **⋮**(추가 명령)을 누르고 **메모 추가**를 고릅니다.
3. 메모 칸에 아래를 넣습니다.

    ```
    식 연습 카드. 입력 칸의 식을 바꿔 가며 실행한다.
    ```

4. **저장**을 누릅니다.

    **완료 기준**: 카드에 메모 기호가 보이고, 포인터를 올리면 메모가 보인다.

5. 구성 창의 **코드 보기** 탭을 엽니다.

    **완료 기준**: JSON 에 `"type": "Compose"` 와 `runAfter` 가 보인다.

6. **코드 보기** 탭의 내용을 고쳐 봅니다.

    **완료 기준**: 입력되지 않는다.

7. 캔버스에서 **작성** 카드를 마우스 오른쪽 단추로 누르고 **작업 복사**를 고릅니다.
8. **작성** 아래 **+** 를 마우스 오른쪽 단추로 누르고 **작업 붙여넣기** › **작업 붙여넣기**를 고릅니다.

    **완료 기준**: 카드 이름 끝에 ` 1` 이 붙은 카드가 생긴다.

9. 붙여넣은 카드를 누르고 구성 창의 **⋮**(추가 명령) › **삭제**를 고릅니다. **저장**을 누릅니다.

    **완료 기준**: 트리거 아래에 메모가 달린 **작성** 카드 하나만 남아 있다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: 이름 규칙[^naming] · Power Automate 기능 활용[^peek] · 디자이너[^designer] · 범위 활용 지침[^scope-guide] · 작업 옵션과 댓글[^multistep] · 제한[^limits] · 오류 코드[^errref] · 작업 스키마[^schema]

[^naming]: **Use consistent naming for flow components** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/use-consistent-naming-conventions> (2026-11-02 확인). 이름 규칙 여섯 가지와 예.
[^peek]: **Streamline workflow creation with Power Automate features** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/use-peekcode-addnotes> (2026-11-02 확인). 코드 보기가 읽기 전용이라는 것, 메모 추가, 작업 복사. 한국어판은 코드를 편집할 수 있다고 옮겼다. 영어판을 따랐다.
[^designer]: **Explore the cloud flows designer** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/flows-designer> (2026-11-02 확인). 추가 명령의 메모 · 삭제, 코드 보기 탭, 복사 · 붙여넣기 단축키, 흐름 이름 편집. 문서는 붙여넣은 이름에 `-copy` 가 붙는다고 적지만 실측은 ` 1` 이다.
[^scope-guide]: **Organize your flows with scopes** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/create-scopes> (2026-11-02 확인). 범위에 메모를 다는 권장.
[^multistep]: **Move, delete, and add options to actions in a cloud flow** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/multi-step-logic-flow> (2026-11-02 확인). 클래식 디자이너의 댓글과 제한, 새 디자이너의 메모.
[^limits]: **Limits of automated, scheduled, and instant flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/limits-and-config> (2026-11-02 확인). 작업 · 트리거 이름 80자.
[^errref]: **Cloud flow error code reference** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/error-reference> (2026-11-02 확인). `DuplicateActionName` 의 원인과 처리, 식의 카드 이름은 공백 대신 밑줄.
[^schema]: **Schema reference guide for trigger and action types in Azure Logic Apps** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/logic-apps-workflow-actions-triggers> (2026-11-02 확인). Compose 작업 정의의 `type` · `inputs` · `runAfter`. Azure Logic Apps 문서다.
