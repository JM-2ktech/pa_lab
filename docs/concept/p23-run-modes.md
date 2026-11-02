---
title: "P23. 실행 방식"
parent: "개념 9. 실행과 운영"
nav_order: 23
concept:
  id: P23
  grade: B
  used_in: "Lab 4 ② 13번 디자이너 실행 · ⑥ 54번 게시와 콘솔 목록"
  tokens: ["콘솔", "**게시**", "**실행**(▶)"]
  sample: true
---

# P23. 실행 방식

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. 콘솔의 실행 · 편집 · 게시와 상태 문구는 Lab 4 실측을 따랐다.
     속성 · 세부 정보 · 실행 URL · 바탕 화면 바로 가기 만들기 · 키보드 단축키로 실행은 이 PC 에 설치된 PAD 의 한국어 리소스에서 확인했고 화면은 보지 않았다.
     ⚠️ 실측할 것: 수업 계정에서 실행 URL 과 바탕 화면 바로 가기 메뉴가 보이는가(문서는 실행 조건만 적었다). 유인 · 무인 라벨(실행 모드 드롭다운)의 포털 표기.
     ⚠️ 문서에 없는 것: 키보드 단축키 실행의 라이선스 조건, 디자이너 실행이 「로컬 유인」인지. 본문에 단정하지 않았다.
     문서의 URL 넷째 형식은 workflowIName 으로 오타가 있어 workflowName 으로 옮겼다. 콘솔 문서는 단추를 Start, 시작 문서는 Run 으로 적는다. 화면은 실행이다. -->

> **다루는 것**: 데스크톱 흐름을 시작하는 경로, 유인과 무인의 조건, 프리미엄 기능의 구분, 클라우드와 컴퓨터를 잇는 구조
>
> **쓰는 곳**: Lab 4 13번 도구 모음의 **실행**(▶) · 54번 게시와 콘솔 흐름 목록. 유인 · 무인 실행과 실행 URL 은 랩에서 쓰지 않습니다.

---

## 시작 경로

| 경로 | 시작하는 곳 | 입력 변수의 값 | 라이선스 조건 |
|---|---|---|---|
| 디자이너 | 도구 모음 **실행**(▶) | 기본값 | 추가 비용 없음 |
| 콘솔 | 흐름 목록의 **실행** | **흐름 입력** 창에 입력 | 추가 비용 없음 |
| 키보드 단축키 | 흐름 **속성** › **일반** 에 설정한 키 | 문서에 없음 | 문서에 없음 |
| 바탕 화면 바로 가기 | 콘솔에서 만든 바로 가기 | 콘솔이 물음 | Premium 또는 종량제 환경 |
| 실행 URL | 브라우저 · Windows 실행 · 명령 프롬프트 · 작업 스케줄러 | `inputArguments` 또는 콘솔이 물음 | Premium 또는 종량제 환경 |
| 클라우드 흐름 | **데스크톱용 Power Automate로 빌드된 흐름 실행** 작업 | 작업의 입력 칸 | 유인은 Premium, 무인은 Process 플랜 |

콘솔의 **실행**은 흐름을 로컬 유인 모드로 실행합니다.[^console] 로컬 유인 모드로는 한 번에 한 흐름만 실행됩니다.[^url] 회사 또는 학교 계정은 콘솔 실행까지 추가 비용 없이 쓸 수 있습니다.[^freeorg]

버전 관리가 켜진 환경에서 콘솔과 클라우드가 실행하는 것은 게시한 버전입니다.[^version] **저장**은 초안만 만듭니다. 켜진 작업이 하나도 없으면 게시 단추가 꺼져 있습니다.

---

## 콘솔 설정과 흐름 속성

| 위치 | 항목 | 동작 |
|---|---|---|
| 콘솔 **설정** | 모니터링/알림 | Windows 알림 · 흐름 모니터링 창 · 알림 없음 중 선택 |
| 콘솔 **설정** | 단축키 | 실행 중인 흐름의 일시 중지 · 다시 시작, 즉시 중지 |
| 콘솔 **설정** | 외부에서 흐름을 호출할 때 확인 대화 상자 | URL · 바로 가기 실행 전 확인. 기본 켬 |
| 흐름 **속성** › **일반** | 이름 · 설명 | 편집 |
| 흐름 **속성** › **일반** | 키보드 단축키로 실행 | 로컬 실행 키 설정 |
| 흐름 **속성** › **일반** | 태그(미리 보기) | 흐름을 묶는 레이블 |
| 흐름 **속성** › **일반** | 오류 시 동작 | 실행 오류 처리 방식 |
| 흐름 **속성** › **일반** | 흐름 시간 제한 | 기본 끔. 콘솔 · 클라우드 실행이 이 시간을 넘으면 중지하고 시간 초과 처리 |
| 흐름 **속성** › **일반** | 로그에 스크린샷 추가 | 실패할 때 화면을 실행 작업 세부 정보에 올림 |
| 흐름 **속성** › **세부 정보** | 소유자 · 만든 날짜 · 수정 날짜 · 흐름 ID · 스키마 버전 | 읽기 |
| 흐름 **속성** › **세부 정보** | 실행 URL | 환경 ID 와 흐름 ID 로 만든 주소 |

