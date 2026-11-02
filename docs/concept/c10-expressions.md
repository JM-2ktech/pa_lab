---
title: "C10. 식 모음"
parent: "개념 2. 자료형과 식"
nav_order: 10
concept:
  id: C10
  grade: A
  used_in: "Lab 1 ⑥ 예약 트리거와 식 · Lab 2 ③ 대상월 · ⑤ 거르기와 세기 · Lab 3 ⑥ 반려 회신"
  tokens: ["formatDateTime(", "concat(", "length(", "string(", "first("]
  sample: true
---

# C10. 식 모음

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. 식은 expression-cookbook 영어판 30개 패턴을 옮겼다. variables() · triggerBody() 자리를 상수로 바꾸었고, 상수로 바꾼 결과값은 문서 규칙으로 계산했다.
     ⚠️ 문서는 AI 도움으로 썼다고 적혀 있어 functions reference 와 대조했다. 어긋난 곳:
        8번 — 요리책은 addDays() 가 소수를 받는다고 적는다. 함수 참조의 days 는 Integer 다. 본문은 정수만 쓴다
        9번 — 요리책은 로캘이 없으면 흐름의 국가별 설정을 따른다고 적는다. 함수 참조는 기본값 en-us 다. 본문은 함수 참조를 따랐다
        11번 — 요리책은 날짜 차이 함수가 없다고 적는다. 함수 참조에 dateDifference() 가 있다. 두 식을 함께 적었다
        12번 — 요리책은 `mm/DD/yyyy` 의 결과를 `30/18/2026` 으로 적는다. .NET 사용자 지정 형식에서 D 는 지정자가 아니어서 글자 그대로 나온다(`30/DD/2026`). 본문은 `mm/dd/yyyy` 로 바꿨다
        14번 — 빈 배열의 first() 가 null 이라는 것은 요리책에만 있다
        20번 — 요리책의 createObject() 는 함수 참조에 없다. 대신 addProperty() 를 적었다. C8 표에도 createObject() 가 있다
        23번 — 요리책은 `div(mul(값, 100), 100)` 을 잘라 내기 식으로 적는다. 함수 참조의 규칙으로는 부동 소수점이 그대로 남는다. 샘플로 확인한다
        24 · 25번 — 요리책의 `int(float(값))` · `float(75)` 는 함수 참조의 인수 형식(String)과 다르다. 25번 샘플은 `float('75')` 로 적었다
     ⚠️ 실측할 것: `int(float('3.14'))` 의 결과, `createObject()` 가 저장되는가, 13번 고급 모드가 새 디자이너에 있는가, 5번 출력의 줄바꿈 표시, `first(json('[]'))` 의 출력, `empty(null)` · `coalesce(null, …)` 처럼 null 상수를 넣은 식이 저장되는가 -->

> **다루는 것**: 텍스트 · 날짜 · 배열 · JSON · 숫자 · 조건의 식 패턴 30개
>
> **쓰는 곳**: Lab 1 `formatDateTime(convertFromUtc(utcNow(), 'Korea Standard Time'), 'yyyy-MM-dd')` · Lab 2 `concat('점검 ', string(length(body('점검행'))), …)` · Lab 3 `first(…)?['comments']`

---

## 이 페이지의 식

아래 식은 작성 카드의 **입력** 칸에 ***fx*** 로 넣어 그대로 실행하도록 상수로 적었습니다. 실제 흐름에서는 상수 부분을 동적 콘텐츠나 `body('카드')` · `triggerBody()?['키']` · `variables('이름')` 로 바꿉니다.

식은 Microsoft Learn의 식 요리책에서 옮겼습니다.[^cookbook] 함수의 동작은 함수 참조[^functions]와 대조했고, 두 문서가 다른 곳은 그 패턴의 조건에 적었습니다.

