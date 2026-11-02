---
title: "C2. 흐름 세 유형과 트리거"
parent: "개념 1. 흐름의 구성"
nav_order: 2
concept:
  id: C2
  grade: A
  used_in: "Lab 1 ② 인스턴트 흐름 · ⑥ 예약 트리거와 식 · Lab 2 ② 예약 흐름"
  tokens: ["수동으로 흐름 트리거", "Recurrence", "인스턴트 클라우드 흐름", "예약된 클라우드 흐름", "입력 추가"]
  sample: true
---

# C2. 흐름 세 유형과 트리거

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. 후보의 샘플(랩의 흐름을 세 유형 표에 넣어 본다)은 유형 표의 「이 과정의 흐름」 열로 옮겼고, 랩이 만들지 않는 자동화 유형을 샘플로 뒀다.
     샘플 항목은 마지막에 지운다. 마감일이 빈 항목이 남으면 Lab 1 52번 건수가 달라질 수 있고(null 은 비교에서 빈 문자열로 바뀐다) 39번 항목 수도 달라진다.
     ⚠️ 실측할 것: 라벨 「자동화된 클라우드 흐름」과 빌드 창의 칸 이름, 트리거 이름 「항목이 만들어지는 경우」(한국어판 커넥터 문서), 목록의 「+ 새로 만들기」 · 항목 삭제 메뉴 · 사이트 콘텐츠, 테스트 중 SharePoint 트리거가 실행되기까지 걸리는 시간, 내 흐름의 ⋮ 메뉴와 꺼짐 표시, Recurrence 구성 창의 칸 이름(문서는 Azure Logic Apps 것이다)
     ⚠️ 트리거 입력 유형의 전체 목록을 모은 문서를 찾지 못했다. 표는 Lab 1 실측 셋과 파일 입력만 적었다.
     ⚠️ 폴링 간격은 라이선스 플랜 기준 문서 값이다. 교육 계정의 플랜은 확인하지 않았다. -->

> **다루는 것**: 클라우드 흐름의 세 유형, 트리거의 입력과 Recurrence 의 칸, 폴링과 웹후크, 트리거가 돌지 않을 때 확인할 것
>
> **쓰는 곳**: Lab 1 11~15번 인스턴트 클라우드 흐름 · 수동으로 흐름 트리거 · 41·42번 예약된 클라우드 흐름 · Recurrence · Lab 2 ② 월 단위 Recurrence

---

## 트리거와 작업

트리거는 클라우드 흐름을 시작하는 이벤트입니다. 작업은 트리거 뒤에 흐름이 수행하는 일입니다. 흐름을 저장하려면 트리거 하나와 작업 하나가 있어야 합니다.[^work]

대부분의 커넥터가 미리 만들어진 트리거를 제공합니다.[^triggers] 트리거를 바꾸려면 트리거 카드를 고르고 구성 창 위쪽 ⋮ 에서 삭제를 누릅니다. 캔버스에 **트리거 추가** 카드가 생기고 여기서 새 트리거를 고릅니다.[^work]

---

## 세 유형

Copilot 없이 만들 때는 유형을 직접 고릅니다.[^cloud]

| 유형 | 고르는 경우 | 시작하는 것 | 트리거 예 | 이 과정의 흐름 |
|---|---|---|---|---|
| 자동화된 클라우드 흐름 | 이벤트가 일어난 뒤 자동으로 처리 | 서비스에서 일어난 이벤트 | 새 이메일이 도착하는 경우(V3) · 항목이 만들어지는 경우 | 샘플의 `항목 감지_HGD` |
| 인스턴트 클라우드 흐름 | 사람이 필요할 때 시작 | 포털이나 모바일 앱의 단추 | 수동으로 흐름 트리거 | `업무요청 접수_HGD` |
| 예약된 클라우드 흐름 | 정해진 시각과 주기로 처리 | 일정 | Recurrence | `마감 알림_HGD` · `월간 점검보고서_HGD` |

SharePoint 커넥터의 트리거 예입니다.[^sharepoint]

| 트리거 | 시작하는 때 |
|---|---|
| 항목이 만들어지는 경우 | 항목을 만들 때 |
| 항목을 만들거나 수정하는 경우 | 항목을 만들 때와 수정할 때마다 |
| 항목 또는 파일이 수정되는 경우 | 수정할 때. 만들 때는 시작되지 않음 |
| 항목이 삭제되는 경우 | 목록에서 항목을 삭제할 때. 사이트 모음 관리자만 사용 |
| 파일이 만들어지는 경우(속성에만 해당) | 라이브러리에 항목을 만들 때. 라이브러리 열의 속성만 돌려줌 |

