---
title: "C9. 출력 참조와 카드 이름"
parent: "개념 2. 자료형과 식"
nav_order: 9
concept:
  id: C9
  grade: A
  used_in: "Lab 1 ⑥ 예약 트리거와 식 · Lab 2 ④ 행 읽기 · ⑤ 거르기와 세기 · ⑥ 표 만들기 · Lab 3 ⑥ 반려 회신"
  tokens: ["body('", "outputs('", "item()", "first(", "배열_필터링", "승인_시작_및_대기"]
  sample: true
---

# C9. 출력 참조와 카드 이름

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행.
     ⚠️ 문서로 확인한 것: 공백은 밑줄이 된다 · 이름은 대소문자까지 정확히 맞아야 한다 · 없는 이름은 저장 때 InvalidTemplate · 이름을 바꾸면 식을 새 이름으로 고친다(이상 error-reference).
     ⚠️ 문서로 확인하지 못한 것: 이름을 바꿀 때 디자이너가 동적 콘텐츠 칩과 fx 식을 자동으로 고치는가. 샘플 17~19번이 이것을 관찰한다. 완료 기준을 단정하지 않았다. 실측 후 본문에 결과를 적는다.
     ⚠️ 문서로 확인하지 못한 것: 괄호 등 공백 밖의 문자(`메일 보내기(V2)` · `항목 가져오기(2개 이상)`)가 식에서 어떻게 적히는가
     ⚠️ 실측할 것: `?['body/responses']` 의 슬래시 표기를 설명한 문서를 찾지 못했다. error-reference 의 `outputs('Get_item')?['body/title']` 과 Lab 3 실측, Lab 1 45번 동적 콘텐츠 이름 body/value 가 근거다. `body('원본행')?['value']` 와 값이 같은지 실행으로 확인한다
     ⚠️ 실측할 것: 작성 카드를 부르는 `outputs('작성')`. 문서에는 작성의 동적 콘텐츠가 Outputs 라고만 있다. 샘플 6번 코드 보기로 확인한다
     ⚠️ 문서와 랩이 어긋남: flows-designer 는 붙여넣은 카드 이름 끝에 -copy 가 붙는다고 적는다. Lab 2 32번 실측은 ` 1` 이다. 랩 실측을 따랐다
     ⚠️ 실측할 것: 같은 작업을 다시 놓은 작성 카드의 이름이 `작성 1` 인가(Lab 3 35번의 메일 카드가 근거), 삭제 때 확인 창이 뜨는가, `각각에 적용` 카드의 기본 이름, 수동 트리거 텍스트 입력의 키 text, triggerOutputs() 의 출력 모양
     ⚠️ 승인 커넥터 문서는 일반 승인의 출력을 dynamic 으로 적고, responses 배열은 텍스트 승인의 정의에만 있다. 일반 승인의 responses 가 배열이라는 것은 Lab 3 40 · 56번 실측이 근거다 -->

> **다루는 것**: 앞 카드와 트리거의 출력을 식에서 부르는 함수와, 식에 들어가는 카드 이름의 규칙
>
> **쓰는 곳**: Lab 1 `length(body('배열_필터링'))` · Lab 2 `body('원본행')?['value']` · `item()?['점검월']` · Lab 3 `first(outputs('승인_시작_및_대기')?['body/responses'])?['comments']`

---

## 출력을 부르는 함수

| 함수 | 돌려주는 값 | 쓰는 곳 |
|---|---|---|
| `outputs('카드')` | 그 카드의 출력 전체 | 트리거 뒤의 모든 카드 |
| `body('카드')` | 그 카드의 출력 중 `body` | 커넥터 작업 · 배열 필터링 · 선택 · HTML 테이블 만들기 |
| `triggerOutputs()` | 트리거의 출력 전체 | 트리거 뒤의 모든 카드 |
| `triggerBody()` | 트리거의 출력 중 `body` | 트리거 뒤의 모든 카드 |
| `item()` | 배열을 도는 작업이 지금 다루는 항목 | 배열 필터링 · 선택 · 표 만들기의 열 |
| `items('반복')` | 지정한 반복의 현재 항목 | 각각에 적용 안 |
| `variables('변수')` | 그 변수의 값 | 변수 초기화 뒤 |
| `first(값)` | 배열이나 문자열의 첫 항목 | 어디서나 |

