---
title: "P10. 인스턴스"
parent: "개념 6. 웹과 UI 요소"
nav_order: 10
concept:
  id: P10
  grade: A
  used_in: "Lab 4 ⑥ Excel · Lab 5 ② 브라우저 열기 · ⑤ Excel 저장 · ⑥ 마무리 · Lab 6 ② 조건 읽기 · ③ 결과 파일 · ⑦ 저장과 알림 · Lab 7 ③ 요청 읽기 · ⑥ 마무리"
  tokens: ["ExcelInstance", "%Browser%", "Excel 인스턴스", "웹 브라우저 인스턴스", "결과엑셀", "요청엑셀"]
  sample: true
---

# P10. 인스턴스

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. 값은 make_data.py 와 C:\PA실습 의 파일에서 옮겼다(거래처목록 A1 거래처명, 발굴조건 A1 키워드).
     ⚠️ 실측할 것: 닫은 Excel 인스턴스를 읽을 때의 오류 문구(문서에는 작업별 예외 이름만 있다), 브라우저를 닫은 뒤 %Browser.IsAlive% 값,
        「창 가져오기」 「실행 중인 Excel에 첨부」 「Outlook 시작」 라벨(랩에 없어 한국어판 문서를 따랐다), 새 Microsoft Edge 시작의 「실행 중인 인스턴스에 연결」 라벨 -->

> **다루는 것**: 열어 둔 브라우저 · 창 · Excel 을 가리키는 변수와 시작 · 사용 · 닫기의 짝
>
> **쓰는 곳**: Lab 4 `%ExcelInstance%` · Lab 5 `%Browser%` · Lab 6 `%결과엑셀%` · Lab 7 `%요청엑셀%`

---

## 인스턴스가 담는 것

인스턴스는 열려 있는 대상을 가리키는 자료형입니다.[^types] 시작 작업이 변수로 만들고, 뒤의 작업은 칸에 이 변수를 받아 어느 대상을 다룰지 정합니다.

| 인스턴스 | 만드는 작업 | 기본 변수 이름 | 받는 작업 | 닫는 작업 |
|---|---|---|---|---|
| 웹 브라우저 인스턴스 | 새 Microsoft Edge 시작 · 새 Chrome 시작 · 새 Firefox 시작 | `Browser` | 브라우저 자동화 작업 | 웹 브라우저 닫기 |
| 웹 브라우저 인스턴스(새 탭) | 새 탭 만들기 | `NewBrowser` | 브라우저 자동화 작업 | 웹 브라우저 닫기 |
| 창 인스턴스 | 창 가져오기 | `AutomationWindow` | 창을 인스턴스로 찾는 UI 자동화 작업 | 창 닫기 |
| Excel 인스턴스 | Excel 시작 · 실행 중인 Excel에 첨부 | `ExcelInstance` | Excel 작업 | Excel 닫기 |
| Outlook 인스턴스 | Outlook 시작 | `OutlookInstance` | Outlook 작업 | Outlook 닫기 |

**웹 페이지에서 데이터 추출**을 Excel 스프레드시트 저장으로 두면 이 작업도 `ExcelInstance` 를 만듭니다.[^web]

---

## 시작 · 사용 · 닫기

세 묶음 모두 시작 작업 → 다루는 작업 → 닫는 작업 순서입니다. 다루는 작업마다 같은 인스턴스 변수가 들어갑니다.

```
Excel 시작                       및 다음 문서 열기 → %ExcelInstance%
Excel 워크시트에서 읽기           Excel 인스턴스 = %ExcelInstance%
Excel 닫기                       Excel 인스턴스 = %ExcelInstance%
```

```
새 Microsoft Edge 시작           이니셜 URL → %Browser%
웹 페이지 버튼 누르기             웹 브라우저 인스턴스 = %Browser%
웹 브라우저 닫기                 웹 브라우저 인스턴스 = %Browser%
```

닫는 작업이 없으면 흐름이 끝나도 창이 그대로 남습니다.[^lab]

---

## 둘 이상 열 때

같은 시작 작업을 두 번 놓으면 변수 이름에 번호가 붙어 `ExcelInstance` · `ExcelInstance2` 가 됩니다.[^lab] 구분하기 쉽도록 **변수 생성됨**에서 이름을 바꿉니다. 변수 이름에는 한글도 쓸 수 있습니다.

다루는 작업을 새로 놓으면 인스턴스 칸에 변수 하나가 미리 들어 있습니다. 그 변수가 지금 다룰 대상인지 저장하기 전에 확인합니다.[^lab]

---

## 새로 열기와 연결

