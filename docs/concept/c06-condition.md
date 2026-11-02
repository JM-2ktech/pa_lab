---
title: "C6. 조건 카드와 조건 식"
parent: "개념 1. 흐름의 구성"
nav_order: 6
concept:
  id: C6
  grade: B
  used_in: "Lab 1 ④ 조건 · ⑥ 예약 트리거와 식 · Lab 2 ⑤ 거르기와 세기 · Lab 3 ③ 결과 분기"
  tokens: ["조건 구성 창", "다음과 같음", "다음과 같지 않음", "작거나 같음", "Filter Query"]
  sample: true
---

# C6. 조건 카드와 조건 식

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. C7 의 식 연습장_HGD 가 수동 트리거 + 작성 카드 하나라고 보고 썼다.
     ⚠️ 문서의 and · or 예는 값이 정해진 식과 item() 을 쓴 식이다. item() 식은 반복 안에서만 값이 있어 샘플에 넣지 않았다. 랩 본문에는 and · or · not · equals 식이 없다. 조건 카드와 Filter Query 줄만 쓴다.
     ⚠️ 실측할 것: 샘플 8번 — equals 가 대소문자를 구분하는지 문서에 적혀 있지 않다. Lab 3 20번 경고(approve 로 적으면 False)의 근거는 승인 문서의 「응답 값은 대소문자를 구분한다」이고, 비교 쪽 동작은 확인 전이다. 실행 결과를 보고 8번 완료 기준과 본문을 고친다.
     ⚠️ 실측할 것: 새 디자이너의 줄 추가 라벨(문서는 구 화면의 「추가」), 줄 묶음 And · Or 라벨, 실측되지 않은 연산자 라벨 「보다 크거나 같음」(한국어판 add-condition), 고급 모드의 새 디자이너 경로(문서의 고급 모드 설명은 구 디자이너 기준으로 보인다), 조건의 왼쪽 값에 식을 넣고 오른쪽을 fx true 로 두는 샘플 10·11번이 Lab 1 26번처럼 도는지, 카드 삭제 라벨.
     연산자와 함수의 대응은 문서에 표가 없어 이름으로 맞췄다. 코드 보기에서 확인한다.
     문서 and-less 합친 식은 열 이름이 DueDate 와 dueDate 로 어긋난다. 표에는 less 단독 식만 옮겼다. -->

> **다루는 것**: 조건 카드의 구성, 오른쪽 값의 형식, 논리 함수와 조건, 카드와 식을 고르는 기준
>
> **쓰는 곳**: Lab 1 24~26번 조건 · 다음과 같음 · fx `true` · 47번 작거나 같음 · Lab 2 30번 다음과 같지 않음 · Lab 3 19·20번 결과 다음과 같음 `Approve`. 조건 식은 랩에서 쓰지 않음

---

## 조건 카드의 구성

조건 카드는 값을 비교해 참이면 True 가지, 거짓이면 False 가지를 실행합니다.[^add]

| 부분 | 내용 |
|---|---|
| 왼쪽 값 | 값 선택 칸. 동적 콘텐츠 또는 식 |
| 연산자 | 드롭다운. 기본은 다음과 같음 |
| 오른쪽 값 | 값 선택 칸. 글자 · 동적 콘텐츠 · 식 |
| True 가지 | 조건이 참일 때 실행하는 작업 |
| False 가지 | 조건이 거짓일 때 실행하는 작업 |

실행되지 않은 가지의 카드는 실행 화면에서 건너뜀으로 표시됩니다. 조건 줄을 채우면 아래에 빈 줄이 하나 더 생기고 실행에 영향을 주지 않습니다. **추가** 단추로 줄을 더해 복잡한 조건을 만듭니다.[^add]

| 연산자 | 같은 비교를 하는 함수 |
|---|---|
| 다음과 같음 | `equals` |
| 다음과 같지 않음 | `not(equals(...))` |
| 작거나 같음 | `lessOrEquals` |
| 보다 크거나 같음 | `greaterOrEquals` |

---

## 오른쪽 값의 형식

| 왼쪽 값 | 오른쪽에 넣는 것 | 입력 방법 |
|---|---|---|
| 예/아니요 | `true` · `false` | fx 로 입력. 칸에 직접 입력하면 문자열이 됨 |
| 승인 결과 | `Approve` · `Reject` | 칸에 글자 그대로. 문서는 응답 값이 대소문자를 구분한다고 적음[^sequential] |
| 숫자 | `10` | 칸에 입력[^add] |
| `yyyy-MM-dd` 날짜 문자열 | 같은 꼴의 문자열 | 동적 콘텐츠 또는 식 |

날짜 문자열을 그대로 비교하면 ISO 꼴에서만 순서가 맞습니다. `greater('2026-03-18', '2026-03-15')` 는 `true` 입니다. `greater('03/18/2026', '12/01/2025')` 는 `0` 이 `1` 보다 작아 `false` 입니다. 다른 꼴은 `ticks()` 로 바꿔 비교합니다.[^cookbook]

