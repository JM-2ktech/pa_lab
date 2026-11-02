---
title: "P24. 클라우드 흐름에서 호출"
parent: "개념 9. 실행과 운영"
nav_order: 24
concept:
  id: P24
  grade: B
  used_in: "랩에서 쓰지 않음"
  tokens: []
  sample: true
---

# P24. 클라우드 흐름에서 호출

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. 클라우드 흐름 부분은 프리미엄 라이선스와 컴퓨터 등록이 필요해 샘플에 넣지 않았다. 샘플은 입력 · 출력 변수를 콘솔에서 실행하는 데까지다.
     변수 창의 + · 입력 · 출력 묶음은 Lab 4 15번 화면에서 확인했다. 새 입력 변수 · 외부 이름 · 민감함으로 표시 · 선택 사항으로 표시 · 흐름 입력 · JSON 편집기는 이 PC 의 PAD 한국어 리소스에서 확인했고 화면은 보지 않았다.
     ⚠️ 실측할 것: 새 입력 변수 창의 저장 단추와 흐름 입력 창의 확인 단추 라벨, 외부 이름에 한글이 되는가, 변수 설정의 변수 칸에 출력 변수 이름을 넣는 방식.
     ⚠️ 실측할 것: 포털 작업의 한국어 이름. ko-kr 문서가 세 가지로 적는다 — 데스크톱용 Power Automate 사용하여 빌드된 흐름 실행 / Power Automate for desktop으로 빌드된 흐름 실행 / 데스크톱용 Power Automate로 빌드된 흐름 실행. 본문은 마지막 표기를 썼다.
     ⚠️ 문서에 없는 것: 데이터 테이블 기본값의 JSON 편집기 형식. 클라우드 흐름 쪽 JSON 만 문서에 있어 샘플에서 뺐다. 출력 변수를 뒤 작업이 동적 콘텐츠로 읽는다는 표현은 교육 모듈의 스크린샷 설명이고 커넥터 참조는 동적 출력이라고만 적는다.
     ko-kr trigger-desktop-flows 는 Asynchronous Pattern 을 「동기 패턴」으로 옮겼다. 본문은 영어판을 따랐다. -->

> **다루는 것**: 클라우드 흐름에서 데스크톱 흐름을 실행하는 필수 조건, 입력 · 출력 변수와 데이터 테이블로 값을 주고받는 방법
>
> **쓰는 곳**: 랩에서 쓰지 않음

---

## 필수 조건

문서가 적은 조건은 넷입니다.[^trigger]

| 조건 | 내용 |
|---|---|
| 컴퓨터 | 데스크톱 흐름을 실행할 등록된 컴퓨터 또는 컴퓨터 그룹 |
| 계정 | 회사 또는 학교 계정 |
| 연결 | 구성된 데스크톱 흐름 연결 |
| 라이선스 | 유인 실행은 해당 라이선스, 무인 실행은 무인 추가 기능. 연결을 만든 사용자에게 필요 |

작업이 속한 Desktop flows 커넥터는 프리미엄 등급입니다.[^uiflow] 무료 사용자가 이 작업을 추가하면 평가판을 시작하라는 메시지가 뜹니다.[^premium] 버전 관리가 켜진 환경에서는 게시한 버전이 클라우드에서 실행됩니다.[^version]

---

## 컴퓨터 등록

Power Automate machine runtime 앱에 로그인하면 현재 환경에 컴퓨터가 등록됩니다. 설치할 때 machine runtime 앱 설치 옵션을 고릅니다.[^machines]

| 조건 | 내용 |
|---|---|
| 버전 | Power Automate 2.8.73.21119 이상 |
| Windows | Windows 10 Home · Windows 11 Home 은 직접 연결 불가 |
| 환경 | `MicrosoftFlowExtensionsCore` 솔루션 1.2.4.1 이상. Teams 환경에는 등록 불가 |
| 역할 | Environment Maker 또는 Desktop Flow Machine Owner |
| 네트워크 | 문서 「Desktop flow services required for runtime」의 서비스에 접근 가능 |
| 보안 | 컴퓨터를 보호하고 컴퓨터 관리자를 신뢰할 수 있어야 함 |

