---
title: "C28. Outlook · Teams · SharePoint · Excel 흐름"
parent: "더 읽을거리 · Cloud Flow"
nav_order: 28
concept:
  id: C28
  grade: C
  used_in: "Lab 1 ③ 항목 만들기 · ④ 조건 · ⑥ 예약 트리거와 식 · Lab 2 ④ 행 읽기 · ⑧ 파일 만들기 · Lab 3 ① 공유 링크 · ④ 승인 메일 · ⑤ 승인 Teams"
  tokens: ["메일 보내기(V2)", "채팅 또는 채널에서 메시지 게시", "항목 만들기", "테이블에 있는 행 나열", "파일 만들기", "공유 링크 만들기"]
  sample: false
---

# C28. Outlook · Teams · SharePoint · Excel 흐름

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안. 샘플 없음. 랩이 네 앱의 작업을 조작으로 이미 다룬다.
     ⚠️ 실측할 것: 메일 본문 칸의 HTML 보기 단추. email-customization 은 </> 를 구 디자이너 탭에 적고 새 디자이너 탭은 프리릴리스 문구만 적는다. @mention 토큰 작업의 한국어 이름, Teams 게시 위치의 채널 · 그룹 채팅 라벨, Excel 리본의 자동화 탭 라벨.
     ⚠️ 문서 사이 차이: 메일 첨부 25MB(fix-connection-failures)와 메일 내용 49MB(커넥터 참조). 인라인 이미지 100KB(email-customization)와 data URI 1MB(커넥터 참조). Excel 문서의 *.xlxb 는 *.xlsb 의 오타로 보고 xlsb 로 적었다.
     설계 표의 「표에 있는 행 나열」은 Lab 2 실측 라벨 「테이블에 있는 행 나열」로 적었다. -->

> **다루는 것**: 네 앱을 흐름에서 쓸 때의 커넥터 선택, 보내는 방식, 조건과 제한
>
> **쓰는 곳**: Lab 1 `메일 보내기(V2)` · `채팅 또는 채널에서 메시지 게시` · `항목 가져오기(2개 이상)` · Lab 2 `테이블에 있는 행 나열` · `파일 만들기` · Lab 3 `파일 또는 폴더에 대한 공유 링크 만들기`

---

## Outlook

| 계정 | 커넥터 |
|---|---|
| 회사 · 학교 계정 | Office 365 Outlook |
| 개인 Microsoft 계정 | Outlook.com |

두 커넥터는 메일 · 일정 · 연락처 작업이 비슷합니다.[^email] 작업 추가 창에서 **더 보기**를 누르면 그 커넥터의 작업이 모두 보이고, 별 아이콘으로 즐겨찾기한 작업은 위에 보입니다.

메일을 꾸미고 보내는 방법입니다.[^emailc]

| 하려는 일 | 방법 |
|---|---|
| 서식 있는 본문 | 본문 칸의 HTML 보기(`</>`)에 HTML 입력 |
| Outlook에서 만든 서식 사용 | Outlook으로 본인에게 보내고 원본 보기에서 html 태그 사이를 복사해 붙여넣기 |
| 이미지 넣기 | 클라우드 저장소에 올리고 익명 URL을 본문 HTML의 이미지 `src` 로 지정 |
| 배포 목록으로 보내기 | 메일 사용 보안 그룹 · 배포 목록 주소를 받는 사람에 입력. 구성원의 그룹 사서함으로 도착 |
| 구성원 개인 사서함으로 보내기 | Microsoft Entra ID의 그룹 구성원 가져오기 뒤 각각에 적용 안에서 메일 보내기 |
| 공유 사서함 자동 회신 | Outlook 웹에서 다른 사서함을 열고 자동 회신 설정 |
| 시각을 현지 시간으로 표시 | 메일의 시각은 기본 UTC. 시간대 변환 사용. [C11](c11-datetime.html) |

Office 365 Outlook 커넥터의 조건입니다.[^outlook]