함수의 인수와 결과는 함수 참조를 따랐습니다.[^functions] 함수가 돌려준 값 안의 키를 읽는 표기는 [C8](c08-json.html)에서 다룹니다.

실제 식에서는 이렇게 읽습니다.

| 식 | 읽는 값 |
|---|---|
| `body('배열_필터링')` | 카드 **배열 필터링**의 본문. 조건에 맞은 항목의 배열 |
| `length(body('배열_필터링'))` | 위 배열의 개수 |
| `body('원본행')?['value']` | 카드 **원본행**의 본문 안 `value`. 표의 행 배열 |
| `item()?['결과']` | From 배열의 한 행에서 `결과` 열의 값 |
| `outputs('승인_시작_및_대기')?['body/responses']` | 카드 **승인 시작 및 대기**의 출력에서 `body` 안 `responses`. 응답의 배열 |
| `first(outputs('승인_시작_및_대기')?['body/responses'])?['comments']` | 첫 응답의 `comments` |

---

## outputs()와 body()

커넥터 작업의 출력에는 상태 코드와 머리글, 본문이 함께 들어 있습니다. `outputs('카드')` 는 이 전체를 돌려주고 `body('카드')` 는 본문만 돌려줍니다.[^functions]

```
{
  "statusCode": 200,
  "headers": { "Content-Type": "application/json; charset=utf-8" },
  "body": { "value": [ … ] }
}
```

아래 세 식은 같은 값을 가리킵니다. 첫 줄과 둘째 줄은 함수 참조의 정의대로이고, 셋째 줄은 동적 콘텐츠가 쓰는 표기입니다.

```
body('원본행')?['value']
outputs('원본행')?['body']?['value']
outputs('원본행')?['body/value']
```

카드마다 출력의 모양이 다릅니다.

| 카드 | 부르는 식 | 얻는 값 |
|---|---|---|
| 항목 가져오기(2개 이상) · 테이블에 있는 행 나열 | `body('카드')?['value']` | 항목의 배열 |
| 배열 필터링 · 선택 | `body('카드')` | 배열[^shape] |
| HTML 테이블 만들기 | `body('카드')` | 문자열[^shape] |
| 작성 | `outputs('카드')` | 입력에 넣은 값 |
| 승인 시작 및 대기 | `outputs('카드')?['body/키']` | 본문 안의 값 |

---

## 식에 들어가는 카드 이름

식의 카드 이름은 화면의 이름에서 공백을 밑줄로 바꾼 글자입니다.[^errors] 대소문자까지 정확히 맞아야 합니다. 작은따옴표로 감쌉니다.

| 화면의 카드 이름 | 식의 표기 |
|---|---|
| `배열 필터링` | `body('배열_필터링')` |
| `승인 시작 및 대기` | `outputs('승인_시작_및_대기')` |
| `원본행` | `body('원본행')` |
| `Get item` | `outputs('Get_item')` |

괄호처럼 공백 밖의 문자가 든 이름의 표기는 문서에 없습니다. 동적 콘텐츠로 값을 넣은 뒤 그 카드의 **코드 보기**에서 식을 읽습니다.[^peek]

같은 범위에 같은 이름의 카드를 둘 수 없습니다.[^errors] 같은 작업을 다시 놓거나 카드를 복사해 붙여넣으면 이름 끝에 ` 1` 이 붙습니다. `조치필요 1` 을 부르는 식은 `body('조치필요_1')` 입니다.

카드 이름은 하는 일을 설명하는 말로 짓고, 여러 흐름에 같은 규칙을 씁니다.[^naming] 이름 규칙은 [C21](c21-naming.html)에서 다룹니다.

---

## 카드 이름을 바꿀 때

