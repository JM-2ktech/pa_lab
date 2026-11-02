---
title: "P28. 웹 자동화 사례 모음"
parent: "더 읽을거리 · PAD"
nav_order: 28
concept:
  id: P28
  grade: C
  used_in: "랩에서 쓰지 않음"
  tokens: []
  sample: true
---

# P28. 웹 자동화 사례 모음

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행.
     ⚠️ 실측할 것: 작업 이름. 한국어판 how-to 는 「웹 페이지에서 요소의 세부 정보 가져오기」「웹페이지에서 JavaScript 기능 실행」「웹 페이지의 텍스트 필드에 포커스」,
        참조 문서는 「웹 페이지 요소의 세부 정보 가져오기」「웹 페이지에서 JavaScript 함수 실행」「웹 페이지의 텍스트 필드에 포커스 설정」. 본문은 참조 문서를 따랐다.
     ⚠️ 실측할 것: 특성 이름 목록의 HRef 표기와 값. 모의 사이트의 링크는 detail.html?no=… 상대 경로다. 값이 상대 주소로 오면 샘플 6번의 웹 페이지로 이동이 실패한다.
     ⚠️ 실측할 것: 웹 페이지로 이동 「탐색」 칸의 라벨. 한국어판 참조는 forward 를 「전달」로 옮겼다. 본문은 「앞으로」로 적었다.
     ⚠️ 문서 어긋남: 새 탭 how-to 는 자동화 브라우저를 가장 간단한 방법으로 적고, 참조 문서는 같은 옵션을 사용 중단으로 표시한다. 본문은 참조 문서를 따랐다.
     ⚠️ 문서 어긋남: 링크 목록 how-to 의 예시 선택기는 li:eq(0) 인데 바꾸는 설명은 tr:eq(0) 이다. 본문은 :eq(0) 부분을 바꾼다고 적었다.
     ⚠️ 문서 어긋남: 스크롤 how-to 는 scrollTop -= 10 을 「아래로 10픽셀」이라 적는다. 값을 빼는 식과 방향이 맞지 않아 본문에는 방향을 적지 않았다. -->

> **다루는 것**: iframe · 새 탭 · 스크롤 · 브라우저 대화 상자 · 링크 목록 · 페이지 세부 정보 여섯 사례의 문제와 쓰는 작업
>
> **쓰는 곳**: 랩에서 쓰지 않음

---

## 여섯 사례

| 사례 | 문제 | 쓰는 작업 |
|---|---|---|
| iframe | 페이지 안에 다른 HTML 문서가 들어 있음 | 브라우저 자동화 작업 · UI 자동화 작업 · 웹 페이지로 이동 |
| 새 탭을 여는 링크 | 흐름의 브라우저 인스턴스가 새 탭을 가리키지 않음 | 웹 페이지 요소의 세부 정보 가져오기 · 웹 페이지로 이동 · 새 Microsoft Edge 시작 |
| 스크롤 | 대상 요소가 화면 밖에 있음 | 웹 페이지의 텍스트 필드에 포커스 설정 · 웹 페이지에서 JavaScript 함수 실행 |
| 브라우저 대화 상자 | 저장 · 열기 · 업로드 창이 웹 페이지 밖의 창임 | 기록기 · UI 자동화 작업 |
| 링크 목록 | 링크 여러 개를 차례로 눌러야 함 | 웹 페이지에서 데이터 추출 · 반복 · 웹 페이지에서 링크 클릭 · 웹 페이지로 이동 |
| 페이지 세부 정보 | 제목 · 주소 · 본문처럼 페이지 자체의 값이 필요함 | 웹 페이지의 세부 정보 가져오기 |

---

## iframe

iframe 은 HTML 문서 안에 들어 있는 다른 HTML 문서입니다. 외부 콘텐츠를 페이지에 넣을 때 씁니다.[^iframe]

| 상황 | 방법 |
|---|---|
| iframe 이 원래 페이지와 같은 도메인 | 브라우저 자동화 작업을 그대로 씀 |
| 브라우저 자동화 작업이 제대로 동작하지 않음 | UI 자동화 작업으로 처리 |
| iframe 이 다른 도메인 | 웹 페이지 요소의 세부 정보 가져오기로 **소스 링크** 특성을 읽고, 웹 페이지로 이동 또는 새 탭 만들기로 그 주소를 연 뒤 브라우저 자동화 작업을 씀 |

