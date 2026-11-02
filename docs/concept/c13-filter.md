---
title: "C13. 필터 쿼리와 배열 필터링"
parent: "개념 2. 자료형과 식"
nav_order: 13
concept:
  id: C13
  grade: A
  used_in: "Lab 1 ⑥ 예약 트리거와 식 · Lab 2 ④ 행 읽기 · ⑤ 거르기와 세기"
  tokens: ["Filter Query", "배열 필터링", "항목 가져오기(2개 이상)", "테이블에 있는 행 나열", "흐름 검사기", "필터 쿼리"]
  sample: true
---

# C13. 필터 쿼리와 배열 필터링

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행.
     ⚠️ 실측할 것: 항목 가져오기(2개 이상) 고급 매개 변수의 라벨(필터 쿼리 · 주문 기준 · 상위 개수 등은 한국어판 커넥터 참조 표기),
     한국어 사이트에서 제목 열의 내부 이름이 Title 인지, 원시 출력에 _xb9c8__xac10__xc77c_ 키가 보이는지,
     마감일 ge '2000-01-01' 의 실패 코드(400 으로 추정), 내부 이름으로 쓴 날짜 비교가 걸러지는지,
     동적 콘텐츠 「마감일」이 내부 이름의 식으로 들어가는지(Lab 1 46번과 같은 질문),
     배열 필터링 고급 모드의 라벨과 @ 식 입력, 필터 쿼리의 대소문자 구분, 한글 열 이름이 Excel 필터 쿼리에서 실제로 실패하는지.
     ★ 강의에서 말로 짚을 것 — Lab 1 ⑥ 저작 메모의 트레이드오프를 「두 방식의 차이」 표로 짚는다. 기본은 가져오는 작업에서 거르는 것이다.
     랩 본문은 바꾸지 않는다(CLAUDE.md §5).
     문서 대조: OR 은 SharePoint 커넥터 참조의 필터 쿼리 설명에만 나온다. 항목 가져오기 심층 문서의 연산자 목록에는 없다 -->

> **다루는 것**: 원본에서 거르는 필터 쿼리와 흐름 안에서 거르는 배열 필터링의 차이, 필터 쿼리의 문법과 내부 열 이름
>
> **쓰는 곳**: Lab 1 `항목 가져오기(2개 이상)` 뒤의 `배열 필터링` · 흐름 검사기 경고 · Lab 2 `점검행` · `조치필요` · `주의행` · `이상행`

---

## 두 방식의 차이

| | 필터 쿼리 | 배열 필터링 |
|---|---|---|
| 거르는 곳 | 원본 서버 | 흐름 안 |
| 놓는 칸 | 항목 가져오기(2개 이상) 등의 필터 쿼리 | 데이터 작업 카드 하나 더 |
| 흐름으로 들어오는 항목 | 조건에 맞는 것 | 건수 상한까지 전부 |
| 문법 | OData 글자 | 왼쪽 값 · 연산자 · 오른쪽 값 |
| 열 이름 | 내부 이름 | 동적 콘텐츠 · `item()?['키']` |
| 쓸 수 있는 입력 | 필터를 지원하는 작업 | 모든 배열 |
| 대소문자 | 문서에 적혀 있지 않음 | 구분 |
| 흐름 검사기 | 경고 없음 | 항목 가져오기의 필터 쿼리 없음 경고 1건 |

필터 쿼리를 쓸 수 있는 원본에서는 가져오는 작업에서 거르는 것이 기본입니다.[^relevant] 흐름이 처리하는 데이터가 적을수록 실행이 빠르고 오류 가능성이 줄어듭니다.[^relevant] 실행 기록에 읽고 쓰는 데이터 양에는 처리량 제한도 있습니다.[^relevant]

배열 필터링을 고르는 경우는 셋입니다.

| 경우 | 이유 |
|---|---|
| 원본에 필터 기능이 없음 | 앞 작업의 출력 · 외부 데이터[^guide] |
| 열 이름이 필터 쿼리에 들어가지 않음 | Excel 은 영숫자 열 이름만 받음[^excel] |
| 내부 이름을 쓰지 않으려 함 | 카드가 하나 늘고 흐름 검사기 경고 1건이 뜸 |