구성 창 맨 위의 카드 이름을 눌러 바꿉니다.[^pa-dataops] 문서가 적은 절차는 이름을 바꾼 뒤 그 카드를 부르는 식을 새 이름으로 고치는 것입니다. `outputs('Old_Name')` 은 `outputs('New_Name')` 이 됩니다.[^errors]

디자이너가 동적 콘텐츠 칩과 ***fx*** 로 넣은 식을 자동으로 고치는지는 문서에 적혀 있지 않습니다. 샘플에서 확인합니다.

식에 이름이 들어가기 전에 카드 이름을 바꾸면 고칠 식이 없습니다. 흐름 안의 작업 이름을 바꾸지 못하는 경우도 있습니다. Power Apps 트리거를 쓰는 흐름은 알려진 문제로 올라 있고, 트리거를 지웠다가 다시 놓는 우회 절차가 문서에 있습니다.[^triggers]

---

## item()과 items()

`item()` 은 인수가 없습니다. 배열을 도는 작업 안에서 현재 항목을 돌려줍니다. 배열 필터링이라면 **From** 에 넣은 배열의 한 항목이고, 항목이 객체이면 `item()?['열 이름']` 으로 값을 읽습니다.[^shape]

`items('반복')` 은 **각각에 적용** 안에서 씁니다. 카드 이름을 인수로 받아 그 반복의 현재 항목을 돌려줍니다.[^functions] 반복은 [C18](c18-loops.html)에서 다룹니다.

---

## 트리거의 출력

`triggerBody()` 는 `trigger().outputs.body` 의 줄임이고 `triggerOutputs()` 는 `trigger().outputs` 의 줄임입니다.[^functions]

수동 트리거의 입력값은 `triggerBody()` 안에 있습니다. 날짜 입력은 `triggerBody()?['date']` 로 읽고[^datetime] 텍스트 입력은 `triggerBody()?['text']` 로 읽습니다.

---

## variables()

변수를 부를 때는 **변수 초기화** 카드의 이름을 쓰지 않습니다. 변수의 이름을 씁니다.[^vars] 변수는 [C19](c19-variables.html)에서 다룹니다.

---

## first()

`first()` 는 배열의 첫 항목이나 문자열의 첫 글자를 돌려줍니다.[^functions]

| 식 | 결과 |
|---|---|
| `first(createArray(0, 1, 2))` | `0` |
| `first('hello')` | `h` |

승인의 `responses` 는 응답자마다 항목이 하나씩 있는 배열입니다.[^approvals] 응답 의견처럼 배열 안의 값을 동적 콘텐츠로 고르면 디자이너가 그 카드를 **For each** 로 감쌉니다. `first()` 로 항목 하나를 읽는 식은 감싸지 않습니다.

식 요리책은 빈 배열에 쓴 `first()` 가 오류 없이 `null` 을 돌려준다고 적습니다.[^cookbook] 함수 참조에는 이 경우가 적혀 있지 않습니다.

---

## 흔한 실패

| 나오는 때 | 오류 | 원인 | 고치는 법 |
|---|---|---|---|
| 저장 | `InvalidTemplate` | 없는 카드를 부름. 이름 오타 | 화면의 이름과 맞춤 |
| 저장 | `InvalidTemplate` | 공백을 그대로 적음. `outputs('Get item')` | 공백을 밑줄로 |
| 저장 | `InvalidTemplate` | 대소문자가 다름 | 화면의 대소문자와 맞춤 |
| 저장 | `FlowCheckerError` | 병렬 가지의 값을 부름. 값이 있다고 보장되지 않음 | 같은 경로의 앞 카드 값을 부름 |
| 저장 | `DuplicateActionName` | 다른 카드가 쓰는 이름으로 바꿈 | 둘 중 하나의 이름을 바꾸고 식을 고침 |
| 실행 | `ExpressionEvaluationFailed` | 값이 비어 있는데 안의 키를 읽음 | `?` · `coalesce()` |

표의 원인과 고치는 법은 오류 코드 참조를 따랐습니다.[^errors]

---

## 샘플