- 컴퓨터 하나는 한 번에 한 환경의 흐름만 클라우드에서 실행합니다.
- 실행 환경을 바꾸면 그 컴퓨터의 연결이 모두 지워집니다.
- PC 를 초기화하면 등록이 사라집니다.
- 가상 컴퓨터는 machine runtime 을 설치한 뒤 복제하지 않습니다.

---

## 데스크톱 흐름 연결

포털에서 **데이터 › 연결 › 새 연결**을 누르고 `Desktop flows` 를 검색합니다. 흐름에서 작업을 추가할 때도 연결이 없으면 만들라고 묻습니다.[^conn]

| 방식 | 값 | 실행 모드 | 조건 |
|---|---|---|---|
| 사용자 이름과 암호 | 컴퓨터 또는 그룹 · 도메인과 사용자 이름 · 암호 | 유인 · 무인 | 자격 증명으로 바꾸려면 Azure Key Vault 또는 CyberArk(미리 보기) |
| 로그인으로 연결 | 컴퓨터 또는 그룹 · Microsoft Entra 계정 | 유인만 | 같은 테넌트, Entra 조인 또는 AD 도메인 조인, 사용자 세션 열림 |
| 서비스 주체 실행 소유자 | 컴퓨터 또는 그룹 · 사용자 계정 · 암호 · 클라이언트 ID · 인증서 | 문서에 표기 없음 | 커넥터 참조에 있는 인증 형식[^uiflow] |

사용자 이름 표기는 로컬 계정 `MACHINENAME\User` · `local\User`, 도메인 계정 `DOMAIN\User`, Entra 계정 `username@domain.com` 입니다.

- 로그인으로 연결은 대기 시간이 1시간으로 제한됩니다.
- AD 조인만 된 컴퓨터는 테넌트를 허용 목록에 넣어야 합니다. 넣지 않으면 `UnallowedTenantForConnectWithSignIn` 으로 실패합니다.
- 연결은 다른 사용자와 공유하지 못합니다. 공유 대상은 서비스 주체 사용자뿐이고 권한은 사용 또는 편집입니다.
- 연결을 만들면 Power Automate 가 그 컴퓨터에 Windows 세션을 만들 수 있게 됩니다. 흐름의 공동 소유자를 신뢰할 수 있어야 합니다.[^machines]

---

## 호출 순서

1. 클라우드 흐름을 만듭니다. 인스턴트 또는 자동화 흐름입니다.[^trigger]
2. 작업 검색에 `Power Automate for desktop` 을 입력하고 **데스크톱용 Power Automate로 빌드된 흐름 실행**을 고릅니다.
3. 연결이 없으면 만듭니다.
4. 실행 모드(유인 · 무인)를 고릅니다.
5. **데스크톱 흐름**에서 기존 흐름을 고릅니다.
6. 새로 만들려면 **새 데스크톱 흐름 만들기**를 고르고 이름을 넣은 뒤 「앱 시작」을 누릅니다.
7. 브라우저가 Power Automate 를 열지 물으면 **열기**를 누릅니다.
8. 데스크톱 흐름의 입력 변수가 작업의 칸으로 나타납니다. 값을 넣습니다.
9. 뒤에 오는 작업에서 출력 변수의 값을 읽습니다.[^module]

| 작업 매개 변수 | 키 | 필수 | 내용 |
|---|---|---|---|
| 데스크톱 흐름 | `uiFlowId` | 예 | 실행할 흐름 |
| 실행 모드 | `runMode` | 예 | 유인 또는 무인 |
| 유인 모드 | `runSession` | | 유인일 때 데스크톱 또는 Picture-in-Picture |
| 비디오 로그 | `videoLogger` | | 무인일 때 비디오 로그 켜기 · 끄기 |
| 우선순위 | `runPriority` | | 실행 우선순위 |
| 입력 | `item` | 예 | 입력 변수의 값. 동적 |