---

## 인스턴트 흐름의 입력

수동으로 흐름 트리거의 구성 창에서 **+ 입력 추가**로 실행할 때 받을 값을 정합니다.[^datetime] 실행하는 사람이 흐름 실행 창에서 값을 넣고, 뒤의 작업은 이 값을 동적 콘텐츠로 읽습니다.

| 입력 유형 | 실행 창의 칸 |
|---|---|
| 텍스트 | 글자 입력 |
| 예/아니요 | 켜기 · 끄기 |
| 날짜 | 날짜 선택 |
| 파일 | 파일 선택.[^editor] 식에서 `triggerBody()['file']['name']` 으로 파일 이름을 읽음 |

---

## 흐름이 쓰는 연결

공유한 흐름을 실행할 때 쓰는 연결은 트리거에 따라 다릅니다.[^trouble]

| 트리거 | 실행에 쓰는 연결 |
|---|---|
| 수동 트리거 | 트리거를 시작한 사용자의 연결 |
| Recurrence | 흐름을 만든 사람의 연결 |

연결은 [C3](c03-connectors.html)에서 다룹니다. 실행 전용 사용자가 쓸 연결을 정하는 설정은 [C20](c20-sharing.html)에서 다룹니다.

---

## Recurrence 의 칸

예약 흐름의 트리거는 Recurrence 입니다. 만들기 창에서 일정을 정하면 이 트리거가 흐름에 들어갑니다.[^triggers] 칸의 조건은 Azure Logic Apps 문서에 있고 Power Automate 문서가 이 문서를 고급 옵션으로 연결합니다.[^schedule][^recurrence]

| 칸 | 값 | 조건 |
|---|---|---|
| 간격 | 양의 정수 | 월 1~16 · 주 1~71 · 일 1~500 · 시간 1~12,000 · 분 1~72,000 · 초 1~9,999,999 |
| 빈도 | 초 · 분 · 시간 · 일 · 주 · 월 | 월 빈도는 매달 같은 날짜에 실행 |
| 표준 시간대 | 목록에서 선택 | 시작 시간을 지정할 때만 적용 |
| 시작 시간 | `YYYY-MM-DDTHH:MM:SSZ` | 끝에 `Z` 가 있으면 표준 시간대를 무시 |
| 이 요일에 | 월요일 ~ 일요일 | 빈도가 주일 때 |
| 이 시간에 | 0~23 | 빈도가 일 · 주일 때 |
| 이 분에 | 0~59 | 빈도가 일 · 주일 때 |

일정에 따른 동작입니다.[^recurrence][^trouble]

| 설정 | 동작 |
|---|---|
| 시작 시간 없음 | 저장할 때 첫 실행이 바로 돎 |
| 시작 시간 지정 | 시작 시간보다 먼저 실행되지 않음. 단순 일정이면 시작 시간이 첫 실행 |
| 시각을 지정하지 않음 | 다음 실행을 직전 실행 시각으로 계산하므로 시작 시각이 조금씩 밀릴 수 있음 |
| 미래의 시작 시간과 일 · 주 · 월 빈도 | 각각 24시간 · 7일 · 1개월 전에 구성해야 첫 회차를 건너뛰지 않음 |
| 시각 지정 | 실행 시각이 1분 안에서 달라질 수 있음 |

식을 트리거 입력에 넣으면 값은 저장할 때 계산됩니다. 트리거 입력의 `utcNow()` 는 저장한 시각으로 고정되고 실행할 때 다시 계산되지 않습니다.[^trouble] 시간대 변환은 [C11](c11-datetime.html)에서 다룹니다.

---

## 폴링 트리거와 웹후크 트리거

커넥터의 트리거는 이벤트를 확인하는 방식으로 나뉩니다.[^optimize][^architecture]

| 항목 | 폴링 트리거 | 웹후크 트리거 |
|---|---|---|
| 확인 방식 | 일정 간격으로 서비스에 새 데이터를 물음 | 서비스에 등록해 이벤트 알림을 받음 |
| 흐름을 껐다 켤 때 | 꺼져 있던 동안의 이벤트까지 처리 | 켠 뒤에 일어난 이벤트만 처리 |
| 많은 이벤트가 밀렸을 때 | 켜는 순간 전부 처리해 지연이 생길 수 있음 | 해당 없음 |
| 구분하는 방법 | 트리거 카드 **코드 보기**에 `recurrence` 와 `frequency` 가 있음 | `recurrence` 가 없음 |

