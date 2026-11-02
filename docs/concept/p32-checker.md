---
title: "P32. 흐름 검사기와 문제 해결"
parent: "더 읽을거리 · PAD"
nav_order: 32
concept:
  id: P32
  grade: C
  used_in: "랩에서 쓰지 않음"
  tokens: []
  sample: true
---

# P32. 흐름 검사기와 문제 해결

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. 흐름 검사기는 관리형 환경에서만 된다. 런북이 교육 환경의 Managed Environment 를 켜므로 샘플을 두었다.
     ⚠️ 실측할 것: 디자이너 오른쪽의 흐름 검사기 단추 모양과 라벨, 규칙의 한국어 화면 이름, 규칙의 기본 켜짐 여부. 샘플 3번은 빈 If 를 Incomplete if 로 잡는다고 가정한다.
     ⚠️ 문서 어긋남: 알려진 제한은 규칙 사용자 지정이 켜기 · 끄기와 심각도뿐이라 적고, 구성 절은 매개 변수 값도 포털에서 정한다고 적는다. 본문은 구성 절을 따랐다.
     ⚠️ 영어판과 한국어판 어긋남: Empty on block error action → 「블록 오류 시 비우기」, Incomplete if → 「불완전한 경우」. 본문 규칙 이름은 영문을 함께 적었다.
     ⚠️ 영어판과 한국어판 어긋남: 영어판 문제 해결 문서에 있는 「호스트된 머신에서는 서비스 계정을 바꿀 수 없다」는 주가 한국어판에 없다.
     랩 1 의 흐름 검사기는 클라우드 흐름 디자이너의 기능이고 이 페이지의 대상이 아니다. -->

> **다루는 것**: 데스크톱 흐름의 정적 분석 규칙과 런타임 문제를 진단하는 도구
>
> **쓰는 곳**: 랩에서 쓰지 않음. Lab 1 ⑥ 50번의 흐름 검사기는 클라우드 흐름 디자이너의 기능

---

## 흐름 검사기

흐름 검사기는 솔루션 검사기의 정적 분석 기능이고, 디자이너의 창에서 결과를 봅니다. 작업을 추가 · 제거 · 수정할 때마다 자동으로 다시 분석합니다. 관리형 환경에서만 쓸 수 있습니다.[^checker]

| 화면 | 내용 |
|---|---|
| 흐름 검사기 단추 | 디자이너 오른쪽. 숫자는 흐름의 전체 위반 수 |
| 점수 | 지킨 규칙의 비율(%). 흐름을 바꿀 때마다 다시 계산 |
| 위반 요약 | 규칙 이름과 위반한 작업 · 변수의 수 |
| 규칙 선택 | 해당 작업을 강조하고 자세한 설명을 보여 줌. 변수 위반은 변수 창으로 이동 |
| 위반 타일 | 오류 내용 · 권장 수정 · 문서 링크. 머리글의 슬라이더로 같은 규칙의 위반 사이를 이동 |
| 검색 · 필터 | 창에서 검색하고 하위 흐름별로 거름 |
| 작업 영역 표시 | 오류와 경고를 줄 옆에 표시. 하위 흐름 탭에도 상태 표시 |

---

## 규칙

| 규칙 | 종류 | 걸리는 조건 | 고치는 방법 |
|---|---|---|---|
| 안전하지 않은 암호(Unsafe password security) | 보안 | 암호를 안전하지 않게 다룸 | 직접 암호화된 텍스트 입력. 여러 머신이면 민감으로 표시한 변수 |
| 하위 흐름 재귀(Recursion between two subflows) | 디자인 | 하위 흐름끼리 서로 호출 | 재귀 호출을 없앰 |
| 변수 길이 초과(Variable length exceeded) | 유지 관리 | 변수 이름이 40자 초과 | 이름을 줄임 |
| 입력 변수 기본값(Input variable default values) | 유지 관리 | 입력 · 출력 변수에 기본값 없음 | 기본값을 넣음 |
| 입출력 변수 수(Threshold on number of input and output variables) | 유지 관리 | 입력 · 출력 변수가 25개 초과 | 25개 이하로 줄임 |
| 빈 블록 오류(Empty on block error action) | 디자인 | 블록 오류 시 작업이 비어 있음 | 오류를 처리하는 작업을 넣음 |
| 중첩 If(Nested if clauses) | 유지 관리 | If 중첩이 5단계 초과 | 5단계 이하로 고침 |
| 불완전한 If(Incomplete if) | 디자인 | If 가 비었거나 Else 쪽에만 작업이 있음 | 각 갈래에 작업을 넣음 |
| 무한 루프(Infinite loop) | 디자인 | 끝나지 않는 반복 | 종료 조건 · 최대 횟수 · 시간 제한을 둠 |
| 대기 과다(Misuse of wait actions) | 성능 | 대기 작업이 10개 초과 | 없애거나 합침 |
| 긴 대기(Immense wait time) | 성능 | 대기 시간을 600초 넘게 고정 | 줄이거나 나누고 사이에 검사를 둠 |
| 도달하지 못하는 작업(Unreached actions) | 유지 관리 | 실행되지 않는 작업이 있음 | 지우거나 실행 경로로 옮김 |
| 불필요한 하위 흐름(Not needed subflow) | 유지 관리 | 작업이 없거나 꺼진 작업만 있거나 5개 미만 | 지우거나 합침 |

