---
title: "P5. 자료형의 속성"
parent: "개념 5. 변수와 제어"
nav_order: 5
concept:
  id: P5
  grade: B
  used_in: "랩에서 쓰지 않음"
  tokens: []
  sample: true
---

# P5. 자료형의 속성

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. 속성 이름은 datatype-properties 영어판에서 옮겼다. 한국어판은 속성 이름을 번역했다(Length → 길이, Count → 개수, Name → 이름, RowsCount → 행 수, FilesCount → 파일 수). 표기로 쓰면 안 된다. 한국어판은 RootPath 설명도 「전체 경로」로 적었다.
     영어판 표기의 대소문자는 그대로 옮겼다(텍스트 isEmpty · 데이터 테이블 IsEmpty).
     Lab 4~7 본문에는 속성 표기가 없다(grep 확인).
     ⚠️ 실측할 것: `%Files[0].Name%` 형식(문서의 예는 PDF 표 정보 목록의 `%VariableName[ItemNumber].PropertyName%` 이고 파일 목록의 예가 아니다) · Extension 값에 점이 붙는지 · 폴더의 하위 폴더 가져오기의 칸 이름 「폴더 필터」와 생성 변수 Folders · 오류 속성은 샘플에 넣지 않았다(P18) -->

> **다루는 것**: `%변수.속성%` 표기와 텍스트 · 날짜 · 목록 · 파일 · 폴더 · 데이터 테이블 · 데이터 행 · 오류의 속성
>
> **쓰는 곳**: 랩에서 쓰지 않음

---

## 표기

일부 자료형은 값에 딸린 속성을 가집니다. 속성은 날짜의 일처럼 값의 일부이거나 목록의 크기처럼 값을 설명하는 정보입니다.[^props]

| 표기 | 읽는 값 |
|---|---|
| `%변수.속성%` | 그 변수의 속성 |
| `%Files.Count%` | 파일 목록의 항목 수 |
| `%Files[0].Name%` | 파일 목록 첫 항목의 이름 |

속성 이름은 영어로 적습니다. 한국어판 문서의 표는 `Length` 를 `길이`, `Count` 를 `개수` 로 번역해 두었습니다.

---

## 텍스트

| 속성 | 값 |
|---|---|
| `Length` | 글자 수 |
| `isEmpty` | 비어 있으면 True, 글자가 있으면 False |
| `ToUpper` | 대문자로 쓴 텍스트 |
| `ToLower` | 소문자로 쓴 텍스트 |
| `Trimmed` | 앞뒤 공백을 뺀 텍스트 |

---

## 날짜

| 속성 | 값 |
|---|---|
| `Year` | 연도 |
| `Month` | 월 |
| `Day` | 일 |
| `DayOfWeek` | 요일 이름. Sunday · Monday 등 |
| `DayOfYear` | 그해의 몇 번째 날. 1~365 또는 366 |
| `Hour` | 시 |
| `Minute` | 분 |
| `Second` | 초 |

---

## 목록

| 속성 | 값 |
|---|---|
| `Count` | 항목 수 |

---

## 파일