폴링 트리거는 라이선스 플랜에 따라 확인 간격이 다릅니다. 문서의 예는 Free 플랜 15분, Flow for Office 365 플랜 5분입니다. 이벤트가 일어난 뒤 흐름이 시작되기까지 몇 분이 걸릴 수 있습니다.[^trouble]

---

## 트리거가 돌지 않을 때

문서의 점검 순서를 표로 옮겼습니다.[^failures][^trouble] 트리거에 조건을 걸어 실행 횟수를 줄이는 방법은 [C26](c26-trigger-conditions.html)에서 다룹니다.

| 증상 | 확인할 것 |
|---|---|
| 흐름이 꺼짐 | 누군가 끈 흐름. 켜기. 바로 다시 꺼지면 DLP 정책 위반 확인 |
| 흐름이 일시 중단됨 | 실패가 반복되어 자동으로 중단된 흐름. 실패 원인을 고친 뒤 켜기 |
| 예약 흐름의 실행 기록이 없음 | 되풀이 설정과 표준 시간대 |
| 자동화 흐름의 실행 기록이 없음 | 이벤트가 실제로 일어났는지. 시험 항목을 만들고 5~10분 대기 |
| 인스턴트 흐름의 실행 기록이 없음 | 사람이 시작했는지 |
| 실행이 모두 취소됨 | 트리거의 동시성 설정 |
| 세부 정보 화면의 흐름 트리거 문제 오류 | 트리거 등록 실패. 원인을 고친 뒤 흐름을 편집하고 저장 |
| 연결 오류 | 연결 목록의 연결 수정 |
| 하위 폴더의 파일에 반응하지 않음 | SharePoint 파일 트리거는 하위 폴더에서 시작되지 않음 |
| 예약 시각보다 먼저 실행됨 | Recurrence 의 시작 시간 지정 |

---

## 끄기와 켜기

왼쪽 메뉴 **내 흐름**에서 흐름 옆 ⋮ 를 눌러 끄기 · 켜기 · 편집 · 삭제를 고릅니다. 흐름을 고르면 28일 실행 기록을 볼 수 있습니다. 계정 하나에 흐름을 600개까지 둘 수 있습니다.[^logicflow]

---

## 샘플

자동화된 클라우드 흐름을 만들어 목록 항목으로 시작시킵니다. `업무요청_HGD` 목록을 씁니다. 없으면 [Lab 1](../lab1.html)의 1~8번으로 만듭니다.

1. 아래 링크로 Power Automate를 엽니다.

    [Power Automate — {{ site.pa.environment }}]({{ site.pa.powerautomate_url }}){:target="_blank"}

2. 왼쪽 메뉴 **+ 만들기**를 누르고 **시작(처음부터)**의 **자동화된 클라우드 흐름**을 고릅니다.
3. **흐름 이름**에 아래를 입력합니다. `HGD` 는 본인 이니셜로 바꿉니다.

    ```
    항목 감지_HGD
    ```

4. 트리거 검색 칸에 아래를 입력하고 **SharePoint** 아래 **항목이 만들어지는 경우**를 고릅니다. **만들기**를 누릅니다.

    ```
    항목이 만들어지는
    ```

5. 트리거 카드를 누릅니다. **사이트 주소** 드롭다운에서 실습 사이트를 고릅니다. 목록에 없으면 **사용자 지정 값 입력**을 고르고 아래 주소를 붙여넣습니다.

    ```
    {{ site.pa.sharepoint_site }}
    ```

6. **목록 이름** 드롭다운에서 본인의 `업무요청_HGD` 를 고릅니다.
7. 트리거 카드 아래 **+** › **작업 추가**를 누르고 **기본 제공 도구** › **데이터 작업** › **작성**을 고릅니다.
8. **입력** 칸을 누르고 번개 단추에서 **항목이 만들어지는 경우** 아래 **제목**을 고릅니다.
9. **저장**을 누릅니다.

    **완료 기준**: 저장 완료 알림이 뜨고 카드에 빨간 오류 표시가 없다.

10. **테스트** › **수동** › **테스트**를 누릅니다. 트리거 동작을 하라는 안내가 뜹니다.
11. 새 탭에서 실습 사이트를 열고 `업무요청_HGD` 목록을 엽니다. 메뉴에 목록이 없으면 **사이트 콘텐츠**에서 찾습니다.

    [Power Automate 실습 사이트]({{ site.pa.sharepoint_site }}){:target="_blank"}

