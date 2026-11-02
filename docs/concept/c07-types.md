---
title: "C7. 자료형"
parent: "개념 2. 자료형과 식"
nav_order: 7
concept:
  id: C7
  grade: A
  used_in: "Lab 1 ④ 조건 · ⑥ 예약 트리거와 식 · Lab 2 ④ 행 읽기 · ⑤ 거르기와 세기"
  tokens: ["string(", "length(", "예/아니요", "['value']"]
  sample: true
---

# C7. 자료형

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. 흐름 `식 연습장_HGD` 를 이 페이지가 만들고 다른 개념 페이지가 같이 쓴다. 이름 · 입력 이름을 바꾸면 그쪽도 고친다.
     ⚠️ 실측할 것: 텍스트 입력은 기본이 필수(`*`)다(Lab 1 35번 화면). 다른 페이지 샘플은 입력값 없이 흐름 실행을 누르므로 6번에서 선택 사항으로 바꾼다.
        ⋯ 메뉴의 라벨 「필드 선택 사항」은 Copilot Studio 워크플로 문서 한국어판(flows-request-for-information)의 표기다. Power Automate 트리거 문서에는 없다
     ⚠️ 실측할 것: 입력 유형별 triggerBody() 키. 문서에는 date 예만 있다. 텍스트 입력의 키 text 는 다른 페이지가 전제한다
     ⚠️ 실측할 것: 연결이 없는 흐름의 흐름 실행 창에 계속 단계가 있는가(Lab 1 34번은 연결이 셋일 때의 화면이다)
     ⚠️ 실측할 것: 숫자 입력 유형의 자료형, 식 편집기가 `[1, 2, 3]` 표기를 받는가(워크플로 정의 언어 문서의 표기다)
     ⚠️ 실측할 것: 조건 오른쪽에 true 를 글자로 입력했을 때의 판정. Lab 1 저작 메모에 같은 항목이 미확인으로 남아 있다 -->

> **다루는 것**: 클라우드 흐름의 값이 가지는 자료형과, 자료형을 바꾸는 함수
>
> **쓰는 곳**: Lab 1 `true`(예/아니요와 비교) · `length(body('배열_필터링'))`(정수) · Lab 2 `body('원본행')?['value']`(배열) · `string(length(body('점검행')))`(정수를 문자열로)

---

## 자료형 여섯 가지

변수로 만들 수 있는 자료형은 여섯 가지입니다.[^vars] 작업의 입력과 출력, 식의 결과도 이 형식으로 읽습니다.

| 자료형 | 변수의 형식 이름 | 담는 것 | 식에서 적는 표기 |
|---|---|---|---|
| 문자열 | string | 글자 | `'이상'` |
| 정수 | integer | 소수 없는 수 | `32` |
| 부동 소수점 | float | 소수 있는 수 | `3.14` |
| 부울 | boolean | 참 · 거짓 | `true` · `false` |
| 배열 | array | 항목의 나열 | `createArray('주의', '이상')` · `[1, 2, 3]` |
| 객체 | object | 키와 값의 쌍 | `json('{"결과":"이상"}')` |

식 안의 문자열은 작은따옴표로 감쌉니다. 큰따옴표는 쓰지 않습니다.[^wdl] 수와 배열에는 따옴표를 붙이지 않습니다. `'42'` 는 문자열이고 `42` 는 정수입니다.

값이 없는 상태는 `null` 입니다. 논리 함수와 조건에서 비교할 때 `null` 은 빈 문자열 `""` 로 바뀝니다.[^functions] `null` 을 읽는 표기는 [C8](c08-json.html)에서 다룹니다.

---

## 식과 글자

칸에 입력한 글자는 글자 그대로 들어갑니다. ***fx*** 로 넣은 식은 실행할 때 계산됩니다. 부울과 비교하는 값은 ***fx*** 로 `true` 를 넣습니다.