| 분류 | 패턴 | 함수 |
|---|---|---|
| 텍스트 | 1~6 | `toLower` · `toUpper` · `substring` · `replace` · `split` · `concat` · `decodeUriComponent` · `contains` |
| 날짜와 시간 | 7~12 | `formatDateTime` · `utcNow` · `convertTimeZone` · `addDays` · `parseDateTime` · `dayOfWeek` · `ticks` · `dateDifference` |
| 배열 | 13~17 | 배열 필터링 작업 · `first` · `last` · `length` · `join` · `contains` |
| JSON | 18~22 | `json` · `?[]` · `addProperty` · `string` · `coalesce` · `empty` |
| 숫자 | 23~25 | `formatNumber` · `int` · `float` · `string` · `div` · `mul` |
| 조건 | 26~30 | `if` · `coalesce` · `empty` · `greater` · `ticks` · `and` · `or` |

---

## 텍스트

### 패턴 1. 대문자 · 소문자로 바꾸기

비교하거나 저장하기 전에 입력값의 대소문자를 맞춥니다.

```
toLower('John.Smith@Contoso.COM')
```

결과: `john.smith@contoso.com`

```
toUpper('Hello World')
```

결과: `HELLO WORLD`

조건: 비교할 때는 양쪽에 같은 함수를 씁니다. 한쪽만 바꾸면 대소문자가 섞인 상대와 같지 않다고 나옵니다.

### 패턴 2. 문자열 일부 읽기

앞에서 몇 글자, 뒤에서 몇 글자, 가운데 구간을 읽습니다. 순서대로 앞 · 뒤 · 가운데입니다.

```
substring('Invoice-2026-0042', 0, 7)
```

결과: `Invoice`

```
substring('Invoice-2026-0042', sub(length('Invoice-2026-0042'), 4), 4)
```

결과: `0042`

```
substring('Invoice-2026-0042', 8, 4)
```

결과: `2026`

조건: 둘째 인수는 0부터 세는 시작 번호이고 셋째 인수는 길이입니다. `substring('ABCDE', 1, 3)` 은 `BCD` 입니다. 셋째 인수를 빼면 끝까지 읽습니다. 시작 번호와 길이의 합이 문자열 길이를 넘으면 오류입니다. 끝 번호로 적고 범위를 넘어도 오류가 없는 함수는 `slice()` 입니다. `slice('Hello World', 2, 5)` 는 `llo` 입니다.

### 패턴 3. 글자 바꾸기

글자를 지우거나 구분 문자를 바꿉니다.

```
replace('2026/03/18', '/', '-')
```

결과: `2026-03-18`

조건: 대소문자를 구분합니다. `replace('Hello', 'hello', 'Hi')` 는 `Hello` 그대로입니다. 찾는 글자가 없으면 원래 문자열을 돌려줍니다.

### 패턴 4. 문자열을 배열로 나누기

쉼표나 세미콜론으로 이어진 값을 항목으로 나눕니다.

```
split('alice@contoso.com,bob@contoso.com,carol@contoso.com', ',')
```

결과: `["alice@contoso.com","bob@contoso.com","carol@contoso.com"]`

조건: 구분 문자 뒤의 공백이 남습니다. `split('a, b, c', ',')` 는 `["a"," b"," c"]` 입니다. 공백은 선택 작업에서 항목마다 `trim()` 으로 지웁니다. 구분 문자가 없으면 항목 하나의 배열이 됩니다.

### 패턴 5. 줄바꿈을 넣어 잇기

메일이나 Teams 메시지 본문을 여러 줄로 만듭니다.

```
concat('Line 1', decodeUriComponent('%0A'), 'Line 2')
```

결과: `Line 1` 과 `Line 2` 가 두 줄로 나옵니다.

조건: Windows 줄바꿈은 `%0D%0A` 입니다. 식 안에 `\n` 을 적으면 줄이 바뀌지 않고 글자 `\n` 이 나옵니다. 출력이 HTML이면 `<br>` 을 씁니다.

### 패턴 6. 문자열에 글자가 있는지 보기

제목이나 본문에 특정 낱말이 있는지 따져 흐름을 나눕니다.

```
contains('Project Alpha Review', 'Alpha')
```

결과: `true`

