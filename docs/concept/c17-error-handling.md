---
title: "C17. 오류 처리"
parent: "개념 3. 승인과 실행 기록"
nav_order: 17
concept:
  id: C17
  grade: B
  used_in: "랩에서 쓰지 않음"
  tokens: []
  sample: true
---

# C17. 오류 처리

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. 흐름 전체 상태 · 범위 상태 · result() · 종료의 세부는 Azure Logic Apps 문서가 출처다. 샘플에서 Power Automate 동작을 확인한다.
     ⚠️ 샘플의 식은 트리거 입력 키 `text` 를 전제한다. C7 의 텍스트 입력이 첫 입력이 아니면 키가 달라진다.
     ⚠️ 실측할 것(라벨): 설정 탭의 이후 실행(ko-kr 문서마다 이후에 실행 · 이후 실행 · 실행 후) · 네 상태(ko-kr Logic Apps 문서 성공함 · 실패함 · 건너뛰기 · 제한 시간 초과) · 재시도 정책 유형 이름 · 작업 시간 초과 · 종료 카드의 상태 · 코드 · 메시지 칸 · 추가 명령(⋮) › 삭제
     ⚠️ 실측할 것(동작): Try 안 작성 카드의 자동 이름(작성 1 로 가정, Lab 3 35번과 같은 규칙) · 실패 실행의 전체 상태 표시 · Catch 만 남기고 지울 때 삭제 순서
     ⚠️ 문서 대조: error-handling 문서의 실행 URL 식은 environments · flows · runs 뒤 슬래시가 없고 run 객체 전체를 넣는다. 본문 식은 슬래시를 넣고 run.name 을 쓰도록 고쳤다. 실행해 열리는지 확인한다.
        fix-flow-failures 문서는 실패할 때마다 복구 팁 메일이 간다고 적고, understand-flow-failure-notifications 는 알려진 해결법이 있을 때만 28일 간격으로 간다고 적는다. 본문은 뒤 문서를 따랐다. -->

> **다루는 것**: 작업이 실패했을 때 흐름이 할 일을 정하는 방법 — 이후 실행, 범위와 Try · Catch, `result()` · `workflow()`, 재시도 정책, 종료 작업, 실패 알림
>
> **쓰는 곳**: 랩에서 쓰지 않음

---

## 작업의 네 상태

작업은 끝날 때 상태를 하나 남깁니다.[^la-error]

| 상태 | 영문 라벨 | 코드 보기의 값 | 뜻 |
|---|---|---|---|
| 성공함 | Is successful | `Succeeded` | 오류 없이 끝남 |
| 실패함 | Has failed | `Failed` | 오류로 끝남 |
| 건너뜀 | Is skipped | `Skipped` | 실행되지 않음. 앞 작업이 실패했거나 조건의 다른 가지에 있을 때 |
| 시간 초과 | Has timed out | `TimedOut` | 정해 둔 시간 안에 끝나지 않음 |

처리되지 않은 오류가 나면 그 작업은 실패함, 뒤따르는 작업은 건너뜀으로 표시됩니다.[^la-error]

---

## 이후 실행

다음 작업은 앞 작업의 상태가 허용 목록에 있을 때만 실행됩니다. 이 목록을 정하는 설정이 **이후 실행**(Run after)입니다. 카드를 누르고 구성 창의 설정 탭에서 고칩니다.[^designer]

| 항목 | 내용 |
|---|---|
| 기본값 | 성공함 하나 |
| 고르는 수 | 여러 상태를 함께 고를 수 있음. 최소 하나 |
| 기본값 지우기 | 다른 상태를 먼저 고른 뒤 지움 |
| 앞 작업이 여럿일 때 | 작업마다 상태를 따로 고름 |
| 흐름의 첫 작업 | 설정 없음. 트리거가 성공하면 실행됨 |

코드 보기에는 `runAfter` 속성으로 나옵니다.[^la-error]

```
"runAfter": {
  "Try": ["Failed", "TimedOut"]
}
```

---

## 실행 전체의 상태

실행이 끝나면 가지마다 완료 상태를 따져 실행 전체의 상태를 정합니다.[^la-error]