흐름 `식 연습장_HGD` 를 씁니다. 없으면 [C7](c07-types.html)의 샘플로 만듭니다.

1. `식 연습장_HGD` 의 **편집**을 눌러 디자이너를 엽니다.
2. **작성** 카드를 누릅니다. **입력** 칸을 비우고 ***fx*** 로 아래 식을 넣습니다.

    ```
    createArray('정상', '이상', '주의')
    ```

3. **작성** 아래 **+**를 누르고 **작업 추가**를 고릅니다. **기본 제공 도구**에서 **데이터 작업**을 누르고 **작성**을 고릅니다.

    **완료 기준**: 새 카드 이름이 `작성 1` 이다.

4. `작성 1` 의 **입력** 칸에 ***fx*** 로 아래 식을 넣습니다.

    ```
    first(outputs('작성'))
    ```

5. **저장**을 누르고 **테스트** › **수동** › **테스트**를 누릅니다. **흐름 실행**을 누르고 **완료**를 누릅니다. 실행 화면에서 **작성 1** 카드를 누릅니다.

    **완료 기준**: 출력이 `정상` 이다.

6. **편집**을 눌러 디자이너로 돌아옵니다. `작성 1` 의 **입력** 칸을 비우고 번개 단추를 눌러 **작성** 아래 **출력**을 고릅니다. 구성 창의 **코드 보기** 탭을 엽니다.

    **완료 기준**: `inputs` 에 `outputs('작성')` 이 보인다.

7. `작성 1` 아래 **+** › **작업 추가**에서 **기본 제공 도구** › **데이터 작업**을 누르고 **배열 필터링**을 고릅니다.
8. **From** 칸에 ***fx*** 로 아래 식을 넣습니다.

    ```
    outputs('작성')
    ```

9. **Filter Query** 왼쪽 **값 선택** 칸에 ***fx*** 로 아래 식을 넣습니다. 연산자는 **다음과 같음** 그대로 둡니다.

    ```
    item()
    ```

10. **Filter Query** 오른쪽 **값 선택** 칸에 아래를 입력합니다.

    ```
    이상
    ```

11. **배열 필터링** 아래 **+** › **작업 추가**에서 **기본 제공 도구** › **데이터 작업**을 누르고 **작성**을 고릅니다. **입력** 칸에 ***fx*** 로 아래 식을 넣습니다. 카드 이름의 공백이 밑줄이 됩니다.

    ```
    body('배열_필터링')
    ```

12. 5번과 같이 저장하고 실행합니다. 실행 화면에서 **작성 2** 카드를 누릅니다.

    **완료 기준**: 출력이 항목 하나의 배열 `["이상"]` 이다.

13. **편집**을 누릅니다. **작성 2** 의 식을 아래로 바꿔 저장하고 실행합니다. **흐름 실행** 창의 `입력값` 칸에 `공조기-2` 를 입력합니다.

    ```
    triggerBody()?['text']
    ```

    **완료 기준**: **작성 2** 의 출력이 `공조기-2` 다.

14. **작성 2** 의 식을 아래로 바꿔 13번과 같이 실행합니다.

    ```
    triggerOutputs()
    ```

    **완료 기준**: 출력에 `body` 키가 보이고 그 안에 입력값이 있다.

15. **작성 2** 의 식을 공백이 든 아래 식으로 바꾸고 **저장**을 누릅니다.

    ```
    outputs('작성 1')
    ```

    **완료 기준**: 저장되지 않고 오류가 표시된다.

16. 식의 공백을 밑줄로 고치고 **저장**을 누릅니다.

    ```
    outputs('작성_1')
    ```

    **완료 기준**: 저장된다.

17. **작성** 카드를 누르고 구성 창 맨 위의 카드 이름을 아래로 바꿉니다.

    ```
    원본값
    ```

18. **작성 1** 과 **배열 필터링** 을 차례로 누르고 **코드 보기** 탭을 엽니다.

    **완료 기준**: 동적 콘텐츠로 넣은 `작성 1` 과 ***fx*** 로 넣은 **배열 필터링**의 식에서 카드 이름이 `원본값` 인지 `작성` 인지 읽는다.