| 대상 | 새로 열기 | 열려 있는 대상에 연결 |
|---|---|---|
| Edge | 시작 모드 새 인스턴스 시작 | 시작 모드 실행 중인 인스턴스에 연결. 탭 제목 · 탭 URL · 전경 창으로 찾음 |
| Excel | Excel 시작 | 실행 중인 Excel에 첨부. 문서 이름이나 경로로 찾음 |
| 창 | 응용 프로그램 실행으로 앱을 띄운 뒤 창 가져오기 | 창 가져오기. 특정 창 또는 전경 창 |

브라우저 자동화는 Power Automate 를 실행한 Windows 사용자와 다른 사용자로 연 브라우저에는 연결하지 못합니다.[^autoweb] 브라우저 쪽 칸은 [P13](p13-web-structure.html), Excel 쪽 칸은 [P14](p14-excel.html)에서 다룹니다.

---

## 인스턴스의 속성

인스턴스 변수에도 `%변수.속성%` 표기가 됩니다.[^props]

| 표기 | 값 |
|---|---|
| `%Browser.IsAlive%` | 브라우저 창이 열려 있으면 True, 아니면 False |
| `%Browser.Handle%` | 브라우저 인스턴스의 핸들 |
| `%Browser.DisplayRectangleX%` · `%Browser.DisplayRectangleY%` | 창 왼쪽 위 모서리의 x · y 위치 |
| `%Browser.HtmlDialogs%` | 현재 페이지의 대화 상자 |
| `%ExcelInstance.Handle%` | Excel 인스턴스의 핸들 |
| `%AutomationWindow.Handle%` | 창 인스턴스의 핸들 |

---

## 흔한 실패

| 증상 | 원인 | 고치는 방법 |
|---|---|---|
| 쓰려던 파일이 아닌 파일을 다룸 | 인스턴스 칸의 기본 변수를 그대로 둠 | 칸을 그 파일의 인스턴스로 바꿈 |
| 다루는 작업이 실패함 | 인스턴스를 이미 닫은 줄 뒤에 작업을 둠 | 닫는 줄을 뒤로 옮기거나 열려 있는 인스턴스로 바꿈 |
| 파일이 읽기 전용으로 열림 | 흐름이 열 파일이 이미 열려 있음 | 실행 전에 그 파일의 Excel 창을 닫음 |
| 실행 뒤 창이 쌓임 | 닫는 작업이 없거나 중간 실행이 닫는 줄 앞에서 끝남 | 닫는 작업을 두거나 남은 창을 손으로 닫음 |

---

## 샘플

흐름 `개념 연습_HGD` 를 씁니다. 없으면 [P2](p02-types.html)의 1·2번으로 만듭니다.

1. Power Automate 콘솔에서 `개념 연습_HGD` 의 **편집**을 눌러 디자이너를 엽니다.
2. 작업 영역의 빈 곳을 한 번 누르고 `Ctrl` + `A` 를 누른 뒤 `Delete` 를 눌러 **Main** 의 줄을 지웁니다.
3. 작업 검색 칸에 `Excel 시작` 을 입력하고 **Excel 시작**을 작업 영역으로 끌어다 놓습니다. **및 다음 문서 열기**로 바꾸고 **문서 경로**에 아래를 넣은 뒤 **저장**을 누릅니다.

    ```
    C:\PA실습\거래처목록.xlsx
    ```

4. **Excel 시작**을 1번 줄 아래로 하나 더 놓습니다. **및 다음 문서 열기**로 바꾸고 **문서 경로**에 아래를 넣습니다.

    ```
    C:\PA실습\발굴조건.xlsx
    ```

5. **변수 생성됨**의 `ExcelInstance2` 를 눌러 아래로 바꾸고 **저장**을 누릅니다.

    ```
    조건엑셀
    ```

6. 작업 검색 칸에 `Excel 워크시트에서 읽기` 를 입력하고 **Excel 워크시트에서 읽기**를 2번 줄 아래로 끌어다 놓습니다. **Excel 인스턴스**를 `%ExcelInstance%` 로 둡니다. **검색**은 **단일 셀의 값**으로 두고 **시작 열** · **시작 행**에 아래를 차례로 넣습니다.

    ```
    A
    ```

    ```
    1
    ```

7. **변수 생성됨**의 `ExcelData` 를 아래로 바꾸고 **저장**을 누릅니다.

    ```
    첫셀1
    ```

8. **Excel 워크시트에서 읽기**를 3번 줄 아래로 하나 더 놓습니다. **Excel 인스턴스**를 `%조건엑셀%` 로 바꿉니다. 칸은 6번과 같이 **단일 셀의 값** · `A` · `1` 로 둡니다.
9. **변수 생성됨**의 이름을 아래로 바꾸고 **저장**을 누릅니다.

    ```
    첫셀2
    ```

