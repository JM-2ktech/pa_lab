---
title: "C26. 트리거 조건"
parent: "더 읽을거리 · Cloud Flow"
nav_order: 26
concept:
  id: C26
  grade: C
  used_in: "랩에서 쓰지 않음"
  tokens: []
  sample: true
---

# C26. 트리거 조건

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. triggerOutputs()?['body/Title'] 은 트리거 조건 예로 문서에 적혀 있지 않다. 문서의 예는 메일 제목 조건 화면뿐이다. 실행해서 확인한다.
     ⚠️ 실측할 것: 만들기 화면의 자동화된 클라우드 흐름 라벨, SharePoint 트리거의 한국어 이름(한국어판에 항목이 만들어진 경우 · 항목을 만들 때가 섞여 있다), 설정 탭의 트리거 조건 · + 추가 라벨, 목록의 새 항목 단추, 배열 필터링의 고급 모드에서 편집 라벨과 왼쪽 값에 트리거 값을 고를 수 있는지
     ⚠️ 문서 사이 차이: 트리거 조건이 false일 때 customize-triggers 는 실행 기록이 남지 않는다고, triggers-troubleshoot 는 모든 실행 보기에서 건너뛴 트리거 확인을 볼 수 있다고 적는다. 동시성 기본 병렬도는 limits-and-config 25, optimize-power-automate-triggers 1 이다. 되돌리는 방법도 문서마다 다르다. 문서의 OR 예는 @or (test1, test2, test3) 으로 공백이 있어 공백 없이 적었다. -->

> **다루는 것**: 트리거 설정에 식을 넣어 조건에 맞는 이벤트에서만 흐름을 시작하는 방법, 폴링 · 웹후크 트리거의 차이, 트리거 동시성
>
> **쓰는 곳**: 랩에서 쓰지 않음

---

## 흐름 안의 조건과 트리거 조건

트리거 조건은 흐름이 시작되기 전에 평가합니다. 조건이 false이면 흐름이 시작되지 않습니다.[^customize]

| 항목 | 조건 카드 | 트리거 조건 |
|---|---|---|
| 넣는 곳 | 작업으로 추가 | 트리거의 **설정** 탭 |
| 조건이 false일 때 | 흐름은 실행. 갈래만 달라짐 | 흐름을 시작하지 않음 |
| Power Platform 요청 | 이벤트마다 실행되어 소비 | 실행 수가 줄어 소비 감소 |
| 실행 기록 | 실행마다 남음 | 시작되지 않은 이벤트는 실행이 없음 |

문서의 예입니다. 승인된 청구서만 처리하는 흐름에 청구서 메일이 1,000건 오고 승인된 것이 50건이면, 조건 카드로 거를 때 1,000번 실행되고 트리거 조건으로 거를 때 50번 실행됩니다.

---

## 작성 규칙

| 규칙 | 내용 |
|---|---|
| 넣는 경로 | 트리거 선택 › 설정 탭 › 트리거 조건 **+ 추가** |
| 시작 글자 | 모든 조건은 `@` 로 시작 |
| 여러 줄 | **+ 추가**로 줄을 늘리면 모든 줄이 참일 때 실행(AND) |
| OR | 한 줄 안에서 `@or()` 사용 |
| 함수 | 조건 식과 같음. [C6](c06-condition.html) |

식의 모양입니다.

```
@equals(triggerOutputs()?['body/Title'], '승인')
```

```
@contains(triggerOutputs()?['body/Title'], '긴급')
```

```
@or(equals(triggerOutputs()?['body/Title'], 'A'), equals(triggerOutputs()?['body/Title'], 'B'))
```

트리거 출력의 키 이름은 실행 기록의 트리거 출력이나 트리거의 **코드 보기**에서 확인합니다.[^errors] SharePoint의 한글 열은 내부 이름이 인코딩됩니다. 내부 이름은 [C13](c13-filter.html)에 있습니다.

식을 직접 쓰지 않고 배열 필터링에서 만들 수도 있습니다.[^customize]

