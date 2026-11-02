---
title: "C18. 반복과 동시성"
parent: "개념 3. 승인과 실행 기록"
nav_order: 18
concept:
  id: C18
  grade: B
  used_in: "챌린지 요구사항 3 · 4 · 쓰는 기능 표 · 확인 ④⑤ · Lab 3 ⑥ 40번(동적 콘텐츠가 For each 로 감싸는 동작)"
  tokens: ["각각에 적용", "동시성 제어"]
  sample: true
---

# C18. 반복과 동시성

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. Do until 의 동작 세부는 Azure Logic Apps 문서가 출처다. 기본 60회는 Power Automate limits 문서와 일치한다. 기본 1시간은 Logic Apps 문서에만 있다.
     ⚠️ Logic Apps 문서의 For each 는 기본이 병렬이고 Power Automate 의 각각에 적용은 기본이 순차다. 본문은 Power Automate 문서를 따랐다.
     ⚠️ 실측할 것(라벨): 반복 카드 이름 — 문서는 각각에 적용 · Apply to each · For each 를 섞어 쓴다. Lab 3 40번은 For each 로 적었다. 챌린지 저작 메모도 같은 항목을 실측 대기로 둔다.
        Do until — ko-kr common-data-model-approve 는 「기한」으로 옮겼다(오역으로 보인다). 화면 이름 확인. 조건 칸 이름(Loop Until) · 횟수 · 시간 제한 칸 이름.
        설정 탭의 동시성 제어 · 병렬 처리 수준. 이전 단계에서 출력 선택 칸 이름. 실행 화면에서 반복을 넘겨 보는 조작.
     ⚠️ 실측할 것(동작): 동적 콘텐츠로 배열 속성을 고를 때 감싸는 동작은 Lab 3 40번 본문을 따랐다. 문서에서 찾지 못했다.
        병렬 실행에서 변수 증가의 결과. Power Automate 문서는 증가 · 감소를 예외처럼 적고, Logic Apps 문서는 증가 · 감소 · 추가 모두 예측할 수 없다고 적는다. 본문은 뒤쪽을 따라 순차를 권했다.
        값 칸에 숫자 10 을 그냥 넣었을 때 정수로 처리되는지. 샘플은 fx 로 넣었다. -->

> **다루는 것**: 클라우드 흐름의 반복 두 가지 — 각각에 적용과 Do until, 순차와 동시 실행, 반복 안의 변수, 반복을 줄이는 방법
>
> **쓰는 곳**: 챌린지 요구사항 3 · 4 각각에 적용, 확인 ⑤ 동시성 제어 · Lab 3 ⑥ 40번 `first(...)` 식을 쓰는 이유

---

## 반복 두 가지

클라우드 흐름의 반복은 작업 추가 창의 기본 제공 도구 › 컨트롤에 있는 두 작업입니다.[^la-loops][^apply]

| 항목 | 각각에 적용 | Do until |
|---|---|---|
| 영문 이름 | Apply to each · For each | Do until |
| 하는 일 | 배열의 항목마다 안의 작업을 실행 | 조건이 참이 될 때까지 안의 작업을 되풀이 |
| 입력 | 배열 | 조건식과 한도 |
| 반복 횟수 | 배열의 항목 수 | 조건이 참이 될 때까지. 한도 안에서 |
| 조건 확인 | 없음 | 안의 작업을 실행한 뒤 |
| 최소 실행 | 항목 수만큼 | 한 번 |
| 동시 실행 | 1~50 | 해당 없음 |

---

## 각각에 적용

입력과 한도입니다.[^apply][^limits][^errref][^schema]

| 항목 | 내용 |
|---|---|
| 입력 칸 | **이전 단계에서 출력 선택** |
| 입력 값 | 배열. 배열이 아니면 실패 |
| 현재 항목 | `item()` · `items('카드 이름')` |
| 항목 수 한도 | 성능 프로필 Low 5,000 · 나머지 100,000 |
| 넘을 때 오류 | `WorkflowRunActionRepetitionQuotaExceeded` |
| 안에 둘 수 없는 작업 | 변수 초기화 · 종료 |

항목 안의 값을 읽는 표기입니다.[^functions]