---

## 필터 쿼리의 문법

모양은 `열 이름 연산자 값` 입니다. 글자 값은 작은따옴표로 감쌉니다.[^items]

| 연산자 | 뜻 | 대상 |
|---|---|---|
| `eq` | 같음 | 숫자 · 문자열 |
| `ne` | 같지 않음 | 숫자 · 문자열 |
| `lt` | 작음 | 숫자 |
| `le` | 작거나 같음 | 숫자 |
| `gt` | 큼 | 숫자 |
| `ge` | 크거나 같음 | 숫자 |
| `startswith(열, '값')` | 값으로 시작함 | 문자열 |
| `substringof('값', 열)` | 값을 포함함 | 문자열 |

문서의 예입니다.[^items]

```
Location eq 'Midwest'
```

```
Location eq 'Midwest' and Status eq 'Approved'
```

```
startswith(Title, 'A')
```

조건은 `and` 로 잇습니다. 커넥터 참조의 칸 설명에는 `OR` 예도 있습니다.[^connector] `substringof` 의 인수 순서는 값이 먼저, 열이 뒤입니다.[^rest]

날짜 비교에 식을 넣는 예입니다. 작은따옴표 사이의 `formatDateTime(...)` 은 ***fx***로 넣는 식입니다.[^items]

```
startswith(Title, 'A') and Start_x0020_Date gt 'formatDateTime(utcNow(),'yyyy-MM-dd')'
```

조회 열은 `/` 로 참조 목록의 열까지 적습니다. `Country` 가 조회 열이고 `Title` 이 참조 목록의 열입니다.[^items]

```
Country/Title eq 'New Zealand'
```

SharePoint REST 문서에 지원하지 않는다고 적힌 것은 아래입니다.[^rest]

| 분류 | 지원하지 않음 |
|---|---|
| 산술 | `add` · `sub` · `mul` · `div` · `mod` |
| 수학 함수 | `round` · `floor` · `ceiling` |
| 문자열 함수 | `endswith` · `replace` · `substring` · `tolower` · `toupper` · `trim` · `concat` |
| 열 종류 | 여러 값을 담는 조회 열 · 사용자 열 |

---

## 내부 이름

SharePoint 열에는 화면에 보이는 이름과 내부 이름이 따로 있습니다. 필터 쿼리와 주문 기준은 내부 이름을 받습니다.[^items] 내부 이름은 열을 만들 때 그때의 이름으로 자동 생성되고, 뒤에 바뀌지 않습니다.[^field]

| 화면 이름 | 내부 이름 | 규칙 |
|---|---|---|
| `제목` | `Title` | 기본 열 |
| `Start Date` | `Start_x0020_Date` | 공백이 `_x0020_`. `0` 은 숫자 |
| `마감일` | `_xb9c8__xac10__xc77c_` | 글자마다 `_x` + 16진수 코드 + `_` |

`마감일` 은 `마`(`b9c8`) · `감`(`ac10`) · `일`(`c77c`) 세 글자가 이어진 값입니다. 문서가 적은 것은 공백 인코딩이고, 한글의 예는 이 과정의 목록에서 확인한 값입니다.

| 내부 이름을 찾는 곳 | 방법 |
|---|---|
| 실행 기록 | 항목 가져오기 카드의 원시 출력에 나오는 키 |
| 목록 설정 | 열 목록에서 열 이름을 누른 페이지의 주소 끝[^qa] |

열을 영문 이름으로 만든 뒤 화면 이름을 한글로 바꾸면 내부 이름은 영문으로 남습니다.[^field]

배열 필터링의 왼쪽 값을 동적 콘텐츠로 고르면 내부 이름을 입력하지 않습니다. 항목 가져오기 출력의 키는 내부 이름이고, 식으로 직접 쓸 때는 `item()?['_xb9c8__xac10__xc77c_']` 처럼 적습니다.

---

## 항목 가져오기의 칸

**항목 가져오기(2개 이상)**는 목록에, 파일 가져오기는 라이브러리에 씁니다. 두 작업의 기능은 같습니다.[^items]