웹 페이지에서 데이터 추출 작업의 **추출 시 데이터 처리**를 켜면 iframe 안의 정보를 표시하고 숨겨진 요소를 거릅니다. 데이터가 크면 추출 시간이 늘어나 문서는 켜지 않기를 권합니다.[^web]

---

## 새 탭을 여는 링크

데스크톱 흐름은 브라우저 인스턴스로 특정 창의 특정 탭에 있는 페이지를 가리킵니다. 링크가 새 탭을 열면 그 탭에서 이어 가기 위한 설정이 더 필요합니다.[^newtab]

| 방법 | 절차 | 조건 |
|---|---|---|
| 주소를 읽어 같은 탭에서 열기 | 웹 페이지 요소의 세부 정보 가져오기의 특성 이름을 `HRef` 로 두고, 결과를 웹 페이지로 이동의 URL 에 넣음 | 링크에 주소가 있을 때 |
| JavaScript 링크 실행 | 링크의 JavaScript 함수를 읽어 웹 페이지로 이동의 URL 에 `JavaScript:` 와 함수를 넣음 | 링크가 JavaScript 로 되어 있을 때 |
| 새 탭에 연결 | 링크를 누른 뒤 브라우저 시작 작업의 시작 모드를 실행 중인 인스턴스에 연결로 둠 | Edge · Internet Explorer · Chrome · Firefox |

**실행 중인 인스턴스에 연결**은 대상 탭을 세 방식으로 고릅니다.[^web]

| 방식 | 고르는 탭 |
|---|---|
| 제목 사용 | 제목 또는 제목의 일부가 맞는 탭 |
| URL 기준 | URL 또는 URL 의 일부가 맞는 탭 |
| 전경 창 사용 | 맨 앞 창의 활성 탭 |

URL 로 연결하면 시간 제한의 절반 동안 정확히 일치하는 탭을 찾고, 남은 시간에는 부분 일치로 찾습니다.[^web]

탭을 흐름에서 직접 열 때는 새 탭 만들기를 씁니다. Edge · Chrome · Firefox 에서 지원하고, 새 탭의 인스턴스는 `NewBrowser` 변수에 담깁니다.[^web]

웹 페이지로 이동은 URL 말고도 뒤로 · 앞으로 · 다시 로드를 고를 수 있습니다.[^web]

자동화 브라우저는 탭이 없어 모든 링크를 같은 인스턴스에서 엽니다.[^newtab] 이 옵션은 사용 중단 예정이고, 참조 문서는 새 자동화에 쓰지 않도록 안내합니다.[^web]

---

## 스크롤

특정 요소까지 내리려면 **웹 페이지의 텍스트 필드에 포커스 설정**을 씁니다. UI 요소 칸에 대상 요소를 지정합니다. 작업 이름은 텍스트 필드이지만 대상은 어떤 요소든 됩니다. 긴 목록 맨 아래의 「더 보기」 요소를 고르면 페이지 끝으로 내려갑니다.[^scroll]

좌표로 움직이려면 웹 페이지에서 JavaScript 함수 실행을 씁니다.[^scroll]

| 목적 | 함수 안의 코드 |
|---|---|
| 좌표로 이동 | `window.scrollTo(xpos, ypos);` |
| 페이지 맨 아래로 이동 | `window.scrollTo(0, document.body.scrollHeight);` |
| 요소 안에서 세로 이동 | `document.getElementById('divElem').scrollTop -= 10;` |

**JavaScript 함수** 칸에는 아래 모양으로 넣습니다. `xpos` · `ypos` 에는 값 · 속성 · 변수를 쓸 수 있습니다.

```
function ExecuteScript()
{
window.scrollTo(0, document.body.scrollHeight);
}
```

이 작업의 조건입니다.[^web][^manifest]

| 항목 | 내용 |
|---|---|
| 결과 | 함수의 반환값이 `Result` 변수에 담김 |
| 개발자 도구 | 브라우저의 개발자 도구가 켜져 있어야 함. 그룹 정책으로 꺼져 있으면 동작하지 않음 |
| Firefox | 이 작업을 쓸 수 없음 |
| 실행 중 표시 | 브라우저에 디버깅 시작 알림이 뜸. 실행 결과에는 영향 없음 |