| 식 | 읽는 값 |
|---|---|
| `item()` | 현재 항목 전체 |
| `item()?['설비명']` | 현재 항목의 그 키 값 |
| `items('각각에_적용')?['설비명']` | 이름을 지정한 반복의 현재 항목. 반복이 겹칠 때 바깥 항목을 읽음 |

배열 안 항목의 값을 동적 콘텐츠로 고르면 디자이너가 그 카드를 각각에 적용으로 감쌉니다. 식으로 넣으면 감싸지 않습니다.

---

## Do until

Do until 은 세 경우에 멈춥니다.[^la-loops][^limits]

| 멈추는 경우 | 값 |
|---|---|
| 조건이 참 | 안의 작업을 실행한 뒤 확인 |
| 횟수 한도 | 기본 60회 · 최대 5,000회 |
| 시간 한도 | 기본 1시간. ISO 8601 표기. 예: `PT1H` · `PT2H` |

| 항목 | 동작 |
|---|---|
| 시간 한도에 닿을 때 | 진행 중인 반복은 끝까지 실행. 다음 반복을 시작하지 않음 |
| 중간 반복의 실패 | 다음 반복이 이어서 실행됨 |
| Do until 의 상태 | 마지막 반복의 작업이 모두 성공하면 성공. 하나라도 실패하면 실패 |
| 실행 기록 | 실행 중에는 **Running** 만 보임. 끝난 뒤 반복마다 결과를 봄 |
| 현재 반복 번호 | `iterationIndexes('카드 이름')` |

조건에 쓰는 값은 반복 안에서 바뀌어야 합니다. 바뀌지 않으면 한도에 닿을 때까지 돕니다. 변수로 조건을 쓴 식의 예입니다.[^la-loops]

```
equals(variables('합계'), 100)
```

---

## 순차와 동시 실행

각각에 적용은 기본이 순차 실행입니다. 한 항목이 끝나야 다음 항목을 시작합니다.[^parallel] 카드의 설정 탭에서 **동시성 제어**를 켜고 병렬 처리 수준을 정하면 여러 항목을 함께 처리합니다.

| 항목 | 내용 |
|---|---|
| 병렬 처리 수준 | 1~50. 기본 1 |
| 적용 범위 | 흐름의 최상위 반복에서만. 겹친 반복의 안쪽은 항상 순차 |
| 효과 | 항목 4개를 2로 11초, 4로 6초, 6으로 6초, 끄면 21초(문서의 비교 값) |
| 값을 크게 잡을 때 | 작업 분할 · 스레드 대기 · 호출 지연이 더해져 반드시 빨라지지는 않음 |
| 쓰는 경우 | 메일 개별 발송 · 레코드 갱신 · 사용자 일괄 생성 · 병렬 승인 |
| 쓰지 않는 경우 | 항목 순서가 결과에 영향을 줄 때. 변수를 쓰는 반복 |

비슷한 이름의 설정이 트리거에도 있습니다.[^limits]

| 설정 | 정하는 것 | 범위 | 기본 |
|---|---|---|---|
| 각각에 적용의 동시성 제어 | 한 실행 안에서 함께 도는 반복 수 | 1~50 | 1 |
| 트리거의 동시성 제어 | 흐름이 함께 실행되는 수 | 1~100. 켜면 기본 25 | 꺼짐. 켜면 트리거를 지우고 다시 넣어야 되돌림 |

---

## 반복 안의 변수

변수는 흐름 전체에 하나입니다. 반복이 바뀌어도 값이 유지됩니다.[^variables]

| 작업 | 순차 실행 | 동시 실행 |
|---|---|---|
| 변수 초기화 | 반복 안에 둘 수 없음 | 반복 안에 둘 수 없음 |
| 변수 증가 · 변수 감소 | 예측 가능 | 예측할 수 없을 수 있음 |
| 변수 설정 | 예측 가능 | 예측할 수 없을 수 있음 |
| 배열 변수에 추가 · 문자열 변수에 추가 | 항목 순서대로 | 순서와 결과를 예측할 수 없을 수 있음 |

변수를 쓰는 반복은 순차로 둡니다.[^variables][^la-loops] 변수 작업은 [C19](c19-variables.html)에서 다룹니다.