**코드 보기**에서 식은 `@` 로 시작합니다. 글자 사이에 든 식은 `@{ }` 로 감쌉니다. 이렇게 감싼 식의 결과는 언제나 문자열입니다.[^wdl]

| 코드 보기의 값 | 결과 | 자료형 |
|---|---|---|
| `"이상"` | `이상` | 문자열 |
| `"@length('abcd')"` | `4` | 정수 |
| `"@{length('abcd')}"` | `4` | 문자열 |
| `"건수 @{length('abcd')}"` | `건수 4` | 문자열 |

---

## 수동 트리거의 입력 유형

수동 트리거의 입력 유형은 텍스트 · 예/아니요 · 파일 · 이메일 · 숫자 · 날짜 여섯 가지입니다.

| 입력 유형 | 식에서 받는 값 |
|---|---|
| 텍스트 | 문자열 |
| 예/아니요 | 부울 |
| 숫자 | 수 |
| 날짜 | `YYYY-MM-DD` 모양의 문자열. `triggerBody()?['date']` 로 읽음[^datetime] |

---

## 날짜 값의 자료형

변수의 형식에 날짜는 없습니다. 날짜 함수는 시각을 문자열로 받고 문자열로 돌려줍니다.[^functions] 시각의 모양과 시간대는 [C11](c11-datetime.html)에서 다룹니다.

---

## 자료형을 바꾸는 함수

| 함수 | 받는 값 | 예 | 결과 | 조건 |
|---|---|---|---|---|
| `string()` | 모든 값 | `string(42)` | `"42"` | `null` 은 빈 문자열이 됨 |
| `int()` | 정수 모양의 문자열 | `int('42')` | `42` | `int('3.14')` 는 오류[^cookbook] |
| `float()` | 수 모양의 문자열 | `float('3.14')` | `3.14` | 둘째 인수는 로캘. `float('10.000,333', 'de-DE')` 는 `10000.333` |
| `decimal()` | 소수 모양의 문자열 | `decimal('1.2345678912312131')` | `1.234567891231213` | 자릿수를 지키려면 `string()` 으로 감쌈 |
| `bool()` | 수 · 문자열 | `bool('true')` | `true` | `bool(1)` · `bool(-1)` 은 `true`, `bool(0)` · `bool('false')` 는 `false` |
| `array()` | 문자열 하나 | `array('hello')` | `["hello"]` | 항목이 여럿이면 `createArray()` |
| `createArray()` | 항목 두 개 이상 | `createArray('주의', '이상')` | `["주의","이상"]` | 항목의 형식을 섞지 않음. 인수가 없으면 저장 오류[^errors] |
| `json()` | JSON 모양의 문자열 | `json('[1, 2, 3]')` | `[1, 2, 3]` | [C8](c08-json.html) |

`float()` 는 쉼표를 천 단위 구분으로 읽습니다. `float('10,000.333')` 은 `10000.333` 입니다. 함수 참조는 `float('12,3,4,5678')` 이 `12345678` 이 되는 입력도 유효하다고 적습니다.[^functions]

바꾸기 전에 문자열을 검사하는 함수가 있습니다.

| 함수 | 예 | 결과 |
|---|---|---|
| `isInt()` | `isInt('10')` | `true` |
| `isFloat()` | `isFloat('10,000.00')` | `true` |
| `isFloat()` 에 로캘 지정 | `isFloat('10.000,00', 'de-DE')` | `true` |

---

## 형식이 다른 값의 처리

문자열이 와야 하는 곳에 다른 형식을 넣으면 자동으로 문자열로 바뀝니다.[^functions] 나머지는 함수마다 규칙이 있습니다.

