---
title: "C11. 날짜와 시간대"
parent: "개념 2. 자료형과 식"
nav_order: 11
concept:
  id: C11
  grade: A
  used_in: "Lab 1 ② 인스턴트 흐름 · ⑥ 예약 트리거와 식 · Lab 2 ② 예약 흐름 · ③ 대상월"
  tokens: ["utcNow()", "convertFromUtc(", "addToTime(", "formatDateTime(", "Korea Standard Time", "표준 시간대"]
  sample: true
---

# C11. 날짜와 시간대

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. 결과값은 함수 참조와 .NET 형식 문자열 문서의 규칙으로 계산했다.
     ⚠️ 문서 대조: convertTimeZone 문서와 함수 참조의 예에 `2018-01-01T80:00:00` 오타가 있어 쓰지 않았다. date-time-values 의 `hh` 예시 결과 `1:45:30 PM` 은 .NET 규칙(`01`)과 다르다. 표는 .NET 을 따랐다.
     ⚠️ Recurrence 동작은 Azure Logic Apps 문서가 출처다. Power Automate 의 run-scheduled-tasks 가 고급 옵션 문서로 이 문서를 잇는다.
     ⚠️ 실측할 것: `addToTime(..., -1, 'Month')` 의 음수. 문서는 더할 수라고만 적는다. Lab 2 16번 실측으로 동작한다
     ⚠️ 실측할 것: 시간대가 없는 시각을 넣은 addToTime() 결과에 Z 가 붙지 않는가(표의 3단계), `ko-KR` 로캘의 `dddd` 결과와 한글 글자가 든 형식 문자열, 시간대 변환 작업의 칸 라벨(한국어판 문서 표기), 되풀이 구성 창의 이 시간에는 · 이 분에 라벨(Lab 1 저작 메모 표기) -->

> **다루는 것**: 날짜 값의 모양, UTC와 한국 시각의 변환, 형식 문자열, 날짜 계산 함수, 예약 트리거의 시간대
>
> **쓰는 곳**: Lab 1 `formatDateTime(convertFromUtc(utcNow(), 'Korea Standard Time'), 'yyyy-MM-dd')` · 표준 시간대 · Lab 2 `formatDateTime(addToTime(convertFromUtc(utcNow(),'Korea Standard Time'),-1,'Month'),'yyyy-MM')`

---

## 날짜 값의 모양

날짜 값의 자료형은 문자열입니다.[^functions] 함수가 기본으로 내는 모양은 ISO 8601을 따르는 형식 `o` 입니다.

```
2026-10-05T23:30:00.0000000Z
```

| 부분 | 뜻 |
|---|---|
| `2026-10-05` | 날짜 |
| `T` | 날짜와 시각을 나누는 글자 |
| `23:30:00.0000000` | 시각. 초 아래 숫자 7개 |
| `Z` | UTC |

끝에 `Z` 가 있으면 UTC 시각입니다.[^convert] `convertFromUtc()` 의 결과에는 시간대 표시가 없습니다.[^functions]

---

## 기본 시간대는 UTC

Power Automate는 기본으로 UTC를 씁니다.[^datetime] `utcNow()` 는 언제나 UTC 시각을 돌려줍니다.[^cookbook] 한국은 UTC+09:00이므로 한국 시각 00:00~08:59의 UTC 날짜는 전날입니다.

| 한국 시각 | UTC | `formatDateTime(utcNow(), 'yyyy-MM-dd')` |
|---|---|---|
| 2026-10-06 08:30 | 2026-10-05 23:30 | `2026-10-05` |
| 2026-10-06 09:00 | 2026-10-06 00:00 | `2026-10-06` |

커넥터마다 날짜 형식과 시간대가 다르고, UTC만 쓰는 서비스도 있습니다.[^convert] 흐름을 한 번 실행해 그 작업의 출력을 보면 확인됩니다. 승인의 시각은 언제나 UTC로 표시됩니다.[^approvals] 실행 화면의 시작 시간은 `(현지 시간)` 을 붙여 표시합니다.

수동 트리거의 날짜 입력은 `YYYY-MM-DD` 로 입력합니다. 시각이 없는 날짜 문자열입니다.

---

## 시간대 변환

세 함수 모두 마지막 인수로 형식 문자열을 받습니다. 빼면 결과는 형식 `o` 입니다.[^functions]