---

## 반복이 늘리는 작업 수

작업 수는 반복 횟수만큼 곱해집니다. 작업 2개를 10번 도는 반복은 21개입니다(반복 1 + 2 × 10).[^faq][^understand]

| 항목 | 내용 |
|---|---|
| 세는 것 | 성공 · 실패한 작업. 재시도와 페이지 매김 요청 |
| 세지 않는 것 | 건너뛴 작업 |
| 식이 여러 개인 작업 | 하나로 셈 |
| 하루 한도 | Microsoft 365 6,000 · Premium 40,000 · Process 250,000 |

---

## 중첩 반복을 피하는 이유

반복 안에 반복을 두면 횟수가 곱해집니다.[^anti]

| 영향 | 내용 |
|---|---|
| 실행 시간 | 10회 × 10회는 100회. 항목마다 작업이 많을수록 길어짐 |
| 한도 | 항목 수와 하루 작업 수 한도에 빠르게 닿음. 오류 예시는 100 × 100 = 10,000 |
| 동시 실행 | 안쪽 반복은 항상 순차 |
| 중첩 깊이 | 범위 · 조건 · 스위치와 합쳐 8수준까지 |

| 대신 쓰는 방법 | 내용 |
|---|---|
| 원본에서 거르기 | 필터 쿼리로 대상 항목만 가져옴. [C13](c13-filter.html) |
| 관련 행을 한 번에 가져오기 | Dataverse **행 나열**의 확장 쿼리로 부모와 자식을 한 번에 읽음 |
| 배치 요청 | 수천 건 갱신은 서비스의 배치 API |
| 동시 실행 | 배치가 없는 서비스는 최대 50까지 동시 처리 |

---

## 데이터 작업으로 대체

항목마다 작업을 실행할 필요가 없고 모양만 바꾸거나 거를 때는 반복 대신 데이터 작업을 씁니다. 데이터 작업은 항목 수와 상관없이 작업 하나로 셉니다.[^data-guide][^understand]

| 하려는 일 | 반복 대신 |
|---|---|
| 조건에 맞는 항목만 남기기 | 배열 필터링 |
| 항목의 키를 고르거나 이름 바꾸기 | 선택 |
| 항목을 구분자로 이어 문자열 만들기 | 조인 |
| 표로 만들기 | HTML 테이블 만들기 · CSV 테이블 만들기 |
| 건수 세기 | `length()` |
| 첫 항목 읽기 | `first()` |

데이터 작업의 입력과 출력은 [C12](c12-dataops.html)에서 다룹니다.

---

## 자기 자신을 다시 실행하는 흐름

항목이 바뀔 때 시작하는 흐름이 같은 항목을 고치면 자기 자신을 다시 실행합니다. 저장할 때 디자이너가 무한 루프 경고를 띄웁니다. 트리거 조건으로 실행을 제한하거나, 처리한 항목을 감지하면 **종료**로 끝냅니다.[^anti] 트리거 조건은 [C26](c26-trigger-conditions.html)에서 다룹니다.

---

## 흔한 실패

반복에서 나오는 오류와 고치는 곳입니다.[^troubleshoot][^errref]

| 증상 | 원인 | 고치는 곳 |
|---|---|---|
| 카드가 뜻하지 않은 반복 안에 들어감 | 배열 안의 동적 콘텐츠를 고름 | 식으로 넣거나 `first()` 로 항목 하나를 읽음 |
| 처리 항목 수가 예상과 다름 | 앞 작업이 항목을 더 많거나 적게 가져옴 | 입력 칸의 배열과 앞 작업의 필터 |
| 값이 다른 항목의 값으로 보임 | 다른 단계나 다른 항목의 필드를 읽음 | 실행 기록의 입력 |
| 변수 값이 실행마다 달라짐 | 동시 실행과 변수를 함께 씀 | 동시성 제어를 끔 |
| Do until 이 한도까지 돎 | 조건의 값이 반복 안에서 바뀌지 않음 | 조건과 안의 작업 |
| 저장되지 않음 | 반복 안의 변수 초기화 · 종료, 중첩 8수준 초과 | 위치와 깊이 |

---

## 샘플

