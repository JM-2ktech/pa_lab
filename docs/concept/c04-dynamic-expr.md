---
title: "C4. 동적 콘텐츠와 식"
parent: "개념 1. 흐름의 구성"
nav_order: 4
concept:
  id: C4
  grade: A
  used_in: "Lab 1 ③ 항목 만들기 · ④ 조건 · ⑥ 예약 트리거와 식 · Lab 2 ③ 대상월 · ④ 행 읽기 · ⑦ 보고서 본문 · Lab 3 ② 승인 요청 · ⑥ 반려 회신"
  tokens: ["번개 단추", "동적 콘텐츠", "식 편집기", "***fx***", "더 보기"]
  sample: true
---

# C4. 동적 콘텐츠와 식

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. C7 의 식 연습장_HGD 가 수동 트리거 + 작성 카드 하나라고 보고 썼다. C7 이 트리거에 입력을 더 두면 번개 목록의 위치만 달라진다.
     ⚠️ 실측할 것: 입력 없는 수동 트리거의 동적 콘텐츠에 「사용자 이메일」이 보이는지(Lab 1 20번은 입력 셋이 있는 트리거다), 식 편집기의 탭 라벨(문서는 동적 콘텐츠 · 함수), 4번(fx 없이 입력한 식이 글자 그대로 출력되는지, 문서에는 없고 Lab 1 26번 경고와 같은 동작으로 보았다), 코드 보기에 식이 @ · @{ } 로 보이는지, 슬래시 단축 메뉴의 라벨
     동적 콘텐츠의 정의는 date-time-values 예제 절에 한 줄 있다. 동적 콘텐츠만 다룬 문서는 찾지 못했다. -->

> **다루는 것**: 칸에 값을 넣는 세 방법, 동적 콘텐츠 목록의 동작, 식 편집기와 식의 표기, 저장되는 모양, 식 오류가 드러나는 시점
>
> **쓰는 곳**: Lab 1 19~22번 번개 단추 · 26번 fx `true` · 43번 `formatDateTime(convertFromUtc(utcNow(), 'Korea Standard Time'), 'yyyy-MM-dd')` · Lab 2 13번 대상월 · Lab 3 40번 `first(outputs('승인_시작_및_대기')?['body/responses'])?['comments']`

---

## 칸에 값을 넣는 세 방법

구성 창의 칸에는 글자를 직접 넣거나, 번개 단추로 동적 콘텐츠를 넣거나, ***fx*** 단추로 식을 넣습니다.[^designer]

| 방법 | 단추 | 칸에 보이는 모양 | 실행할 때의 값 |
|---|---|---|---|
| 글자 입력 | 없음 | 입력한 글자 | 입력한 글자 그대로 |
| 동적 콘텐츠 | 번개(동적 콘텐츠 삽입) | 칩 | 앞 단계의 출력 |
| 식 | ***fx***(식 삽입) | ***fx*** 표시가 붙은 칩 | 함수를 계산한 결과 |

칸에서 슬래시(`/`)를 입력해도 동적 콘텐츠 삽입과 식 삽입을 고를 수 있습니다.[^designer]

한 칸에 글자와 칩을 함께 넣을 수 있습니다.[^logicflow] 앞 단계의 값만 읽는 식은 fx 칩 대신 해당 값 이름의 칩으로 보이기도 합니다.

---

## 동적 콘텐츠

동적 콘텐츠는 트리거와 작업이 만들어 낸 값입니다. 앞 단계의 값을 골라 칸에 넣거나 식에 씁니다.[^datetime]

| 동작 | 내용 |
|---|---|
| 목록의 묶음 | 트리거 · 작업의 이름별로 묶어 보여 줌 |
| **더 보기** | 처음에는 일부만 보임. 찾는 값이 없으면 누름[^logicflow] |
| 칸 형식 필터 | 칸의 자료형에 맞는 값만 보여 줌. 문자열 칸의 목록에는 문자열 값만 나옴[^editor] |
| 같은 이름의 값 | 여러 카드에 같은 이름이 있으면 묶음 제목으로 카드를 구분 |
| 새 열 | SharePoint · Excel 열을 나중에 추가하면 작업을 지우고 다시 넣어야 보임[^designer] |

---

## 식 편집기

식은 함수로 값을 계산하거나 바꿉니다. 실행 중에 생기는 작업 출력도 함수로 읽습니다.[^conditions]

넣는 순서는 칸 누르기, fx 단추, 식 입력, **추가**입니다. 앞 단계의 값을 함수에 넘길 때는 함수 괄호 안에 커서를 두고 동적 콘텐츠 탭에서 값을 고른 뒤 추가를 누릅니다.[^designer]

| 식 편집기 | 내용 |
|---|---|
| 탭 | 동적 콘텐츠 · 함수 |
| 검색 칸 | 두 탭 모두에서 값과 함수를 검색 |
| 여러 줄 입력 | 긴 식을 여러 줄로 편집 |
| 크기 | 그리퍼로 한두 줄 늘림. 전체 페이지로 확장 가능 |
| 자동 완성 | 함수 이름과 매개 변수 안내[^classic] |