| 칸 | 영문 | 하는 일 |
|---|---|---|
| 필터 쿼리 | Filter Query | 조건에 맞는 항목만 돌려줌 |
| 주문 기준 | Order By | 정렬. `Title asc` · `Start_x0020_Date desc` |
| 상위 개수 | Top Count | 돌려줄 건수. [C14](c14-limits.html) |
| 항목을 폴더로 제한 | Limit Entries to Folder | 지정한 폴더의 항목만. 비우면 목록 전체 |
| 중첩된 항목 포함 | Include Nested Items | 하위 폴더 항목 포함. 기본 true |
| 보기별 열 제한 | Limit Columns by View | 그 보기에 있는 열만 돌려줌 |

칸 이름은 한국어판 커넥터 참조의 표기입니다.[^connector]

---

## Excel의 필터 쿼리

**테이블에 있는 행 나열**도 필터 쿼리 칸이 있고, 조건은 SharePoint와 다릅니다.[^excel]

| 항목 | SharePoint 항목 가져오기 | Excel 테이블에 있는 행 나열 |
|---|---|---|
| 비교 | `eq` · `ne` · `lt` · `le` · `gt` · `ge` | `eq` · `ne` |
| 문자열 함수 | `startswith` · `substringof` | `contains` · `startswith` · `endswith` |
| 조건 수 | `and` 로 이음 | 열 하나에 필터 함수 하나 |
| 정렬 | 열 뒤에 `asc` · `desc` | 열 하나 |
| 열 이름 | 내부 이름 | 영숫자 이름만 |
| 데이터 시점 | 적혀 있지 않음 | 필터 · 정렬을 쓰면 최신이 아닐 수 있음 |
| 파일에 걸린 필터 | 해당 없음 | 필터 쿼리를 쓰면 그 위에 쌓임. 쓰지 않으면 무시 |
| 숨겨진 열이 있는 표 | 해당 없음 | OData 매개 변수를 쓸 수 없음 |

`Filter Query` · `Order By` · `Select Query` 는 영숫자 열 이름만 받습니다.[^excel] 한글 열 이름은 흐름에서 **배열 필터링**으로 거릅니다. Excel 출력의 키는 열 머리글 그대로이므로 식은 `item()?['점검월']` 입니다.

출력의 열 이름에서 일부 문자는 인코딩됩니다. `Column [one]#1` 은 `Column [one]_x0023_1` 이 됩니다.[^excel]

| 문자 | 인코딩 |
|---|---|
| `.` | `_x002e_` |
| `@` | `_x0040_` |
| `:` | `_x003a_` |
| `#` | `_x0023_` |

---

## 배열 필터링의 구성

From 칸에 배열, Filter Query 칸에 왼쪽 값 · 연산자 · 오른쪽 값을 넣습니다. 표기와 입출력은 [C12](c12-dataops.html)에서 다룹니다.

| 항목 | 내용 |
|---|---|
| 항목을 가리키는 식 | `item()` 은 From 배열의 한 항목 |
| 연산자 라벨 | 다음과 같음 · 다음과 같지 않음 · 작거나 같음 등 |
| 대소문자 | 구분[^ops] |
| 조건을 식으로 | 고급 모드에 `@equals(item()?['Status'], 'Active')`[^cookbook] |
| 날짜 비교 | `yyyy-MM-dd` 끼리는 글자 순서로 맞음. 다른 형식은 `ticks()`[^cookbook] |

날짜 형식은 [C11](c11-datetime.html)에서 다룹니다.

---

## 샘플

흐름 `식 연습장_HGD` 를 씁니다. 없으면 [C7](c07-types.html)의 샘플로 만듭니다. 읽는 목록은 [Lab 1](../lab1.html) ①에서 만든 `업무요청_HGD` 입니다. 건수의 기준은 Lab 1 ⑤의 두 항목 `프린터 토너 교체` · `회의실 예약 변경` 입니다.