| 식 | 결과 | 규칙 |
|---|---|---|
| `add(1, 1.5)` | `2.5` | 정수와 부동 소수점을 섞을 수 있음 |
| `div(11, 5)` | `2` | 정수끼리 나누면 정수 |
| `div(11, 5.0)` | `2.2` | 한쪽이 부동 소수점이면 부동 소수점 |
| `concat('건수 ', string(3))` | `건수 3` | `concat()` 의 인수는 문자열 |
| `equals(true, 1)` | `true` | `equals()` 는 형식이 달라도 같다고 판정할 수 있음 |
| `strongEquals(1, 1.0)` | `true` | 정수와 부동 소수점은 함께 비교함. 그 밖에 형식이 다르면 오류 |

---

## 자료형이 맞지 않을 때의 오류

| 오류 | 나오는 때 | 상황 |
|---|---|---|
| `InvalidTemplate` | 저장 | 상수만 쓴 식의 형식 오류. `int('abc')` · `div(100, 0)` |
| `ExpressionEvaluationFailed` | 실행 | 동적 값이 식과 맞지 않음. 숫자가 아닌 글자에 `int()` |
| `ContentConversionFailed` | 실행 | 작업 사이의 변환 실패. 정수 칸에 문자열, 객체 하나를 받는 칸에 배열, 다른 모양의 날짜 문자열 |
| `BadRequest (400)` | 실행 | 커넥터 API가 형식이 다른 값을 거절함 |

문서가 드는 대처는 세 가지입니다.[^errors] 변환 전에 검사하는 `if(isInt(값), int(값), 0)`, 명시적으로 바꾸는 `int()` · `float()` · `string()` · `bool()` · `json()`, 배열에서 항목 하나를 고르는 `first()` 입니다.

---

## 샘플

식을 바꿔 가며 실행하는 흐름 `식 연습장_HGD` 를 만듭니다. 다른 개념 페이지의 샘플도 이 흐름을 씁니다.

1. 아래 링크로 Power Automate를 엽니다. 위쪽 가운데 **환경**이 `{{ site.pa.environment }}` 인지 확인합니다.

    [Power Automate — {{ site.pa.environment }}]({{ site.pa.powerautomate_url }}){:target="_blank"}

2. 왼쪽 메뉴 **+ 만들기**를 누르고 **시작(처음부터)**의 **인스턴트 클라우드 흐름**을 고릅니다.
3. **인스턴트 클라우드 흐름 작성** 창의 **흐름 이름**에 아래를 입력합니다. `HGD` 대신 본인 이니셜을 넣습니다. 트리거 목록에서 **수동으로 흐름 트리거**를 고르고 **만들기**를 누릅니다.

    ```
    식 연습장_HGD
    ```

4. 왼쪽 구성 창의 **매개 변수** 탭에서 **+ 입력 추가**를 누르고 **사용자 입력 유형 선택**에서 **텍스트**를 고릅니다.
5. 입력 이름 칸에 아래를 입력합니다.

    ```
    입력값
    ```

6. 입력 줄 오른쪽 **⋯**를 누르고 **필드 선택 사항**을 고릅니다.
7. 트리거 카드 아래 **+**를 누르고 **작업 추가**를 고릅니다. **기본 제공 도구**에서 **데이터 작업**을 누르고 **작성**을 고릅니다. 작업이 하나도 없는 흐름은 저장되지 않으므로 저장은 이 카드를 놓은 뒤에 합니다.
8. **입력** 칸을 누르고 ***fx*** 단추를 누릅니다. 식 편집기에 아래를 붙여넣고 **추가**를 누릅니다.

    ```
    string(42)
    ```

9. 위쪽 명령 모음의 **저장**을 누릅니다.

    **완료 기준**: 「흐름을 진행할 준비가 되었습니다」 알림이 뜬다.

10. **테스트**를 누르고 **흐름 테스트** 창에서 **수동**을 고른 뒤 **테스트**를 누릅니다. **흐름 실행** 창이 뜨면 **흐름 실행**을 누르고 **완료**를 누릅니다. `입력값` 칸은 비워 둡니다. 칸 이름 옆에 `*` 가 있으면 아무 글자나 넣습니다.
11. 실행 화면에서 **작성** 카드를 누르고 왼쪽 **출력**을 봅니다.

    **완료 기준**: 출력이 `42` 다.