| 항목 | 내용 |
|---|---|
| 메일 내용 크기 | 최대 49MB. 문제 해결 문서는 첨부 25MB로 적음[^fixconn] |
| 연결당 5분 전송량 | 메일 보내기 작업 500MB |
| 본문 내장 이미지 | data URI 하나당 1MB. 다른 문서는 인라인 이미지 100KB로 적음[^emailc] |
| 호출 세는 법 | 메일 1통이 1건. 받는 사람 · 참조 · 숨은 참조가 여러 명이어도 1건 |
| 공유 사서함 작업 | Microsoft 365 공유 사서함만. 권한 부여 후 반영까지 약 2시간 |
| 그룹 주소 | Office 365 그룹 주소는 공유 사서함 주소로 쓸 수 없음 |
| 여러 첨부 | 파일이 깨지면 배열 변수에 첨부를 모아 지정 |
| 인증 | 서비스 주체 인증 미지원 |

---

## Teams

메시지는 **채팅 또는 채널에서 메시지 게시** 작업으로 보냅니다. 다음으로 게시 칸이 보내는 사람을, 게시 위치 칸이 받는 곳을 정합니다.[^teamsend]

| 다음으로 게시 | 게시 위치 | 추가로 고르는 칸 | 쓰는 때 |
|---|---|---|---|
| 흐름 봇 | 채널 | 팀 · 채널 | 특정 사용자와 묶지 않는 채널 공지 |
| 흐름 봇 | 그룹 채팅 | 그룹 채팅 | 그룹 채팅 알림 |
| 흐름 봇 | 흐름 봇과 채팅 | Recipient | 한 사람에게 보내는 알림 |
| 사용자 | 채널 | 팀 · 채널 | 연결에 로그인한 사용자 이름으로 게시 |
| 사용자 | 그룹 채팅 | 그룹 채팅 | 연결에 로그인한 사용자 이름으로 게시 |
| Microsoft Copilot Studio 에이전트 | 에이전트와 채팅 | Recipient | 에이전트 이름으로 보내는 알림 |

흐름 봇 메시지의 보낸 사람은 Teams에 **워크플로**로 보입니다(2026-10-05 실측).

자주 쓰는 구성입니다.

| 하려는 일 | 구성 |
|---|---|
| 새 그룹 채팅에 게시 | 채팅 만들기 작업을 먼저 두고, 게시 작업의 그룹 채팅에 사용자 지정 값으로 Conversation ID 지정 |
| 사용자 멘션 | 사용자의 @mention 토큰 가져오기 작업을 먼저 두고, 메시지에 그 토큰 삽입. 작업 하나에 사용자 한 명 |
| 메시지 안의 줄바꿈과 링크 | 메시지 칸의 코드 보기에 `<br>` · `<a href>` 입력[^teamsfmt] |
| 메시지에서 흐름 시작 | Teams 메시지 선택 트리거. 기본 환경에서만 동작 |
| 적응형 카드 | 카드를 게시하고 응답을 받는 작업과 트리거 사용[^teamsov] |

조건과 제한입니다.[^teams]

| 항목 | 내용 |
|---|---|
| 라이선스 | Teams에서 흐름을 쓰는 데 추가 라이선스 없음[^teamsov] |
| 메시지 크기 | 약 28KB. HTML · 이미지 · 링크 · 표 · 멘션 포함. 넘으면 `Request Entity too large` |
| 프라이빗 채널 | 게시 불가 |
| 그룹 채팅 목록 | 최근 50개만 표시[^teamsend] |
| 멘션 | 사용자만. 채널 · 팀 불가. 메시지당 사용자 20명 · 태그 20개 |
| 긴급 · 중요 표시 | 설정 불가[^teamsend] |
| 채팅 만들기 | 채팅당 20명까지. 게스트 미지원 |
| Workflows 앱 | Teams 관리 센터에서 허용되어 있어야 함 |
| 흐름 봇 | 상용 테넌트만. 정부 클라우드 미지원 |
| 기본 환경 전용 트리거 | 메시지 선택 · 작성 상자 · 적응형 카드 응답 |
| 폴링 간격 | 새 채널 메시지 · 채널 메시지 멘션 3분, 팀 구성원 추가 · 제거 5분 |
| 키워드 트리거 | 한 단어만 |
| 채널 메시지 트리거 | 최상위 메시지만. 답글에서는 실행되지 않음 |

