---
title: Lab 4. Desktop 흐름 기본
nav_order: 5
---

# Lab 4. Desktop 흐름 기본 🖥️

<!-- 저작 메모(학생 비노출) — 실측 전 초안(2026-10-02). 촬영·실측 전이다.

     ★ 이 랩의 자리
       - Day 2 첫 랩. 받는 것은 없다 — Day 1 클라우드 흐름과 이어지는 객체가 없다.
       - 넘기는 것은 객체가 아니라 PAD 조작 습관이다. 작업 검색 → 끌어 놓기 → 매개 변수 입력 → 저장,
         생성된 변수 이름 바꾸기, 블록(If·Loop·For each) 안에 끌어 넣기, %변수% 입력, Excel 실행·닫기.
       - PAD 설치·로그인은 「PAD 개요」 30분 안에 끝낸다(PA_설계 §2). 스텝으로 세지 않는다.

     ★ 실측 — 실측 전. 53스텝 · 컷 53(스텝당 1컷) 예정.

     ★ 랩 간 의존
       - Lab 5 `공고 조회_HGD` 는 이 흐름을 열지 않는다. 같은 습관(작업 검색·끌어 놓기·Excel 실행/닫기·실행 후 변수 창 보기)을 그대로 쓴다.
       - Lab 6 ④·⑤ 의 「For each」 · 「If」 · `%CurrentItem%` 는 이 랩 ⑤·⑥(36·47·48번)에서 처음 나온다.
       - 37번에서 ⑤의 반복 변수를 `CurrentFile` 로 바꾼다. ⑥ 47번의 「For each」가 `CurrentItem` 이름을 그대로 쓰게 하려는 것이다.
         37번을 지우면 47번의 기본 이름이 달라질 수 있다(⚠️ 아래).
       - ⑤는 파일을 옮기므로 두 번째 실행부터 옮길 pdf가 없다. 「준비」에 압축 다시 풀기를 적었다.

     ⚠️ 실측할 것
       - 작업 이름: MS Learn 한국어판은 Loop = 「반복」, For each = 「각각에 대해」, Else = 「그 밖의 경우」,
         Launch Excel = 「Excel을 시작」(본문 설명은 「Excel 실행」)으로 적는다. 본문은 PA_설계 §6 표기(Loop · For each · Else · Excel 실행)를 따랐다. 화면 글자로 바꾼다.
       - 매개 변수 라벨: MS Learn 한국어판 표가 영문 라벨을 그대로 둔다. 아래는 전부 추정이다.
         변수 설정(설정·값) · 메시지 표시(메시지 상자 제목·표시할 메시지) · 입력 대화 표시(입력 대화 제목·입력 대화 메시지)
         · If(첫 번째 피연산자·연산자·두 번째 피연산자, 같음(=)) · Loop(시작 값·증분·끝)
         · 폴더 만들기(새 폴더 만들기 위치·새 폴더 이름) · 폴더의 파일 가져오기(폴더·파일 필터)
         · For each(반복할 값·저장 위치) · 파일 이동(이동할 파일·대상 폴더)
         · Excel 실행(Excel 실행: 다음 문서 열기 · 문서 경로) · Excel 워크시트에서 읽기(검색: 워크시트에서 사용 가능한 모든 값 · 고급 › 범위의 첫 줄에 열 이름이 포함되어 있음)
         · 목록에 항목 추가(항목 추가·목록에) · Excel 닫기(Excel을 닫기 전: 문서 저장 안 함)
       - 생성 변수의 이름은 작업 대화 상자 아래 「생성된 변수」에서 눌러 바꾼다고 적었다. 화면 위치와 라벨 확인.
       - 37번에서 이름을 바꾸지 않았을 때 47번 「For each」의 기본 이름이 `CurrentItem2` 가 되는지.
       - 33번: `정리완료` 폴더가 이미 있을 때 「폴더 만들기」가 오류 없이 지나가는지(52번 전체 실행이 ⑤를 다시 지난다).
       - 51·53번: 목록 변수 `%AGradeList%` 를 메시지에 넣으면 항목이 한 줄에 하나씩 나오는지.
       - 45번: 「범위의 첫 줄에 열 이름이 포함되어 있음」이 고급 접힘 안에 있는지.
       - 23번: 입력값 `a`(소문자)는 거짓 가지로 간다. 본문에 적지 않았다.
       - 6번: 작업 창·작업 영역·변수 창은 MS Learn 「흐름 디자이너」 한국어판의 용어다. 화면 머리글과 대조한다.

     ✔ 1~15번 실측(2026-10-05)
       - 콘솔: 계정은 제목 표시줄 오른쪽 위, 환경은 오른쪽 위 「환경」 → 환경 창 목록. 새 흐름은 왼쪽 막대 「흐름」 → 「새 흐름」(빈 목록) / 「+ 새로운」.
         ⚠️ 「+ 새로운」 드롭다운 항목은 아직 안 봤다. 공용 계정이라 수강생 화면에는 흐름이 이미 있을 수 있다
       - 「흐름 만들기」 창에 「Power Fx 사용」 토글이 있다(기본 끔). 끈 채로 둔다 — 이 랩은 %변수% 문법
       - 디자이너: 작업 창 머리글 「작업」, 검색 칸 라벨 「검색」, 작업 영역 탭 「Main」, 변수 창 머리글 「변수」(오른쪽 세로 막대 {x} 로 여닫음).
         변수 창은 전역/로컬 탭, 묶음 입력 · 출력 · 흐름. 「흐름 변수」가 아니라 「흐름」
       - 변수 설정 칸 라벨은 「변수」 · 「값」(설정 아님). 작업을 끌어 놓거나 두 번 클릭하면 대화 상자가 바로 열린다
       - 메시지 표시 라벨 메시지 상자 제목 · 표시할 메시지 확인. 생성 변수 영역 라벨은 「변수 생성됨」(ButtonPressed)
       - 변수 두 번 클릭 → 「흐름 변수 편집」 창(변수 이름 · 기본 데이터 형식 · 기본값 · 변수 값) -->