| 가지의 마지막 작업 | 가지의 완료 상태 |
|---|---|
| 성공함 | 성공 |
| 실패함 | 실패 |
| 건너뜀 | 건너뛴 작업의 앞 작업 상태를 따름 |

가지 중 하나라도 실패로 끝나면 실행 전체가 실패입니다. 범위가 실패해도 뒤따르는 처리가 성공으로 끝나면 실행 전체는 성공으로 기록됩니다.[^la-scope]

---

## 범위

**범위**(Scope)는 작업을 묶는 컨트롤 작업입니다. 작업 추가 창의 기본 제공 도구 › 컨트롤에 있습니다.[^scopes]

| 항목 | 내용 |
|---|---|
| 상태 | 안의 작업이 모두 끝나면 범위 자체의 상태가 정해짐 |
| 성공 | 안의 작업이 모두 성공 |
| 실패 | 안의 작업이 하나라도 실패 |
| 실패 표시 | 범위 전체에 실패 하나. 실패한 작업은 범위를 펼쳐 찾음 |
| 범위 카드의 오류 | `ActionFailed. An action failed. No dependent actions succeeded.` |
| 중첩 | 범위 · 조건 · 스위치 · 각각에 적용을 합쳐 8수준까지. 넘으면 저장 · 실행되지 않음 |
| 안에 두지 않는 것 | 트리거 · 응답 작업 · 변수 초기화([C19](c19-variables.html)) |
| 복사 | 안의 작업까지 통째로 복사됨 |
| 작업 수 | 범위 카드도 작업 하나로 셈[^understand] |

범위의 상태를 값으로 읽는 식은 아래와 같습니다. 이후 실행 대신 조건 카드로 가를 때 씁니다.[^la-scope]

```
actions('Try')?['status']
```

관련 있는 작업만 묶습니다. 모든 작업을 범위에 넣을 필요는 없습니다. 범위에 메모를 달면 흐름을 읽기 쉬워집니다.[^scope-guide]

---

## Try · Catch · Finally

범위 세 개와 이후 실행을 조합하면 오류 처리 구조가 됩니다.[^guide][^playbook]

```
Try       범위  주 작업
Catch     범위  이후 실행 = Try 의 실패함 · 건너뜀 · 시간 초과
Finally   범위  이후 실행 = Catch 의 성공함 · 실패함 · 건너뜀 · 시간 초과
```

| Try | Catch | Finally | 실행 전체 |
|---|---|---|---|
| 성공 | 건너뜀 | 실행됨 | 성공 |
| 실패 | 실행됨 | 실행됨 | 성공. Catch 에 종료 작업을 두면 실패 |

Catch 아래 작업을 기본값(성공함)으로 두면 Catch 가 건너뜀일 때 함께 건너뜁니다. Try 결과와 관계없이 실행할 작업은 네 상태를 모두 고릅니다.

---

## result()

`result('범위 이름')` 은 범위 안 최상위 작업의 결과를 배열로 돌려줍니다.[^functions] 범위 이름의 공백은 `_` 로 적습니다.

| 속성 | 담는 것 |
|---|---|
| `name` | 작업 이름 |
| `status` | `Succeeded` · `Failed` 등 |
| `code` | 결과 코드. 예: `NotFound` |
| `inputs` · `outputs` | 작업의 입력과 출력 |
| `startTime` · `endTime` | 시작과 끝 시각 |
| `trackingId` · `clientTrackingId` | 추적 ID |

스위치와 조건 안에 있는 작업의 결과는 들어오지 않습니다.[^functions] 실패한 작업만 고르려면 **배열 필터링**을 씁니다.[^la-error]

From 칸의 식:

```
result('Try')
```

Filter Query 왼쪽 칸의 식. 연산자는 다음과 같음, 오른쪽 값은 `Failed` 입니다.

```
item()?['status']
```

거른 결과에서 첫 작업의 이름을 읽는 식:

```
first(body('배열_필터링'))?['name']
```

---

## workflow()

`workflow()` 는 현재 실행의 정보를 객체로 돌려줍니다.[^guide][^functions]