| 함수 | 인수 | 예 | 결과 |
|---|---|---|---|
| `convertFromUtc` | 시각 · 대상 시간대 · 형식 | `convertFromUtc('2026-10-05T23:30:00Z', 'Korea Standard Time')` | `2026-10-06T08:30:00.0000000` |
| `convertToUtc` | 시각 · 원본 시간대 · 형식 | `convertToUtc('2026-10-06T08:30:00', 'Korea Standard Time')` | `2026-10-05T23:30:00.0000000Z` |
| `convertTimeZone` | 시각 · 원본 시간대 · 대상 시간대 · 형식 | `convertTimeZone('2026-10-05T23:30:00Z', 'UTC', 'Korea Standard Time', 'yyyy-MM-dd HH:mm')` | `2026-10-06 08:30` |

시간대 이름은 Windows 기본 시간대의 이름입니다.[^tz] 함수 참조는 이름의 문장 부호를 빼야 할 수 있다고 적습니다.[^functions]

| 이름 | UTC 차이 | 지역 |
|---|---|---|
| `Korea Standard Time` | +09:00 | 서울 |
| `Tokyo Standard Time` | +09:00 | 도쿄 |
| `China Standard Time` | +08:00 | 베이징 |
| `UTC` | 0 | 협정 세계시 |
| `Pacific Standard Time` | -08:00 | 미국 태평양 |
| `Eastern Standard Time` | -05:00 | 미국 동부 |

함수 대신 기본 제공 작업 **시간대 변환**을 쓸 수도 있습니다. 칸은 기본 시간 · 소스 시간대 · 대상 시간대 · 형식 문자열입니다.[^convert]

---

## 형식 문자열

`formatDateTime()` 은 시각 · 형식 · 로캘을 받습니다. 로캘을 빼면 `en-us` 입니다.[^functions]

사용자 지정 형식은 두 글자 이상의 문자열입니다.[^custom] 아래 표의 결과는 `2026-10-05T14:05:09Z` 기준입니다.

| 지정자 | 뜻 | 결과 |
|---|---|---|
| `yyyy` | 연도. 숫자 4개 | `2026` |
| `yy` | 연도. 숫자 2개 | `26` |
| `MM` | 월. 숫자 2개 | `10` |
| `MMM` | 월 약칭 | `Oct` |
| `MMMM` | 월 이름 | `October` |
| `dd` | 일. 숫자 2개 | `05` |
| `ddd` | 요일 약칭 | `Mon` |
| `dddd` | 요일 이름 | `Monday` |
| `HH` | 24시간제 시 | `14` |
| `hh` | 12시간제 시 | `02` |
| `mm` | 분 | `05` |
| `ss` | 초 | `09` |
| `tt` | 오전 · 오후 | `PM` |

대소문자로 뜻이 갈립니다. `MM` 은 월이고 `mm` 은 분입니다. `HH` 는 24시간제이고 `hh` 는 12시간제입니다. 지정자가 아닌 글자는 그대로 나옵니다. `'yyyy년 MM월'` 의 결과는 `2026년 10월` 입니다.

한 글자 형식은 표준 형식으로 읽습니다.[^custom] 결과는 같은 시각의 `en-us` 표기입니다.

| 형식 | 결과 |
|---|---|
| `d` | `10/5/2026` |
| `D` | `Monday, October 5, 2026` |
| `g` | `10/5/2026 2:05 PM` |
| `t` | `2:05 PM` |
| `T` | `2:05:09 PM` |
| `u` | `2026-10-05 14:05:09Z` |
| `y` | `October 2026` |

`'d'` 의 결과는 날짜 전체입니다. 일만 내려면 `'%d'` 나 `dayOfMonth()` 를 씁니다.[^custom]

---

## 날짜 계산 함수

아래 함수는 받은 시각의 글자를 기준으로 계산하고 시간대를 바꾸지 않습니다. 한국 날짜 기준이면 먼저 변환합니다.