태그와 흐름 시간 제한은 회사 또는 학교 계정에서만 쓸 수 있습니다. 태그 · 스크린샷 · 시간 제한은 v2 스키마에 저장한 흐름에만 적용됩니다. 흐름 실행 로그를 보는 것은 프리미엄 기능입니다.[^console]

---

## 유인과 무인

클라우드 흐름에서 시작할 때 **실행 모드**를 고릅니다. 유인은 로그인한 상태에서, 무인은 백그라운드에서 실행합니다.[^uiflow]

| 항목 | 유인 | 무인 |
|---|---|---|
| Windows 세션 | 연결의 사용자로 로그인한 잠기지 않은 세션 필요 | 모든 사용자가 로그아웃한 컴퓨터 필요 |
| 세션을 만드는 쪽 | 사용자 | Power Automate. 원격 데스크톱(RDP) 세션을 만들고 끝나면 로그아웃 |
| 화면 | 화면 또는 Picture-in-Picture | 대상 컴퓨터 화면이 잠긴 채로 유지됨 |
| 라이선스 | Power Automate Premium | Power Automate Process 플랜 |
| 연결 방식 | 사용자 이름과 암호 · 로그인으로 연결 | 사용자 이름과 암호. 로그인으로 연결은 실패 |
| 동시 실행 | 문서에 없음 | 무인 봇 하나가 한 번에 한 흐름 |
| 대표 오류 | `AttendedUserSessionNotActive` · `AttendedUserNotLoggedIn` | `SessionExistsForTheUserWhenUnattended` · `UnattendedUserSessionLocked` · `UnattendedUserSessionDisconnected` |

오류 이름의 조건은 문제 해결 문서에 있습니다.[^queue] 연결 방식의 제한은 [P24](p24-from-cloud.html)에서 다룹니다.[^conn] 무인 봇은 컴퓨터에 프로세스 용량을 할당해 만듭니다.[^machines]

무인 실행의 조건은 아래와 같습니다.[^unattended]

| 조건 | 내용 |
|---|---|
| Windows 10 · 11 | 잠긴 세션을 포함해 활성 사용자 세션이 있으면 실행 불가 |
| Windows Server | 연결과 같은 사용자의 잠긴 세션이 있으면 오류 |
| 사용자 권한 | 연결의 사용자가 원격 데스크톱 세션을 만들 수 있어야 함. 대부분 **Remote Desktop Users** 그룹 구성원. 일부 Citrix 구성은 **Direct Access Users** 그룹 |
| 화면 해상도 | 원격 세션 기본 해상도가 작성 때와 다를 수 있음. 요소를 찾지 못하거나 다른 요소를 누를 수 있음 |
| 권한 상승 | 승격된 권한으로 실행 불가 |
| 실행 중 로그인 | 지원하지 않음. 흐름이 실패할 수 있음 |
| 주변 장치 | 오디오 · 카메라 · 웹캠 · 비디오 캡처 장치 지원 안 함 |

해상도는 흐름 세부 정보의 **편집**에서 무인 실행용 표시 해상도를 켜서 정합니다. 부모 흐름이 다른 데스크톱 흐름을 부르면 전체가 부모의 해상도로 실행됩니다.[^console]

세션 재사용을 켜면 무인 실행이 끝난 세션을 잠가 두고 다음 실행에 다시 씁니다. 포털 **모니터 › 머신**에서 대상을 고르고 그 설정에서 켭니다. 사용자가 여러 세션을 가질 수 있는 컴퓨터에서는 지원하지 않습니다.[^unattended]

무인 실패의 원인은 비디오 로그로 봅니다. 실행 모드가 무인인 작업의 고급 매개 변수에서 켭니다. Power Automate for desktop 2.66 이상이 필요합니다. 실패 전 60초를 기록하고 기본 경로 `%localappdata%\Microsoft\Power Automate Desktop\VideoLogs` 에 저장합니다.[^trigger]

