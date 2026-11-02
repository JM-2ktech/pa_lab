---
title: "P16. 대기와 시간 제한"
parent: "개념 6. 웹과 UI 요소"
nav_order: 16
concept:
  id: P16
  grade: B
  used_in: "Lab 5 ③ 입력과 검색 15번 고급 · ④ 표 추출 27 · 28번 · Lab 6 ⑧ 오류 대비 · Lab 7 ② 앱 실행과 로그온 10번"
  tokens: ["응용 프로그램 로드 대기", "페이지가 로드될 때까지 대기", "재시도 정책", "시간 제한"]
  sample: true
---

# P16. 대기와 시간 제한

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. 숨김판 practice/bid/hide.html 은 마지막 쪽 단추를 display:none + disabled 로 남긴다. :not([disabled]) 는 2026-10-06 실측으로 선택기에서 동작했다. 페이지 선택기 칸에 넣어 멈추는지는 이 샘플로 처음 확인한다.
     ⚠️ 문서와 실측이 다른 곳: 데이터 추출의 Timeout 은 문서에 60초에 실패한다고 적혀 있다. Lab 5 28번 첫 실행은 3분 넘게 멈추지 않았다. 숨김판에서 60초 뒤 실패하는지 샘플에서 확인한다.
     ⚠️ 실측할 것: 웹 페이지 콘텐츠 대기 · 창 콘텐츠 대기 · 창 대기 · 파일 대기 대화 상자에 시간 초과 칸이 있는지(문서의 매개 변수 표에 없다. 이미지 대기 · 프로세스 대기 · 화면의 텍스트 대기는 표에 있다),
        「웹 페이지 콘텐츠 대기」 「웹 페이지가」 칸 라벨, 「중지」 단추의 동작, 「시간 제한」 칸의 라벨(문서는 Timeout 을 「시간 초과」 또는 「시간 제한」으로 섞어 적는다), 흐름 속성의 「흐름 시간 제한」 라벨(한국어판 콘솔 문서가 「흐름 시간 초과」 「흐름 시간 제한」을 섞어 적는다), 라이브 웹 도우미 고급 설정의 페이지 선택기 칸 라벨,
        응용 프로그램 실행의 시간 제한 0 의 뜻(문서는 최대 대기 시간이라고만 적었다), 「응용 프로그램 완료 대기」 라벨. 「흐름이 쪽을 넘기는」 구조는 문서에도 랩에도 실행 예가 없다(저작 메모 근거만 있다) -->

> **다루는 것**: 대기 작업의 종류, 작업에 딸린 대기와 시간 제한, 페이지 선택기가 멈추지 않은 사례, 흐름 시간 제한, 구성 파일
>
> **쓰는 곳**: Lab 5 페이지가 로드될 때까지 대기 · 웹 페이지 로드 시간 제한 60 · Lab 6 재시도 정책 고정 2회 · Lab 7 응용 프로그램 로드 대기

---

## 기다리는 세 가지 방식

| 방식 | 작업 | 끝나는 조건 |
|---|---|---|
| 정한 시간만큼 | 대기 | 지정한 초가 지남 |
| 조건이 될 때까지 | 웹 페이지 콘텐츠 대기 등 | 텍스트 · 요소 · 창이 나타나거나 사라짐 |
| 작업에 딸린 대기 | 페이지가 로드될 때까지 대기 등 | 페이지 로드 완료 또는 시간 제한 |

문서는 조건 대기에 시간 제한을 두어 쓰고, 일반 **대기**는 피하라고 권합니다.[^perf]

---

## 대기 작업

| 작업 | 묶음 | 기다리는 것 | 문서에 있는 시간 칸 |
|---|---|---|---|
| 대기 | 흐름 제어 | 지정한 초 | 지속 시간 |
| 웹 페이지 콘텐츠 대기 | 브라우저 자동화 | 페이지에 요소 · 텍스트가 나타나거나 사라짐 | 없음 |
| 창 콘텐츠 대기 | UI 자동화 | 창에 요소 · 텍스트가 나타나거나 사라짐. 요소의 사용 · 사용 안 함 상태 | 없음 |
| 창 대기 | UI 자동화 | 창이 열림 · 닫힘 · 포커스를 얻음 · 잃음 | 없음 |
| 이미지 대기 | UI 자동화 | 이미지가 나타나거나 사라짐 | 시간 제한 오류로 실패 |
| 프로세스 대기 | 시스템 | 프로세스가 시작되거나 멈춤 | 시간 제한 오류로 실패 |
| 파일 대기 | 파일 | 파일이 만들어지거나 지워짐 | 없음 |
| 화면에서 텍스트 대기(OCR) | OCR | 화면에 텍스트가 나타나거나 사라짐 | 시간 제한 오류로 실패 |
| 바로 가기 키 대기 | 마우스 및 키보드 | 지정한 키 입력 | 시간 초과 때 흐름 계속 |