| 식 | 값 |
|---|---|
| `workflow()?['name']` | 흐름 ID |
| `workflow()?['tags']?['flowDisplayName']` | 흐름 표시 이름 |
| `workflow()?['tags']?['environmentName']` | 환경 ID |
| `workflow()?['tags']?['logicAppName']` | 흐름 ID |
| `workflow()?['tags']?['createdBy']` | 만든 사람 |
| `workflow()?['tags']?['triggerType']` | 트리거 유형 |
| `workflow()?['tags']?['state']` | 흐름 상태 |
| `workflow()?['run']?['name']` | 실행 ID |

실행 주소를 만드는 식입니다. 실패 메일이나 오류 기록에 넣으면 해당 실행을 바로 엽니다.

```
concat('https://make.powerautomate.com/environments/', workflow()?['tags']?['environmentName'], '/flows/', workflow()?['tags']?['logicAppName'], '/runs/', workflow()?['run']?['name'])
```

사용자 지정 기록과 알림 작업을 늘리면 작업 수가 늘어 흐름 성능이 떨어집니다.[^guide]

---

## 재시도 정책

**재시도 정책**은 네트워크나 서비스의 일시적 오류에 같은 요청을 다시 보내는 설정입니다.[^guide] 카드의 설정 탭 네트워킹 묶음에 있습니다.[^designer] 요청이 시간 초과나 실패로 끝나 408 · 429 · 5xx 응답을 받으면 동작합니다.[^la-error]

| 유형 | 동작 |
|---|---|
| 기본값 | 아래 표의 지수 간격 |
| 없음 | 다시 보내지 않음 |
| 지수 간격 | 점점 넓어지는 범위에서 고른 간격을 기다렸다가 다시 보냄. 문서가 권하는 유형 |
| 고정 간격 | 정한 간격을 기다렸다가 다시 보냄 |

기본값은 성능 프로필에 따라 다릅니다.[^designer][^limits]

| 성능 프로필 | 다시 보내는 횟수 | 간격 |
|---|---|---|
| Low | 2회 | 5분 단위로 늘어 마지막은 약 10분 |
| Medium · High, 프리미엄 커넥터 없음 | 8회 | 7초 단위로 늘어 마지막은 약 1시간 |
| Medium · High, 프리미엄 커넥터 있음 | 12회 | 7초 단위로 늘어 마지막은 약 1시간 |

성능 프로필은 흐름 소유자의 플랜을 따릅니다. Microsoft 365 플랜과 모든 평가판은 Low, Power Automate Premium 은 Medium, Process 라이선스는 High 입니다.[^limits]

직접 정할 때의 값입니다. 시간은 ISO 8601 표기로 적습니다.[^limits][^la-error]

| 항목 | 범위 | 표기 예 |
|---|---|---|
| 횟수 | 1~90 | `2` |
| 간격 | 5초~1일 | `PT5S` · `PT30S` · `P1D` |
| 최소 · 최대 간격 | 지수 간격에서 선택. 기본 5초 · 1일 | `PT5S` · `P1D` |

재시도도 실행한 작업 수에 들어갑니다.[^limits]

---

## 시간 제한

작업과 실행에는 시간 제한이 있습니다.[^designer][^limits][^errref]

| 항목 | 내용 |
|---|---|
| 작업 시간 초과 | 카드의 설정 탭 일반 묶음. 재시도와 비동기 응답 사이의 최대 기간. 요청 하나의 시간 제한은 바꾸지 않음 |
| 표기 | ISO 8601. 예: `PT5M` 은 5분 |
| 실행 한 번의 한도 | 30일. 승인처럼 대기 중인 단계를 포함. 넘으면 대기 중인 단계가 시간 초과 |
| 시간 초과 처리 | 다음 작업의 이후 실행에서 시간 초과를 고름 |

---

## 종료 작업

**종료**(Terminate)는 실행을 멈추고 지정한 상태를 돌려주는 컨트롤 작업입니다. 진행 중인 작업은 취소되고 남은 작업은 건너뜁니다.[^schema]

| 상태 | 코드 보기의 값 | 코드 · 메시지 칸 |
|---|---|---|
| 성공 | `Succeeded` | 쓰지 않음 |
| 실패 | `Failed` | 씀. 실패 원인을 적음 |
| 취소됨 | `Cancelled` | 쓰지 않음 |