---

## SharePoint

흐름에서 많이 쓰는 시나리오는 승인, 파일과 목록 관리, 예전 워크플로의 전환입니다. 트리거로 목록 · 라이브러리의 변경을 감지하고 40개가 넘는 작업으로 다룹니다.[^spov]

조건과 제한입니다.[^sp]

| 항목 | 내용 |
|---|---|
| 지원 목록 | 일반 목록과 일반 문서 라이브러리만. 공지 · 연락처 · 일정 · 작업 템플릿 미지원 |
| 목록 이름 | 이름에 마침표가 있으면 동적 값으로 넣을 때 오류. 드롭다운에서 고르거나 ID 사용 |
| 첨부 | 목록 항목 첨부 최대 90MB |
| 선택한 파일 · 항목 트리거 | SharePoint의 자동화 메뉴에는 기본 환경의 흐름만 표시 |
| 파일 트리거 | 하위 폴더의 파일 변경에서는 실행되지 않음. 필요하면 흐름을 여러 개 둠[^trigger] |
| 트리거 동시성 | 켠 뒤 끌 수 없음. [C26](c26-trigger-conditions.html) |
| 게스트 | 커넥터 작업의 드롭다운 목록을 볼 수 없음 |
| 조건부 액세스 | SharePoint와 Power Automate의 요구 조건이 다르면 목록에서 흐름을 열 때 인증 오류[^spov] |
| 결과가 불완전할 때 | 위임 한도가 원인일 수 있음. 건수 한도는 [C14](c14-limits.html) |
| 열 이름 | 표시 이름과 내부 이름이 다름. [C13](c13-filter.html) |

---

## Excel

Excel을 흐름과 잇는 경로는 두 가지입니다.

| 경로 | 시작하는 곳 | 만들어지는 환경 | 조건 |
|---|---|---|---|
| Excel 안에서 만들기[^xlflow] | Excel 리본의 자동화 탭 › 작업 자동화에서 템플릿 선택 | 항상 기본 환경 | Excel 웹 · 데스크톱. Mac 제외. 기본 환경의 흐름만 목록에 표시 |
| 흐름에서 파일 읽기와 쓰기[^excel] | Excel Online (Business) 커넥터 작업 | 흐름이 있는 환경 | 아래 표 |

Excel Online (Business) 커넥터의 조건과 제한입니다.[^excel]

| 항목 | 내용 |
|---|---|
| 파일 형식 | xlsx · xlsb |
| 파일 크기 | 최대 25MB |
| 요청 크기 | 요청당 최대 5MB |
| 행 나열 건수 | 기본 256행. 전체를 읽으려면 페이지 매김 설정 |
| 열 수 | 처음 500열. 필요한 열은 Select Query로 지정 |
| 필터 쿼리 함수 | `eq` · `ne` · `contains` · `startswith` · `endswith`. 열 하나에 함수 하나 |
| 정렬 | 열 하나 |
| 열 이름 | Filter Query · Order By · Select Query는 영숫자 열 이름만 |
| 파일 잠금 | 커넥터를 마지막으로 쓴 뒤 최대 6분 동안 수정 · 삭제가 잠길 수 있음 |
| 동시 쓰기 | 여러 클라이언트의 동시 수정은 지원하지 않음. 데이터 불일치 가능 |
| 권한 | 읽기 작업에도 파일 쓰기 권한 필요. 없으면 403. 읽기 전용 파일은 502 |
| 쓰기 반영 | 행 추가 · 수정 · 삭제는 성공 후 최대 30초 지연 |
| 키 열 | 대소문자 구분. 여러 행이 일치하면 첫 행만 수정 · 삭제 |
| 숨긴 열 | 표에 숨긴 열이 있으면 OData 매개 변수 사용 불가 |
| 기존 필터 | Excel에 걸어 둔 필터는 작업에 필터를 지정하지 않으면 무시됨. 지정하면 그 위에 추가됨 |
| 피벗 테이블 | 지원하지 않음 |
| 숫자만 있는 열 머리글 | 행 수정 · 삭제에서 예기치 않은 동작. 다른 글자를 포함하도록 변경 |
| 파일 버전 | 읽기 작업만 돌려도 버전 기록에 새 버전이 생길 수 있음 |
| 스크립트 실행 | 10초에 3회, 하루 1,600회 |
| 파일 선택기 | 폴더당 200개까지 표시 |