웹 페이지 콘텐츠 대기는 대상 칸을 네 가지 중에서 고릅니다.[^web]

| 웹 페이지가 | 넣는 칸 |
|---|---|
| 요소 포함 | UI 요소 |
| 요소를 포함하지 않음 | UI 요소 |
| 텍스트 포함 | 텍스트 |
| 텍스트가 포함되지 않음 | 텍스트 |

**시간 제한 오류로 실패**를 켜면 정한 시간이 지난 뒤 작업이 실패합니다. 끄면 작업은 조건이 될 때까지 끝없이 기다립니다.[^ui]

---

## 작업에 딸린 대기와 시간 제한

대기 작업을 따로 두지 않아도 작업 자체에 대기가 있습니다. 시간 칸의 단위는 초입니다.

| 작업 | 칸 | 기본값 | 시간이 지나면 |
|---|---|---|---|
| 새 Microsoft Edge 시작 | 페이지가 로드될 때까지 대기 | 켬 | — |
| 새 Microsoft Edge 시작 · 웹 양식 작업 · 웹 페이지로 이동 · 링크 클릭 | 웹 페이지 로드 시간 제한 | 60 | 작업 오류 |
| 새 Microsoft Edge 시작 | 시간 제한 | 60 | 브라우저 시작 실패 |
| 웹 페이지에서 데이터 추출 | 시간 제한 | 60 | 추출 실패 |
| 창 가져오기 | 창을 찾을 수 없으면 실패 · 시간 제한 | 켬 · 없음 | 작업 실패. 끄면 나타날 때까지 기다림 |
| 응용 프로그램 실행 | 응용 프로그램 시작 후 · 시간 제한 | 즉시 계속 · 0 | 시간이 지나면 다음 작업으로 진행 |

응용 프로그램 실행의 **응용 프로그램 시작 후**는 즉시 계속 · 응용 프로그램 로드 대기 · 응용 프로그램 완료 대기 세 값입니다.[^sys]

---

## 재시도

요소가 늦게 나타나 작업이 실패할 때는 재시도를 설정할 수 있습니다. 대화 상자 왼쪽 아래 **오류**를 눌러 재시도 정책을 고릅니다.[^lab] 문서의 기본값은 2초 간격 1회입니다.[^err] 오류 처리 전체는 [P18](p18-errors.html)에서 다룹니다.

---

## 페이지 선택기가 멈추지 않은 사례

**웹 페이지에서 데이터 추출**의 페이지 선택기는 다음 쪽 요소를 찾지 못해야 멈춥니다. 모의 사이트를 고치며 실측한 결과입니다.[^lab]

| 사이트 상태 | 결과 |
|---|---|
| 마지막 쪽 다음 단추가 `disabled` 로 남고, 화면 안에서 표만 바뀜 | PAD 가 계속 눌러 3분 넘게 멈추지 않음. `DataFromWebPage` 비어 있음 |
| 마지막 쪽 다음 단추를 `display:none` 으로 숨김 | PAD 가 요소를 찾아 계속 누름 |
| 마지막 쪽 다음 단추를 문서에서 지우고, 쪽마다 주소를 바꿔 새로 엶 | 2쪽까지 읽고 멈춤. 16행 |

첫째 실행에서 추출 작업의 시간 제한 60 은 실행을 멈추지 못했습니다. 문서에는 60초 뒤 작업이 실패한다고 적혀 있습니다.[^web]

사이트의 단추는 흐름 쪽에서 고칠 수 없습니다. 상태에 따라 대응이 나뉩니다.[^lab]

| 사이트 상태 | 대응 |
|---|---|
| 마지막 쪽 단추에 `disabled` 가 있음 | 페이지 선택기에 `:not([disabled])` 를 붙임 |
| 마지막 쪽 단추를 숨기기만 함 | 페이지 선택기를 쓰지 않고 흐름이 쪽을 넘김 |