19. **저장**을 누릅니다.

    **완료 기준**: 저장되는지 오류가 나는지 확인한다.

20. 카드 이름을 다시 `작성` 으로 되돌립니다.
21. **작성 2** 를 마우스 오른쪽 단추로 누르고 **삭제**를 고릅니다.
22. **배열 필터링**을 같은 방법으로 삭제합니다.
23. **작성 1** 을 같은 방법으로 삭제합니다.
24. **작성** 카드의 식을 아래로 바꾸고 **저장**을 누릅니다.

    ```
    string(42)
    ```

    **완료 기준**: 저장되고, 캔버스에 트리거와 **작성** 카드 하나가 있다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: 함수 참조[^functions] · 오류 코드 참조[^errors] · 데이터 작업(Logic Apps)[^shape] · 데이터 작업[^pa-dataops] · 이름 규칙[^naming] · 코드 보기[^peek] · 트리거 문제 해결[^triggers] · 날짜 값[^datetime] · 변수[^vars] · 표준 승인 커넥터[^approvals] · 식 요리책[^cookbook]

[^functions]: **Reference guide to functions in expressions for workflows in Azure Logic Apps and Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/workflow-definition-language-functions-reference> (2026-11-02 확인). `body()` · `outputs()` · `item()` · `items()` · `triggerBody()` · `triggerOutputs()` · `variables()` · `first()` 의 정의, `body()` 가 `actions().outputs.body` 의 줄임이라는 것, 출력 예시의 `statusCode` · `headers` · `body`.
[^errors]: **Cloud flow error code reference** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/error-reference> (2026-11-02 확인). 식의 카드 이름은 공백 대신 밑줄을 쓰고 대소문자까지 맞아야 한다는 것, 없는 이름의 `InvalidTemplate`, 병렬 가지 참조의 `FlowCheckerError`, `DuplicateActionName` 과 이름을 바꾼 뒤 식을 고치는 절차. 문서 끝에 AI 도움으로 썼다고 적혀 있다.
[^shape]: **Shape data in workflows for Azure Logic Apps** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/logic-apps-perform-data-operations> (2026-11-02 확인). `body('Filter_array')` · `body('Select')` · `body('Create_HTML_table')` 표기, 표 만들기의 열과 배열 필터링 · 선택에서 쓰는 `item()`, For each 안의 `items()`.
[^pa-dataops]: **Use data operations** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/data-operations> (2026-11-02 확인). 카드 제목을 눌러 이름을 바꾸는 것, 작성의 동적 콘텐츠 이름이 Outputs 라는 것.
[^naming]: **Use consistent naming for flow components** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/use-consistent-naming-conventions> (2026-11-02 확인). 설명이 되는 이름과 일관된 규칙.
[^peek]: **Streamline workflow creation with Power Automate features** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/use-peekcode-addnotes> (2026-11-02 확인). 코드 보기로 카드의 JSON 정의를 읽는 것.
[^triggers]: **Troubleshoot Power Automate trigger problems and errors** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/troubleshoot/power-platform/power-automate/flow-run-issues/triggers-troubleshoot> (2026-11-02 확인). Power Apps 트리거 흐름에서 작업 이름을 바꾸지 못하는 문제와 우회 절차.
[^datetime]: **Customize or format date and time values in a flow** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/date-time-values> (2026-11-02 확인). `triggerBody()?['date']`.
[^vars]: **Store and manage values in variables** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/create-variable-store-values> (2026-11-02 확인). 변수를 부를 때 작업 이름 대신 변수 이름을 쓴다는 것.
[^approvals]: **Standard approvals** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/approvals/> (2026-11-02 확인). 응답의 정의 `Responses`(array of object)와 `responses.comments`. 문서의 이 정의는 텍스트 승인 항목에 있다.
[^cookbook]: **Expression cookbook for cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/expression-cookbook> (2026-11-02 확인). 14번 패턴. 빈 배열에 쓴 `first()`. 문서 끝에 AI 도움으로 썼다고 적혀 있다.