조건: 대소문자를 구분합니다. 구분 없이 찾으려면 양쪽을 `toLower()` 로 감쌉니다.

```
contains(toLower('Project Alpha Review'), toLower('ALPHA'))
```

결과: `true`

---

## 날짜와 시간

시각의 모양과 시간대는 [C11](c11-datetime.html)에서 다룹니다.

### 패턴 7. 현재 시각을 형식에 맞춰 내기

파일 이름이나 메일에 실행 시각을 적습니다.

```
formatDateTime(utcNow(), 'yyyy-MM-dd HH:mm')
```

결과: 실행 시각의 UTC. 예 `2026-03-18 14:30`

```
convertTimeZone(utcNow(), 'UTC', 'Korea Standard Time', 'yyyy-MM-dd HH:mm')
```

결과: 실행 시각의 한국 시각

조건: `utcNow()` 는 언제나 UTC입니다.

### 패턴 8. 날짜 더하기와 빼기

기한이나 알림 날짜를 계산합니다. 음수를 주면 뺍니다.

```
addDays('2026-03-18T00:00:00Z', 7)
```

결과: `2026-03-25T00:00:00.0000000Z`

```
addDays('2026-03-18T00:00:00Z', -30)
```

결과: `2026-02-16T00:00:00.0000000Z`

조건: 하루보다 작은 단위는 `addHours()` · `addMinutes()` 를 씁니다. 함수 참조는 더할 일 수를 정수로 적습니다.

### 패턴 9. 문자열을 날짜로 읽기

`03/18/2026` 같은 글자를 날짜 함수에 넣을 수 있는 시각으로 바꿉니다.

```
parseDateTime('03/18/2026', 'en-US')
```

결과: `2026-03-18T00:00:00.0000000`

셋째 인수로 모양을 지정할 수 있습니다.

```
parseDateTime('20260318', 'en-US', 'yyyyMMdd')
```

결과: `2026-03-18T00:00:00.0000000`

조건: 로캘을 적습니다. `03/04/2026` 은 로캘에 따라 3월 4일도 되고 4월 3일도 됩니다. 로캘을 빼면 함수 참조상 `en-us` 입니다. 식 요리책은 흐름의 국가별 설정을 따른다고 적습니다.

### 패턴 10. 요일 얻기

평일과 주말에 다른 처리를 합니다.

```
dayOfWeek('2026-03-18T00:00:00Z')
```

결과: `3`

```
or(equals(dayOfWeek('2026-03-21T00:00:00Z'), 0), equals(dayOfWeek('2026-03-21T00:00:00Z'), 6))
```

결과: `true`

조건: 일요일이 `0`, 월요일이 `1`, 토요일이 `6` 입니다. 주말은 `0` 과 `6` 을 둘 다 비교합니다.

### 패턴 11. 두 날짜의 차이

요청일과 완료일 사이의 일수를 셉니다.

```
div(sub(ticks('2026-03-18'), ticks('2026-03-01')), 864000000000)
```

결과: `17`

```
dateDifference('2026-03-01', '2026-03-18')
```

결과: `17.00:00:00`

조건: `ticks()` 식의 나누는 수는 일 `864000000000`, 시간 `36000000000`, 분 `600000000` 입니다. `dateDifference()` 의 결과는 문자열입니다. 식 요리책은 날짜 차이 함수가 없다고 적지만 함수 참조에 있습니다. 먼저 온 날짜를 둘째 인수로 주면 음수가 됩니다.

### 패턴 12. 날짜를 읽기 좋은 모양으로

메일이나 보고서에 쓸 모양으로 바꿉니다.

```
formatDateTime('2026-03-18T14:30:00Z', 'MMMM dd, yyyy')
```

결과: `March 18, 2026`

```
formatDateTime('2026-03-18T14:30:00Z', 'MM/dd/yyyy')
```

결과: `03/18/2026`

조건: `MM` 은 월이고 `mm` 은 분입니다. 일은 소문자 `dd` 입니다. `formatDateTime('2026-03-18T14:30:00Z', 'mm/dd/yyyy')` 는 `30/18/2026` 입니다.