흐름이 쪽을 넘길 때는 첫 번째만 읽는 추출을 반복 안에 두고, 쪽 표시를 읽어 마지막 쪽이면 반복을 끝냅니다. 반복의 종료는 [P8](p08-loops.html)에서 다룹니다.

선택기 표현의 동작 여부는 [P12](p12-selectors.html)의 연산자 절에 있습니다.

---

## 흐름 시간 제한

흐름 전체의 실행 시간에 상한을 두는 속성입니다. 기본값은 꺼짐입니다.[^con]

| 항목 | 내용 |
|---|---|
| 여는 곳 | 콘솔에서 흐름을 오른쪽 단추 › 속성 › 일반 탭 |
| 값 | 정수와 시간 단위(초 · 분 · 시간) |
| 적용 범위 | 콘솔 또는 클라우드에서 시작한 실행 |
| 넘으면 | 흐름이 멈추고 시간 초과로 끝남 |
| 조건 | 회사 또는 학교 계정. Power Automate v2 스키마에 저장된 흐름 |

---

## 구성 파일로 바꾸는 시간 제한

PAD 구성 요소끼리 통신하는 시간 제한은 구성 파일로 바꿉니다. 요소를 잡거나 작업을 실행할 때 오래 걸리다 실패하면 씁니다.[^cfg]

| 키 | 대상 | 쓰는 경우 |
|---|---|---|
| `AutomationServerEndpoint.DesignTime.ConnectionTimeout` | 디자이너 · 기록기가 자동화 서버에 연결 | 설계 중 연결 오류 |
| `AutomationServerEndpoint.DesignTime.CallTimeout` | 디자이너 · 기록기의 메시지 주고받기 | 요소를 잡는 데 너무 오래 걸림 |
| `AutomationServerEndpoint.Runtime.ConnectionTimeout` | 실행 로봇이 자동화 서버에 연결 | 실행 중 연결 오류 |
| `AutomationServerEndpoint.Runtime.CallTimeout` | 실행 로봇의 메시지 주고받기 | 작업 실행이 오래 걸려 시간 초과로 실패 |
| `AutomationServerEndpoint.ExtractDataFromWeb.ConnectTimeout` | 데이터 추출 모듈의 연결 | 추출 대상을 잡을 때 연결 오류 |
| `AutomationServerEndpoint.ExtractDataFromWeb.CallTimeout` | 데이터 추출 모듈의 메시지 | 오류 없이 요소가 잡히지 않음 |
| `WebExtensionsMessageProxy.OpenTimeout` · `SendTimeout` | 브라우저 확장 메시지 호스트 | 브라우저 연결 · 전송 오류 |
| `Recorder.LaunchBrowserTimeout` | 기록기의 브라우저 시작 | 확장 설치 팝업 문제 |

SAP · Java · 원격 데스크톱용 키도 있습니다. 문서의 표에서 찾습니다.[^cfg]

| 순서 | 할 일 |
|---|---|
| 1 | PAD 와 관련 프로세스를 모두 끔. `PAD.BrowserNativeMessageHost` 를 끄려면 확장을 끄고 브라우저 창을 모두 닫음 |
| 2 | `%LOCALAPPDATA%\Microsoft\Power Automate Desktop\Configurations` 폴더가 없으면 만듦 |
| 3 | 그 안에 `UIAutomationTimeOut.config` 를 만듦 |
| 4 | `appSettings` 안에 키와 값을 넣음. 값 형식은 `HH:MM:SS` |
| 5 | 저장하고 PAD 를 엶 |

```
<?xml version="1.0" encoding="utf-8" ?>
<configuration>
  <appSettings>
    <add key="AutomationServerEndpoint.Runtime.CallTimeout" value="00:05:00" />
  </appSettings>
</configuration>
```

이 과정의 랩과 샘플은 이 파일을 쓰지 않습니다.

---

## 흔한 실패

| 증상 | 원인 | 고치는 방법 |
|---|---|---|
| 흐름이 끝나지 않음 | 대기 조건이 맞지 않음 | 중지하고 조건의 글자와 요소를 확인. 시간 제한 칸이 있으면 켬 |
| 실행 환경이 바뀌면 실패함 | 일반 대기의 초 수가 페이지 속도와 맞지 않음 | 조건 대기로 바꿈 |
| 데이터 추출이 끝나지 않음 | 마지막 쪽에 다음 요소가 남음 | 사례 절의 대응을 씀 |
| 요소를 찾지 못한다는 오류가 간헐적으로 남 | 요소가 나타나기 전에 작업이 실행됨 | 앞에 조건 대기를 두거나 재시도를 설정함 |
| 페이지 로드 시간 초과 오류 | 페이지가 시간 안에 로드되지 않음 | 웹 페이지 로드 시간 제한을 늘림 |
| 앱 창이 뜨기 전에 다음 줄이 실패함 | 응용 프로그램 실행이 즉시 계속 | 응용 프로그램 로드 대기로 바꿈 |