조건에서 값을 비교할 때 null 은 빈 문자열로 바뀝니다. 빈 문자열과의 비교와 null 과의 비교는 결과가 다릅니다.[^functions]

---

## 논리 함수

함수는 `true` 또는 `false` 를 돌려줍니다. `if` 는 지정한 값을 돌려줍니다.[^expressions][^functions]

| 함수 | 결과 | 예 | 예의 결과 |
|---|---|---|---|
| `and` | 모두 참이면 참 | `and(greater(1,10),equals(0,0))` | false |
| `or` | 하나라도 참이면 참 | `or(greater(1,10),equals(0,0))` | true |
| `not` | 반대 값 | `not(contains('200 Success','Fail'))` | true |
| `equals` | 두 값이 같으면 참 | `equals('abc', 'abcd')` | false |
| `less` | 첫 값이 작으면 참 | `less(10,100)` | true |
| `lessOrEquals` | 첫 값이 작거나 같으면 참 | `lessOrEquals(10,10)` | true |
| `greater` | 첫 값이 크면 참 | `greater(10,10)` | false |
| `greaterOrEquals` | 첫 값이 크거나 같으면 참 | `greaterOrEquals(10,100)` | false |
| `empty` | 비어 있으면 참 | `empty('')` | true |
| `contains` | 항목이 있으면 참 | `contains('hello world', 'world')` | true |
| `startsWith` | 그 글자로 시작하면 참 | `startsWith('hello world', 'hello')` | true |
| `endsWith` | 그 글자로 끝나면 참 | `endsWith('hello world', 'world')` | true |
| `if` | 조건에 따라 지정한 값 | `if(equals(1, 1), 'yes', 'no')` | yes |

함수마다 받는 값과 조건이 다릅니다.[^expressions][^functions][^cookbook]

| 함수 | 조건 |
|---|---|
| `and` · `or` | 인수는 부울. 함수 참조는 인수를 둘 이상 받는 형식으로 적음 |
| `less` · `greater` 계열 | 정수 · 부동 소수점 · 문자열 |
| `equals` | 형식이 달라도 오류 없이 결과를 돌려줌. `equals(true, 1)` 은 true |
| `strongEquals` | 형식이 다르면 오류. 정수와 부동 소수점은 섞어 쓸 수 있음 |
| `empty` | 문자열 · 배열 · 객체. `empty(null)` 은 true, 숫자에 쓰면 오류 |
| `contains` | 문자열 · 배열 · 사전. 대소문자 구분 |
| `startsWith` · `endsWith` | 대소문자 구분 안 함 |

식에는 `>` · `<` · `&&` · `||` 같은 연산자 기호를 쓰지 않습니다. `greater()` · `and()` · `or()` 함수를 씁니다.[^cookbook]

---

## 문서의 조건 식

문서의 예입니다. `item()` 은 각각에 적용 안에서 현재 행을 읽습니다.[^expressions]

| 고르는 행 | 식 |
|---|---|
| Status 가 blocked 이고 Assigned 가 John Wonder | `and(equals(item()?['Status'], 'blocked'), equals(item()?['Assigned'], 'John Wonder'))` |
| Status 와 Assigned 가 모두 빔 | `and(empty(item()?['Status']), empty(item()?['Assigned']))` |
| 납부액이 받을 금액보다 적음 | `greater(item()?['Due'], item()?['Paid'])` |
| 마감이 하루 안에 옴 | `less(item()?['DueDate'], addDays(utcNow(),1))` |

문서 원문은 조건 카드의 고급 모드에 넣는 식이라 앞에 `@` 가 붙습니다.

---

## 카드와 식을 고르는 기준

| 쓰는 것 | 고르는 경우 | 결과 |
|---|---|---|
| 조건 카드 한 줄 | 값 하나를 다른 값과 비교 | 두 가지로 나뉨 |
| 조건 카드 여러 줄 | 값 여러 개를 비교하고 사람이 읽기 쉽게 둠 | 두 가지로 나뉨 |
| 조건 카드 + 식 | 왼쪽 값을 함수로 계산해야 함 | 두 가지로 나뉨 |
| `if()` | 가지 없이 값 하나만 고름 | 값 |

식을 깊이 겹치면 읽기 어려워집니다. 문서는 이 경우 여러 줄의 조건 카드를 권합니다.[^cookbook] 필터 쿼리와 배열 필터링은 [C13](c13-filter.html)에서 다룹니다.

---

## 샘플

흐름 `식 연습장_HGD` 를 씁니다. 없으면 [C7](c07-types.html)의 샘플로 만듭니다.

1. `식 연습장_HGD` 의 **편집**을 눌러 디자이너를 엽니다.
2. **작성** 카드를 누릅니다. **입력** 칸을 비우고 ***fx*** 단추를 누릅니다. 식 편집기에 아래를 붙여넣고 **추가**를 누릅니다.

    ```
    and(greater(1,10),equals(0,0))
    ```