10. 작업 검색 칸에 `Excel 닫기` 를 입력하고 **Excel 닫기**를 4번 줄 아래로 놓습니다. **Excel 인스턴스**를 `%ExcelInstance%` 로 두고 **Excel을 닫기 전**이 **문서 저장 안 함**인지 확인한 뒤 **저장**을 누릅니다.
11. **Excel 닫기**를 하나 더 놓고 **Excel 인스턴스**를 `%조건엑셀%` 로 바꾼 뒤 **저장**을 누릅니다.
12. 도구 모음의 **실행**(▶)을 누릅니다.
13. 오른쪽 세로 막대의 **{x}** 를 눌러 변수 창을 엽니다.

    **완료 기준**: `첫셀1` 은 `거래처명`, `첫셀2` 는 `키워드` 다. 같은 작업이 인스턴스 칸에 따라 다른 파일을 읽었다.

14. **Excel 워크시트에서 읽기**를 맨 아래로 놓습니다. **Excel 인스턴스**를 `%조건엑셀%` 로 바꾸고 **저장**을 누릅니다.
15. **실행**(▶)을 누릅니다.

    **완료 기준**: 맨 아래 줄에서 오류가 나고 실행이 멈춘다. 그 인스턴스는 바로 위 줄에서 닫혔다.

16. 맨 아래 줄을 누르고 `Delete` 를 누릅니다.
17. 작업 검색 칸에 `Edge` 를 입력하고 **브라우저 자동화** 아래 **새 Microsoft Edge 시작**을 맨 아래로 놓습니다. **이니셜 URL**에 아래를 넣고 **저장**을 누릅니다.

    ```
    {{ site.url }}{{ site.baseurl }}/practice/bid/
    ```

18. 작업 검색 칸에 `변수 설정` 을 입력하고 **변수 설정**을 맨 아래로 놓습니다. **변수**와 **값**에 아래를 차례로 넣고 **저장**을 누릅니다.

    ```
    닫기전
    ```

    ```
    %Browser.IsAlive%
    ```

19. 작업 검색 칸에 `브라우저 닫기` 를 입력하고 **웹 브라우저 닫기**를 맨 아래로 놓습니다. **웹 브라우저 인스턴스**가 `%Browser%` 인지 확인하고 **저장**을 누릅니다.
20. **변수 설정**을 맨 아래로 놓고 아래를 차례로 넣은 뒤 **저장**을 누릅니다.

    ```
    닫은뒤
    ```

    ```
    %Browser.IsAlive%
    ```

21. **실행**(▶)을 누르고 변수 창을 봅니다.

    **완료 기준**: `닫기전` 은 `True`, `닫은뒤` 는 `False` 다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: 변수 데이터 형식[^types] · 변수 데이터 형식 속성[^props] · Excel 작업[^excel] · 브라우저 자동화 작업[^web] · 웹 페이지 자동화[^autoweb] · UI 자동화 작업[^ui] · Outlook 작업[^outlook] · 이 과정의 실측 기록[^lab]

[^types]: **Variable data types** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/variable-data-types> (2026-11-02 확인). 인스턴스 네 종류와 각각을 만드는 작업.
[^props]: **Variable data type properties** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/datatype-properties> (2026-11-02 확인). 웹 브라우저 · 창 · Excel 인스턴스의 속성.
[^excel]: **Excel actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/excel> (2026-11-02 확인). Excel 시작 · 실행 중인 Excel에 첨부 · Excel 닫기의 칸과 생성 변수 `ExcelInstance`. 인스턴스가 여러 파일 중 어느 것을 다룰지 정한다는 것.
[^web]: **Browser automation actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/webautomation> (2026-11-02 확인). 브라우저 시작 작업과 생성 변수 `Browser`, 새 탭 만들기의 `NewBrowser`, 데이터 추출의 Excel 저장이 만드는 `ExcelInstance`, 웹 브라우저 닫기.
[^autoweb]: **Automate webpages** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/automation-web> (2026-11-02 확인). 브라우저 인스턴스를 먼저 만들어야 한다는 것, 다른 시스템 사용자로 연 브라우저에 연결하지 못한다는 것.
[^ui]: **UI automation actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/uiautomation> (2026-11-02 확인). 창 가져오기의 특정 창 · 전경 창과 생성 변수 `AutomationWindow`, 창 닫기의 창 인스턴스 찾기.
[^outlook]: **Outlook actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/outlook> (2026-11-02 확인). Outlook 시작 · Outlook 닫기와 생성 변수 `OutlookInstance`.
[^lab]: **이 과정의 실측 기록** — Lab 5 10 · 19번, Lab 6 15 · 25 · 32 · 50번(2026-10-05 · 06 실측). 닫는 작업이 없을 때 창이 남는 것, `ExcelInstance2` 번호 붙음, 인스턴스 칸의 기본값, 열린 파일이 읽기 전용으로 열릴 수 있다는 것.