---

## 배열

### 패턴 13. 조건으로 배열 거르기

배열에서 조건에 맞는 항목만 남깁니다. 이 패턴은 식 하나로 쓰지 않습니다. 배열 필터링 작업에 아래 값을 넣습니다.

**From** 칸의 식:

```
json('[{"Name":"A","Status":"Active"},{"Name":"B","Status":"Closed"}]')
```

**Filter Query** 왼쪽 칸의 식(연산자 다음과 같음):

```
item()?['Status']
```

**Filter Query** 오른쪽 칸의 값:

```
Active
```

결과: `[{"Name":"A","Status":"Active"}]`

조건: 거르는 글자는 대소문자를 구분합니다.[^dataops] 식 요리책은 고급 모드에 `@equals(item()?['Status'], 'Active')` 를 넣는 방법도 적습니다. 배열 필터링은 [C13](c13-filter.html)에서 다룹니다.

### 패턴 14. 첫 항목과 마지막 항목

목록에서 첫 항목이나 최근 항목을 읽습니다.

```
first(createArray('A', 'B', 'C'))
```

결과: `A`

```
last(createArray('A', 'B', 'C'))
```

결과: `C`

조건: 문자열에도 씁니다. `first('hello')` 는 `h` 이고 `last('abcd')` 는 `d` 입니다. 식 요리책은 빈 배열에 쓰면 오류 없이 `null` 을 돌려준다고 적습니다. 함수 참조에는 이 경우가 적혀 있지 않습니다.

### 패턴 15. 항목 세기

조회 결과가 몇 건인지 셉니다.

```
length(createArray('A', 'B', 'C'))
```

결과: `3`

조건: 문자열의 글자 수도 셉니다. `length('hello')` 는 `5` 입니다. 배열처럼 보이는 문자열을 넣으면 글자 수가 나옵니다.

### 패턴 16. 배열을 문자열 하나로 잇기

이름이나 메일 주소 목록을 구분 문자로 잇습니다.

```
join(createArray('Alice', 'Bob', 'Carol'), '; ')
```

결과: `Alice; Bob; Carol`

조건: 문자열 배열에 씁니다. 객체 배열은 선택 작업으로 필드를 먼저 고른 뒤 잇습니다.

### 패턴 17. 배열에 값이 있는지 보기

다음 단계로 가기 전에 항목이 목록에 있는지 확인합니다.

```
contains(createArray('North', 'South', 'East', 'West'), 'East')
```

결과: `true`

조건: 대소문자를 구분합니다. 객체 배열에서는 객체 전체를 비교합니다. 속성 하나로 찾으려면 배열 필터링으로 거른 뒤 `length()` 를 봅니다.

---

## JSON

JSON의 구조와 `?[]` 표기는 [C8](c08-json.html)에서 다룹니다.

### 패턴 18. JSON 문자열을 객체로 바꾸기

JSON을 문자열로 돌려주는 작업의 출력을 구조로 바꿉니다.

```
json('{"name":"Alice","age":30}')?['name']
```

결과: `Alice`

조건: 대부분의 커넥터 작업은 이미 구문 분석한 JSON을 돌려줍니다. 그런 출력에 `json()` 을 다시 쓰면 오류입니다. 함수 참조상 `null` 문자열은 빈 객체가 됩니다.

### 패턴 19. 깊은 곳의 값 읽기

중첩된 응답에서 값 하나를 읽습니다.

```
json('{"data":{"items":[{"name":"Widget"}]}}')?['data']?['items']?[0]?['name']
```

결과: `Widget`

조건: `?` 를 빼면 중간 값이 `null` 일 때 오류입니다. `?` 가 있으면 `null` 을 돌려줍니다.

### 패턴 20. 값으로 JSON 만들기

요청 본문을 값들로 조립합니다.

```
json(concat('{"name":"', 'Alice', '","status":"', 'Active', '"}'))
```

결과: `{"name":"Alice","status":"Active"}`