12. 오른쪽 위 **편집**을 눌러 디자이너로 돌아옵니다. **작성** 카드의 **입력** 칸을 비우고 ***fx*** 로 아래 식을 넣어 9~11번을 되풀이합니다.

    ```
    add(int('40'), 2)
    ```

    **완료 기준**: 출력이 `42` 다.

13. 같은 글자를 문자열로 잇는 식으로 바꿔 되풀이합니다.

    ```
    concat('40', '2')
    ```

    **완료 기준**: 출력이 `402` 다.

14. 부동 소수점으로 바꾸는 식으로 바꿔 되풀이합니다.

    ```
    float('3.14')
    ```

    **완료 기준**: 출력이 `3.14` 다.

15. 부울로 바꾸는 식으로 바꿔 되풀이합니다.

    ```
    bool('false')
    ```

    **완료 기준**: 출력이 `false` 다.

16. 배열을 만드는 식으로 바꿔 되풀이합니다.

    ```
    createArray('주의', '이상')
    ```

    **완료 기준**: 출력이 항목 두 개의 배열이다.

17. 배열의 개수를 문자열에 잇는 식으로 바꿔 되풀이합니다.

    ```
    concat('건수 ', string(length(createArray('주의', '이상'))))
    ```

    **완료 기준**: 출력이 `건수 2` 다.

18. 정수로 바꿀 수 없는 상수를 넣고 **저장**을 누릅니다.

    ```
    int('3.14')
    ```

    **완료 기준**: 저장되지 않고 오류가 표시된다.

19. 식을 아래로 되돌리고 **저장**을 누릅니다.

    ```
    string(42)
    ```

    **완료 기준**: 「흐름을 진행할 준비가 되었습니다」 알림이 뜨고, 캔버스에 트리거와 **작성** 카드 하나가 있다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: 변수[^vars] · 식 요리책[^cookbook] · 함수 참조[^functions] · 워크플로 정의 언어[^wdl] · 오류 코드 참조[^errors] · 날짜 값[^datetime]

[^vars]: **Store and manage values in variables** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/create-variable-store-values> (2026-11-02 확인). 변수의 자료형 여섯 가지.
[^cookbook]: **Expression cookbook for cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/expression-cookbook> (2026-11-02 확인). 24번 패턴. `int()` 는 소수 문자열에서 오류가 나고, 상수면 저장할 때 잡힌다는 것. 문서 끝에 AI 도움으로 썼다고 적혀 있다.
[^functions]: **Reference guide to functions in expressions for workflows in Azure Logic Apps and Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/workflow-definition-language-functions-reference> (2026-11-02 확인). 변환 함수의 인수와 결과, 암시적 변환, 비교할 때의 null, `div()` · `add()` · `equals()` · `strongEquals()` 의 규칙, 날짜 함수의 시각이 문자열이라는 것.
[^wdl]: **Schema reference guide for the Workflow Definition Language in Azure Logic Apps** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/logic-apps-workflow-definition-language> (2026-11-02 확인). `@` 와 `@{ }` 의 결과 형식, 문자열의 작은따옴표, 수 · 배열의 표기.
[^errors]: **Cloud flow error code reference** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/error-reference> (2026-11-02 확인). `InvalidTemplate` · `ExpressionEvaluationFailed` · `ContentConversionFailed` · `BadRequest` 의 원인과 대처. 문서 끝에 AI 도움으로 썼다고 적혀 있다.
[^datetime]: **Customize or format date and time values in a flow** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/date-time-values> (2026-11-02 확인). 트리거의 **날짜** 입력을 `triggerBody()?['date']` 로 읽는 예.