1. [Power Automate — {{ site.pa.environment }}]({{ site.pa.powerautomate_url }}){:target="_blank"}를 엽니다. 왼쪽 메뉴 **내 흐름**에서 `식 연습장_HGD` 를 열고 **편집**을 누릅니다.
2. 트리거 카드 아래 **+** › **작업 추가**에서 `항목 가져오기` 를 검색해 **SharePoint** 아래 **항목 가져오기(2개 이상)**를 고릅니다.
3. **사이트 주소** 드롭다운에서 **Power Automate 실습**을 고릅니다. 목록에 없으면 **사용자 지정 값 입력**을 고르고 아래 주소를 붙여넣습니다.

    ```
    {{ site.pa.sharepoint_site }}
    ```

4. **목록 이름**에서 본인의 `업무요청_HGD` 를 고릅니다.
5. 구성 창 맨 위의 카드 이름을 아래로 바꿉니다.

    ```
    목록항목
    ```

6. **작성** 카드를 누릅니다. **입력** 칸을 비우고 ***fx*** 단추를 누릅니다. 식 편집기에 아래를 붙여넣고 **추가**를 누릅니다.

    ```
    length(body('목록항목')?['value'])
    ```

7. **저장**을 누릅니다. **흐름 검사기**에 경고가 뜨면 창을 닫습니다. **테스트** › **수동** › **테스트**를 누릅니다. **흐름 실행** 창에 연결 확인이 나오면 **계속**을 누르고, **흐름 실행**을 누른 뒤 **완료**를 누릅니다. 입력 칸이 비어 실행되지 않으면 아무 글자나 넣습니다.
8. 실행 화면에서 **작성** 카드를 누릅니다.

    **완료 기준**: 출력이 목록의 항목 수와 같다. Lab 1 ⑤의 두 항목이면 `2` 다.

9. **목록항목** 카드를 누르고 출력 칸 오른쪽 위 **원시 출력 표시**를 누릅니다.

    **완료 기준**: 항목마다 `Title` 과 `_xb9c8__xac10__xc77c_` 키가 보인다.

10. **편집**을 누르고 **목록항목** 카드를 누릅니다. **고급 매개 변수**에서 **필터 쿼리**에 체크합니다. **필터 쿼리** 칸에 아래를 입력합니다.

    ```
    startswith(Title, '프린터')
    ```

11. **저장**을 누르고 7번과 같이 실행합니다. **작성** 카드를 누릅니다.

    **완료 기준**: 출력이 `1` 이다. **목록항목** 카드의 출력에는 `프린터 토너 교체` 만 있다.

12. **편집**을 누르고 **필터 쿼리** 칸을 아래로 바꿉니다. **저장**을 누르고 7번과 같이 실행합니다.

    ```
    substringof('예약', Title)
    ```

    **완료 기준**: **작성** 출력이 `1` 이고, **목록항목** 카드의 출력에 `회의실 예약 변경` 만 있다.

13. **편집**을 누르고 **필터 쿼리** 칸을 화면 이름으로 쓴 아래로 바꿉니다. **저장**을 누르고 7번과 같이 실행합니다.

    ```
    마감일 ge '2000-01-01'
    ```

    **완료 기준**: **목록항목** 카드가 실패로 표시된다.

14. **편집**을 누르고 **필터 쿼리** 칸을 내부 이름으로 쓴 아래로 바꿉니다. **저장**을 누르고 7번과 같이 실행합니다.

    ```
    _xb9c8__xac10__xc77c_ ge '2000-01-01'
    ```

    **완료 기준**: **작성** 출력이 목록의 항목 수와 같다.

15. **편집**을 누르고 **필터 쿼리** 칸을 비웁니다. **목록항목** 아래 **+** › **작업 추가**에서 **기본 제공 도구 › 데이터 작업**을 누르고 **배열 필터링**을 고릅니다.
16. **From** 칸에서 ***fx***를 누르고, 아래 식을 붙여넣은 뒤 **추가**를 누릅니다.

    ```
    body('목록항목')?['value']
    ```

17. **Filter Query** 왼쪽 **값 선택** 칸에 ***fx***로 아래 식을 넣습니다. 연산자는 **다음과 같음**으로 둡니다.

    ```
    item()?['Title']
    ```