> **이번 랩 완성물**: 변수·조건·반복·파일 정리·Excel 읽기를 한 흐름에 담은 Desktop 흐름 `PAD 기본_HGD`
>
> **예상 시간**: 80분
>
> **완성 신호**: `C:\PA실습\정리완료` 폴더에 pdf 3개가 옮겨지고, 메시지 창에 A 등급 거래처 5곳이 뜬다

{: .time }
80분 타이머. 6단(시작 → 변수와 메시지 → 입력과 조건 → 반복 → 파일과 폴더 → Excel)으로 나눠 진행합니다.

---

## 준비

- 실습 파일을 PC에 받습니다. [PA실습.zip 다운로드](../assets/download/PA실습.zip)
- 받은 파일을 `C:\` 에 풉니다. `C:\PA실습\` 폴더 안에 `거래처목록.xlsx` 와 `정리대상` 폴더가 보이면 됩니다.
- Power Automate Desktop(이하 PAD)이 설치되어 있고, 교육용 계정으로 로그인되어 있어야 합니다. 「PAD 개요」 시간에 확인한 상태 그대로입니다.
- PAD가 없으면 설치합니다.
  - [PAD 설치 파일 받기](https://go.microsoft.com/fwlink/?linkid=2102613){:target="_blank"} — `Setup.Microsoft.PowerAutomate.exe` 를 받아 실행합니다. PC 관리자 권한이 필요합니다.
  - 관리자 권한이 없으면 Microsoft Store 판을 설치합니다. 경로는 [Power Automate 설치](https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/install){:target="_blank"} 문서에 있습니다. 두 판을 함께 설치할 수는 없습니다.[^install]
  - Lab 5에서 쓰는 [Edge 확장 Microsoft Power Automate](https://microsoftedge.microsoft.com/addons/detail/microsoft-power-automate/kagpabjoboikccfdghpdlaaopmgpgfdc){:target="_blank"}도 함께 설치합니다. 설치 마지막 화면에서 확장 설치를 건너뛰었을 때만 해당합니다.[^ext]
- ⑤ 파일과 폴더를 처음부터 다시 하려면 `C:\PA실습\` 을 지우고 압축을 다시 풉니다. 한 번 실행하면 pdf가 `정리완료` 로 옮겨져 옮길 파일이 남지 않습니다.

---

## 단계 ① 시작

1. 시작 메뉴 검색에 `power` 를 입력하고 **최고의 매치**의 **Power Automate**(앱)를 실행합니다.

    ![시작 메뉴 검색 결과의 Power Automate 앱](../assets/lab4/lab4-01.png)

2. 콘솔 제목 표시줄 오른쪽 위의 계정 이름이 교육용 계정(**교육**)인지 확인합니다.

    ![콘솔 제목 표시줄 오른쪽 위의 계정 이름 교육](../assets/lab4/lab4-02.png)

3. 콘솔 오른쪽 위 **환경**이 `{{ site.pa.environment }}` 인지 확인합니다. 다르면 **환경**을 누르고 목록에서 `{{ site.pa.environment }}` 를 고릅니다.

    ![콘솔 오른쪽 위의 환경 표시](../assets/lab4/lab4-03.png)

    ![환경 창 목록의 edu261006](../assets/lab4/lab4-03b.png)

4. 왼쪽 막대의 **흐름**을 누르고 **새 흐름**을 누릅니다. 목록에 흐름이 이미 있으면 위쪽 **+ 새로운**을 누릅니다.

    ![흐름 화면 — 왼쪽 흐름 메뉴, 위쪽 + 새로운, 가운데 새 흐름 단추](../assets/lab4/lab4-04.png)

5. **흐름 만들기** 창의 **흐름 이름**에 아래를 입력하고 **만들기**를 누릅니다. `HGD` 대신 본인 이니셜을 넣습니다. **Power Fx 사용**은 끈 채로 둡니다.

    ```
    PAD 기본_HGD
    ```

    이 랩은 변수를 `%Course%` 처럼 `%` 로 감싸 씁니다. Power Fx를 켜면 식 문법이 달라집니다.

    ![흐름 만들기 창 — 흐름 이름 PAD 기본_EDU, Power Fx 사용 끔](../assets/lab4/lab4-05.png)

6. 디자이너 창이 열리면 세 영역을 확인합니다. 왼쪽이 **작업** 창, 가운데가 작업 영역(**Main** 탭), 오른쪽이 **변수** 창입니다. 변수 창은 오른쪽 세로 막대의 **{x}** 로 열고 닫습니다.

    ![작업 창 · 빈 작업 영역 · 변수 창이 보이는 디자이너](../assets/lab4/lab4-06.png)

7. 작업 창 맨 위의 **검색** 칸(이하 작업 검색 칸)을 확인합니다. 이 랩의 작업은 모두 이 칸에 이름을 입력해 찾고, 찾은 작업을 작업 영역으로 끌어다 놓습니다. 예를 들어 `브라우저` 를 입력하면 브라우저 자동화 작업만 남습니다.

    ![작업 검색 칸에 브라우저를 입력해 걸러진 작업 목록](../assets/lab4/lab4-07.png)

## 단계 ② 변수와 메시지

8. 작업 검색 칸에 `변수 설정` 을 입력하고, 결과의 **변수 설정**을 작업 영역으로 끌어다 놓습니다. 두 번 클릭해도 됩니다. **변수 설정** 대화 상자가 열립니다.

    ![작업 검색 결과의 변수 설정 — 두 번 클릭 또는 끌어 놓기](../assets/lab4/lab4-08.png)

9. **변수** 칸의 `NewVar` 를 눌러 지우고 아래를 입력합니다.

    ```
    Course
    ```

    ![변수 설정 대화 상자의 변수 칸에 입력한 Course](../assets/lab4/lab4-09.png)

10. **값** 칸에 아래를 입력하고 **저장**을 누릅니다.

    ```
    PA 실습
    ```

    ![값 칸에 PA 실습을 넣은 변수 설정 대화 상자와 저장 단추](../assets/lab4/lab4-10.png)

11. 작업 검색 칸에 `메시지 표시` 를 입력하고, **메시지 상자** 아래 **메시지 표시**를 1번 줄 아래로 끌어다 놓습니다.

    ![1번 줄 아래로 끌어 놓는 메시지 표시 작업](../assets/lab4/lab4-11.png)

12. **메시지 상자 제목**과 **표시할 메시지**에 아래를 차례로 입력하고 **저장**을 누릅니다.

    ```
    Lab 4
    ```

    ```
    %Course% 과정을 시작합니다.
    ```

    `%` 로 감싼 이름은 변수입니다. 입력란 오른쪽 위의 **{x}** 를 눌러 변수 목록에서 골라도 같은 글자가 들어갑니다. 대화 상자 아래 **변수 생성됨**의 `ButtonPressed` 는 누른 단추가 담기는 변수입니다.

    ![제목 Lab 4 · 메시지 %Course% 과정을 시작합니다.를 입력한 메시지 표시 대화 상자](../assets/lab4/lab4-12.png)

13. 디자이너 위쪽 도구 모음의 **실행**(▶)을 누릅니다.

    ![작업 두 줄과 도구 모음의 실행 단추](../assets/lab4/lab4-13.png)

14. 메시지 창에 `PA 실습 과정을 시작합니다.` 가 뜨면 **확인**을 누릅니다.

    ![제목 Lab 4 의 PA 실습 과정을 시작합니다. 메시지 창](../assets/lab4/lab4-14.png)

15. 오른쪽 세로 막대의 **{x}** 를 눌러 변수 창을 엽니다. **흐름** 묶음에 `Course` 와 그 값 `PA 실습` 이 보입니다.

    **완료 기준**: `Course` 옆에 `PA 실습` 이 보인다.

    ![변수 창 흐름 묶음의 ButtonPressed OK · Course PA 실습](../assets/lab4/lab4-15.png)

    `Course` 를 두 번 클릭하면 **흐름 변수 편집** 창에서 **변수 값**을 볼 수 있습니다. 확인한 뒤 **취소**로 닫습니다.

    ![흐름 변수 편집 창 — 변수 이름 Course · 변수 값 PA 실습](../assets/lab4/lab4-15b.png)
{: start="8" }

## 단계 ③ 입력과 조건

16. 작업 검색 칸에 `입력 대화 표시` 를 입력하고, **입력 대화 표시** 를 2번 줄 아래로 끌어다 놓습니다.

    ![촬영: 2번 줄 아래로 끌어 놓는 입력 대화 표시 작업](../assets/lab4/lab4-16.png)

17. **입력 대화 제목** 과 **입력 대화 메시지** 에 아래를 차례로 입력하고 **저장** 을 누릅니다. 입력한 글자는 생성된 변수 `UserInput` 에 들어갑니다.

    ```
    등급 확인
    ```

    ```
    등급을 입력하세요. (A 또는 B)
    ```

    ![촬영: 제목과 메시지를 입력한 입력 대화 표시 대화 상자와 생성된 변수 UserInput](../assets/lab4/lab4-17.png)

18. 작업 검색 칸에 `If` 를 입력하고, **If** 를 3번 줄 아래로 끌어다 놓습니다.

    ![촬영: 작업 검색 결과의 If](../assets/lab4/lab4-18.png)

19. 아래와 같이 맞추고 **저장** 을 누릅니다. 작업 영역에 **If** 와 **End** 두 줄이 생깁니다.

    | 항목 | 값 |
    |---|---|
    | 첫 번째 피연산자 | `%UserInput%` |
    | 연산자 | 같음(=) |
    | 두 번째 피연산자 | `A` |

    ![촬영: 피연산자와 연산자를 맞춘 If 대화 상자](../assets/lab4/lab4-19.png)

20. **메시지 표시** 를 **If** 와 **End** 사이로 끌어다 놓고, **표시할 메시지** 에 아래를 입력한 뒤 **저장** 을 누릅니다.

    ```
    A 등급입니다.
    ```

    {: .warning }
    **If 와 End 사이에 놓습니다.** 들여쓰기된 자리에 들어가야 조건이 참일 때만 실행됩니다. End 아래에 놓이면 끌어서 옮깁니다.

    ![촬영: If 블록 안으로 들여쓰기된 메시지 표시](../assets/lab4/lab4-20.png)

21. 작업 검색 칸에 `Else` 를 입력하고, **Else** 를 20번에서 넣은 메시지 표시 아래, **End** 위로 끌어다 놓습니다.

    ![촬영: 메시지 표시와 End 사이에 놓인 Else](../assets/lab4/lab4-21.png)

22. **메시지 표시** 를 **Else** 와 **End** 사이로 끌어다 놓고, **표시할 메시지** 에 아래를 입력한 뒤 **저장** 을 누릅니다.

    ```
    A 등급이 아닙니다.
    ```

    ![촬영: If · Else · End 안에 메시지 표시가 하나씩 들어간 작업 영역](../assets/lab4/lab4-22.png)

23. **실행** 을 누릅니다. 첫 메시지 창에서 **확인** 을 누르고, 입력 창에 `A` 를 입력한 뒤 **확인** 을 누릅니다.

    **완료 기준**: `A 등급입니다.` 가 뜬다.

    ![촬영: A 등급입니다 메시지 창](../assets/lab4/lab4-23.png)

24. 한 번 더 **실행** 하고, 이번에는 입력 창에 `B` 를 입력합니다.

    **완료 기준**: `A 등급이 아닙니다.` 가 뜬다.

    ![촬영: A 등급이 아닙니다 메시지 창](../assets/lab4/lab4-24.png)

25. 변수 창에서 `UserInput` 의 값을 확인합니다. 마지막에 입력한 `B` 가 들어 있습니다.

    ![촬영: 변수 창의 UserInput 값 B](../assets/lab4/lab4-25.png)
{: start="16" }

## 단계 ④ 반복

26. 작업 검색 칸에 `Loop` 를 입력하고, **Loop** 를 작업 영역 맨 아래로 끌어다 놓습니다.

    {: .warning }
    **8번 줄 End 아래, 들여쓰기 없는 자리에 놓습니다.** Else 블록 안에 들어가면 B를 입력했을 때만 반복합니다.

    ![촬영: 맨 아래 End 밑으로 끌어 놓는 Loop](../assets/lab4/lab4-26.png)

27. 아래와 같이 맞추고 **저장** 을 누릅니다. 반복 횟수는 생성된 변수 `LoopIndex` 에 들어갑니다.

    | 항목 | 값 |
    |---|---|
    | 시작 값 | `1` |
    | 증분 | `1` |
    | 끝 | `3` |

    ![촬영: 1 · 1 · 3을 넣은 Loop 대화 상자와 생성된 변수 LoopIndex](../assets/lab4/lab4-27.png)

28. **메시지 표시** 를 **Loop** 와 **End** 사이로 끌어다 놓고, **표시할 메시지** 에 아래를 입력한 뒤 **저장** 을 누릅니다.

    ```
    %LoopIndex%번째 반복입니다.
    ```

    ![촬영: Loop 블록 안의 메시지 표시](../assets/lab4/lab4-28.png)

29. **실행** 합니다. 앞 절의 메시지와 입력 창을 지나면 반복 메시지가 세 번 뜹니다. 뜰 때마다 **확인** 을 누릅니다.

    **완료 기준**: `1번째` · `2번째` · `3번째 반복입니다.` 가 차례로 뜬다.

    ![촬영: 3번째 반복입니다 메시지 창](../assets/lab4/lab4-29.png)

30. 디자이너 위쪽의 **저장** 을 누릅니다.

    ![촬영: 디자이너 도구 모음의 저장 단추](../assets/lab4/lab4-30.png)
{: start="26" }

## 단계 ⑤ 파일과 폴더

31. 파일 탐색기에서 `C:\PA실습\정리대상` 을 엽니다. pdf 3개 · txt 2개 · xlsx 1개, 모두 6개 파일이 있습니다.

    ![촬영: 정리대상 폴더의 파일 6개](../assets/lab4/lab4-31.png)

32. PAD 디자이너로 돌아와 작업 검색 칸에 `폴더 만들기` 를 입력하고, **폴더 만들기** 를 작업 영역 맨 아래로 끌어다 놓습니다.

    ![촬영: 작업 검색 결과의 폴더 만들기](../assets/lab4/lab4-32.png)

33. **새 폴더 만들기 위치** 와 **새 폴더 이름** 에 아래를 차례로 입력하고 **저장** 을 누릅니다.

    ```
    C:\PA실습
    ```

    ```
    정리완료
    ```

    ![촬영: 위치와 이름을 넣은 폴더 만들기 대화 상자](../assets/lab4/lab4-33.png)

34. 작업 검색 칸에 `폴더의 파일 가져오기` 를 입력하고, **폴더의 파일 가져오기** 를 맨 아래로 끌어다 놓습니다.

    ![촬영: 작업 검색 결과의 폴더의 파일 가져오기](../assets/lab4/lab4-34.png)

35. **폴더** 와 **파일 필터** 에 아래를 차례로 입력하고 **저장** 을 누릅니다. 찾은 파일 목록은 생성된 변수 `Files` 에 들어갑니다.

    ```
    C:\PA실습\정리대상
    ```

    ```
    *.pdf
    ```

    ![촬영: 폴더와 파일 필터를 넣은 폴더의 파일 가져오기 대화 상자와 생성된 변수 Files](../assets/lab4/lab4-35.png)

36. 작업 검색 칸에 `For each` 를 입력하고, **For each** 를 맨 아래로 끌어다 놓습니다.

    ![촬영: 작업 검색 결과의 For each](../assets/lab4/lab4-36.png)

37. **반복할 값** 에 `%Files%` 를 입력합니다. 아래 **저장 위치** 의 `CurrentItem` 을 눌러 `CurrentFile` 로 바꾸고 **저장** 을 누릅니다.

    ```
    %Files%
    ```

    ```
    CurrentFile
    ```

    {: .warning }
    **반복 변수 이름을 `CurrentFile` 로 바꿉니다.** ⑥의 For each 가 `CurrentItem` 이름을 씁니다. 여기서 바꾸지 않으면 48·49번의 `%CurrentItem[...]%` 가 다른 변수를 가리킵니다.

    ![촬영: 반복할 값 %Files%와 저장 위치 CurrentFile을 넣은 For each 대화 상자](../assets/lab4/lab4-37.png)

38. 작업 검색 칸에 `파일 이동` 을 입력하고, **파일 이동** 을 **For each** 와 **End** 사이로 끌어다 놓습니다.

    ![촬영: For each 블록 안으로 끌어 놓는 파일 이동](../assets/lab4/lab4-38.png)

39. **이동할 파일** 과 **대상 폴더** 에 아래를 차례로 입력하고 **저장** 을 누릅니다.

    ```
    %CurrentFile%
    ```

    ```
    C:\PA실습\정리완료
    ```

    ![촬영: 이동할 파일과 대상 폴더를 넣은 파일 이동 대화 상자](../assets/lab4/lab4-39.png)

40. **실행** 합니다. 앞 절의 메시지와 입력 창을 지나면 ⑤의 작업이 이어서 돕니다.

    ![촬영: 실행이 끝난 디자이너와 변수 창의 Files](../assets/lab4/lab4-40.png)

41. 파일 탐색기에서 `C:\PA실습` 을 다시 엽니다.

    **완료 기준**: `정리완료` 폴더에 pdf 3개가 있고, `정리대상` 에는 txt 2개 · xlsx 1개만 남았다.

    ![촬영: pdf 3개가 들어간 정리완료 폴더](../assets/lab4/lab4-41.png)
{: start="31" }

## 단계 ⑥ Excel

42. 작업 검색 칸에 `Excel 실행` 을 입력하고, **Excel 실행** 을 작업 영역 맨 아래로 끌어다 놓습니다.

    ![촬영: 작업 검색 결과의 Excel 실행](../assets/lab4/lab4-42.png)

43. **Excel 실행** 을 **다음 문서 열기** 로 바꾸고, **문서 경로** 에 아래를 입력한 뒤 **저장** 을 누릅니다. 생성된 변수는 `ExcelInstance` 입니다.

    ```
    C:\PA실습\거래처목록.xlsx
    ```

    ![촬영: 다음 문서 열기와 문서 경로를 넣은 Excel 실행 대화 상자](../assets/lab4/lab4-43.png)

44. 작업 검색 칸에 `Excel 워크시트에서 읽기` 를 입력하고, **Excel 워크시트에서 읽기** 를 맨 아래로 끌어다 놓습니다.

    ![촬영: 작업 검색 결과의 Excel 워크시트에서 읽기](../assets/lab4/lab4-44.png)

45. **검색** 을 **워크시트에서 사용 가능한 모든 값** 으로 바꿉니다. **고급** 을 펼쳐 **범위의 첫 줄에 열 이름이 포함되어 있음** 을 켜고 **저장** 을 누릅니다. 읽은 표는 생성된 변수 `ExcelData` 에 들어갑니다.

    {: .warning }
    **범위의 첫 줄에 열 이름이 포함되어 있음을 켭니다.** 켜야 머리글 `거래처명` · `등급` 을 열 이름으로 씁니다. 끄면 머리글이 데이터 첫 행으로 읽히고 48번의 `['등급']` 이 열을 찾지 못합니다.

    ![촬영: 모든 값 검색과 첫 줄 열 이름 옵션을 켠 Excel 워크시트에서 읽기 대화 상자](../assets/lab4/lab4-45.png)

46. 작업 검색 칸에 `새 목록 만들기` 를 입력하고, **새 목록 만들기** 를 맨 아래로 끌어다 놓습니다. 생성된 변수 `List` 를 눌러 아래로 바꾸고 **저장** 을 누릅니다.

    ```
    AGradeList
    ```

    ![촬영: 생성된 변수를 AGradeList로 바꾼 새 목록 만들기 대화 상자](../assets/lab4/lab4-46.png)

47. **For each** 를 맨 아래로 끌어다 놓습니다. **반복할 값** 에 아래를 입력하고, **저장 위치** 가 `CurrentItem` 인지 확인한 뒤 **저장** 을 누릅니다.

    ```
    %ExcelData%
    ```

    ![촬영: 반복할 값 %ExcelData%와 저장 위치 CurrentItem인 For each 대화 상자](../assets/lab4/lab4-47.png)

48. **If** 를 47번의 **For each** 와 **End** 사이로 끌어다 놓고, 아래와 같이 맞춘 뒤 **저장** 을 누릅니다.

    | 항목 | 값 |
    |---|---|
    | 첫 번째 피연산자 | `%CurrentItem['등급']%` |
    | 연산자 | 같음(=) |
    | 두 번째 피연산자 | `A` |

    ![촬영: For each 블록 안에 놓인 If와 피연산자 설정](../assets/lab4/lab4-48.png)

49. 작업 검색 칸에 `목록에 항목 추가` 를 입력하고, **목록에 항목 추가** 를 48번 **If** 와 그 아래 **End** 사이로 끌어다 놓습니다. **항목 추가** 와 **목록에** 에 아래를 차례로 입력하고 **저장** 을 누릅니다.

    ```
    %CurrentItem['거래처명']%
    ```

    ```
    %AGradeList%
    ```

    ![촬영: If 블록 안의 목록에 항목 추가 대화 상자](../assets/lab4/lab4-49.png)

50. 작업 검색 칸에 `Excel 닫기` 를 입력하고, **Excel 닫기** 를 맨 아래(For each 의 **End** 아래)로 끌어다 놓습니다. **Excel을 닫기 전** 이 **문서 저장 안 함** 인지 확인하고 **저장** 을 누릅니다.

    ![촬영: 맨 아래 놓인 Excel 닫기와 문서 저장 안 함 설정](../assets/lab4/lab4-50.png)

51. **메시지 표시** 를 맨 아래로 끌어다 놓습니다. **메시지 상자 제목** 과 **표시할 메시지** 에 아래를 차례로 입력하고 **저장** 을 누릅니다.

    ```
    A 등급 거래처
    ```

    ```
    %AGradeList%
    ```

    ![촬영: 제목 A 등급 거래처와 메시지 %AGradeList%를 넣은 메시지 표시 대화 상자](../assets/lab4/lab4-51.png)

52. 디자이너 위쪽의 **저장** 을 누르고 **실행** 합니다. 앞 절의 메시지와 입력 창을 지나면 Excel 이 열렸다가 닫힙니다.

    ![촬영: Excel 거래처목록이 열렸다 닫히는 동안의 디자이너](../assets/lab4/lab4-52.png)

53. 마지막 메시지 창을 확인하고 **확인** 을 누릅니다.

    **완료 기준**: `A 등급 거래처` 창에 한빛시청 · 누리개발원 · 가람교육청 · 다온공사 · 미르제약 다섯 곳이 보이고, 변수 창의 `AGradeList` 가 5개 항목이다.

    ![촬영: A 등급 거래처 5곳이 뜬 메시지 창](../assets/lab4/lab4-53.png)
{: start="42" }

---

## 확인

**필수**: 여기까지 되면 이 랩은 통과입니다

- ① 본인 이니셜이 붙은 Desktop 흐름 `PAD 기본_HGD` 가 있다 (5번)
- ② 실행하면 `PA 실습 과정을 시작합니다.` 가 뜬다 (12·14번)
- ③ 입력값 `A` 와 `B` 가 서로 다른 메시지로 갈린다 (19~24번)
- ④ 반복 메시지가 1·2·3 세 번 뜬다 (27~29번)
- ⑤ `C:\PA실습\정리완료` 에 pdf 3개가 있다 (33~41번)
- ⑥ 메시지 창에 A 등급 거래처 5곳이 뜬다 (45~53번)
{: .checklist }

**관찰**: 나오면 좋고, 안 나와도 실패가 아닙니다

- ⑦ 실행 뒤 변수 창에서 `Files` 와 `ExcelData` 를 열어 내용을 볼 수 있다 (40·52번)
{: .checklist }

---

## 여기까지의 흐름

빈 흐름에 26줄이 생겼습니다. 디자이너 왼쪽의 줄 번호와 대조합니다.

```
 1  변수 설정: Course = PA 실습
 2  메시지 표시: %Course% 과정을 시작합니다.
 3  입력 대화 표시: 등급 확인 → UserInput
 4  If %UserInput% = A
 5      메시지 표시: A 등급입니다.
 6  Else
 7      메시지 표시: A 등급이 아닙니다.
 8  End
 9  Loop LoopIndex 1부터 3까지 1씩