| 조건 | 내용 |
|---|---|
| 끝난 작업 | 영향 없음 |
| 놓을 수 없는 곳 | 각각에 적용 · Do until 안. 순차 실행이어도 같음 |

---

## 서비스가 보내는 실패 메일

Power Automate 가 소유자에게 보내는 메일은 두 종류입니다.[^notify]

| 메일 | 보내는 때 | 내용 |
|---|---|---|
| 실행별 실패 알림 | 알려진 해결법이 있는 실패 직후 | 해결 절차 |
| 주간 실패 요약 | 매주 | 모든 환경의 일주일치 실패 |

| 실패 유형 | 실행별 알림 |
|---|---|
| 끊기거나 만료된 연결 | 보냄 |
| 스로틀링된 작업 | 보냄 |
| AI Builder 오류 · 데스크톱 흐름 오류 | 보냄 |
| 알려진 커넥터 오류. 예: Outlook 작업의 잘못된 받는 사람 | 보냄 |
| 해결법을 특정하지 못한 일반 실패 | 보내지 않음 |
| 앞 작업 실패로 함께 실패 처리된 작업 | 보내지 않음. 원인은 처음 실패한 작업 |

| 항목 | 내용 |
|---|---|
| 받는 사람 | 소유자와 공동 소유자. 실행 전용 사용자와 관리자는 받지 않음 |
| 다시 보내는 간격 | 같은 흐름은 28일에 한 번 |
| 켜짐 여부 | 모든 흐름에 기본으로 켜져 있지는 않음. 흐름 설정에서 확인 |

오류 코드는 [C22](c22-error-codes.html)에서 다룹니다.

---

## 실패 알림 만들기

실행별 알림이 가지 않는 실패까지 받으려면 Catch 안에 알림 작업을 둡니다.[^guide]

```
Try     범위  주 작업
Catch   범위  이후 실행 = Try 의 실패함 · 시간 초과
├─ 배열 필터링       From = result('Try') · status 다음과 같음 Failed
├─ 메일 보내기(V2)   본문 = 실패한 작업 이름 + 실행 주소
└─ 종료              상태 = 실패 · 코드 · 메시지
```

- 오류 내용을 SharePoint 목록 같은 저장소에 함께 기록할 수 있습니다.
- 마지막의 **종료**가 없으면 실행 기록에는 성공으로 남습니다.

---

## 흔한 실패

저장과 실행에서 나오는 오류와 고치는 곳입니다.[^errref][^troubleshoot]

| 증상 | 원인 | 고치는 곳 |
|---|---|---|
| Try 가 실패해도 Catch 가 실행되지 않음 | Catch 의 이후 실행이 성공함 그대로 | Catch 의 설정 탭 |
| Try 가 실패했는데 실행 기록은 성공 | Catch 가 성공으로 끝남 | Catch 끝에 종료 작업 |
| Try 가 성공하면 아래 작업이 건너뜀 | Catch 아래 작업의 이후 실행이 성공함 그대로 | 네 상태 선택 |
| `result()` 에 작업이 빠짐 | 조건이나 스위치 안의 작업 | 최상위로 옮기거나 그 범위를 따로 읽음 |
| 저장할 때 `InvalidTemplate` | 식의 카드 이름 오타. 값이 상수인 `int('abc')` 도 저장 때 걸림 | 식 |
| 실행할 때 `ExpressionEvaluationFailed` | 동적 값이 식의 형식과 맞지 않음 | `coalesce()` · `if(empty())` |
| Catch 안의 식이 실패 | 실행되지 않은 작업의 출력을 읽음 | `?` 와 `coalesce()` |

데스크톱 흐름의 오류 처리는 [P18](p18-errors.html)에서 다룹니다.

---

## 샘플

흐름 `식 연습장_HGD` 를 씁니다. 없으면 [C7](c07-types.html)의 샘플로 만듭니다.