---

## 바로 가기와 URL 실행

조건은 셋입니다. 컴퓨터에 Power Automate for desktop 이 설치되어 있고, 사용자가 로그인해 있고, Power Automate Premium 플랜이나 종량제 환경 사용 권한이 있어야 합니다.[^url]

바로 가기는 콘솔에서 흐름 이름을 마우스 오른쪽 단추로 눌러 **바탕 화면 바로 가기 만들기**를 고르면 생깁니다. 바탕 화면 폴더에 만들어지고 다른 폴더로 옮길 수 있습니다.

실행 URL 은 아래 네 형식입니다.

```
"ms-powerautomate:/console/flow/run?workflowName=[workflowName]"
```

```
"ms-powerautomate:/console/flow/run?workflowId=[workflowId]"
```

```
"ms-powerautomate:/console/flow/run?environmentId=[environmentId]&workflowId=[workflowId]"
```

```
"ms-powerautomate:/console/flow/run?environmentId=[environmentId]&workflowName=[workflowName]"
```

- 환경을 적지 않은 두 형식은 콘솔에서 고른 환경을 씁니다.
- 콘솔 환경과 URL 의 환경이 다르면 콘솔 환경이 바뀝니다.
- 흐름 ID 와 이름이 모두 없으면 명령을 무시합니다.
- 흐름이 이미 실행 중이면 URL 을 불러도 다시 실행되지 않습니다.

| 추가 매개 변수 | 값 | 조건 |
|---|---|---|
| `inputArguments` | 입력 변수의 외부 이름과 값을 담은 JSON | 텍스트 · 숫자 · 부울만. 부울은 소문자 `true` · `false`. 빠진 입력은 콘솔이 물음 |
| `autologin` | `true` | 현재 Windows 사용자로 로그인. 사용자가 로그아웃 상태이고 Power Automate 가 실행 중이 아닐 때. 화면에서 직접 로그아웃했으면 동작하지 않음 |
| `runId` | GUID | 이 GUID 이름의 폴더에 로그 저장 |

`inputArguments` 의 JSON 은 특수 문자를 이스케이프합니다. 큰따옴표는 `\"` 입니다.

```
"ms-powerautomate:/console/flow/run?workflowId=[workflowId]&inputArguments={\"[External name 1]\": [Value 1],\"[External name 2]\": [Value 2]}"
```

브라우저에서 부를 때는 백슬래시를 없애고 URL 인코딩을 합니다. URL 을 부르는 프로그램의 글자 수 제한을 넘으면 흐름이 실패합니다.

`runId` 의 로그 경로입니다.

```
C:\Users\[Username]\AppData\Local\Microsoft\Power Automate Desktop\Console\Scripts\[Flow ID]\Runs\[Run ID]
```

MSI 로 설치한 컴퓨터의 명령 프롬프트 표기입니다.

```
"C:\Program Files (x86)\Power Automate Desktop\dotnet\PAD.Console.Host.exe" "ms-powerautomate:/console/flow/run?workflowName=[workflowName]"
```

작업 스케줄러에서는 새 작업의 **동작** 탭에 프로그램과 인수를 나눠 넣습니다.

| 설치 방식 | 프로그램/스크립트 | 인수 추가 |
|---|---|---|
| MSI | `C:\Program Files (x86)\Power Automate Desktop\dotnet\PAD.Console.Host.exe` | `ms-powerautomate:/console/flow/run?workflowName=[workflowName]` |
| Microsoft Store | `C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe` | `-Command "Start-Process \"ms-powerautomate:/console/flow/run?workflowName=[workflowName]""` |

확인 대화 상자를 끄면 악의적으로 공유된 흐름이 알림 없이 실행될 수 있습니다.[^url]

---

## 프리미엄 기능의 구분

| 라이선스 | 범위 |
|---|---|
| 회사 또는 학교 계정 | 추가 비용 없음. 작업 · 레코더 · 콘솔 실행. 기본 환경에 Dataverse 데이터베이스 필요 |
| Power Automate 평가판 | 90일. 콘솔의 **Go 프리미엄** 또는 포털의 데스크톱 흐름 영역에서 시작 |
| Power Automate Premium | 무인 RPA · 호스트형 RPA 를 뺀 프리미엄 RPA 기능 전체 |
| Power Automate Process | 무인 실행 |
| 종량제 | Azure 구독으로 지불. 그 환경 안에서 대부분의 프리미엄 기능 |

문서가 프리미엄 RPA 기능으로 적은 목록입니다.[^premium]