3. **저장**을 누르고 **테스트** › **수동** › **테스트**를 누릅니다. **흐름 실행**을 누르고 **완료**를 누릅니다.
4. 실행 화면에서 **작성** 카드를 누릅니다.

    **완료 기준**: 출력이 `false` 다.

5. 실행 화면 오른쪽 위 **편집**을 눌러 디자이너로 돌아옵니다. **작성** 카드의 식을 아래로 바꿔 3·4번을 되풀이합니다.

    ```
    or(greater(1,10),equals(0,0))
    ```

    **완료 기준**: 출력이 `true` 다.

6. 비어 있는지 보는 식으로 바꿔 되풀이합니다.

    ```
    empty('')
    ```

    **완료 기준**: 출력이 `true` 다.

7. 값을 고르는 식으로 바꿔 되풀이합니다.

    ```
    if(equals(1, 1), 'yes', 'no')
    ```

    **완료 기준**: 출력이 `yes` 다.

8. 대소문자가 다른 문자열을 비교하는 식으로 바꿔 되풀이합니다.

    ```
    equals('Approve', 'approve')
    ```

    **완료 기준**: 출력이 `true` 또는 `false` 로 보인다. 문서에 이 비교의 결과가 적혀 있지 않으므로 출력을 확인합니다.

9. **편집**을 누르고 **작성** 카드 아래 **+** › **작업 추가**를 누릅니다. **기본 제공 도구** › **컨트롤** › **조건**을 고릅니다.
10. 조건 구성 창의 왼쪽 **값 선택** 칸에서 ***fx*** 단추를 누르고 아래를 붙여넣은 뒤 **추가**를 누릅니다.

    ```
    greater(10, 5)
    ```

11. 연산자가 **다음과 같음**인지 확인합니다. 오른쪽 **값 선택** 칸에서 ***fx*** 단추를 누르고 아래를 붙여넣은 뒤 **추가**를 누릅니다.

    ```
    true
    ```

12. 캔버스의 **True** 가지 안의 **+** › **작업 추가**를 누르고 **기본 제공 도구** › **데이터 작업** › **작성**을 고릅니다. **입력** 칸에 아래를 입력합니다.

    ```
    참 가지
    ```

13. **False** 가지에도 **작성**을 놓고 **입력** 칸에 아래를 입력합니다.

    ```
    거짓 가지
    ```

14. 3번과 같이 저장하고 실행합니다.

    **완료 기준**: **True** 가지의 작성 카드에 초록 체크가 붙고 **False** 가지의 카드는 건너뜀이다.

15. **편집**을 누르고 조건의 왼쪽 값을 아래 식으로 바꿉니다. 3번과 같이 저장하고 실행합니다.

    ```
    greater(1, 10)
    ```

    **완료 기준**: **False** 가지의 작성 카드에 초록 체크가 붙고 **True** 가지의 카드는 건너뜀이다.

16. **편집**을 누르고 **조건** 카드를 고릅니다. 구성 창 위쪽 **⋮** 를 누르고 **삭제**를 고릅니다. **저장**을 누릅니다.

    **완료 기준**: 캔버스에 트리거와 **작성** 카드만 남는다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **실측**: 값 선택 · 다음과 같음 · 다음과 같지 않음 · 작거나 같음 · True · False 라벨, 예/아니요 칸의 `true` 동작, 빈 줄과 건너뜀 표시는 Lab 1~3 실측(2026-10-05)을 따랐습니다.
- **문헌**: 조건 추가[^add] · 조건에서 식 사용[^expressions] · 식 함수 참조[^functions] · 식 요리책[^cookbook] · 순차 승인[^sequential]

[^add]: **Add a condition to a cloud flow** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/add-condition> (2026-11-02 확인). 조건 카드의 왼쪽 값 · 연산자 · 오른쪽 값, **추가** 단추. 문서 화면은 예전 디자이너(**예인 경우** · **아니요인 경우**)다.
[^expressions]: **Use expressions in conditions to check multiple values** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/use-expressions-in-conditions> (2026-11-02 확인). 논리 식 표와 예, 각각에 적용 안의 `item()` 식. 한국어판은 표의 함수 이름 일부를 「그리고」 · 「같음」으로 번역했고 식 자체는 영어다.
[^functions]: **Reference guide to functions in expressions for workflows in Azure Logic Apps and Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/workflow-definition-language-functions-reference> (2026-11-02 확인). 함수별 조건, `equals(true, 1)`, `strongEquals`, `contains` · `startsWith` · `endsWith` 의 대소문자, null 과 빈 문자열.
[^cookbook]: **Expression cookbook for cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/expression-cookbook> (2026-11-02 확인, 문서 끝에 AI 도움 표기). 26 · 28 · 29 · 30번 패턴. 연산자 기호를 쓰지 않는다는 것, 날짜 비교, `empty` 의 조건.
[^sequential]: **Manage sequential approvals with Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/sequential-modern-approvals> (2026-11-02 확인). 승인 응답 값 Approve · Reject 가 대소문자를 구분한다는 것.