| 함수 | 예 | 결과 |
|---|---|---|
| `addDays` | `addDays('2026-10-06T00:00:00Z', 7)` | `2026-10-13T00:00:00.0000000Z` |
| `addHours` · `addMinutes` · `addSeconds` | `addHours('2026-10-06T00:00:00Z', 9)` | `2026-10-06T09:00:00.0000000Z` |
| `addToTime` | `addToTime('2026-10-06T00:00:00Z', 1, 'Week')` | `2026-10-13T00:00:00.0000000Z` |
| `subtractFromTime` | `subtractFromTime('2026-10-06T00:00:00Z', 1, 'Month')` | `2026-09-06T00:00:00.0000000Z` |
| `getFutureTime` | `getFutureTime(7, 'Day')` | 현재 시각 + 7일 |
| `getPastTime` | `getPastTime(1, 'Month', 'yyyy-MM')` | 현재 시각 − 1개월의 연월 |
| `startOfDay` | `startOfDay('2026-10-06T10:30:00Z')` | `2026-10-06T00:00:00.0000000Z` |
| `startOfHour` | `startOfHour('2026-10-06T10:30:00Z')` | `2026-10-06T10:00:00.0000000Z` |
| `startOfMonth` | `startOfMonth('2026-10-06T10:30:00Z', 'yyyy-MM-dd')` | `2026-10-01` |
| `dayOfMonth` | `dayOfMonth('2026-10-06T00:00:00Z')` | `6` |
| `dayOfWeek` | `dayOfWeek('2026-10-06T00:00:00Z')` | `2`. 일요일이 `0` |
| `dayOfYear` | `dayOfYear('2026-10-06T00:00:00Z')` | `279` |
| `ticks` | `ticks('2026-10-06')` | 0001년 1월 1일부터의 100나노초 수 |
| `dateDifference` | `dateDifference('2026-10-01', '2026-10-06')` | `5.00:00:00` |
| `formatTimeSpan` | `formatTimeSpan('5.00:00:00', '%d')` | `5` |
| `parseDateTime` | `parseDateTime('20261006', 'ko-KR', 'yyyyMMdd')` | `2026-10-06T00:00:00.0000000` |

시간 단위 인수는 `Second` · `Minute` · `Hour` · `Day` · `Week` · `Month` · `Year` 입니다.[^functions]

식을 안쪽부터 읽으면 값이 이렇게 바뀝니다. 실행 시각은 한국 시각 2026-10-06 10:00입니다.

```
formatDateTime(addToTime(convertFromUtc(utcNow(),'Korea Standard Time'),-1,'Month'),'yyyy-MM')
```

| 순서 | 식 | 값 |
|---:|---|---|
| 1 | `utcNow()` | `2026-10-06T01:00:00.0000000Z` |
| 2 | `convertFromUtc(…, 'Korea Standard Time')` | `2026-10-06T10:00:00.0000000` |
| 3 | `addToTime(…, -1, 'Month')` | `2026-09-06T10:00:00.0000000` |
| 4 | `formatDateTime(…, 'yyyy-MM')` | `2026-09` |

---

## 날짜 비교

`yyyy-MM-dd` 모양끼리는 사전순과 날짜순이 같아 문자열 비교가 맞습니다. 다른 모양은 `ticks()` 로 바꿔 비교합니다.[^cookbook] 식은 [C10](c10-expressions.html)의 29번 패턴에 있습니다.

---

## 예약 트리거의 시간대

**Recurrence** 트리거는 시작 시간을 `YYYY-MM-DDTHH:MM:SSZ` 로 받고 표준 시간대로 해석합니다.[^schedule] 표준 시간대는 시작 시간이 있을 때만 적용됩니다. 끝에 `Z` 가 있으면 UTC 시각이므로 표준 시간대는 무시됩니다.[^recurrence]

| 시작 시간 | 표준 시간대 | 첫 실행의 한국 시각 |
|---|---|---|
| `2026-11-01T09:00:00` | (UTC+09:00) 서울 | 11월 1일 09:00 |
| `2026-11-01T00:00:00Z` | 없음 | 11월 1일 09:00 |
| `2026-11-01T00:00:00Z` | (UTC+09:00) 서울 | 11월 1일 09:00. 표준 시간대 무시 |
| `2026-11-01T09:00:00Z` | (UTC+09:00) 서울 | 11월 1일 18:00. 표준 시간대 무시 |

일정 칸을 쓰지 않을 때 시작 시간에 따라 첫 실행이 달라집니다.[^patterns]

| 시작 시간 | 첫 실행 | 이후 실행 |
|---|---|---|
| 없음 | 저장하자마자 | 직전 실행 시각 기준 |
| 과거 | 지난 회차를 버리고 다음 미래 회차 | 직전 실행 시각 기준 |
| 지금이나 미래 | 그 시각 | 직전 실행 시각 기준 |