| 기능 | 내용 |
|---|---|
| 자동 시작 · 예약 · 클라우드 흐름 연동 | 클라우드 흐름에서 유인 · 무인 실행을 시작 |
| 프리미엄 · 사용자 지정 커넥터 | 프리미엄 클라우드 커넥터 사용, 사용자 지정 커넥터 생성 |
| AI Builder 용량 | 사용자 지정 · 미리 빌드된 모델. 추가 기능 라이선스이고 Premium 에 일부 크레딧 포함 |
| 프로세스 마이닝 | 비즈니스 프로세스 시각화와 분석 |
| 사용자 지정 작업 | 직접 개발한 자동화 작업 |
| UI 요소 컬렉션 | UI 요소 묶음을 여러 흐름에서 공유 |
| 공유와 협업 | 공동 소유자 · 사용자 액세스로 흐름 공유 |
| 여러 환경 | 환경 격리와 역할 기반 액세스 |
| 중앙 관리와 보고 | 포털에서 흐름 관리, 자세한 실행 로그 |
| 흐름 모니터링 | 포털에서 전체 실행 모니터링 |
| 흐름 큐 관리 | 대기 중인 실행 확인, 우선순위 지정 |
| 봇 오케스트레이션 | 컴퓨터 · 컴퓨터 그룹 관리, 호스트형 RPA 봇 |
| 데스크톱 흐름 분석 | Power Platform 관리 센터의 분석 |
| 고객 지원 | Microsoft 지원 |
| 작업 큐 | 작업 항목 저장 · 우선순위 · 배분 · 처리 |
| 자격 증명 | 흐름에서 자격 증명 사용 |

이 목록 밖의 문서에도 프리미엄 조건이 있습니다. 실행 URL · 바로 가기 실행[^url], 흐름 실행 로그 접근[^console], **로그 메시지** 작업[^log]입니다.

---

## 아키텍처

클라우드에서 컴퓨터로 실행 작업을 보내지만 연결은 컴퓨터 쪽에서 엽니다.[^arch]

```
클라우드 흐름 → Power Automate 클라우드 서비스 → Azure Relay
                                                      ↑ 바깥으로 나가는 HTTPS 443
                                         컴퓨터의 UIFlowService → 세션에서 데스크톱 흐름 실행
```

| 구성 요소 | 내용 |
|---|---|
| UIFlowService | Power Automate 와 함께 설치되는 Windows 서비스. 기본 자동 시작. 사용자 `NT SERVICE\UIFlowService` 로 실행 |
| Azure Relay | 나가는 요청만으로 통신 채널을 여는 서비스. WebSocket 또는 HTTP 롱 폴링 |
| 나가는 연결 | HTTPS · 포트 443 · `*.servicebus.windows.net` |
| 들어오는 포트 | 열지 않아도 됨 |
| 대상 IP | Azure IP 범위 문서의 `ServiceBus` 항목 |
| 게이트웨이 | 데스크톱 흐름용 온-프레미스 데이터 게이트웨이는 더 이상 지원하지 않음. 직접 연결로 전환 |

연결에 넣은 자격 증명은 아래 순서로 다룹니다.

1. 컴퓨터를 등록할 때 공개 키와 개인 키를 만듭니다.
2. 등록 요청에 공개 키를 담아 클라우드에 보내고, 클라우드는 이 키를 등록 정보와 함께 저장합니다.
3. 등록이 끝나면 포털에 컴퓨터가 나타납니다. 연결을 만들기 전에는 흐름에서 쓸 수 없습니다.
4. 포털에서 연결을 만들 때 넣은 사용자 이름과 암호는 공개 키로 암호화해 저장합니다. 개인 키는 컴퓨터에만 있어 클라우드는 이를 풀지 못합니다. 연결을 지우면 저장된 값도 지워집니다.
5. 클라우드에서 실행할 때 작업에 고른 연결을 씁니다.
6. 실행 작업이 암호화된 자격 증명과 함께 컴퓨터로 갑니다. 컴퓨터가 개인 키로 풀어 그 사용자로 로그인합니다.

컴퓨터 그룹은 개인 키를 그룹 암호로 암호화해 클라우드에 저장합니다. 그룹에 들어오는 컴퓨터가 이 암호로 키를 풉니다.

---

## 샘플

콘솔에서 실행하고 흐름 속성의 실행 URL 을 읽습니다. URL 로 실행하지는 않습니다. 실행 조건이 Premium 플랜 또는 종량제 환경입니다.

흐름 `개념 연습_HGD` 를 씁니다. 없으면 [P2](p02-types.html)의 1·2번으로 만듭니다.