조건: 값에 따옴표나 특수 문자가 있으면 잘못된 JSON이 됩니다. 함수 참조에 있는 `addProperty()` 는 글자를 잇지 않고 속성을 더합니다.

```
addProperty(addProperty(json('{}'), 'name', 'Alice'), 'status', 'Active')
```

결과: `{"name":"Alice","status":"Active"}`

식 요리책은 `createObject('name', 'Alice', 'status', 'Active')` 를 권합니다. 함수 참조의 함수 목록에 `createObject` 는 없습니다. 작성 카드의 **입력** 칸에 JSON을 적고 값 부분에 동적 콘텐츠를 넣는 방법도 식 요리책에 있습니다.

### 패턴 21. 객체를 문자열로 바꾸기

JSON을 텍스트 칸에 기록하거나 문자열 인수로 넘깁니다.

```
string(json('{"a":1}'))
```

결과: `{"a":1}`

조건: 줄바꿈과 들여쓰기 없는 JSON이 나옵니다. 보기 좋게 정리하는 함수는 없습니다. `null` 은 빈 문자열이 됩니다.

### 패턴 22. 비어 있는 값 대비하기

값이 비어 있어도 흐름이 멈추지 않게 합니다.

```
coalesce(null, 'default value')
```

결과: `default value`

```
if(empty(''), 'default', '')
```

결과: `default`

조건: `coalesce()` 는 `null` 만 건너뜁니다. 빈 문자열까지 다루려면 `empty()` 를 함께 씁니다. `empty()` 는 `null` 과 빈 문자열에 `true` 를 돌려줍니다.

---

## 숫자

### 패턴 23. 소수 자릿수 맞추기

백분율이나 금액을 정해진 자릿수로 표시합니다.

```
formatNumber(3.14159, 'N2')
```

결과: `3.14`(문자열)

```
float(formatNumber(3.14159, 'N2'))
```

결과: `3.14`(수)

```
formatNumber(1234567890, '#,##0.00', 'en-US')
```

결과: `1,234,567,890.00`

조건: `formatNumber()` 의 결과는 문자열입니다. 계속 계산하려면 `float()` 로 되돌립니다.

식 요리책은 아래 식을 잘라 내기로 적습니다. 함수 참조의 규칙으로는 부동 소수점이 끝까지 유지되어 소수 부분이 남습니다.

```
div(mul(3.14159, 100), 100)
```

결과: `3.14159` 근처의 값. 샘플에서 확인합니다.

### 패턴 24. 문자열과 숫자 사이의 변환

양식이나 메일에서 글자로 받은 수를 계산에 씁니다.

```
int('42')
```

결과: `42`

```
float('3.14')
```

결과: `3.14`

```
string(42)
```

결과: `42`(문자열)

조건: `int('3.14')` 는 소수 부분을 버리지 않고 오류를 냅니다. 상수로 적으면 저장할 때 `InvalidTemplate` 이 나옵니다. 식 요리책은 소수일 수 있는 값에 `int(float(값))` 을 쓰라고 적습니다. 함수 참조의 `int()` 는 인수를 문자열로 적습니다. 변환 함수의 표는 [C7](c07-types.html)에 있습니다.

### 패턴 25. 백분율 계산

완료율이나 사용률을 계산합니다.

```
mul(div(float('75'), float('200')), 100)
```

결과: `37.5`

조건: 정수끼리 나누면 소수 부분이 사라집니다. `div(75, 200)` 은 `0` 입니다. 먼저 부동 소수점으로 바꾸면 `div(float('75'), float('200'))` 이 `0.375` 입니다. 나누는 수가 0인 상수 식은 저장할 때 오류입니다.

---

## 조건

조건 카드와 조건 식은 [C6](c06-condition.html)에서 다룹니다.

### 패턴 26. 식 안의 조건 분기

조건 카드를 더하지 않고 값을 고릅니다.

```
if(equals('Approved', 'Approved'), 'Proceed', 'Wait')
```

결과: `Proceed`