---

## 식의 표기

| 규칙 | 예 | 결과 |
|---|---|---|
| 문자열은 작은따옴표 | `toUpper('Hello World')` | `HELLO WORLD` |
| 숫자 · `true` · `false` · `null` 은 따옴표 없음 | `equals(1, 1)` | `true` |
| 함수 안에 함수 | `formatDateTime(utcNow(), 'yyyy-MM-dd HH:mm')` | 현재 UTC 날짜와 시각 |
| 인수는 왼쪽부터 계산 | `concat('Sophia', 'Owen')` | `SophiaOwen` |
| 앞 단계의 값은 함수로 읽음 | `triggerBody()?['text']` · `outputs('작성')` | 트리거 입력 · 작성의 출력 |

`toUpper()` 는 대문자가 없는 글자를 그대로 둡니다. 한글은 바뀌지 않습니다.[^functions] 식에 `@` 를 붙이지 않고 식 편집기에 함수부터 넣습니다.

---

## 함수 묶음

함수 참조 문서는 함수를 여덟 묶음으로 나눕니다.[^functions] 자주 쓰는 함수는 [C10](c10-expressions.html)에서 다룹니다.

| 묶음 | 함수 예 |
|---|---|
| 문자열 | `concat` · `substring` · `replace` · `split` · `toUpper` · `toLower` · `trim` |
| 컬렉션 | `first` · `last` · `contains` · `empty` · `join` · `length` |
| 논리 비교 | `and` · `or` · `not` · `equals` · `greater` · `less` · `if` |
| 변환 | `string` · `int` · `float` · `bool` · `json` · `createArray` |
| 수학 | `add` · `sub` · `mul` · `div` · `mod` · `min` · `max` |
| 날짜와 시간 | `utcNow` · `addDays` · `addToTime` · `convertFromUtc` · `formatDateTime` · `ticks` |
| 워크플로 | `triggerBody` · `triggerOutputs` · `body` · `outputs` · `item` · `variables` |
| URI 구문 분석 | `uriHost` · `uriPath` · `uriQuery` · `uriScheme` |

---

## 저장되는 모양

흐름 정의에서 식은 `@` 로 시작합니다. 카드의 **코드 보기**에서 읽을 수 있고 여기서 수정할 수는 없습니다.[^peek]

| 칸의 내용 | 정의의 모양 | 예 |
|---|---|---|
| 식 하나만 | `@함수(...)` | `@concat('Sophia', 'Owen')` |
| 글자와 식이 함께 | 식을 `@{ }` 로 감쌈 | `글자/@{함수(...)}/글자` |

문자열이 필요한 곳에 숫자 값을 쓰면 자동으로 문자열로 바뀝니다. 이때 `@{triggerBody()?['123']}` 처럼 중괄호 표기가 됩니다.[^functions]

---

## 식 오류가 드러나는 시점

식에 실행 값이 들어 있는지에 따라 오류가 드러나는 때가 다릅니다.[^errors]

| 식 | 드러나는 때 | 오류 이름 | 예 |
|---|---|---|---|
| 상수만 쓴 식 | 저장 | InvalidTemplate | `int('abc')` · `div(100, 0)` |
| 실행 값이 든 식 | 실행 | ExpressionEvaluationFailed | 문자가 든 변수에 `int()` |
| 작업 사이의 형식 변환 | 실행 | ContentConversionFailed | 정수 칸에 문자열 |

실패한 실행을 읽는 방법은 [C16](c16-run-history.html)에서 다룹니다.

---

## 흔한 실패

| 증상 | 원인 | 조치 |
|---|---|---|
| 식이 글자 그대로 출력됨 | ***fx*** 없이 칸에 입력 | 칸을 비우고 ***fx*** 로 입력 |
| 예/아니요 비교가 늘 False | `true` 를 칸에 직접 입력해 문자열이 됨 | ***fx*** 로 `true` 입력 |
| 목록에 찾는 값이 없음 | 칸 형식과 다른 값 또는 일부만 표시 | **더 보기**, 칸 형식 확인 |
| 값이 엉뚱하게 들어감 | 다른 카드의 같은 이름 값을 고름 | 묶음 제목의 카드 이름 확인 |
| 줄바꿈 대신 `\n` 이 출력됨 | 식에서 `\n` 은 글자 그대로 | `decodeUriComponent('%0A')` 사용[^cookbook] |

---

## 샘플

흐름 `식 연습장_HGD` 를 씁니다. 없으면 [C7](c07-types.html)의 샘플로 만듭니다.

1. `식 연습장_HGD` 의 **편집**을 눌러 디자이너를 엽니다.
2. **작성** 카드를 누릅니다. **입력** 칸을 비우고 아래를 ***fx*** 없이 그대로 입력합니다.

    ```
    toUpper('abc')
    ```