| 조건 | 내용 |
|---|---|
| 미래 시작의 사전 설정 | 일 빈도는 24시간 전, 주 빈도는 7일 전, 월 빈도는 한 달 전에 설정. 그보다 늦으면 첫 회가 건너뛰어질 수 있음[^recurrence] |
| 실행 시각의 밀림 | **이 시간에는** · **이 분에** 같은 일정이 없으면 직전 실행 기준이라 밀릴 수 있음. 이 칸은 일 · 주 빈도에만 있음[^recurrence] |
| 월 빈도 | 매달 같은 날짜에 실행[^schedule] |
| 실행 시각의 오차 | 표시된 시각과 몇 초 차이가 날 수 있음[^triggers] · 시작 시각 값은 최대 1분 차이가 날 수 있음[^recurrence] |
| 일광 절약 시간 | 표준 시간대를 고르면 UTC 쪽이 옮겨져 현지 시각이 유지됨[^recurrence] |
| 트리거에 넣은 식 | 저장할 때 한 번만 계산됨. 트리거 입력의 `utcNow()` 는 저장 시각으로 고정됨[^triggers] |

---

## 흔한 실패

| 증상 | 원인 | 고치는 법 |
|---|---|---|
| 아침에 돈 흐름의 날짜가 하루 전 | UTC를 그대로 씀 | `convertFromUtc()` 를 먼저 씀 |
| 월 칸에 분이 나옴. `2026-30-05` | `mm` 을 씀 | `MM` |
| 오후 2시가 `02` 로 나옴 | `hh` 를 씀 | `HH` |
| 3월 4일이 4월 3일로 읽힘 | 로캘이 다름 | `parseDateTime()` 에 로캘을 적음 |
| 오류 `The date time string must match ISO8601 format.` | 시각 문자열의 모양이 다름[^convert] | `parseDateTime()` 으로 읽음 |
| 날짜 비교가 틀림 | `MM/dd/yyyy` 를 문자열로 비교 | `ticks()` |
| 저장 직후 예약 흐름이 돔 | 시작 시간이 없음 | 시작 시간을 적음 |
| 첫 예약 회차가 돌지 않음 | 시작 시간까지 사전 설정 기간이 모자람 | 더 일찍 설정하거나 다음 회차를 기다림 |

---

## 샘플

흐름 `식 연습장_HGD` 를 씁니다. 없으면 [C7](c07-types.html)의 샘플로 만듭니다.

1. `식 연습장_HGD` 의 **편집**을 눌러 디자이너를 엽니다.
2. **작성** 카드를 누릅니다. **입력** 칸을 비우고 ***fx*** 단추를 누릅니다.

    식 편집기에 아래를 붙여넣고 **추가**를 누릅니다.

    ```
    utcNow()
    ```

3. **저장**을 누르고 **테스트** › **수동** › **테스트**를 누릅니다. **흐름 실행**을 누르고 **완료**를 누릅니다.
4. 실행 화면에서 **작성** 카드를 누릅니다.

    **완료 기준**: 출력의 끝에 `Z` 가 있고, 시각이 지금 한국 시각보다 9시간 이르다.

5. 실행 화면 오른쪽 위 **편집**을 눌러 디자이너로 돌아옵니다. **작성** 카드의 식을 아래로 바꿔 2~4번을 되풀이합니다.

    ```
    convertFromUtc(utcNow(), 'Korea Standard Time')
    ```

    **완료 기준**: 출력의 시각이 지금 한국 시각이고, 끝에 `Z` 가 없다.

6. 고정한 시각을 변환하는 식으로 바꿔 되풀이합니다.

    ```
    convertFromUtc('2026-10-05T23:30:00Z', 'Korea Standard Time', 'yyyy-MM-dd HH:mm')
    ```

    **완료 기준**: 출력이 `2026-10-06 08:30` 이다.

7. 변환 없이 같은 시각의 날짜를 내는 식으로 바꿔 되풀이합니다.

    ```
    formatDateTime('2026-10-05T23:30:00Z', 'yyyy-MM-dd')
    ```

    **완료 기준**: 출력이 `2026-10-05` 다.

8. `MM` 을 `mm` 으로 바꾼 식으로 되풀이합니다.

    ```
    formatDateTime('2026-10-05T23:30:00Z', 'yyyy-mm-dd')
    ```

    **완료 기준**: 출력이 `2026-30-05` 다.

9. 한 달 전의 연월을 내는 식으로 바꿔 되풀이합니다.

    ```
    formatDateTime(addToTime('2026-10-06T10:00:00', -1, 'Month'), 'yyyy-MM')
    ```

    **완료 기준**: 출력이 `2026-09` 다.