---

## 샘플

흐름 `개념 연습_HGD` 를 씁니다. 없으면 [P2](p02-types.html)의 1·2번으로 만듭니다.

1. Power Automate 콘솔에서 `개념 연습_HGD` 의 **편집**을 눌러 디자이너를 엽니다.
2. 작업 영역의 빈 곳을 한 번 누르고 `Ctrl` + `A` 를 누른 뒤 `Delete` 를 눌러 **Main** 의 줄을 지웁니다.
3. Edge 주소창에 아래 주소를 넣고 엽니다. 이 창은 닫지 않습니다.

    ```
    {{ site.url }}{{ site.baseurl }}/practice/bid/
    ```

4. 작업 검색 칸에 `Edge` 를 입력하고 **새 Microsoft Edge 시작**을 작업 영역으로 끌어다 놓습니다. **이니셜 URL**에 아래를 넣습니다.

    ```
    {{ site.url }}{{ site.baseurl }}/practice/bid/
    ```

5. **고급**을 펼칩니다.

    **완료 기준**: **페이지가 로드될 때까지 대기**가 켜져 있고 **웹 페이지 로드 시간 제한**이 `60` 이다.

6. **저장**을 누릅니다. 작업 검색 칸에 `텍스트 필드` 를 입력하고 **웹 페이지의 텍스트 필드 채우기**를 1번 줄 아래로 끌어다 놓습니다.
7. **UI 요소** 드롭다운에서 **UI 요소 추가**를 누릅니다. 3번의 Edge 창에서 **공고명** 입력칸을 `Ctrl` + 왼쪽 클릭합니다.
8. **텍스트**에 아래를 넣습니다. **고급**의 **물리적 키 입력을 사용하여 텍스트 채우기**를 끄고 **저장**을 누릅니다.

    ```
    교육
    ```

9. 작업 검색 칸에 `버튼` 을 입력하고 **웹 페이지 버튼 누르기**를 2번 줄 아래로 끌어다 놓습니다. **UI 요소 추가**로 **검색** 단추를 잡고 **저장**을 누릅니다.
10. 작업 검색 칸에 `콘텐츠 대기` 를 입력하고 **웹 페이지 콘텐츠 대기**를 3번 줄 아래로 끌어다 놓습니다. **웹 페이지가**를 **텍스트 포함**으로 바꾸고 **텍스트**에 아래를 넣은 뒤 **저장**을 누릅니다.

    ```
    검색 결과 16건
    ```

11. 도구 모음의 **실행**(▶)을 누릅니다.

    **완료 기준**: 네 줄이 오류 없이 끝난다.

12. 흐름이 연 Edge 창을 닫습니다. 4번 줄을 두 번 클릭해 열고 **텍스트**를 아래로 바꾼 뒤 **저장**을 누릅니다.

    ```
    검색 결과 99건
    ```

13. **실행**(▶)을 누르고 20초 동안 봅니다.

    **완료 기준**: 4번 줄에서 실행이 멈춰 있고 끝나지 않는다.

14. 도구 모음의 **중지**를 누르고 흐름이 연 Edge 창을 닫습니다.
15. 작업 영역의 빈 곳을 한 번 누르고 `Ctrl` + `A` 를 누른 뒤 `Delete` 를 눌러 **Main** 의 줄을 지웁니다.
16. 3번의 Edge 창 주소창에 아래 주소를 넣고 엽니다. 마지막 쪽 단추를 지우지 않고 숨기는 판입니다.

    ```
    {{ site.url }}{{ site.baseurl }}/practice/bid/hide.html?q=교육
    ```

17. **새 Microsoft Edge 시작**을 작업 영역으로 끌어다 놓습니다. **이니셜 URL**에 아래를 넣고 **저장**을 누릅니다.

    ```
    {{ site.url }}{{ site.baseurl }}/practice/bid/hide.html?q=교육
    ```