---

## 브라우저 대화 상자

저장 · 열기 · 업로드 대화 상자는 브라우저나 Windows 파일 탐색기가 띄우는 창입니다. 웹 페이지의 일부가 아니므로 브라우저 자동화 작업으로 다루지 못하고, 기록기나 UI 자동화 작업을 씁니다.[^prompts]

| 창 | 다루는 방법 |
|---|---|
| 저장 · 열기 · 업로드 대화 상자 | 기록기 · UI 자동화 작업 |
| 페이지를 불러오는 중에 뜨는 팝업 대화 | 브라우저 자동화 작업의 **팝업 대화가 표시되는 경우** 칸. 닫기 · 단추 누르기 · 아무 것도 수행하지 않음 |

웹 페이지에서 다운로드 링크 클릭 작업은 지원이 끝난 Internet Explorer 에서만 동작합니다. 참조 문서는 대신 HTTP 작업을 쓰도록 안내합니다.[^web]

---

## 링크 목록 모두 누르기

| 순서 | 작업 | 설정 |
|---:|---|---|
| 1 | 웹 페이지에서 데이터 추출 | 연속한 링크 두 개에서 값을 추출. 목록의 나머지 링크까지 자동으로 추출됨 |
| 2 | 반복 | 시작 `0`, 끝 `%DataFromWebPage.RowsCount-1%` |
| 3 | 웹 페이지에서 링크 클릭 | 반복 안에 둠. UI 요소는 첫 번째 링크 |
| 4 | 선택기 수정 | 텍스트 편집기에서 `:eq(0)` 을 `:eq(%LoopIndex%)` 로 바꿈 |
| 5 | 웹 페이지로 이동 | 반복 안 맨 끝에 둠. 원래 페이지로 돌아옴 |

`%DataFromWebPage.RowsCount%` 는 추출한 행 수입니다. 열린 페이지에서 할 작업은 3번과 5번 사이에 넣습니다.[^links]

4번의 선택기는 아래처럼 바뀝니다. `[properties]` 는 요소의 특성을 줄여 적은 표기입니다.

```
ul[properties] > li[properties]:eq(0) > a[properties]
```

```
ul[properties] > li[properties]:eq(%LoopIndex%) > a[properties]
```

변수가 든 선택기는 복구 기능으로 고치지 못합니다. 복구는 [P35](p35-selector-repair.html)에서 다룹니다.

---

## 페이지와 요소의 세부 정보

웹 페이지의 세부 정보 가져오기는 이미 만든 브라우저 인스턴스의 페이지에서 값 하나를 읽어 `WebPageProperty` 텍스트 변수에 담습니다.[^details][^web]

| 가져오기 | 읽는 값 |
|---|---|
| 웹 페이지 설명 | 페이지 설명 |
| 웹 페이지 메타 키워드 | 메타 키워드 |
| 웹 페이지 제목 | 제목 |
| 웹 페이지 텍스트 | 본문 글자 |
| 웹 페이지 원본 | 소스 코드 |
| 웹 브라우저의 현재 URL 주소 | 현재 주소 |

메타 키워드가 없는 페이지처럼 값을 읽지 못할 수 있습니다. 작업의 **오류 발생 시**를 실패 후 계속 실행으로 두고, 다음 줄의 If 로 `WebPageProperty` 가 비어 있는지 검사합니다.[^details] 오류 설정은 [P18](p18-errors.html)에서 다룹니다.

페이지 전체가 아닌 요소 하나의 값은 웹 페이지 요소의 세부 정보 가져오기로 읽습니다. 결과는 `AttributeValue` 텍스트 변수에 담기고, 특성 이름의 기본값은 요소 자체의 텍스트입니다.[^web]

---

## 샘플

흐름 `개념 연습_HGD` 를 씁니다. 없으면 [P2](p02-types.html)의 1·2번으로 만듭니다. Main 의 줄을 지우고 쌓습니다.

1. 작업 검색 칸에 `Edge` 를 입력하고 **새 Microsoft Edge 시작**을 작업 영역으로 끌어다 놓습니다. **이니셜 URL**에 아래를 넣고 **저장**을 누릅니다.

    ```
    {{ site.url }}{{ site.baseurl }}/practice/bid/?q=교육
    ```