흐름 `식 연습장_HGD` 를 씁니다. 없으면 [C7](c07-types.html)의 샘플로 만듭니다.

1. [Power Automate — {{ site.pa.environment }}]({{ site.pa.powerautomate_url }}){:target="_blank"}를 엽니다. 왼쪽 메뉴 **내 흐름**에서 `식 연습장_HGD` 를 열고 **편집**을 누릅니다.
2. 트리거와 **작성** 카드 사이의 화살표에 포인터를 올려 **+** › **작업 추가**를 고릅니다. 검색란에 `변수 초기화` 를 입력하고 **변수 초기화**를 고릅니다.
3. **유형**에서 **정수**를 고릅니다. **이름** 칸과 **값** 칸에 아래를 차례로 넣습니다.

    ```
    합계
    ```

    ```
    0
    ```

4. 그 아래 **+** › **작업 추가**에서 **변수 초기화**를 하나 더 놓습니다. **유형**에서 **배열**을 고릅니다. **이름** 칸과 **값** 칸에 아래를 차례로 넣습니다.

    ```
    순서
    ```

    ```
    []
    ```

5. 그 아래 **+** › **작업 추가**를 고릅니다. **기본 제공 도구**에서 **컨트롤**을 누르고 **각각에 적용**을 고릅니다. 화면에 **For each** 로 보이면 그것을 고릅니다.
6. **이전 단계에서 출력 선택** 칸에서 ***fx*** 를 누르고 아래 식을 붙여넣은 뒤 **추가**를 누릅니다.

    ```
    createArray(10, 20, 30)
    ```

7. 반복 안의 **+** › **작업 추가**에서 `변수 증가` 를 검색해 **변수 증가**를 고릅니다. **이름**에서 `합계` 를 고릅니다. **값** 칸에서 ***fx*** 로 아래 식을 넣습니다.

    ```
    item()
    ```

8. **변수 증가** 아래 **+** › **작업 추가**에서 `배열 변수` 를 검색해 **배열 변수에 추가**를 고릅니다. **이름**에서 `순서` 를 고릅니다. **값** 칸에서 ***fx*** 로 같은 식을 넣습니다.

    ```
    item()
    ```

9. 반복 아래의 **작성** 카드를 누릅니다. **입력** 칸을 비우고 ***fx*** 로 아래 식을 넣습니다.

    ```
    concat('합계 ', string(variables('합계')), ' / 순서 ', string(variables('순서')))
    ```

10. **저장**을 누르고 **테스트** › **수동** › **테스트**를 누릅니다. **흐름 실행**을 누르고 **완료**를 누릅니다.
11. 실행 화면에서 **작성** 카드를 누릅니다.

    **완료 기준**: 출력에 `합계 60` 이 있고 `10` · `20` · `30` 이 이 순서로 보인다.

12. **편집**을 누릅니다. 반복 카드를 누르고 구성 창의 **설정** 탭을 엽니다. **동시성 제어**를 켜고 **병렬 처리 수준**을 `3` 으로 정합니다.
13. 10~11번을 되풀이합니다. 두세 번 실행해 결과를 견줍니다.

    **완료 기준**: `순서` 에 `10` · `20` · `30` 세 값이 모두 있다. 순서는 실행마다 달라질 수 있다.

14. **편집**을 누릅니다. 반복 카드의 **동시성 제어**를 끕니다.
15. 반복 아래, **작성** 위의 화살표에서 **+** › **작업 추가**를 고릅니다. **컨트롤**에서 **Do until**을 고릅니다.
16. 조건의 왼쪽 **값 선택** 칸과 오른쪽 **값 선택** 칸에 ***fx*** 로 아래 식을 차례로 넣습니다. 가운데 연산자를 **크거나 같음**으로 바꿉니다.

    ```
    variables('합계')
    ```

    ```
    100
    ```

17. Do until 안의 **+** › **작업 추가**에서 **변수 증가**를 고릅니다. **이름**에서 `합계` 를 고릅니다. **값** 칸에 ***fx*** 로 아래 식을 넣습니다.

    ```
    10
    ```
18. 10~11번을 되풀이합니다.

    **완료 기준**: 출력에 `합계 100` 이 있다. Do until 은 60에서 네 번 돌았다.