18. 오른쪽 칸에 아래를 입력합니다.

    ```
    프린터 토너 교체
    ```

19. **작성** 카드의 **입력**을 비우고 ***fx***로 아래 식을 넣습니다.

    ```
    length(body('배열_필터링'))
    ```

20. **저장**을 누르고 7번과 같이 실행합니다.

    **완료 기준**: **목록항목** 출력은 모든 항목을 담고, **작성** 출력은 `1` 이다. 11번과 건수는 같고, 흐름으로 들어온 항목 수가 다르다.

21. **편집**을 누릅니다. **작성** 카드의 **입력**을 비우고 ***fx***로 아래 식을 넣습니다.

    ```
    utcNow()
    ```

22. **배열 필터링** · **목록항목** 순서로 카드를 마우스 오른쪽 단추로 누르고 **삭제**를 고릅니다. **저장**을 누릅니다.

    **완료 기준**: 캔버스에 트리거와 **작성** 카드만 남아 있다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다. 한글 내부 이름의 예와 흐름 검사기 경고는 Lab 1 실측에서 옮겼습니다.

- **문헌**: 항목 가져오기와 파일 가져오기[^items] · SharePoint 커넥터[^connector] · SharePoint REST OData[^rest] · Field 요소[^field] · 목록 열의 내부 이름 찾기[^qa] · Excel Online (Business) 커넥터[^excel] · 필요한 데이터만 처리[^relevant] · 데이터 작업 활용 지침[^guide] · 데이터 작업 사용[^ops] · 식 요리책[^cookbook]

[^items]: **In-depth analysis into Get items and Get files SharePoint actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/sharepoint/dev/business-apps/power-automate/guidance/working-with-get-items-and-get-files> (2026-11-02 확인, 한국어판 미번역). 서버에서 거르는 필터 쿼리, 연산자 목록과 예, `_x0020_` 인코딩, 정렬 쿼리, 목록과 라이브러리의 구분.
[^connector]: **SharePoint** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/sharepointonline/> (2026-11-02 확인). 항목 가져오기의 칸과 설명, 필터 쿼리 설명의 `OR` 예.
[^rest]: **Use OData query operations in SharePoint REST requests** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/sharepoint/dev/sp-add-ins/use-odata-query-operations-in-sharepoint-rest-requests> (2026-11-02 확인). `startswith` · `substringof` 의 인수 순서, 지원하지 않는 연산자와 함수, 여러 값 조회 열.
[^field]: **Field element (List)** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/sharepoint/dev/schema/field-element-list> (2026-11-02 확인). `Name` 은 사용자가 정한 이름에서 자동 생성되는 내부 이름이고 수명 동안 바뀌지 않는다는 것.
[^qa]: **Adding custom hover text using json to a MS List column** — Microsoft Q&A. <https://learn.microsoft.com/answers/a/1903628> (2026-11-02 확인). 목록 설정의 열 페이지 주소 끝에서 내부 이름을 읽는 방법. 공식 문서가 아닌 답변이다.
[^excel]: **Excel Online (Business)** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/excelonlinebusiness/> (2026-11-02 확인). 필터 함수 목록, 열 하나에 함수 하나, 정렬 열 하나, 영숫자 열 이름 제한, 데이터 지연, 필터 누적, 숨겨진 열, 열 이름 인코딩.
[^relevant]: **Work only with relevant data** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/work-with-relevant-data> (2026-11-02 확인). 필요한 데이터만 처리하는 이유, 처리량 제한, 작업 수준의 필터 쿼리 · 상위 개수 · 보기별 열 제한.
[^guide]: **Work with data operations** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/use-data-operations> (2026-11-02 확인). 필터 기능이 없는 외부 원본에 데이터 작업을 쓴다는 것, 원본에서 거르는 편이 나은 경우.
[^ops]: **Use data operations** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/data-operations> (2026-11-02 확인). 배열 필터링의 비교 글자는 대소문자를 구분한다는 것.
[^cookbook]: **Expression cookbook for cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/expression-cookbook> (2026-11-02 확인). 13번 고급 모드 식, 29번 날짜 문자열 비교와 `ticks()`.