```
if(greater(15, 10), 'Over', 'Under')
```

결과: `Over`

조건: `>` · `<` 연산자는 없습니다. `equals()` · `greater()` · `less()` · `greaterOrEquals()` · `lessOrEquals()` 함수로 비교합니다. 조건을 뒤집는 함수는 `not()` 입니다.

### 패턴 27. 첫 번째로 값이 있는 것 고르기

여러 필드를 차례로 보고 값이 있는 첫 필드를 씁니다.

```
coalesce(null, 'Alice', 'alice@contoso.com', 'Unknown')
```

결과: `Alice`

조건: 빈 문자열은 `null` 이 아니므로 그 값이 선택됩니다. 인수가 모두 `null` 이면 `null` 입니다. 빈 문자열도 건너뛰려면 `if()` 와 함께 씁니다.

```
coalesce(if(empty(''), null, ''), if(empty('Alice'), null, 'Alice'), 'default')
```

결과: `Alice`

### 패턴 28. 값이 비어 있는지 보기

필수 칸에 값이 있는지 처리 전에 확인합니다.

```
empty('')
```

결과: `true`

```
empty(null)
```

결과: `true`

```
empty('hello')
```

결과: `false`

조건: 문자열 · 배열 · 객체에 씁니다. 숫자에 쓰면 오류입니다. `empty(0)` 은 실패합니다. 숫자는 `equals(값, null)` 로 봅니다.

### 패턴 29. 날짜 비교

기한이 지났는지, 어느 쪽이 먼저인지 봅니다.

```
greater(ticks('2026-03-18'), ticks('2026-03-15'))
```

결과: `true`

조건: `yyyy-MM-dd` 모양끼리는 문자열 비교도 맞습니다. `greater('2026-03-18', '2026-03-15')` 는 `true` 입니다. 다른 모양은 맞지 않습니다. `greater('03/18/2026', '12/01/2025')` 는 `false` 입니다.

### 패턴 30. 조건을 묶는 AND · OR

조건 여러 개를 식 하나로 묶습니다.

```
and(equals('Approved', 'Approved'), greater(1500, 1000))
```

결과: `true`

```
or(and(equals(1, 1), equals(2, 2)), and(equals(1, 2), equals(2, 2)))
```

결과: `true`

조건: `&&` · `||` 표기는 없습니다. 함수로 씁니다. 중첩이 깊어지면 줄이 여럿인 조건 카드로 옮깁니다.

---

## 흔한 실패

| 나오는 때 | 오류 | 원인 | 고치는 법 |
|---|---|---|---|
| 저장 | `InvalidTemplate` | 괄호나 작은따옴표의 짝이 맞지 않음 | 짝을 맞춤 |
| 저장 | `InvalidTemplate` | 인수 개수가 틀림. `createArray()` | 인수를 넣음 |
| 저장 | `InvalidTemplate` | 상수의 형식 오류. `int('abc')` · `div(100, 0)` | 상수를 고침 |
| 저장 | `InvalidTemplate` | 문서에서 복사한 식에 보이지 않는 유니코드 문자 | 식을 지우고 직접 입력 |
| 실행 | `ExpressionEvaluationFailed` | 동적 값이 식과 맞지 않음. 숫자가 아닌 글자에 `int()`, 0으로 나눔 | `isInt()` · `coalesce()` · `if(empty(값), …)` |

원인과 고치는 법은 오류 코드 참조를 따랐습니다.[^errors] 식 안의 문자열에 큰따옴표를 쓸 수 없습니다. `length('Hello')` 로 적습니다.[^wdl]

---

## 샘플

흐름 `식 연습장_HGD` 를 씁니다. 없으면 [C7](c07-types.html)의 샘플로 만듭니다.

1. `식 연습장_HGD` 의 **편집**을 눌러 디자이너를 엽니다.
2. **작성** 카드를 누릅니다. **입력** 칸을 비우고 ***fx*** 단추를 누릅니다.

    식 편집기에 아래를 붙여넣고 **추가**를 누릅니다.

    ```
    toLower('John.Smith@Contoso.COM')
    ```