2. 작업 검색 칸에 `세부 정보` 를 입력하고 **웹 페이지의 세부 정보 가져오기**를 맨 아래로 끌어다 놓습니다. **가져오기**를 **웹 페이지 제목**으로 바꾸고 **저장**을 누릅니다.
3. 도구 모음의 **실행**(▶)을 누릅니다. 열린 Edge 창은 닫지 않습니다. 오른쪽 세로 막대의 **{x}** 를 눌러 변수 창을 엽니다.

    **완료 기준**: `WebPageProperty` 가 `모의 공고 조회 — PA 실습` 이다.

4. 작업 검색 칸에 `세부 정보` 를 입력하고 **웹 페이지 요소의 세부 정보 가져오기**를 맨 아래로 끌어다 놓습니다. **UI 요소** 칸의 드롭다운을 열고 **UI 요소 추가**를 누릅니다. 3번에서 열린 Edge 창에서 결과 표 첫 행의 공고명 링크를 `Ctrl` + 왼쪽 클릭으로 잡습니다.
5. **특성 이름**에 아래를 넣고 **저장**을 누릅니다.

    ```
    HRef
    ```

6. 작업 검색 칸에 `웹 페이지로 이동` 을 입력하고 **웹 페이지로 이동**을 맨 아래로 끌어다 놓습니다. **URL**에 아래를 넣고 **저장**을 누릅니다.

    ```
    %AttributeValue%
    ```

7. 작업 검색 칸에 `JavaScript` 를 입력하고 **웹 페이지에서 JavaScript 함수 실행**을 맨 아래로 끌어다 놓습니다. **JavaScript 함수** 칸의 내용을 지우고 아래를 넣은 뒤 **저장**을 누릅니다.

    ```
    function ExecuteScript()
    {
    window.scrollTo(0, document.body.scrollHeight);
    return document.body.scrollHeight;
    }
    ```

8. 3번에서 열린 Edge 창을 닫고 **실행**(▶)을 누릅니다.

    **완료 기준**: Edge 창에 공고 상세 페이지가 열려 있다. 변수 창의 `AttributeValue` 에 `detail.html?no=` 가 들어 있고 `Result` 에 숫자가 있다.

9. 실행으로 열린 Edge 창을 닫습니다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: iframe 처리[^iframe] · 새 탭을 여는 링크[^newtab] · 스크롤[^scroll] · 브라우저 대화 상자[^prompts] · 링크 목록[^links] · 웹 페이지 세부 정보[^details] · 브라우저 자동화 작업[^web] · Manifest V3 전환[^manifest]

[^iframe]: **Handle iframes on a web page** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/how-to/handle-iframes> (2026-11-02 확인). 같은 도메인과 다른 도메인의 처리, 소스 링크 특성.
[^newtab]: **Handle links that open new tabs** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/how-to/links-open-new-tabs> (2026-11-02 확인). HRef 로 주소 읽기, JavaScript 링크, 실행 중인 인스턴스에 연결, 자동화 브라우저의 동작.
[^scroll]: **Scroll on a web page** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/how-to/scroll-web-page> (2026-11-02 확인). 포커스 작업으로 스크롤, scrollTo · scrollHeight · scrollTop.
[^prompts]: **Automate browser prompts** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/how-to/automate-browser-prompts> (2026-11-02 확인). 저장 · 열기 · 업로드 대화 상자를 기록기나 UI 자동화로 다룬다는 것.
[^links]: **Click all the elements in a list of links** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/how-to/click-elements-list-links> (2026-11-02 확인). 데이터 추출 · 반복 · 선택기 수정 · 원래 페이지로 돌아가기의 순서.
[^details]: **Retrieve details from a web page** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/how-to/retrieve-details-web-page> (2026-11-02 확인). 가져올 수 있는 여섯 값, WebPageProperty, 값이 없을 때의 오류 처리.
[^web]: **Browser automation actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/webautomation> (2026-11-02 확인). 작업 이름과 칸, 추출 시 데이터 처리, 탭 연결 방식과 URL 일치 순서, 새 탭 만들기, 자동화 브라우저 사용 중단, 다운로드 링크 작업의 제한.
[^manifest]: **Migration to Manifest V3** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/manifest> (2026-11-02 확인). JavaScript 함수 실행 작업의 개발자 도구 조건, Firefox 제한, 디버깅 알림.