1. [Power Automate — {{ site.pa.environment }}]({{ site.pa.powerautomate_url }}){:target="_blank"}를 엽니다. 왼쪽 메뉴 **내 흐름**에서 `식 연습장_HGD` 를 열고 **편집**을 누릅니다.
2. **작성** 카드 아래 **+** › **작업 추가**를 고릅니다. **기본 제공 도구**에서 **컨트롤**을 누르고 **범위**를 고릅니다.
3. 구성 창 맨 위의 카드 이름 **범위**를 눌러 아래로 바꿉니다.

    ```
    Try
    ```

4. **Try** 안의 **+** › **작업 추가**를 고릅니다. **기본 제공 도구**에서 **데이터 작업**을 누르고 **작성**을 고릅니다.
5. **입력** 칸에서 ***fx*** 를 누르고 아래 식을 붙여넣은 뒤 **추가**를 누릅니다. 텍스트 입력의 값을 정수로 바꾸는 식입니다. 숫자 모양이 아닌 값이 들어오면 실행할 때 실패합니다.

    ```
    int(triggerBody()?['text'])
    ```

6. **Try** 아래 **+** › **작업 추가**를 고릅니다. **컨트롤**에서 **범위**를 고릅니다.
7. 카드 이름을 아래로 바꿉니다.

    ```
    Catch
    ```

8. **Catch** 안의 **+** › **작업 추가**를 고릅니다. **데이터 작업**에서 **작성**을 고릅니다.
9. **입력** 칸에서 ***fx*** 를 누르고 아래 식을 붙여넣은 뒤 **추가**를 누릅니다.

    ```
    result('Try')
    ```

10. **Catch** 카드를 누르고 구성 창의 **설정** 탭을 엽니다. **이후 실행**에서 **Try** 를 펼칩니다.
11. **실패함**을 고르고 **성공함**을 해제합니다.

    **완료 기준**: **Try** 아래에 **실패함** 하나만 체크되어 있다.

12. **저장**을 누르고 **테스트** › **수동** › **테스트**를 누릅니다. **흐름 실행** 창의 텍스트 입력 칸에 아래를 넣고 **흐름 실행**을 누른 뒤 **완료**를 누릅니다.

    ```
    abc
    ```

    **완료 기준**: **Try** 와 그 안의 작성 카드가 실패로, **Catch** 가 성공으로 표시된다.

13. **Catch** 안의 작성 카드를 누릅니다.

    **완료 기준**: 출력이 배열이고, 항목의 `status` 가 `Failed` 다.

14. **편집**을 눌러 디자이너로 돌아옵니다. 12번과 같이 실행하되 입력 칸에 아래를 넣습니다.

    ```
    42
    ```

    **완료 기준**: **Try** 가 성공으로, **Catch** 가 건너뜀으로 표시된다.

15. **편집**을 누릅니다. **Catch** 안의 작성 카드 아래 **+** › **작업 추가**를 고릅니다. **컨트롤**에서 **종료**를 고릅니다.
16. **상태**에서 **실패**를 고릅니다. **코드** 칸과 **메시지** 칸에 아래를 차례로 넣습니다.

    ```
    TryFailed
    ```

    ```
    Try 범위가 실패했습니다.
    ```

17. **저장**을 누르고 12번과 같이 `abc` 로 실행합니다.

    **완료 기준**: **종료** 카드까지 실행되고 실행 전체가 실패로 표시된다.

18. **편집**을 누릅니다. 맨 위 **작성** 카드의 **입력** 칸을 비우고 ***fx*** 로 아래 식을 넣습니다. **저장**을 누르고 `42` 로 실행한 뒤 실행 화면에서 **작성** 카드를 누릅니다.

    ```
    workflow()
    ```

    **완료 기준**: 출력의 `tags` 아래 `flowDisplayName` 이 `식 연습장_HGD` 다.

19. 같은 카드의 식을 아래로 바꿔 18번을 되풀이합니다.

    ```
    concat('https://make.powerautomate.com/environments/', workflow()?['tags']?['environmentName'], '/flows/', workflow()?['tags']?['logicAppName'], '/runs/', workflow()?['run']?['name'])
    ```

    **완료 기준**: 출력이 `https://make.powerautomate.com/environments/` 로 시작하는 주소다.