10      메시지 표시: %LoopIndex%번째 반복입니다.
11  End
12  폴더 만들기: C:\PA실습 \ 정리완료
13  폴더의 파일 가져오기: C:\PA실습\정리대상 · *.pdf → Files
14  For each CurrentFile in %Files%
15      파일 이동: %CurrentFile% → C:\PA실습\정리완료
16  End
17  Excel 실행: C:\PA실습\거래처목록.xlsx → ExcelInstance
18  Excel 워크시트에서 읽기: 모든 값 · 첫 줄 열 이름 → ExcelData
19  새 목록 만들기 → AGradeList
20  For each CurrentItem in %ExcelData%
21      If %CurrentItem['등급']% = A
22          목록에 항목 추가: %CurrentItem['거래처명']% → AGradeList
23      End
24  End
25  Excel 닫기: 문서 저장 안 함
26  메시지 표시: A 등급 거래처 · %AGradeList%
```

---

## 출처

이 랩은 아래를 토대로 만들었습니다. 제품 화면과 동작은 실측이고, 문헌은 항목마다 확인일을 적었습니다. 제품이 바뀌면 문헌 쪽이 먼저 낡습니다.

- **실측**: 2026-10-05 1~15번
- **문헌**: PAD 설치[^install] · 브라우저 확장 설치[^ext] · 콘솔과 새 흐름[^start] · 흐름 디자이너[^designer] · 변수 작업[^variables] · 변수 데이터 형식[^datatypes] · 메시지 상자 작업[^display] · 조건부 작업[^conditionals] · 루프 작업[^loops] · 폴더 작업[^folder] · 파일 작업[^file] · Excel 작업[^excel]

[^install]: **Power Automate 설치** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/install> (2026-10-05 확인). MSI 설치 파일(관리자 권한 필요)과 Microsoft Store 판(권한 불필요)의 차이 · 두 판 동시 설치 불가 · 설치 파일 직접 링크 go.microsoft.com/fwlink/?linkid=2102613.
[^ext]: **Install Power Automate browser extensions** — Microsoft Learn. <https://learn.microsoft.com/power-automate/desktop-flows/install-browser-extensions> (2026-10-05 확인). PAD v2.27 이상용 Edge 확장 링크 · 설치 마지막 화면의 확장 설치 안내.
[^start]: **회사 또는 학교 계정으로 시작하기** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/getting-started-freeorg> (2026-10-02 확인). 콘솔의 새 흐름 단추 · 흐름 이름 입력 후 만들기 · 디자이너의 실행과 저장.
[^designer]: **흐름 디자이너** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/flow-designer> (2026-10-02 확인). 작업 창 · 작업 영역 · 변수 창이라는 영역 이름.
[^variables]: **변수 작업** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/variables> (2026-10-02 확인). 작업 이름 변수 설정 · 새 목록 만들기 · 목록에 항목 추가. 목록에 항목을 넣으려면 먼저 목록 변수가 있어야 한다는 것.
[^datatypes]: **변수 데이터 형식** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/variable-data-types> (2026-10-02 확인). For each 로 데이터 테이블을 돌 때 현재 항목이 데이터 행이고, `%VariableName['ColumnName']%` 로 열 값을 읽는다는 것.
[^display]: **메시지 상자 작업** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/display> (2026-10-02 확인). 작업 이름 메시지 표시 · 입력 대화 표시와 생성 변수 `UserInput` · `ButtonPressed`.
[^conditionals]: **조건부 작업** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/conditionals> (2026-10-02 확인). If 의 첫 번째·두 번째 피연산자와 연산자 같음(=). 한국어판은 Else 를 「그 밖의 경우」로 적는다.
[^loops]: **루프 작업** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/loops> (2026-10-02 확인). Loop 의 시작·증분·끝과 현재 인덱스 변수, For each 의 반복할 값과 현재 항목 변수. 한국어판은 Loop 를 「반복」, For each 를 「각각에 대해」로 적는다.
[^folder]: **폴더 작업** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/folder> (2026-10-02 확인). 폴더 만들기의 위치·이름 매개 변수, 폴더의 파일 가져오기의 파일 필터 와일드카드와 생성 변수 `Files`.
[^file]: **파일 작업** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/file> (2026-10-02 확인). 작업 이름 파일 이동, 이동할 파일에 파일 변수 하나 또는 파일 목록을 넣을 수 있다는 것.
[^excel]: **Excel 작업** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/excel> (2026-10-02 확인). Excel 실행의 문서 열기와 생성 변수 `ExcelInstance`, Excel 워크시트에서 읽기의 「범위의 첫 줄에 열 이름 포함」 옵션과 생성 변수 `ExcelData`, Excel 닫기의 저장 선택지.
