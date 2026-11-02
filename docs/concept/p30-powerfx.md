---
title: "P30. Power Fx"
parent: "더 읽을거리 · PAD"
nav_order: 30
concept:
  id: P30
  grade: C
  used_in: "Lab 4 ① 5번 · Lab 5 ② 6번 · Lab 7 ② 8번에서 끈 채로 둠"
  tokens: ["Power Fx 사용"]
  sample: false
---

# P30. Power Fx

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     샘플을 두지 않았다. Power Fx 는 흐름을 만들 때 켜고, 공용 샘플 흐름 개념 연습_HGD 는 끈 흐름이다. 문서에 기존 흐름을 전환하는 방법이 없다.
     ⚠️ 실측할 것: 만든 흐름의 Power Fx 설정을 바꿀 수 있는지. 문서는 만들 때 켠다고만 적었다.
     ⚠️ 실측할 것: 보간 표시를 글자로 쓰는 표기. 영어판과 한국어판 모두 표기가 ${ 로 보이고 「첫 달러 기호가 이스케이프」라고 설명한다. 설명에 맞춰 $${ 로 적었다.
     ⚠️ 실측할 것: 부울 입력 =true 의 대소문자. 문서에 입력 예가 없다. 함수 참조의 true 표기를 따랐다.
     ⚠️ 실측할 것: =Index(Table, 1).Amount 처럼 데이터 테이블 행에서 열 이름으로 읽는 표기. Dynamic 문서의 점 표기를 데스크톱 흐름에 적용한 것이다.
     ⚠️ 문서 어긋남: =Index(DataRowVar, 1) 을 문서는 「행 1의 칸」이라 적는다. 대상이 데이터 행이라 본문은 「데이터 행의 1번 값」으로 적었다.
     ⚠️ 문서 어긋남: desktop-flows/power-fx 는 변환 함수를 Bool() 로 적고, 함수 참조와 Dynamic 문서는 Boolean() 으로 적는다. 본문은 Boolean() 을 따랐다.
     ⚠️ 문서 어긋남: 일부 한국어판 문서는 Run Power Fx expression 을 「Power Fx 식 실행」과 「Power Fx 표현식 실행」으로 섞어 쓴다. 화면 이름을 확인한다.
     Dynamic 문서는 UntypedObject 의 새 이름이 Dynamic 이라고 적는다. desktop-flows/power-fx 는 아직 Untyped Object 로 적는다. -->

> **다루는 것**: Power Fx 사용 흐름의 식 표기가 `%` 표기와 어떻게 다른지
>
> **쓰는 곳**: Lab 4 ① 5번 · Lab 5 ② 6번 · Lab 7 ② 8번에서 Power Fx 사용을 끈 채로 둠

---

## 켜는 방법

Power Fx 는 Power Platform 전반에서 쓰는 로우코드 식 언어입니다. 데스크톱 흐름에서는 콘솔에서 새 흐름을 만들 때 **Power Fx 사용** 토글을 켭니다.[^fx]

---

## 식 표기 비교

같은 일을 두 표기로 적으면 아래처럼 됩니다.[^fx][^percent][^types][^fxref][^untyped][^selector]

| 항목 | Power Fx 끔 | Power Fx 켬 |
|---|---|---|
| 식 표시 | `%식%` | 입력 맨 앞에 `=` |
| 변수 값 | `%NewVar%` | `=NewVar` |
| 글자 입력 | `교육` | `교육`. `=` 가 없으면 텍스트 |
| 숫자 입력 | `16` | `=16` |
| 부울 입력 | `%True%` | `=true` |
| 글자 사이에 값 넣기 | `%Course% 과정을 시작합니다.` | `${Course} 과정을 시작합니다.` |
| 식의 시작 글자를 글자로 쓰기 | `%%` | `$${` |
| 식 안의 글자 | `'text'` | `"text"` |
| 사칙 연산 | `%5 * 3%` | `=5 * 3` |
| 함수 호출 | `%StartsWith(이름,'교육',True)%` | `=StartsWith(이름, "교육")` |
| 논리 | `%N = 1 OR N = 2%` | `=Or(N = 1, N = 2)` |
| 빈 글자 검사 | `%IsEmpty(이름)%` | `=IsBlank(이름)` |
| 목록 첫 항목 | `%List[0]%` | `=Index(List, 1)` |
| 목록 만들기 | 새 목록 만들기 작업 | `=[1,2,3,4]` |
| 목록 일부 | `%List[2:4]%` | 문서에 표기 없음. `FirstN` · `LastN` 함수 있음 |
| 데이터 테이블의 1행 2열 | `%Table[0][1]%` | `=Index(Index(Table, 1), 2)` |
| 열 이름으로 읽기 | `%Table[0]['Amount']%` | `=Index(Table, 1).Amount` |
| 데이터 행의 1번 값 | `%CurrentItem[0]%` | `=Index(DataRowVar, 1)` |
| 사용자 지정 개체 | `%{ 'prop': 'value' }%` | `={'prop':"value"}` 레코드 |
| 개체의 속성 | `%Obj['prop']%` | `=Obj.prop` |
| 개체의 목록 | — | `=Table({'prop':"value"})` |
| 선택기 안의 변수 | `%WindowName%` | `${WindowName}` |

`IsEmpty` 는 두 표기에서 뜻이 다릅니다. `%` 표기에서는 글자가 하나도 없는 문자열을 검사하고, Power Fx 에서는 빈 표를 검사합니다.[^percent][^fxref]

---

## 동작 비교

표기 밖에서 달라지는 규칙입니다. 켬 쪽은 문서에 적힌 내용이고, 끔 쪽에 규정이 없는 항목은 그대로 적었습니다.[^fx]

| 항목 | Power Fx 끔 | Power Fx 켬 |
|---|---|---|
| 번호 시작 | 0 | 1 |
| 변수 이름 대소문자 | 문서에 규정 없음 | 구분. `NewVar` 와 `newVar` 는 다른 변수 |
| 변수 초기화 | 문서에 규정 없음 | 쓰기 전에 값을 넣어야 함. 없으면 오류 |
| If 작업의 칸 | 첫 번째 피연산자 · 연산자 · 두 번째 피연산자 | 조건식 하나 |
| Switch · Case · 기본 사례 작업 | 사용 | 지원 안 됨 |
| 형식을 모르는 값 | 일반 값 | 동적 변수 · 동적 값으로 구분 |
| 목록에 항목 추가 작업 | 사용 | 사용. 형식이 있는 목록은 형식 없는 개체로 바뀜 |

---

## 동적 변수와 동적 값

| 구분 | 뜻 | 표시 |
|---|---|---|
| 동적 변수 | 실행 중에 형식이나 값이 바뀔 수 있는 변수 | `Deferred type provided` 경고. 목록 · 표 · 레코드 속성에 넣을 수 없음 |
| 동적 값 | 실행할 때 형식이나 구조가 정해지는 값 | 형식 없는 개체로 처리 |

아래가 동적 값으로 처리됩니다.[^fx]

| 대상 | 예 |
|---|---|
| 데이터 테이블 | 모든 데이터 테이블 변수 |
| 구조를 모르는 사용자 지정 개체 | JSON을 사용자 지정 개체로 변환 작업의 결과 |
| 동적 작업 출력 | .NET 스크립트 실행 |
| 데스크톱 흐름 실행의 출력 | 호출한 흐름의 출력 변수 |
| 구조가 정해지지 않은 작업 출력 | Excel 워크시트에서 읽기 · 새 목록 만들기 |

동적 값을 작업 입력이나 식에 쓰면 자동으로 변환됩니다. 작성할 때는 검사하지 않고, 실행 중에 변환이 실패하면 런타임 오류가 납니다.[^fx] 비교 연산자를 쓰기 전에는 변환 함수로 형식을 맞춥니다.[^untyped]

| 변환 대상 | 함수 |
|---|---|
| 텍스트 | `Text()` |
| 숫자 | `Value()` |
| 부울 | `Boolean()` |
| 날짜 · 시간 | `DateValue()` · `TimeValue()` · `DateTimeValue()` |
| GUID | `GUID()` |
| 표 | `Table()` · `ForAll()` |

동적 값의 필드는 점으로 읽고, 없는 필드는 Blank 가 됩니다. 필드 이름이 숫자로 시작하거나 하이픈을 포함하면 작은따옴표로 감쌉니다. `=[1, 2, 3]` 으로 만든 목록의 항목은 `{Value: 1}` 모양의 개체입니다.[^fx][^untyped]

---

## Power Fx 식 실행

변수 묶음의 작업입니다. `Collect` · `Clear` · `ClearCollect` · `Patch` 와 함께 쓰면 목록에 항목 추가와 데이터 테이블에 행 삽입의 동작을 식으로 처리합니다. 파일 목록처럼 형식이 있는 목록에는 `Collect` 를 쓰면 형식이 유지됩니다.[^fx]

`Set` 함수는 변수 값을 바꾸는 데 쓰지 못합니다. 사용자 지정 개체의 속성과 목록의 특정 위치 값은 바꿉니다.[^fx]

```
=Set(Index(Index(DataTable, 1), 1), 42)
```

```
=Set(customObject.property, 17)
```

---

## 함수

전체 목록은 수식 참조에 있습니다. 함수 선택기는 입력칸의 **fx** 단추로 엽니다.[^fxref][^fx]

| 분류 | 함수 |
|---|---|
| 텍스트 | `Char` · `Concat` · `Concatenate` · `EncodeHTML` · `EncodeUrl` · `EndsWith` · `Find` · `Left` · `Len` · `Lower` · `Mid` · `PlainText` · `Proper` · `Replace` · `Right` · `Split` · `StartsWith` · `Substitute` · `Text` · `Trim` · `TrimEnds` · `UniChar` · `Upper` |
| 숫자 | `Abs` · `Average` · `Dec2Hex` · `Decimal` · `Exp` · `Float` · `Hex2Dec` · `Int` · `Ln` · `Log` · `Max` · `Min` · `Mod` · `Power` · `Rand` · `RandBetween` · `Round` · `RoundDown` · `RoundUp` · `Sqrt` · `StdevP` · `Sum` · `Trunc` · `Value` · `VarP` |
| 삼각 | `Acos` · `Acot` · `Asin` · `Atan` · `Atan2` · `Cos` · `Cot` · `Degrees` · `Pi` · `Radians` · `Sin` · `Tan` |
| 날짜 · 시간 | `Date` · `DateAdd` · `DateDiff` · `DateTime` · `DateTimeValue` · `DateValue` · `Day` · `EDate` · `EOMonth` · `Hour` · `IsToday` · `Minute` · `Month` · `Now` · `Second` · `Time` · `TimeValue` · `TimeZoneOffset` · `Today` · `Weekday` · `WeekNum` · `Year` |
| 논리 · 검사 | `And` · `Blank` · `Boolean` · `Coalesce` · `Error` · `If` · `IfError` · `IsBlank` · `IsBlankOrError` · `IsEmpty` · `IsError` · `IsNumeric` · `Not` · `Or` · `Switch` |
| 표 · 레코드 | `AddColumns` · `Clear` · `ClearCollect` · `Collect` · `Count` · `CountA` · `CountIf` · `CountRows` · `Distinct` · `DropColumns` · `Filter` · `First` · `FirstN` · `ForAll` · `Index` · `Last` · `LastN` · `LookUp` · `Patch` · `Remove` · `RenameColumns` · `Search` · `Sequence` · `Set` · `ShowColumns` · `Shuffle` · `Sort` · `SortByColumns` · `Summarize` · `Table` · `With` |
| 기타 | `GUID` · `Language` |

`If` · `Switch` 함수와 If · Switch 작업은 다릅니다. Switch 작업은 지원되지 않고 `Switch` 함수는 목록에 있습니다.

---

## 알려진 제한

문서가 적은 제한입니다.[^fx]

| 항목 | 내용 |
|---|---|
| 일부 함수 | IntelliSense 에 보여도 지원하지 않는 함수가 있음. 작성할 때 `OptionSetValueType` 오류가 남 |
| 하위 흐름 출력 | 목록 · 사용자 지정 개체 · 데이터 테이블 출력은 주의 대상 |
| 형식 검사 | `IsEmpty()` · `Sum()` · `Filter()` · `Concatenate()` · `in` 에 동적 변수를 넣으면 유효성 오류가 날 수 있음. 변환 함수로 형식을 맞춤 |
| 오류 메시지 | `Invalid argument type (UntypedObject). Expecting a Table value instead.` |

---

## 버전별 변화

| 버전 | 시기 | 변화 |
|---|---|---|
| 2.39 | 2023-12 | `=` 없는 입력의 규칙 도입. 공백 없는 숫자는 숫자, `True` · `False` 는 부울, 나머지는 텍스트 |
| 2.41 | 2024-02 | `=` 없는 입력은 모두 텍스트. 숫자와 부울은 `=` 로 시작. `${ }` 보간 지원 |
| 2.42 | 2024-03 | IntelliSense · 함수 선택기 |
| 2.43 | 2024-04 | 변수 이름 대소문자 구분. Power Fx 식 실행 작업. `Collect` · `Clear` · `ClearCollect` · `Patch` 지원. 선택기 안의 변수와 식 |
| 2.48 | 2024-09 | 변수 묶음의 목록 · 데이터 테이블 작업 다시 지원. 형식 없는 개체 지원. `Set` 일부 지원 |

2.42 이하에서 만든 흐름은 변수 이름의 대소문자를 구분하지 않았습니다. 2.48 의 변경은 이전 버전으로 만든 Power Fx 흐름의 실행에 영향을 줄 수 있어 문서는 다시 시험하기를 권합니다.[^fx]

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다.

- **문헌**: 데스크톱 흐름의 Power Fx[^fx] · 수식 참조[^fxref] · Dynamic 값[^untyped] · % 표기[^percent] · 변수 데이터 형식[^types] · 사용자 지정 선택기[^selector]

[^fx]: **Power Fx in desktop flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/power-fx> (2026-11-02 확인). 토글, 달라지는 규칙, 동적 변수와 동적 값, 예제, 제한, 버전별 변화. 식은 영어판에서 옮겼다.
[^fxref]: **Formula reference - desktop flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-platform/power-fx/formula-reference-desktop-flows> (2026-11-02 확인). 데스크톱 흐름에서 쓰는 함수 목록. 분류는 이 페이지에서 묶었다.
[^untyped]: **Dynamic values** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-platform/power-fx/untyped-object> (2026-11-02 확인). 변환 함수 표, 점 표기, 없는 필드가 Blank 가 되는 것, 이전 이름 UntypedObject.
[^percent]: **Use variables and the % notation** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/variable-manipulation> (2026-11-02 확인). % 표기의 식, 따옴표, 비교와 논리, IsEmpty. 식은 영어판에서 옮겼다.
[^types]: **Variable data types** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/variable-data-types> (2026-11-02 확인). 목록 · 데이터 테이블 · 데이터 행 · 사용자 지정 개체의 % 표기와 0부터 세는 번호.
[^selector]: **Build a custom selector** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/build-custom-selectors> (2026-11-02 확인). 선택기 안의 % 변수 표기.