3. **저장**을 누르고 **테스트** › **수동** › **테스트**를 누릅니다. **흐름 실행**을 누르고 **완료**를 누릅니다.
4. 실행 화면에서 **작성** 카드를 누릅니다.

    **완료 기준**: 출력이 `toUpper('abc')` 글자 그대로다.

5. 실행 화면 오른쪽 위 **편집**을 눌러 디자이너로 돌아옵니다. **입력** 칸을 비우고 ***fx*** 단추를 누릅니다. 식 편집기에 아래를 붙여넣고 **추가**를 누른 뒤 3·4번을 되풀이합니다.

    ```
    toUpper('abc')
    ```

    **완료 기준**: 출력이 `ABC` 다.

6. **편집**을 누르고 **입력** 칸을 비웁니다. 번개 단추를 누르고 **수동으로 흐름 트리거** 아래 **사용자 이메일**을 고릅니다. 목록에 없으면 **더 보기**를 누릅니다. 3·4번을 되풀이합니다.

    **완료 기준**: 출력이 흐름을 실행한 계정의 메일 주소다.

7. **편집**을 누르고 **입력** 칸을 비웁니다. ***fx*** 단추를 누르고 식 편집기에 아래를 입력합니다.

    ```
    toUpper()
    ```

8. 괄호 안에 커서를 둡니다. **동적 콘텐츠** 탭에서 **사용자 이메일**을 고르고 **추가**를 누릅니다. 3·4번을 되풀이합니다.

    **완료 기준**: 출력이 대문자로 바뀐 메일 주소다.

9. **편집**을 누르고 **입력** 칸을 비웁니다. 아래 글자를 입력합니다. 끝에 커서를 둔 채 번개 단추로 **사용자 이메일**을 넣습니다. 3·4번을 되풀이합니다.

    ```
    실행자:
    ```

    **완료 기준**: 출력이 `실행자:` 와 메일 주소를 이은 글자다.

10. **편집**을 누르고 **작성** 카드의 **코드 보기**를 누릅니다.

    **완료 기준**: `inputs` 값에 `실행자:` 와 `@{` 로 시작하는 식이 함께 보인다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **실측**: 번개 단추 · fx 단추 · 더 보기 · 칩의 모양, 예/아니요 칸의 `true` 동작은 Lab 1 · Lab 2 실측(2026-10-05)을 따랐습니다.
- **문헌**: 클라우드 흐름 디자이너[^designer] · 클라우드 흐름 만들기[^logicflow] · 날짜와 시간 값[^datetime] · 흐름 편집기 문제[^editor] · 조건에서 식 사용[^conditions] · 구 디자이너와 새 디자이너[^classic] · 식 함수 참조[^functions] · 코드 보기와 메모[^peek] · 오류 코드 참조[^errors] · 식 요리책[^cookbook]

[^designer]: **Explore the cloud flows designer** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/flows-designer> (2026-11-02 확인). 번개와 ***fx*** 단추, 슬래시 단축, 식 편집기, 열을 추가한 뒤 작업을 다시 넣는 것.
[^logicflow]: **Create a cloud flow in Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/get-started-logic-flow> (2026-11-02 확인). 글자와 동적 콘텐츠를 함께 넣는 것, **더 보기**.
[^datetime]: **Customize or format date and time values in a flow** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/date-time-values> (2026-11-02 확인). 동적 콘텐츠의 정의.
[^editor]: **Flow Editor issues and recommendations** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/troubleshoot/power-platform/power-automate/flow-creation/flow-editor-issues-recommendations> (2026-11-02 확인). 칸의 자료형에 따라 목록을 거른다는 것.
[^conditions]: **Use expressions in conditions to check multiple values** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/use-expressions-in-conditions> (2026-11-02 확인). 실행할 때 값을 가져오는 식과 함수.
[^classic]: **Classic designer vs. new designer for cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/classic-vs-modern-designer> (2026-11-02 확인, 문서 끝에 AI 도움 표기). 식 편집기의 자동 완성.
[^functions]: **Reference guide to functions in expressions for workflows in Azure Logic Apps and Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/workflow-definition-language-functions-reference> (2026-11-02 확인). 함수 묶음, `toUpper`, 인수 계산 순서, `@` 와 `@{ }` 표기, 자동 형식 변환.
[^peek]: **Streamline workflow creation with Power Automate features** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/use-peekcode-addnotes> (2026-11-02 확인). 코드 보기가 읽기 전용이라는 것.
[^errors]: **Cloud flow error code reference** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/error-reference> (2026-11-02 확인). InvalidTemplate · ExpressionEvaluationFailed · ContentConversionFailed.
[^cookbook]: **Expression cookbook for cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/expression-cookbook> (2026-11-02 확인, 문서 끝에 AI 도움 표기). 5번 줄바꿈 패턴.