20. **편집**을 누릅니다. **Catch** 카드를 누르고 구성 창의 **⋮**(추가 명령) › **삭제**를 고릅니다. **Try** 도 같은 방법으로 지웁니다. **저장**을 누릅니다.

    **완료 기준**: 트리거 아래에 **작성** 카드 하나만 남아 있다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: 오류 처리 지침[^guide] · 범위[^scopes] · 범위 활용 지침[^scope-guide] · Logic Apps 오류 처리[^la-error] · Logic Apps 범위[^la-scope] · Try · Catch · Finally 구성 예[^playbook] · 함수 참조[^functions] · 디자이너[^designer] · 제한[^limits] · 플랫폼 한도 지침[^understand] · 작업 스키마[^schema] · 실패 알림[^notify] · 오류 코드[^errref] · 문제 해결[^troubleshoot]

[^guide]: **Employ robust error handling** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/error-handling> (2026-11-02 확인). Run after, `workflow()` 스키마, Try · Catch 범위, 재시도 정책, 종료, 기록과 알림. 실행 URL 식은 문서의 식에 슬래시와 `run.name` 을 더해 고쳤다.
[^scopes]: **Use scopes to organize actions in cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/scopes> (2026-11-02 확인). 범위 추가 절차, 중첩 8수준, 실패 표시, 트리거 · 응답 작업을 밖에 두는 것.
[^scope-guide]: **Organize your flows with scopes** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/create-scopes> (2026-11-02 확인). 묶는 기준과 범위 안 메모.
[^la-error]: **Handle workflow errors and exceptions in Azure Logic Apps** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/error-exception-handling> (2026-11-02 확인). 네 상태, 실행 전체 상태 판정, `runAfter`, 재시도 정책 유형과 대상 응답, `result()` 항목 모양과 필터. Azure Logic Apps 문서다.
[^la-scope]: **Group related actions into scopes** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/logic-apps-control-flow-run-steps-group-scopes> (2026-11-02 확인). 범위의 상태, `actions()` 로 상태 읽기, 범위가 실패해도 실행이 성공으로 기록되는 예. Azure Logic Apps 문서다.
[^playbook]: **Create the cloud flow to update an address with Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/rpa-sap-playbook/creating-cloud-flow-to-update-address> (2026-11-02 확인). Catch · Finally 범위에 고르는 상태.
[^functions]: **Reference guide to functions in expressions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/workflow-definition-language-functions-reference> (2026-11-02 확인). `result()` · `workflow()` · `actions()`.
[^designer]: **Explore the cloud flows designer** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/flows-designer> (2026-11-02 확인). 설정 탭의 작업 시간 초과 · 재시도 정책 · 이후 실행, 기본 재시도 횟수.
[^limits]: **Limits of automated, scheduled, and instant flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/limits-and-config> (2026-11-02 확인). 성능 프로필과 플랜, 기본 재시도 간격, 재시도 설정의 한도, 실행 30일, 재시도를 작업 수에 세는 것. 수치는 영어판에서 옮겼다.
[^understand]: **Understand platform limits and avoid throttling** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/understand-limits> (2026-11-02 확인). 범위 카드도 작업 수에 드는 것.
[^schema]: **Schema reference guide for trigger and action types in Azure Logic Apps** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/logic-apps-workflow-actions-triggers> (2026-11-02 확인). Terminate 의 상태 값, 코드와 메시지가 실패 상태에만 쓰이는 것, 반복 안에 둘 수 없는 것. Azure Logic Apps 문서다.
[^notify]: **Understand flow failure notifications** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/understand-flow-failure-notifications> (2026-11-02 확인). 실행별 알림과 주간 요약, 받는 사람, 28일 간격, 유형별 발송 여부.
[^errref]: **Cloud flow error code reference** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/error-reference> (2026-11-02 확인). `InvalidTemplate` 과 `ExpressionEvaluationFailed` 의 차이, 시간 초과 처리, `PT5M` 표기.
[^troubleshoot]: **Troubleshoot cloud flow errors** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/troubleshoot-flow-errors> (2026-11-02 확인). `ActionFailed` 메시지, 실행되지 않은 작업의 출력을 읽는 실패.