3. **저장**을 누르고 **테스트** › **수동** › **테스트**를 누릅니다. **흐름 실행**을 누르고 **완료**를 누릅니다.
4. 실행 화면에서 **작성** 카드를 누릅니다.

    **완료 기준**: 출력이 `john.smith@contoso.com` 이다.

5. 실행 화면 오른쪽 위 **편집**을 눌러 디자이너로 돌아옵니다. 1~6번 패턴의 나머지 식을 하나씩 넣어 2~4번을 되풀이합니다.

    **완료 기준**: 출력이 패턴마다 적은 결과와 같다.

6. 7~12번 패턴의 식으로 되풀이합니다.

    **완료 기준**: 출력이 패턴마다 적은 결과와 같다. 7번의 출력은 실행 시각에 따라 다르다.

7. 14~17번 패턴의 식으로 되풀이합니다.

    **완료 기준**: 출력이 패턴마다 적은 결과와 같다.

8. 18~22번 패턴의 식으로 되풀이합니다.

    **완료 기준**: 출력이 패턴마다 적은 결과와 같다.

9. 23~25번 패턴의 식으로 되풀이합니다.

    **완료 기준**: 출력이 패턴마다 적은 결과와 같다.

10. 26~30번 패턴의 식으로 되풀이합니다.

    **완료 기준**: 출력이 패턴마다 적은 결과와 같다.

11. **작성** 카드 아래 **+**를 누르고 **작업 추가**를 고릅니다. **기본 제공 도구**에서 **데이터 작업**을 누르고 **배열 필터링**을 고릅니다.
12. **From** 칸과 **Filter Query** 를 13번 패턴대로 채웁니다.
13. **저장**을 누르고 3번과 같이 실행합니다. 실행 화면에서 **배열 필터링** 카드를 누릅니다.

    **완료 기준**: 출력이 `Name` 이 `A` 인 항목 하나의 배열이다.

14. **편집**을 누릅니다. **배열 필터링** 카드를 마우스 오른쪽 단추로 누르고 **삭제**를 고릅니다.
15. **작성** 카드의 식을 아래로 바꾸고 **저장**을 누릅니다.

    ```
    int('3.14')
    ```

    **완료 기준**: 저장되지 않고 오류가 표시된다.

16. 식을 아래로 되돌리고 **저장**을 누릅니다.

    ```
    string(42)
    ```

    **완료 기준**: 저장되고, 캔버스에 트리거와 **작성** 카드 하나가 있다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: 식 요리책[^cookbook] · 함수 참조[^functions] · 데이터 작업[^dataops] · 오류 코드 참조[^errors] · 워크플로 정의 언어[^wdl]

[^cookbook]: **Expression cookbook for cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/expression-cookbook> (2026-11-02 확인). 패턴 30개의 식 · 결과 · 조건. 문서 끝에 AI 도움으로 썼다고 적혀 있다. 한국어판은 식 일부가 빠지고 문장이 깨진 곳이 있어 영어판에서 옮겼다.
[^functions]: **Reference guide to functions in expressions for workflows in Azure Logic Apps and Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/workflow-definition-language-functions-reference> (2026-11-02 확인). 각 함수의 인수와 결과, `slice()` · `dateDifference()` · `addProperty()` · `formatNumber()` 의 예, 함수 목록에 `createObject` 가 없다는 것.
[^dataops]: **Use data operations** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/data-operations> (2026-11-02 확인). 배열 필터링의 구성과 대소문자 구분.
[^errors]: **Cloud flow error code reference** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/error-reference> (2026-11-02 확인). `InvalidTemplate` 과 `ExpressionEvaluationFailed` 의 원인과 대처. 문서 끝에 AI 도움으로 썼다고 적혀 있다.
[^wdl]: **Schema reference guide for the Workflow Definition Language in Azure Logic Apps** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/logic-apps-workflow-definition-language> (2026-11-02 확인). 식 안 문자열의 작은따옴표.