10. 한국 시각을 UTC로 바꾸는 식으로 되풀이합니다.

    ```
    convertToUtc('2026-10-06T08:30:00', 'Korea Standard Time')
    ```

    **완료 기준**: 출력이 `2026-10-05T23:30:00.0000000Z` 다.

11. 달의 첫날을 내는 식으로 바꿔 되풀이합니다.

    ```
    startOfMonth('2026-10-06T10:30:00Z', 'yyyy-MM-dd')
    ```

    **완료 기준**: 출력이 `2026-10-01` 이다.

12. 로캘을 지정한 식으로 바꿔 되풀이합니다.

    ```
    formatDateTime('2026-10-05T14:05:09Z', 'yyyy년 MM월 dd일 dddd', 'ko-KR')
    ```

    **완료 기준**: 출력이 `2026년 10월 05일 월요일` 이다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: 함수 참조[^functions] · 시간대 변환[^convert] · 날짜 값[^datetime] · 식 요리책[^cookbook] · 시간대 이름[^tz] · 사용자 지정 형식 문자열[^custom] · 일정에 따라 실행[^schedule] · Recurrence 트리거[^recurrence] · 일정 패턴[^patterns] · 트리거 문제 해결[^triggers] · 표준 승인 커넥터[^approvals]

[^functions]: **Reference guide to functions in expressions for workflows in Azure Logic Apps and Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/workflow-definition-language-functions-reference> (2026-11-02 확인). 날짜 · 시간 함수의 인수와 결과, 형식 `o`, `convertFromUtc()` 결과에 오프셋이 없다는 것, 시간 단위, 시간대 이름의 문장 부호.
[^convert]: **Convert a time zone** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/convert-time-zone> (2026-11-02 확인). `Z` 의 뜻, 커넥터마다 형식과 시간대가 다르다는 것, 시간대 변환 작업의 칸, ISO 8601 오류 메시지, 실행으로 출력의 시간대를 확인하는 방법.
[^datetime]: **Customize or format date and time values in a flow** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/date-time-values> (2026-11-02 확인). Power Automate의 기본이 UTC라는 것, 표준 형식 `g` · `D` 와 사용자 지정 형식.
[^cookbook]: **Expression cookbook for cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/expression-cookbook> (2026-11-02 확인). 7 · 12 · 29번 패턴. `utcNow()` 가 UTC라는 것, `MM` 과 `mm`, `ticks()` 비교. 문서 끝에 AI 도움으로 썼다고 적혀 있다.
[^tz]: **Default Time Zones** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/windows-hardware/manufacture/desktop/default-time-zones> (2026-11-02 확인). `Korea Standard Time` (UTC+09:00) Seoul 등 시간대 이름.
[^custom]: **Custom date and time format strings** — Microsoft Learn(.NET). <https://learn.microsoft.com/ko-kr/dotnet/standard/base-types/custom-date-and-time-format-strings> (2026-11-02 확인). 사용자 지정 지정자의 뜻, 지정자가 아닌 글자는 그대로 나온다는 것, 한 글자 형식은 표준 형식으로 읽는다는 것과 `%` 표기.
[^schedule]: **Run a cloud flow on a schedule** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/run-scheduled-tasks> (2026-11-02 확인). 시작 시간의 모양, 표준 시간대, 월 빈도는 같은 날짜에 실행된다는 것.
[^recurrence]: **Schedule and run recurring workflows with the Recurrence trigger in Azure Logic Apps** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/connectors/connectors-native-recurrence> (2026-11-02 확인). 시작 시간의 `Z` 와 표준 시간대, 사전 설정 기간, 실행 시각의 밀림, 일광 절약 시간. Power Automate 문서가 고급 옵션 문서로 잇는 페이지다.
[^patterns]: **Schedules for recurring workflow triggers in Azure Logic Apps** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/concepts-schedule-automated-recurring-tasks-workflows> (2026-11-02 확인). 시작 시간에 따른 첫 실행과 이후 실행.
[^triggers]: **Troubleshoot Power Automate trigger problems and errors** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/troubleshoot/power-platform/power-automate/flow-run-issues/triggers-troubleshoot> (2026-11-02 확인). 트리거의 식은 저장할 때 계산된다는 것, Recurrence의 초 단위 오차.
[^approvals]: **Standard approvals** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/approvals/> (2026-11-02 확인). 승인 타임스탬프가 UTC로 표시된다는 것.