19. **편집**을 누릅니다. **작성** 카드의 **입력** 칸을 비우고 아래를 넣습니다.

    ```
    연습
    ```

20. Do until · 반복 · **변수 초기화** 두 개를 차례로 누르고 구성 창의 **⋮**(추가 명령) › **삭제**를 고릅니다. **저장**을 누릅니다.

    **완료 기준**: 트리거 아래에 **작성** 카드 하나만 남아 있다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: 각각에 적용[^apply] · 제한[^limits] · 동시 실행 지침[^parallel] · 변수[^variables] · 안티 패턴[^anti] · 데이터 작업 지침[^data-guide] · 플랫폼 한도 지침[^understand] · 라이선스 FAQ[^faq] · Logic Apps 반복[^la-loops] · 함수 참조[^functions] · 작업 스키마[^schema] · 오류 코드[^errref] · 문제 해결[^troubleshoot]

[^apply]: **Use the Apply to each action to process a list of items periodically** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/apply-to-each> (2026-11-02 확인). 각각에 적용이 배열을 입력으로 받는다는 것, 이전 단계에서 출력 선택 칸.
[^limits]: **Limits of automated, scheduled, and instant flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/limits-and-config> (2026-11-02 확인). 각각에 적용 항목 수 Low 5,000 · 나머지 100,000, 동시성 기본 1 · 범위 1~50, Do until 기본 60 · 최대 5,000, 트리거 동시성 1~100 · 기본 25, 중첩 8수준. 수치는 영어판에서 옮겼다.
[^parallel]: **Optimize flows with parallel execution and concurrency** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/implement-parallel-execution> (2026-11-02 확인). 기본 순차, 병렬 처리 수준 비교 표, 겹친 반복의 안쪽은 순차, 쓰는 경우.
[^variables]: **Store and manage values in variables** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/create-variable-store-values> (2026-11-02 확인). 변수가 반복 사이에 유지되는 것, 반복 안 변수는 순차로 두라는 경고, 변수 초기화는 전역 수준에서만 되는 것.
[^anti]: **Avoid anti-patterns** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/avoid-anti-patterns> (2026-11-02 확인). 중첩 반복의 비용, 확장 쿼리, 배치, 동시 처리 50, 무한 루프 경고와 대처.
[^data-guide]: **Work with data operations** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/use-data-operations> (2026-11-02 확인). 배열 필터링 · 선택 · 조인이 반복과 복잡한 식을 줄인다는 것.
[^understand]: **Understand platform limits and avoid throttling** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/understand-limits> (2026-11-02 확인). 작업 수를 세는 규칙, 반복 대신 선택과 배열 필터링을 쓰는 것.
[^faq]: **Power Automate licensing FAQ** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-platform/admin/power-automate-licensing/faqs> (2026-11-02 확인). 반복 1 + 2 × 10 = 21 계산, 플랜별 하루 작업 수.
[^la-loops]: **Run loops to repeat actions in workflows for Azure Logic Apps** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/logic-apps-control-flow-loops> (2026-11-02 확인). Until 이 작업 실행 뒤 조건을 확인하는 것, 횟수 · 시간 한도, 상태 판정, 실행 기록, 병렬에서 변수 작업의 결과. Azure Logic Apps 문서다. 이 문서의 For each 기본값(병렬)은 Power Automate 와 다르다.
[^functions]: **Reference guide to functions in expressions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/workflow-definition-language-functions-reference> (2026-11-02 확인). `item()` · `items()` · `iterationIndexes()`.
[^schema]: **Schema reference guide for trigger and action types in Azure Logic Apps** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/logic-apps-workflow-actions-triggers> (2026-11-02 확인). 종료 작업을 반복 안에 둘 수 없는 것. Azure Logic Apps 문서다.
[^errref]: **Cloud flow error code reference** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/error-reference> (2026-11-02 확인). `WorkflowRunActionRepetitionQuotaExceeded` 의 원인과 처리.
[^troubleshoot]: **Troubleshoot cloud flow errors** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/troubleshoot-flow-errors> (2026-11-02 확인). 반복이 잘못된 항목을 처리할 때 확인하는 곳, 반복의 다른 항목을 읽는 실수.