응답의 열 이름에서 일부 문자는 OData에 맞게 바뀝니다.

| 문자 | 바뀐 값 |
|---:|---|
| `.` | `_x002e_` |
| `@` | `_x0040_` |
| `:` | `_x003a_` |
| `#` | `_x0023_` |

수식이 복잡하거나 행이 많은 통합 문서는 다시 계산 때문에 시간 초과가 나고, 재시도로 데이터가 중복 삽입될 수 있습니다. 수식을 줄이거나 계산 모드를 수동으로 둡니다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다.

- **문헌**: Outlook 개요[^email] · 메일 사용자 지정[^emailc] · Office 365 Outlook 커넥터[^outlook] · 연결 오류 수정[^fixconn] · Teams 개요[^teamsov] · Teams에 메시지 보내기[^teamsend] · Teams 커넥터[^teams] · Teams 메시지 서식[^teamsfmt] · SharePoint 개요[^spov] · SharePoint 커넥터[^sp] · 트리거 문제 해결[^trigger] · Excel과 흐름[^xlflow] · Excel Online 커넥터[^excel]

[^email]: **Overview of using Outlook and Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/email-overview> (2026-11-02 영어판 확인). 커넥터 선택, 작업 찾기.
[^emailc]: **Customize email in flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/email-customization> (2026-11-02 영어판 확인). HTML 본문, 이미지, 배포 목록, 자동 회신, UTC.
[^outlook]: **Office 365 Outlook** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/office365/> (2026-11-02 영어판 확인). General Limits와 알려진 제한.
[^fixconn]: **Fix connection failures in cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/fix-connection-failures> (2026-11-02 영어판 확인). Outlook 첨부 25MB.
[^teamsov]: **Use flows in Microsoft Teams** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/teams/overview> (2026-11-02 영어판 확인). 시나리오와 라이선스.
[^teamsend]: **Send a message in Teams using Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/teams/send-a-message-in-teams> (2026-11-02 영어판 확인). 보내는 사람과 받는 곳의 조합, 새 그룹 채팅, 멘션, 알려진 제한.
[^teams]: **Microsoft Teams** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/teams/> (2026-11-02 영어판 확인). 메시지 크기, 트리거 제한, 프라이빗 채널, 멘션 수.
[^teamsfmt]: **Format agent messages** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/microsoftteams/platform/bots/how-to/format-your-bot-messages> (2026-11-02 영어판 확인). 기본 서식의 `<br>` · `<a href>`.
[^spov]: **Use SharePoint and Power Automate to build workflows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/sharepoint-overview> (2026-11-02 영어판 확인). 시나리오, 작업 수, 조건부 액세스.
[^sp]: **SharePoint** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/sharepointonline/> (2026-11-02 영어판 확인). 일반 제한과 Power Automate 절.
[^trigger]: **Troubleshoot Power Automate trigger problems and errors** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/troubleshoot/power-platform/power-automate/flow-run-issues/triggers-troubleshoot> (2026-11-02 영어판 확인). SharePoint 하위 폴더.
[^xlflow]: **Use flows with Excel** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/flows-excel> (2026-11-02 영어판 확인). Excel 안에서 만들기, 기본 환경 제한.
[^excel]: **Excel Online (Business)** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/excelonlinebusiness/> (2026-11-02 영어판 확인). 작업별 제한, 일반 제한, 열 이름 처리.