12. **+ 새로 만들기**를 누르고 **제목**에 아래를 입력한 뒤 **저장**을 누릅니다.

    ```
    샘플 항목
    ```

13. 디자이너 탭으로 돌아와 실행이 끝날 때까지 기다립니다. 시작까지 5~10분이 걸릴 수 있습니다. 실행이 끝나면 **작성** 카드를 누릅니다.

    **완료 기준**: 카드마다 초록 체크가 붙고 **작성** 출력이 `샘플 항목` 이다.

14. 왼쪽 메뉴 **내 흐름**에서 `항목 감지_HGD` 옆 **⋮** 를 누르고 **끄기**를 고릅니다.

    **완료 기준**: `항목 감지_HGD` 가 꺼짐으로 표시된다.

15. `업무요청_HGD` 목록에서 `샘플 항목` 을 삭제합니다.

    **완료 기준**: 목록에 `샘플 항목` 이 없다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **실측**: 트리거 입력 유형과 흐름 실행 창의 라벨은 Lab 1 실측(2026-10-05)을 따랐습니다.
- **문헌**: 트리거와 작업 다루기[^work] · 트리거[^triggers] · 클라우드 흐름 개요[^cloud] · SharePoint 커넥터[^sharepoint] · 날짜와 시간 값[^datetime] · 흐름 편집기 문제[^editor] · 트리거 문제 해결[^trouble] · 일정에 따라 실행[^schedule] · Recurrence 트리거[^recurrence] · 트리거 최적화[^optimize] · 커넥터 아키텍처[^architecture] · 연결 실패 해결[^failures] · 클라우드 흐름 만들기[^logicflow]

[^work]: **Work with triggers and actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/work-with-triggers-actions> (2026-11-02 확인, 한국어판 미번역). 트리거와 작업의 정의, 저장 조건, 트리거 교체 절차.
[^triggers]: **Triggers in Power Automate cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/triggers-introduction> (2026-11-02 확인). 유형별 트리거 예, 예약 흐름에 Recurrence 가 들어간다는 것.
[^cloud]: **Overview of cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/overview-cloud> (2026-11-02 확인). 세 유형과 쓰임새. 한국어판은 인스턴트를 「즉시」로도 적었다.
[^sharepoint]: **SharePoint** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/sharepointonline/> (2026-11-02 확인). 트리거 목록과 한국어 이름.
[^datetime]: **Customize or format date and time values in a flow** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/date-time-values> (2026-11-02 확인). 수동 트리거의 **+ 입력 추가** › **날짜**.
[^editor]: **Flow Editor issues and recommendations** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/troubleshoot/power-platform/power-automate/flow-creation/flow-editor-issues-recommendations> (2026-11-02 확인). 수동 트리거의 파일 입력과 파일 이름을 읽는 식.
[^trouble]: **Troubleshoot Power Automate trigger problems and errors** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/troubleshoot/power-platform/power-automate/flow-run-issues/triggers-troubleshoot> (2026-11-02 확인). 트리거별 연결, 폴링 간격, 저장할 때 계산되는 식, 흐름 트리거 문제 오류, 하위 폴더, 실행 시각의 오차.
[^schedule]: **Run a cloud flow on a schedule** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/run-scheduled-tasks> (2026-11-02 확인). 간격 · 빈도 · 표준 시간대 · 시작 시간, 월 빈도.
[^recurrence]: **Schedule and run recurring workflows with the Recurrence trigger** — Microsoft Learn(Azure Logic Apps). <https://learn.microsoft.com/ko-kr/azure/connectors/connectors-native-recurrence> (2026-11-02 확인). 간격의 범위, 시작 시간과 `Z`, 저장 때의 첫 실행, 밀림.
[^optimize]: **Optimize Power Automate triggers** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/optimize-power-automate-triggers> (2026-11-02 확인). 폴링과 웹후크, 껐다 켤 때의 차이.
[^architecture]: **Connectors architecture** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/connectors/connector-architecture> (2026-11-02 확인). 폴링 트리거와 푸시 트리거의 구분.
[^failures]: **Fix connection failures in cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/fix-connection-failures> (2026-11-02 확인, 문서 끝에 AI 도움 표기). 흐름 상태와 트리거별 점검 순서.
[^logicflow]: **Create a cloud flow in Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/get-started-logic-flow> (2026-11-02 확인). 내 흐름의 끄기 · 켜기 · 편집 · 삭제, 계정당 흐름 600개.