| 순서 | 조작 |
|---:|---|
| 1 | 흐름에 **배열 필터링** 작업을 추가하고 조건 작성. 왼쪽 값은 트리거의 동적 콘텐츠로 지정 |
| 2 | 고급 모드에서 편집을 눌러 식 복사 |
| 3 | 트리거의 **설정** 탭에서 트리거 조건에 붙여넣기 |
| 4 | **배열 필터링** 작업 삭제 |

---

## 흐름이 시작되지 않을 때

| 증상 | 확인할 것 |
|---|---|
| 항상 시작되지 않음 | 식이 늘 false인지. 없는 필드를 참조하는지 |
| 데이터가 맞는데 시작되지 않음 | 이벤트의 해당 값이 비어 있는지 |
| 시작 여부가 궁금함 | 28일 실행 기록의 모든 실행에서 건너뛴 트리거 확인[^trouble] |
| 식이 기대와 다르게 동작 | 트리거 입력 칸의 식은 저장할 때 한 번 계산됨. `utcNow()` 도 저장 시각으로 고정 |
| SharePoint 파일 트리거 | 하위 폴더의 파일 변경에서는 실행되지 않음 |

원인을 찾을 때는 조건을 잠시 빼고 실행해 트리거 출력의 필드 이름과 값을 본 뒤 조건을 고쳐 넣습니다.[^errors] 조건 외의 원인은 DLP 정책, 끊어진 연결, 프리미엄 커넥터, 대상 권한입니다. [C22](c22-error-codes.html)에 있습니다.

---

## 폴링 트리거와 웹후크 트리거

트리거는 두 방식으로 나뉩니다.[^optimize]

| 항목 | 폴링 | 웹후크 |
|---|---|---|
| 동작 | 주기적으로 서비스를 확인 | 서비스가 이벤트를 알림 |
| 흐름을 꺼 둔 동안의 이벤트 | 다시 켜면 모두 처리 | 처리하지 않음 |
| 다시 켤 때 영향 | 밀린 이벤트가 몰려 지연 | 꺼 둔 동안의 이벤트 누락 |
| 밀린 이벤트 버리기 | 흐름을 복사하고 원본 삭제 | 해당 없음 |
| 구분 | 트리거 **코드 보기**에 `recurrence` 의 `interval` · `frequency` 가 있음[^trouble] | 없음 |

폴링 주기는 라이선스를 따릅니다. 무료 플랜은 15분, Office 365 플랜은 5분입니다.[^trouble] 이벤트가 일어난 뒤 실행까지 이 시간이 걸릴 수 있습니다. 먼저 수동으로 테스트해 바로 실행되면 스로틀링이 원인이 아닙니다.

---

## 트리거 동시성 제어

기본값은 꺼짐이고 조건에 맞는 실행을 가능한 만큼 동시에 시작합니다.[^optimize] 트리거의 **설정**에서 켜면 동시에 도는 실행 수(병렬도)를 정합니다. 읽은 행을 고쳐 쓰는 흐름에서 옛 값을 읽는 문제를 막을 때 씁니다.

| 항목 | 내용 |
|---|---|
| 병렬도 | 1~100[^limits] |
| 켰을 때 기본값 | 제한 문서는 25, 코딩 지침 문서는 1 |
| 대기 실행 | 10 + 병렬도. 넘은 이벤트는 재시도되고 실패할 수 있음[^limits] |
| 분할(Split on) 항목 | 100으로 감소 |
| 끄기 | 켠 뒤 되돌릴 수 없음. 제한 문서는 트리거 삭제 후 재추가, 코딩 지침 문서는 새 흐름 만들기로 적음 |
| SharePoint 트리거 | 끄려 하면 `CannotDisableTriggerConcurrency` 오류. 흐름을 내보내 정의를 고쳐 가져옴[^sp] |
| 실행이 전부 취소됨 | 동시성 설정이 새 실행을 거부한 경우[^fixconn] |

문서는 기본값을 유지하고, 필요하면 동시성이 필요한 작업만 하위 흐름으로 분리해 거기에 켜라고 권장합니다.