작업의 출력도 동적입니다.[^uiflow]

---

## 입력 변수와 출력 변수

| 방향 | 변수 | 주는 쪽 | 받는 쪽 |
|---|---|---|---|
| 클라우드 → 데스크톱 | 입력 변수 | 작업의 입력 칸 | 데스크톱 흐름의 입력 변수 |
| 데스크톱 → 클라우드 | 출력 변수 | 데스크톱 흐름의 출력 변수 | 뒤에 오는 작업 |
| 데스크톱 → 데스크톱 | 입력 · 출력 변수 | **데스크톱 흐름 실행** 작업 | 호출한 흐름과 호출된 흐름 |
| 콘솔 → 데스크톱 | 입력 변수 | **흐름 입력** 창 | 데스크톱 흐름의 입력 변수 |

변수 창의 **+** 를 누르고 「입력」 또는 「출력」을 고르면 대화 상자가 열립니다.[^vars]

| 칸 | 입력 변수 | 출력 변수 | 내용 |
|---|---|---|---|
| 변수 이름 | 필수 | 필수 | 데스크톱 흐름 안의 이름 |
| 데이터 형식 | 필수 | 필수 | 텍스트 · 숫자 · 부울 · 사용자 지정 개체 · 목록 · 데이터 테이블 · 인스턴스 · 세션 |
| 기본값 | 있음 | 없음 | 디자이너 · 콘솔 실행에 쓰는 값 |
| 데이터 하위 형식 | 있음 | 있음 | 인스턴스 · 세션일 때 브라우저 · Excel · Word · Outlook · Access · Terminal |
| 외부 이름 | 필수 | 필수 | 클라우드 흐름 디자이너와 **흐름 입력** 창에 보이는 이름 |
| 설명 | 있음 | 있음 | 호출할 때 보이는 설명 |
| 민감함으로 표시 | 있음 | 있음 | [P26](p26-sensitive.html) |
| 선택 사항으로 표시 | 있음 | 문서 표에 없음 | 빈 값을 허용 |

- 기존 흐름 변수의 이름을 고르면 두 변수를 병합할지 묻습니다. 의도하지 않은 병합은 흐름 오류의 원인이 됩니다.
- 기존 입력 · 출력 변수의 이름은 쓸 수 없습니다.
- 외부 이름을 따로 두면 기존 변수 이름과 충돌하지 않고, 클라우드 쪽 화면에 맞는 이름을 쓸 수 있습니다.[^module]
- 인스턴스 · 세션 형식의 입력 변수는 기본값이 없습니다. **데스크톱 흐름 실행** 작업이나 디자이너에서만 실행합니다.
- 입력 · 출력 변수의 브라우저 인스턴스는 Edge · Chrome · Firefox 입니다.

입력 변수는 기본이 필수입니다. 디버깅에 쓸 기본값과 실행 때 받을 같은 형식의 값이 있어야 합니다. 선택 사항으로 표시하면 둘 다 생략할 수 있습니다. 빈 값을 기본값으로 두는 조작은 형식마다 다릅니다.

| 형식 | 빈 기본값을 만드는 조작 |
|---|---|
| 텍스트 · 숫자 | **기본값** 칸을 비움 |
| 부울 | **기본값**을 `<공백>` 으로 둠 |
| 사용자 지정 개체 · 목록 · 데이터 테이블 | **기본값** 옆 **편집** › **JSON 편집기** 켬 › 내용을 모두 지움 › **저장** |

---

## 데이터 테이블 전달

클라우드 흐름에서 표 모양의 값을 넘기는 순서입니다.[^datatable]