18. 작업 검색 칸에 `데이터 추출` 을 입력하고 **웹 페이지에서 데이터 추출**을 1번 줄 아래로 끌어다 놓습니다. 대화 상자를 열어 둔 채 3번의 Edge 창을 앞으로 가져옵니다.
19. 표의 **공고번호** 머리글에서 마우스 오른쪽 단추를 누르고 **전체 HTML 테이블 추출**을 고릅니다.
20. 표 아래 **다음** 단추에서 마우스 오른쪽 단추를 누르고 **요소를 페이지 선택기로 설정**을 고릅니다. **완료**를 누릅니다.
21. **데이터 추출**을 **사용 가능한 모든 항목**으로 바꾸고 **저장**을 누릅니다.
22. **실행**(▶)을 누르고 30초 동안 흐름이 연 Edge 창을 봅니다.

    **완료 기준**: 창이 「2 / 2」에 머물고 실행이 끝나지 않는다.

23. 도구 모음의 **중지**를 누르고 흐름이 연 Edge 창을 닫습니다.
24. 2번 줄을 두 번 클릭해 엽니다. 3번의 Edge 창을 앞으로 가져옵니다. 라이브 웹 도우미의 **고급 설정**에서 페이지 선택기 값을 아래로 바꿉니다.

    ```
    button[id="btnNext"]:not([disabled])
    ```

25. **완료**를 누르고 대화 상자의 **저장**을 누릅니다.
26. **실행**(▶)을 누릅니다. 끝나면 오른쪽 세로 막대의 **{x}** 를 눌러 변수 창을 엽니다.

    **완료 기준**: 창이 「2 / 2」에서 실행이 끝나고 `DataFromWebPage` 옆에 `16개 행, 8 열` 이 보인다.

27. 흐름이 연 Edge 창을 닫습니다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: 흐름 성능 최적화[^perf] · UI 및 브라우저 자동화의 시간 제한 구성[^cfg] · Power Automate 콘솔[^con] · 브라우저 자동화 작업[^web] · UI 자동화 작업[^ui] · 시스템 작업[^sys] · 파일 작업[^file] · OCR 작업[^ocr] · 마우스 및 키보드 작업[^mk] · 흐름 제어 작업[^flow] · 오류 처리[^err] · 이 과정의 실측 기록[^lab]

[^perf]: **Optimize flow performance** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/desktop-flow-coding-guidelines/optimize-flow-performance> (2026-11-02 확인). 대기 작업에 시간 제한을 두어 쓰고 일반 대기를 피하라는 권고, 흐름 시간 제한 속성.
[^cfg]: **Timeout configuration for UI and browser automation** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/how-to/ui-automation-change-timeout-configuration> (2026-11-02 확인). 구성 파일 위치와 절차, 키와 쓰는 경우, 값 형식. 키와 XML 은 영어판에서 옮겼다.
[^con]: **Power Automate console** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/console> (2026-11-02 확인). 흐름 속성의 흐름 시간 제한, 값 형식, 적용 범위, 계정과 스키마 조건.
[^web]: **Browser automation actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/webautomation> (2026-11-02 확인). 웹 페이지 콘텐츠 대기의 칸, 페이지 로드 대기와 시간 제한의 기본값, 데이터 추출의 시간 제한.
[^ui]: **UI automation actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/uiautomation> (2026-11-02 확인). 창 콘텐츠 대기 · 창 대기 · 이미지 대기의 칸, 시간 제한 오류로 실패, 창 가져오기의 칸.
[^sys]: **System actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/system> (2026-11-02 확인). 프로세스 대기, 응용 프로그램 실행의 시작 후 동작과 시간 제한.
[^file]: **File actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/file> (2026-11-02 확인). 파일 대기의 칸.
[^ocr]: **OCR actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/ocr> (2026-11-02 확인). 화면에서 텍스트 대기의 칸.
[^mk]: **Mouse and keyboard actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/mouseandkeyboard> (2026-11-02 확인). 바로 가기 키 대기의 칸.
[^flow]: **Flow control actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/flowcontrol> (2026-11-02 확인). 대기의 지속 시간.
[^err]: **Handle errors in desktop flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/errors> (2026-11-02 확인). 작업 재시도의 기본값.
[^lab]: **이 과정의 실측 기록** — Lab 5 15 · 27 · 28번, Lab 6 46~48번, Lab 7 10번, 모의 공고 사이트(2026-10-05 · 06 실측). 페이지 선택기가 멈추지 않은 사례와 대응, 재시도 정책의 화면, 응용 프로그램 로드 대기.