규칙의 기본 심각도는 모두 경고입니다.[^checker]

---

## 규칙 구성

구성은 환경 단위로 적용되어 그 환경의 모든 데스크톱 흐름에 영향을 줍니다.[^checker]

| 구성 위치 | 경로 | 할 수 있는 일 |
|---|---|---|
| Power Automate 포털 | **데스크톱 흐름** 페이지 › **흐름 검사기** › 구성 창 › **저장** | 규칙 켜기 · 끄기, 심각도(오류 · 경고 · 정보), 매개 변수 값 |
| Power Platform 관리 센터 | **관리** › **환경** › **관리형 환경 편집** › **솔루션 검사기 적용** | 제외할 규칙. 환경 · 환경 그룹 단위 적용 |

| 조건 | 내용 |
|---|---|
| 우선순위 | 관리 센터 설정이 포털 설정보다 우선. 제한된 규칙은 포털에서 고칠 수 없음 |
| 환경 그룹 | 그룹에 정해진 구성이 있으면 상속되어 개별로 고칠 수 없음 |
| 열려 있는 흐름 | 흐름을 다시 열어야 구성이 적용됨 |
| 권한 | `prvReadmsdyn_analysisoverride` 보기 · `prvWritemsdyn_analysisoverride` 수정 · `prvCreatemsdyn_analysisoverride` 만들기 |

솔루션 전체를 검사하려면 포털의 솔루션 목록에서 솔루션의 메뉴(⋯) › **솔루션 검사기**를 엽니다. 메뉴에 실행 · 결과 보기 · 결과 다운로드가 있습니다. 결과의 개체 이름 열에 위반한 데스크톱 흐름의 이름이 있습니다.[^checker]

---

## 흐름 검사기의 알려진 문제

문서가 적은 문제입니다.[^checker]

| 문제 | 내용 |
|---|---|
| 처리되지 않은 오류 | 규칙 위반 세부 정보를 본 뒤 복사한 작업을 지우면 날 수 있음 |
| 분석 실패 | 입력 대화 표시 · 폴더 선택 대화 표시 · 사용자 지정 양식 표시에 민감으로 표시하지 않은 암호 변수를 쓰면 규칙 평가가 실패함 |

---

## 문제 해결 도구

Power Automate 머신 런타임의 문제 해결 › **문제 해결 도구 실행**으로 엽니다. 관리자 권한이 필요합니다.[^trouble]

| 할 일 | 조작 | 결과 |
|---|---|---|
| 연결 진단 | **진단 도구 시작**. 콘솔에서는 **도움말** › **문제 해결사** › **클라우드 런타임에 대한 연결 문제 진단** | 필요한 서비스별 연결 결과와 로그 |
| 서비스 계정 변경 | **계정 변경** › **이 계정** › 계정과 비밀번호 입력 › **구성** | UIFlowService 를 지정한 계정으로 실행 |
| 머신 로그 수집 | **로그 내보내기** | 바탕 화면에 zip 파일 저장 |

---

## 연결 진단이 확인하는 서비스

| 서비스 | 주소 | 실패할 때 |
|---|---|---|
| Azure Relay | `*.servicebus.windows.net` | 이 주소 또는 로그의 엔드포인트를 허용 |
| Dataverse | `*.dynamics.com` | 이 주소 또는 팀의 Dataverse URL 을 허용 |
| 데스크톱 흐름 서비스 | `*.gateway.prod.island.powerapps.com` · `*.api.powerplatform.com` | 로그 확인. v2.52 부터 뒤쪽 주소도 필요 |

이 연결은 머신에서 도는 Power Automate 서비스(UIFlowService)가 맺습니다. 사용자 세션에서는 되고 서비스로는 안 되면 프록시 규칙을 의심하고 서비스 계정 변경을 검토합니다.[^trouble]

---

## 서비스 계정

서비스의 기본 계정은 설치 프로그램이 만드는 가상 계정 `NT SERVICE\UIFlowService` 입니다. 대부분은 바꾸지 않습니다.[^trouble]

| 바꾸는 경우 | 내용 |
|---|---|
| 네트워크 제한 | 가상 계정의 요청이 Power Automate 클라우드 서비스에 닿지 못함 |
| 권한 제한 | 정책이 가상 계정의 **서비스로 로그온** 권한을 허용하지 않음 |