1. 데스크톱 흐름에 데이터 테이블 형식의 입력 변수를 만듭니다.
2. 클라우드 흐름에서 배열 형식 변수를 초기화합니다. 값은 객체의 배열(JSON)입니다.
3. 그 변수를 **데스크톱용 Power Automate로 빌드된 흐름 실행** 작업의 입력 값으로 넣습니다.

객체 하나가 행 하나이고, 키가 열 이름입니다.

```json
[
  { "공고번호": "A-1", "추정가격": "1000" },
  { "공고번호": "A-2", "추정가격": "2000" }
]
```

데스크톱 흐름에서는 [P4](p04-index.html)의 표기로 읽습니다.[^types]

```
%입력_공고표[0]['추정가격']%
```

---

## 민감한 값

입력 변수에 민감한 데이터가 들어가면 로그에서 가리거나 뺍니다.[^trigger] 클라우드 흐름 쪽 설정은 아래와 같습니다.[^secure] 데스크톱 흐름 쪽은 [P26](p26-sensitive.html)에서 다룹니다.

| 설정 | 위치 | 동작 |
|---|---|---|
| **보안 입력** · **보안 출력** | 작업 **…** › **설정** | 값을 로그에 보이지 않음. 작업에 잠금 아이콘 표시 |
| **보안 텍스트** | 데스크톱 흐름으로 넘기는 입력의 **설정** | 넘기는 값을 민감한 입력으로 처리 |

---

## 제한

| 항목 | 값 |
|---|---|
| 연결당 실행 | 분당 70회[^trigger] |
| 입력 크기 | 2MB. 중국 지역은 1MB[^trigger] |
| 연결당 API 호출 | 60초에 700회[^uiflow] |
| 연결당 Get 외 요청 | 3,600초에 300회[^uiflow] |
| 큐 대기 | 최대 12시간[^machines] |
| 실행 시간 | 제한 없음[^machines] |
| 그룹당 컴퓨터 | 최대 50대[^machines] |

작업 설정에서 **Asynchronous Pattern** 을 끄면 부모 클라우드 흐름을 취소해도 자식 데스크톱 흐름이 멈추지 않습니다.[^trigger]

---

## 샘플

클라우드 흐름 없이 입력 · 출력 변수를 만들고 콘솔에서 실행합니다. **흐름 입력** 창에는 클라우드 흐름 디자이너와 같은 외부 이름이 보입니다.

흐름 `개념 연습_HGD` 를 씁니다. 없으면 [P2](p02-types.html)의 1·2번으로 만듭니다.

1. 콘솔 왼쪽 막대의 **흐름**을 누르고 `개념 연습_HGD` 의 **편집**을 누릅니다.
2. 작업 영역의 빈 곳을 한 번 누르고 `Ctrl` + `A` 로 전체를 선택합니다. 선택한 줄을 마우스 오른쪽 단추로 눌러 **삭제**를 고릅니다.
3. 오른쪽 세로 막대의 **{x}** 를 눌러 변수 창을 엽니다. **+** 를 누르고 **입력**을 고릅니다.
4. **변수 이름** · **기본값** · **외부 이름**에 아래를 차례로 넣습니다. **데이터 형식**은 텍스트로 두고 **저장**을 누릅니다.

    ```
    입력_거래처
    ```

    ```
    V1003
    ```

    ```
    거래처
    ```

5. **+** 를 누르고 **출력**을 고릅니다. **변수 이름** · **외부 이름**에 아래를 차례로 넣습니다. **데이터 형식**은 텍스트로 두고 **저장**을 누릅니다.

    ```
    출력_결과
    ```

    ```
    결과
    ```

    **완료 기준**: 변수 창의 **입력** 묶음에 `입력_거래처`, **출력** 묶음에 `출력_결과` 가 있다.

6. 작업 검색 칸에 `변수 설정` 을 입력하고 **변수 설정**을 끌어다 놓습니다. **변수**와 **값**에 아래를 차례로 넣고 **저장**을 누릅니다.

    ```
    출력_결과
    ```

    ```
    %입력_거래처% 처리 완료
    ```