---

## 샘플

SharePoint 목록 `업무요청_HGD` 를 씁니다. 없으면 [Lab 1](../lab1.html) ①로 만듭니다. 제목에 `긴급` 이 있는 항목에서만 흐름을 시작합니다.

1. [Power Automate — {{ site.pa.environment }}]({{ site.pa.powerautomate_url }}){:target="_blank"}를 엽니다. 왼쪽 메뉴 **+ 만들기**를 누르고 **시작(처음부터)**의 **자동화된 클라우드 흐름**을 고릅니다.
2. **흐름 이름**에 아래를 입력합니다. `HGD` 대신 본인 이니셜을 넣습니다.

    ```
    트리거 조건_HGD
    ```

3. 트리거 검색 칸에 `항목` 을 입력하고 **SharePoint** 아래 **항목이 만들어진 경우**를 고른 뒤 **만들기**를 누릅니다.
4. 트리거 구성 창의 **사이트 주소**에서 `Power Automate 실습 - {{ site.pa.sharepoint_site }}` 를 고릅니다. **목록 이름**에서 `업무요청_HGD` 를 고릅니다.
5. **설정** 탭을 누르고 트리거 조건의 **+ 추가**를 누릅니다. 칸에 아래를 붙여넣습니다.

    ```
    @contains(triggerOutputs()?['body/Title'], '긴급')
    ```

6. 트리거 카드 아래 **+** › **작업 추가**에서 `작성` 을 검색해 **작성**을 고릅니다. **입력** 칸의 ***fx*** 단추를 누르고 아래를 붙여넣은 뒤 **추가**를 누릅니다.

    ```
    triggerOutputs()?['body/Title']
    ```

7. **저장**을 누릅니다.
8. 새 탭에서 `업무요청_HGD` 목록을 열고 새 항목을 추가합니다. **제목**에 아래를 입력하고 저장합니다.

    ```
    일반 문의 HGD
    ```

9. 새 항목을 하나 더 추가합니다. **제목**에 아래를 입력하고 저장합니다.

    ```
    긴급 점검 HGD
    ```

10. 10분 뒤 `트리거 조건_HGD` 의 세부 정보에서 **28일 실행 기록**을 확인합니다.

    **완료 기준**: 실행 기록이 1건이고, 그 실행의 **작성** 카드 출력이 `긴급 점검 HGD` 이다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: 조건으로 트리거 사용자 지정[^customize] · 트리거 최적화[^optimize] · 트리거 문제 해결[^trouble] · 오류 코드 참조[^errors] · 제한과 구성[^limits] · SharePoint 커넥터[^sp] · 연결 오류 수정[^fixconn]

[^customize]: **Customize your triggers with conditions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/customize-triggers> (2026-11-02 확인). 설정 경로, `@` 규칙, AND와 OR, 배열 필터링으로 식 만들기, 청구서 예.
[^optimize]: **Optimize Power Automate triggers** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/optimize-power-automate-triggers> (2026-11-02 영어판 확인). 폴링과 웹후크, 동시성 제어의 기본값과 권장 사항.
[^trouble]: **Troubleshoot Power Automate trigger problems and errors** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/troubleshoot/power-platform/power-automate/flow-run-issues/triggers-troubleshoot> (2026-11-02 영어판 확인). 건너뛴 트리거 확인, 폴링 구분, 폴링 주기, 저장 시점의 식 계산, SharePoint 하위 폴더.
[^errors]: **Cloud flow error code reference** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/error-reference> (2026-11-02 영어판 확인). TriggerConditionNotMet 의 원인과 조치.
[^limits]: **Limits of automated, scheduled, and instant flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/limits-and-config> (2026-11-02 영어판 확인). 동시 실행, 대기 실행, Split on 한도.
[^sp]: **SharePoint** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/sharepointonline/> (2026-11-02 영어판 확인). 동시성 제어를 되돌리는 방법.
[^fixconn]: **Fix connection failures in cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/fix-connection-failures> (2026-11-02 영어판 확인). 전부 취소된 실행의 원인.