1. 콘솔 왼쪽 막대의 **흐름**을 누르고 `개념 연습_HGD` 의 **편집**을 누릅니다.
2. 작업 영역의 빈 곳을 한 번 누르고 `Ctrl` + `A` 로 전체를 선택합니다. 선택한 줄을 마우스 오른쪽 단추로 눌러 **삭제**를 고릅니다.
3. 작업 검색 칸에 `메시지 표시` 를 입력하고 **메시지 표시**를 끌어다 놓습니다. **표시할 메시지**에 아래를 넣고 **저장**을 누릅니다.

    ```
    콘솔에서 실행했습니다.
    ```

4. 도구 모음의 **저장**을 누르고, 바로 오른쪽의 **게시** 단추를 누릅니다.
5. 디자이너 창을 닫습니다.

    **완료 기준**: 콘솔 흐름 목록에서 `개념 연습_HGD` 의 상태가 **실행되고 있지 않음**이고 **실행** 단추가 켜져 있다.

6. `개념 연습_HGD` 의 **실행** 단추를 누릅니다.

    **완료 기준**: 디자이너 없이 `콘솔에서 실행했습니다.` 메시지 창이 뜬다.

7. 메시지 창의 **확인**을 누릅니다.
8. `개념 연습_HGD` 를 마우스 오른쪽 단추로 눌러 **속성**을 고릅니다.
9. **세부 정보** 탭을 누릅니다.

    **완료 기준**: **실행 URL** 이 `ms-powerautomate:/console/flow/run?` 으로 시작한다.

10. 속성 창을 닫습니다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: 아키텍처[^arch] · 무인 실행[^unattended] · 프리미엄 기능[^premium] · 콘솔[^console] · URL 과 바로 가기 실행[^url] · 회사 또는 학교 계정으로 시작[^freeorg] · 버전 관리[^version] · 컴퓨터 관리[^machines] · 흐름 연결[^conn] · 클라우드 흐름에서 시작[^trigger] · 커넥터 참조[^uiflow] · 실행 큐 오류[^queue] · 로그 메시지[^log]

[^arch]: **Power Automate for desktop architecture** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/pad-architecture> (2026-11-02 확인). UIFlowService · Azure Relay · 포트 · 게이트웨이 지원 종료 · 세션 자격 증명 수명 주기.
[^unattended]: **Run unattended desktop flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/run-unattended-desktop-flows> (2026-11-02 확인). 무인 실행 조건, 세션 재사용, 알려진 제한.
[^premium]: **Premium RPA features** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/premium-features> (2026-11-02 확인). 프리미엄 기능 목록, 평가판 · Premium · 종량제의 범위, 무인 실행의 Process 플랜.
[^console]: **Power Automate console** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/console> (2026-11-02 확인). 로컬 유인 실행, 콘솔 설정, 흐름 속성, 무인 실행 해상도.
[^url]: **Run desktop flows via URL or desktop shortcuts** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/run-desktop-flows-url-shortcuts> (2026-11-02 확인). 조건, URL 형식, 매개 변수, 명령 프롬프트, 작업 스케줄러, 확인 대화 상자를 끌 때의 위험.
[^freeorg]: **Get started with a work or school account** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/getting-started-freeorg> (2026-11-02 확인). 추가 비용 없이 쓰는 범위와 콘솔 실행.
[^version]: **Version control in Power Automate for desktop** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/version-control> (2026-11-02 확인). 초안 저장과 게시, 게시 단추가 꺼지는 조건.
[^machines]: **Manage machines** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/manage-machines> (2026-11-02 확인). 무인 봇과 프로세스 용량.
[^conn]: **Manage desktop flow connections** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/desktop-flow-connections> (2026-11-02 확인). 로그인으로 연결은 유인 전용이라는 것.
[^trigger]: **Trigger desktop flows from cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/trigger-desktop-flows> (2026-11-02 확인). 비디오 로그의 조건과 저장 경로.
[^uiflow]: **Desktop flows 커넥터** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/connectors/uiflow/> (2026-11-02 확인). 실행 모드와 유인 모드 매개 변수의 설명.
[^queue]: **Troubleshoot desktop flow run queue errors** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/troubleshoot/power-platform/power-automate/desktop-flows/troubleshoot-desktop-flow-run-queue-errors> (2026-11-02 확인). 유인 · 무인 세션 오류의 조건.
[^log]: **Log message action** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/logging> (2026-11-02 확인). 로그 메시지가 프리미엄 기능이라는 것.