7. 작업 검색 칸에 `메시지 표시` 를 입력하고 **메시지 표시**를 1번 줄 아래로 끌어다 놓습니다. **표시할 메시지**에 아래를 넣고 **저장**을 누릅니다.

    ```
    %출력_결과%
    ```

8. 도구 모음의 **실행**(▶)을 누릅니다.

    **완료 기준**: 메시지 창에 `V1003 처리 완료` 가 뜬다. 기본값이 쓰인 결과다.

9. 메시지 창의 **확인**을 누릅니다. 도구 모음의 **저장**을 누르고, 바로 오른쪽의 **게시** 단추를 누릅니다. 디자이너 창을 닫습니다.
10. 콘솔 흐름 목록에서 `개념 연습_HGD` 의 **실행** 단추를 누릅니다.

    **완료 기준**: **흐름 입력** 창에 외부 이름 `거래처` 가 보인다.

11. `거래처` 칸에 아래를 넣고 확인 단추를 누릅니다.

    ```
    V1007
    ```

    **완료 기준**: 메시지 창에 `V1007 처리 완료` 가 뜬다.

12. 메시지 창의 **확인**을 누릅니다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: 클라우드 흐름에서 시작[^trigger] · 데이터 테이블 전달[^datatable] · 변수 창[^vars] · 컴퓨터 관리[^machines] · 흐름 연결[^conn] · 커넥터 참조[^uiflow] · 프리미엄 기능[^premium] · 버전 관리[^version] · 변수 데이터 형식[^types] · 민감한 입력 관리[^secure] · 교육 모듈[^module]

[^trigger]: **Trigger desktop flows from cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/trigger-desktop-flows> (2026-11-02 확인). 필수 조건 넷, 호출 순서, 입력 크기, 연결당 실행 수, 부모 취소의 제한. 한국어판은 Asynchronous Pattern 을 「동기 패턴」으로 적어 영어판을 따랐다.
[^datatable]: **Pass a datatable from a cloud flow to a desktop flow** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/how-to/passing-datatable> (2026-11-02 확인). 데이터 테이블 입력 변수와 객체 배열 JSON.
[^vars]: **Manage variables and the variables pane** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/manage-variables> (2026-11-02 확인). 입력 · 출력 변수의 칸, 병합, 인스턴스 입력, 선택적 입력과 빈 기본값.
[^machines]: **Manage machines** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/manage-machines> (2026-11-02 확인). 컴퓨터 등록 조건, 환경 변경, 세션 신뢰, 대기와 실행 시간, 그룹 크기.
[^conn]: **Manage desktop flow connections** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/desktop-flow-connections> (2026-11-02 확인). 연결 만드는 경로, 두 방식, 로그인으로 연결의 조건과 제한, 공유 범위.
[^uiflow]: **Desktop flows 커넥터** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/connectors/uiflow/> (2026-11-02 확인). 프리미엄 등급, 인증 형식, 작업 매개 변수, 호출 제한.
[^premium]: **Premium RPA features** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/premium-features> (2026-11-02 확인). 작업을 추가할 때의 평가판 안내.
[^version]: **Version control in Power Automate for desktop** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/version-control> (2026-11-02 확인). 게시한 버전이 콘솔 · 클라우드에서 실행된다는 것.
[^types]: **Variable data types** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/variable-data-types> (2026-11-02 확인). 데이터 테이블의 행 번호와 열 이름 표기.
[^secure]: **Manage sensitive input like passwords** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/how-tos-use-sensitive-input> (2026-11-02 확인). 보안 입력 · 보안 출력 · 보안 텍스트.
[^module]: **Run a Power Automate desktop flow from a cloud flow** — Microsoft Learn 교육 모듈. <https://learn.microsoft.com/ko-kr/training/modules/pad-powerautomate/2-run-pad-flows-power-automate> (2026-11-02 확인). 외부 이름의 쓰임, 클라우드 작업이 출력 변수를 읽는다는 것.