명령줄 도구 `TroubleshootingTool.Console.exe` 로도 바꿉니다. PAD 설치 폴더에 있고, 인수 없이 실행하면 명령 목록이 나옵니다. PAD 를 업그레이드하면 서비스 계정이 기본값으로 돌아갑니다. 호스트된 머신에서는 바꿀 수 없습니다.[^trouble]

---

## 클라우드에서 호출한 실행의 오류 코드

클라우드 흐름에서 호출한 유인 · 무인 실행이 실패하면 오류 코드를 문서에서 찾습니다. 유인 실행에 해당하는 코드 일부입니다.[^run-errors]

| 오류 코드 | 조치 |
|---|---|
| `UnsupportedRpaScriptSchemaVersion` | 흐름이 더 최신 PAD 로 만들어짐. 머신에 최신 PAD 를 설치 |
| `AttendedUserSessionNotActive` · `AttendedUserNotLoggedIn` | 맞는 사용자로 로그인했는지, 세션이 잠겨 있지 않은지 확인 |
| `LocalPlaybackOrRecordingOngoing` | 같은 세션에서 기록이나 테스트 재생이 진행 중인지 확인 |
| `UIFlowAlreadyRunning` | 머신에서 다른 데스크톱 흐름이 실행 중. 끝나기를 기다림 |
| `UIFlowAgentNotAvailable` | 머신에서 UIFlowService 서비스가 실행 중인지 확인 |
| `NoListenerConnected` · `ConnectionTimeout` | 머신이 온라인이고 필요한 주소와 통신하는지 확인 |
| `EndpointDoNotExist` · `DnsError` | 머신을 다시 등록하고 실행을 다시 예약 |
| `DesktopFlowsActionTimeout` | 작업의 시간 제한을 늘리거나 흐름을 나눔 |

머신 등록과 클라우드 호출은 [P24](p24-from-cloud.html)에서 다룹니다.

---

## 지원

Power Automate 지원 사이트 `make.powerautomate.com/support` 에 자가 진단과 지원 요청이 있습니다. 지원 요청의 문제 유형에는 **데스크톱 흐름**을 넣습니다. 고객 지원은 최신 공개 릴리스 후 1년 안에 나온 버전, 보안 문제는 6개월 안의 릴리스가 대상입니다. 이 기준은 바뀔 수 있다고 문서에 적혀 있습니다.[^trouble]

---

## 샘플

흐름 `개념 연습_HGD` 를 씁니다. 없으면 [P2](p02-types.html)의 1·2번으로 만듭니다. Main 의 줄을 지우고 쌓습니다.

1. 작업 검색 칸에 `if` 를 입력하고 **조건** 아래 **If**를 작업 영역으로 끌어다 놓습니다. **첫 번째 피연산자**와 **두 번째 피연산자**에 아래를 넣고 **저장**을 누릅니다.

    ```
    1
    ```

    ```
    1
    ```

    **완료 기준**: 작업 영역에 **If** 와 **End** 두 줄이 있고 사이가 비어 있다.

2. 디자이너 오른쪽의 **흐름 검사기** 단추를 누릅니다.

    **완료 기준**: 창에 점수가 보이고, 위반 목록에 불완전한 If 규칙이 있다.

3. 불완전한 If 규칙을 누릅니다.

    **완료 기준**: 작업 영역의 If 줄이 강조되고 수정 방법이 적힌 타일이 보인다.

4. 작업 검색 칸에 `메시지 표시` 를 입력하고 **메시지 표시**를 **If** 와 **End** 사이로 끌어다 놓습니다. **표시할 메시지**에 아래를 넣고 **저장**을 누릅니다.

    ```
    검사기 확인
    ```

    **완료 기준**: 불완전한 If 규칙이 위반 목록에서 사라지고 점수가 바뀐다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: 흐름 검사기[^checker] · 런타임 문제 해결[^trouble] · 실행 오류[^run-errors]

[^checker]: **Flow checker** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/static-analysis> (2026-11-02 확인). 디자이너의 정적 분석, 규칙 목록과 수치, 구성 위치와 우선순위, 관리형 환경 제한, 알려진 문제.
[^trouble]: **Troubleshoot desktop flows runtime** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/troubleshoot> (2026-11-02 확인). 문제 해결 도구, 연결 진단 표, 서비스 계정 변경, 로그 수집, 지원 범위.
[^run-errors]: **Errors when running attended or unattended desktop flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/troubleshoot/power-platform/power-automate/desktop-flows/troubleshoot-errors-running-attended-or-unattended-desktop-flows> (2026-11-02 확인). 오류 코드별 조치. 유인 실행에 해당하는 일부만 옮겼다. 영어판으로 읽었다.