| 속성 | 값 |
|---|---|
| `FullName` | 전체 경로 |
| `RootPath` | 루트 경로. 예 `C:\` |
| `Directory` | 파일이 있는 폴더 |
| `Name` | 확장명을 포함한 파일 이름 |
| `NameWithoutExtension` | 확장명을 뺀 파일 이름 |
| `Extension` | 확장명 |
| `Size` | 크기(바이트) |
| `CreationTime` | 만든 날짜 |
| `LastAccessed` | 마지막으로 접근한 날짜 |
| `LastModified` | 마지막으로 수정한 날짜 |
| `IsHidden` | 숨김 파일이면 True |
| `IsSystem` | 시스템 파일이면 True |
| `IsReadOnly` | 읽기 전용이면 True |
| `IsArchive` | 보관 파일이면 True |
| `Exists` | 파일이 있으면 True |
| `isEmpty` | 파일이 비어 있으면 True |

---

## 폴더

| 속성 | 값 |
|---|---|
| `FullName` | 전체 경로 |
| `RootPath` | 루트 경로. 예 `C:\` |
| `Parent` | 상위 폴더 |
| `Name` | 폴더 이름 |
| `CreationTime` | 만든 날짜 |
| `LastModified` | 마지막으로 수정한 날짜 |
| `IsHidden` | 숨김 폴더이면 True |
| `Exists` | 폴더가 있으면 True |
| `isEmpty` | 폴더가 비어 있으면 True |
| `FilesCount` | 폴더 안의 파일 수 |
| `FoldersCount` | 폴더 안의 폴더 수 |

---

## 데이터 테이블

| 속성 | 값 |
|---|---|
| `RowsCount` | 행 수 |
| `Columns` | 열 이름의 목록 |
| `IsEmpty` | 비어 있으면 True, 항목이 있으면 False |
| `ColumnHeadersRow` | 머리글을 담은 데이터 행 |

---

## 데이터 행

| 속성 | 값 |
|---|---|
| `ColumnsCount` | 행이 가진 열 수 |
| `ColumnsNames` | 머리글의 목록 |

---

## 오류

**마지막 오류 가져오기** 작업이 만드는 오류 변수의 속성입니다.[^errors] 작업과 사용법은 [P18](p18-errors.html)에서 다룹니다.

| 속성 | 값 |
|---|---|
| `ActionIndex` | 오류를 낸 작업의 번호 |
| `ActionName` | 오류를 낸 작업의 이름 |
| `ErrorDetails` | 오류의 세부 정보 |
| `Location` | 오류를 낸 작업과 하위 흐름의 이름과 번호 |
| `Message` | 오류 메시지 |
| `SubflowName` | 오류를 낸 작업이 든 하위 흐름의 이름 |

---

## 다른 자료형

아래 자료형의 속성은 [변수 데이터 형식 속성 문서](https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/datatype-properties){:target="_blank"}에 있습니다.

| 분류 | 자료형 |
|---|---|
| 메일 | 메일 메시지 · Exchange 메일 메시지 · Outlook 메일 메시지 · Exchange 연결 |
| FTP | FTP 파일 · FTP 폴더 · FTP 연결 |
| 인스턴스와 세션 | 웹 브라우저 인스턴스 · 창 인스턴스 · Excel 인스턴스 · CMD 세션 · 터미널 세션 |
| 연결과 데이터 | SQL 연결 · PDF 테이블 정보 · XML 노드 · 자격 증명 |
| 디렉터리와 클라우드 | Active Directory 항목 · 그룹 정보 · 사용자 정보 · EBS 스냅샷 · EBS 볼륨 · Azure 관리 디스크 · Azure 리소스 그룹 · Azure 스냅샷 |

---

## 샘플

`C:\PA실습` 폴더의 파일 목록을 읽어 속성을 확인합니다. 작업은 작업 검색 칸에 이름을 입력해 찾습니다. 흐름 `개념 연습_HGD` 를 씁니다. 없으면 [P2](p02-types.html)의 1·2번으로 만듭니다.

1. 콘솔 흐름 목록에서 `개념 연습_HGD` 의 **편집**을 누릅니다. 디자이너가 이미 열려 있으면 그 창을 씁니다.
2. **Main** 탭의 빈 곳을 한 번 누르고 `Ctrl` + `A` 로 전체를 고른 뒤 `Delete` 키를 누릅니다.
3. 작업 검색 칸에 `폴더의 파일` 을 입력하고, **폴더** 아래 **폴더의 파일 가져오기**를 작업 영역으로 끌어다 놓습니다. **폴더**와 **파일 필터**에 아래를 차례로 넣고 **저장**을 누릅니다. 찾은 파일 목록은 **변수 생성됨**의 `Files` 에 담깁니다.

    ```
    C:\PA실습
    ```

    ```
    *.xlsx
    ```

4. 작업 검색 칸에 `변수 설정` 을 입력하고 **변수 설정**을 맨 아래로 끌어다 놓습니다. **변수** 칸과 **값** 칸에 아래를 차례로 넣고 **저장**을 누릅니다.

    ```
    파일수
    ```

    ```
    %Files.Count%
    ```

5. **변수 설정**을 하나 더 놓고 아래를 넣습니다.

    ```
    파일이름
    ```

    ```
    %Files[0].Name%
    ```

6. **변수 설정**을 하나 더 놓고 아래를 넣습니다.

    ```
    순수이름
    ```

    ```
    %Files[0].NameWithoutExtension%
    ```

7. **변수 설정**을 하나 더 놓고 아래를 넣습니다.

    ```
    확장명
    ```

    ```
    %Files[0].Extension%
    ```

8. **변수 설정**을 하나 더 놓고 아래를 넣습니다.

    ```
    바이트
    ```

    ```
    %Files[0].Size%
    ```

9. **변수 설정**을 하나 더 놓고 아래를 넣습니다.

    ```
    수정일
    ```

    ```
    %Files[0].LastModified%
    ```

10. **변수 설정**을 하나 더 놓고 아래를 넣습니다. 날짜 값의 속성입니다.

    ```
    수정연도
    ```

    ```
    %수정일.Year%
    ```

11. **변수 설정**을 하나 더 놓고 아래를 넣습니다.

    ```
    수정요일
    ```

    ```
    %수정일.DayOfWeek%
    ```

12. **변수 설정**을 하나 더 놓고 아래를 넣습니다. 텍스트 값의 속성입니다.

    ```
    글자수
    ```

    ```
    %파일이름.Length%
    ```

13. **변수 설정**을 하나 더 놓고 아래를 넣습니다.

    ```
    대문자
    ```

    ```
    %파일이름.ToUpper%
    ```

14. 작업 검색 칸에 `하위 폴더` 를 입력하고, **폴더** 아래 **폴더의 하위 폴더 가져오기**를 맨 아래로 끌어다 놓습니다. **폴더**와 **폴더 필터**에 아래를 차례로 넣고 **저장**을 누릅니다. 찾은 폴더 목록은 **변수 생성됨**의 `Folders` 에 담깁니다.

    ```
    C:\PA실습
    ```

    ```
    정리대상
    ```

15. **변수 설정**을 맨 아래로 끌어다 놓고 아래를 넣습니다.

    ```
    폴더파일수
    ```

    ```
    %Folders[0].FilesCount%
    ```

16. **변수 설정**을 하나 더 놓고 아래를 넣습니다. 데이터 테이블 하나를 만듭니다.

    ```
    공고표
    ```

    ```
    %{^['공고번호', '추정가격'], ['A-1', '1000'], ['A-2', '2000']}%
    ```

17. **변수 설정**을 하나 더 놓고 아래를 넣습니다.

    ```
    행수
    ```

    ```
    %공고표.RowsCount%
    ```

18. **변수 설정**을 하나 더 놓고 아래를 넣습니다.

    ```
    열목록
    ```

    ```
    %공고표.Columns%
    ```

19. 작업 검색 칸에 `각각의` 를 입력하고 **각각의 경우**를 맨 아래로 끌어다 놓습니다. **반복할 값**과 **저장 위치**에 아래를 차례로 넣고 **저장**을 누릅니다.

    ```
    %공고표%
    ```

    ```
    공고
    ```

20. **변수 설정**을 **각각의 경우**와 **End** 사이로 끌어다 놓고 아래를 넣습니다. 현재 항목은 데이터 행입니다.

    ```
    열수
    ```

    ```
    %공고.ColumnsCount%
    ```

21. 도구 모음의 **실행**(▶)을 누릅니다. 오른쪽 세로 막대의 **{x}** 를 눌러 변수 창을 엽니다.

    **완료 기준**: `파일수` 가 탐색기에서 본 `C:\PA실습` 의 xlsx 파일 수와 같다. `파일이름` 은 `.xlsx` 로 끝나고 `순수이름` 은 확장명 없이 보인다. `폴더파일수` 는 탐색기에서 본 `C:\PA실습\정리대상` 의 파일 수와 같다. `행수` 2 · `열수` 2 이고 `열목록` 에 공고번호 · 추정가격이 들어 있다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: 변수 데이터 형식 속성[^props] · 변수 데이터 형식[^types] · 폴더 작업[^folder] · 오류 처리[^errors]

[^props]: **Variable data type properties** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/datatype-properties> (2026-11-02 확인). `%VariableName.PropertyName%` 표기와 속성 표. 속성 이름은 영어판 `en-us` 에서 옮겼다.
[^types]: **Variable data types** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/variable-data-types> (2026-11-02 확인). `%VariableName[ItemNumber].PropertyName%` 표기, For each 의 현재 항목이 데이터 행이라는 것.
[^folder]: **Folder actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/folder> (2026-11-02 확인). 폴더의 파일 가져오기와 폴더의 하위 폴더 가져오기의 칸, 생성 변수 `Files` · `Folders`.
[^errors]: **Handle errors in desktop flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/errors> (2026-11-02 확인). 마지막 오류 가져오기가 속성 여섯 개를 가진 오류 변수를 만든다는 것.
