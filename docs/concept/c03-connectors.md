---
title: "C3. 커넥터 · 작업 · 연결"
parent: "개념 1. 흐름의 구성"
nav_order: 3
concept:
  id: C3
  grade: A
  used_in: "Lab 1 ③ 항목 만들기 · ④ 조건 · ⑥ 예약 트리거와 식 · Lab 2 ④ 행 읽기 · ⑧ 파일 만들기 · Lab 3 ② 승인 요청"
  tokens: ["연결 만들기", "작업 추가", "기본 제공 도구", "Office 365 Outlook", "Microsoft Teams", "Excel Online"]
  sample: true
---

# C3. 커넥터 · 작업 · 연결

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행.
     ⚠️ 실측할 것: 연결 화면의 경로. add-manage-connections 는 「데이터 › 연결」, getting-started 와 triggers-troubleshoot 는 「더보기 › 연결」로 적었다. 샘플은 더보기로 썼다. 세부 정보 · 이 연결을 사용하는 흐름 라벨도 한국어판 기준이다.
     ⚠️ 실측할 것(공용 계정): 교육 계정 edu@2ktech.co.kr 하나를 함께 쓸 때 연결 목록이 몇 줄로 보이는지, 다른 수강생이 만든 연결을 다시 고르게 되는지, Lab 1 16번의 연결 만들기 창이 언제 뜨지 않는지. 문서에 공용 계정 설명이 없어 본문에 단정하지 않았다. 샘플 완료 기준도 줄 수를 적지 않았다.
     ⚠️ 작업 추가 창에 프리미엄 표시가 어떻게 보이는지 실측. 문서가 확인해 주는 것은 커넥터 목록의 PREMIUM 표시와 커넥터 문서의 Class 행이다.
     문서의 표준 승인 커넥터 영문 이름은 Standard approvals 다(Lab 3 실측 라벨 「표준 승인」과 같다). -->

> **다루는 것**: 커넥터 · 트리거 · 작업 · 연결의 구분, 작업 추가 창, 표준과 프리미엄 등급, 연결 관리와 연결이 깨지는 경우
>
> **쓰는 곳**: Lab 1 16번 SharePoint › 항목 만들기와 연결 만들기 · 24번 기본 제공 도구 › 컨트롤 · 27번 Microsoft Teams · 30번 Office 365 Outlook · Lab 2 17번 Excel Online(Business) · Lab 3 8번 표준 승인

---

## 네 가지 이름

| 이름 | 뜻 | 화면에서 보이는 곳 | 예 |
|---|---|---|---|
| 커넥터 | 서비스 하나를 쓰도록 트리거와 작업을 묶은 것 | **작업 추가** 창의 묶음 제목 | SharePoint · Office 365 Outlook |
| 트리거 | 흐름을 시작하는 이벤트 | 캔버스 맨 위 카드 | 수동으로 흐름 트리거 |
| 작업 | 트리거 뒤에 하는 일. 조회 · 쓰기 · 수정 · 삭제 | 캔버스의 카드 | 항목 만들기 · 메일 보내기(V2) |
| 연결 | 커넥터를 특정 계정으로 쓰기 위한 인증 정보 | 구성 창 아래의 연결 표시 | `edu@2ktech.co.kr에 연결했습니다.` |

각 커넥터는 작업과 트리거의 집합을 제공합니다.[^architecture] 연결은 Power Automate 와 외부 서비스를 잇습니다. 흐름은 이 연결로 사용자를 대신해 작업합니다.[^solution] 같은 연결을 쓰는 작업이 여럿이면 연결을 바꿀 때 해당 작업을 모두 고칩니다.[^solution]

---

## 작업 추가 창

캔버스의 **+** › **작업 추가**를 누르면 구성 창이 네 구역으로 열립니다.[^actions]

| 구역 | 담긴 것 |
|---|---|
| 즐겨찾기 | 별표를 누른 커넥터 · 작업 · 범주 |
| AI 기능 | AI 기능 묶음 |
| 기본 제공 도구 | 변수 · 반복 · 조건 같은 흐름의 구성 요소 |
| 커넥터별 | 전체 커넥터 목록. 많이 쓰는 20개가 위쪽 |

**기본 제공 도구** 아래에는 컨트롤(조건)과 데이터 작업(작성 · 배열 필터링)이 있습니다. 이 작업들을 놓을 때는 연결 만들기 창이 뜨지 않습니다.

이름이 같은 작업이 여러 커넥터에 있습니다. 예를 들어 파일 만들기는 SharePoint 와 비즈니스용 OneDrive 양쪽에 있습니다. 검색 결과에서 커넥터 제목을 확인하고 고릅니다. 목록에 없는 작업은 더 보기를 누릅니다.[^work]

---

## 커넥터의 종류와 등급

커넥터는 만든 쪽과 등급으로 나뉩니다.[^overview][^licenses] 라이선스별 포함 여부는 [C1](c01-map.html)의 표에 있습니다.

| 구분 | 종류 | 내용 |
|---|---|---|
| 만든 쪽 | 미리 만든 커넥터 | 수정 없이 사용 |
| 만든 쪽 | 사용자 지정 커넥터 | 직접 만들어 등록 |
| 등급 | 표준 | 표준 커넥터 권한으로 사용 |
| 등급 | 프리미엄 | 프리미엄 커넥터 권한이 필요 |

프리미엄 커넥터를 쓰는 흐름을 편집하거나 수동으로 시작하려면 사용자마다 Power Automate Premium 또는 Process 라이선스가 필요합니다.[^trouble] 커넥터 등급은 Power Automate 의 커넥터 목록에서 이름 아래 *PREMIUM* 표시로 확인하거나, 커넥터 문서의 Class 행에서 확인합니다.[^trouble][^approvals]

이 과정에서 쓰는 커넥터입니다. 다섯 개 모두 표준 등급 목록에 있습니다.[^standard][^approvals]

| 커넥터 | 등급 | 작업 예 |
|---|---|---|
| SharePoint | 표준 | 항목 만들기 · 항목 가져오기(2개 이상) · 파일 만들기 |
| Office 365 Outlook | 표준 | 메일 보내기(V2) |
| Microsoft Teams | 표준 | 채팅 또는 채널에서 메시지 게시 |
| Excel Online(Business) | 표준 | 테이블에 있는 행 나열 |
| 표준 승인 | 표준 | 승인 시작 및 대기 |

프리미엄 목록의 예는 SQL Server · Microsoft Dataverse · Salesforce · Azure Key Vault · Desktop flows 입니다.[^premium]

---

## 연결

연결에는 외부 서비스에 접근할 때 필요한 인증 정보가 들어 있습니다.[^solution] 연결에 딸린 자격 증명은 커넥터 플랫폼의 자격 증명 저장소에 저장됩니다.[^architecture] 보통 연결은 한 번 로그인하면 관리자가 제거할 때까지 계속 쓸 수 있습니다.[^trouble]

연결을 만드는 경로는 둘입니다. 흐름에 커넥터 작업을 처음 놓을 때 뜨는 **연결 만들기** 창, 그리고 연결 목록의 새 연결입니다.[^connections] 인증 방식이 여러 개인 커넥터도 있습니다. 예를 들어 SQL Server 는 Microsoft Entra ID · SQL Server 인증 · Windows 인증 · 연결 문자열을 지원합니다.[^logicflow]

연결에 붙는 조건입니다.[^connections][^approvals][^solution][^trouble]

| 항목 | 내용 |
|---|---|
| 연결 목록 | 내가 만든 연결을 모아 보는 화면 |
| Power Apps | 연결을 공유. 한쪽에서 만들거나 고치거나 지우면 양쪽에 반영 |
| 계정 | 조직 정책에 따라 Power Automate 로그인 계정과 같은 계정으로 연결해야 할 수 있음 |
| 게이트웨이 | SharePoint 같은 일부 커넥터는 온-프레미스 데이터 게이트웨이 연결을 지원 |
| 표준 승인 | 계정당 연결 1개 |
| 솔루션 안의 흐름 | 연결 대신 연결 참조를 사용 |
| DLP 정책 | 관리자가 커넥터를 Business · Non-Business 로 나눠 함께 쓰는 것을 제한 |

연결 목록에서 하는 일입니다.[^connections]

| 하는 일 | 조작 |
|---|---|
| 새 연결 | 페이지 위쪽 **새 연결** › 커넥터 옆 **+** › 자격 증명 입력 |
| 연결 삭제 | 연결 고르기 › **…** › **삭제** |
| 깨진 연결 고치기 | 해당 연결의 **연결 수정** › 새 자격 증명 입력 |
| 상태와 생성 날짜 보기 | 연결 고르기 › **…** › **세부 정보** |
| 쓰는 흐름 찾기 | 세부 정보의 **이 연결을 사용하는 흐름** |
| 쓰는 앱 찾기 | 세부 정보의 **이 연결을 사용하는 앱** |

---

## 연결이 깨지는 경우

문서가 드는 원인입니다.[^failures]

| 원인 | 내용 |
|---|---|
| 암호 변경 | 저장된 토큰이 무효가 됨 |
| MFA 정책 변경 | 기존 토큰이 새 정책을 만족하지 못함 |
| 관리자 동의 철회 | 서비스 접근 동의가 사라짐 |
| 토큰 만료 | 사용하지 않은 지 약 90일이 지난 새로 고침 토큰 |
| 서비스 주체 비밀 만료 | 서비스 주체 연결의 클라이언트 비밀 만료 |

실행 기록의 오류 코드로도 구분합니다. 401 Unauthorized 는 연결 토큰 만료나 암호 변경이고, 403 Forbidden 은 대상 자원의 권한 부족이나 DLP 정책 차단입니다.[^failures]

연결 목록에서 **연결 수정**으로 다시 로그인합니다. 다른 사람 소유의 연결이면 그 사람이 다시 인증하거나, 내 연결을 만들어 흐름에 지정합니다.[^failures]

---

## 샘플

연결 목록에서 내 계정의 연결과 그 연결을 쓰는 흐름을 봅니다. 수강생이 계정 하나를 함께 쓰므로 이 샘플에서는 삭제와 연결 수정을 누르지 않습니다.

1. 아래 링크로 Power Automate를 엽니다.

    [Power Automate — {{ site.pa.environment }}]({{ site.pa.powerautomate_url }}){:target="_blank"}

2. 왼쪽 메뉴 **더보기**를 누르고 **연결**을 고릅니다.

    **완료 기준**: 연결 목록 화면이 열린다. 목록이 비어 있으면 [Lab 1](../lab1.html)의 16번을 마친 뒤 다시 엽니다.

3. **SharePoint** 줄을 고르고 **…** 를 눌러 **세부 정보**를 고릅니다.

    **완료 기준**: 상태와 생성 날짜가 보인다.

4. **이 연결을 사용하는 흐름**을 고릅니다.

    **완료 기준**: 이 연결을 쓰는 흐름의 목록 또는 빈 목록이 보인다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **실측**: 구성 창의 연결 표시, 기본 제공 도구 아래의 묶음, 커넥터의 화면 이름, 연결 창이 뜨지 않는 작업은 Lab 1~3 실측(2026-10-05)을 따랐습니다.
- **문헌**: 커넥터 아키텍처[^architecture] · 솔루션 인식 흐름의 이점[^solution] · 작업[^actions] · 트리거와 작업 다루기[^work] · 커넥터 개요[^overview] · 라이선스 유형[^licenses] · 트리거 문제 해결[^trouble] · 표준 승인 커넥터[^approvals] · 표준 커넥터 목록[^standard] · 프리미엄 커넥터 목록[^premium] · 연결 관리[^connections] · 클라우드 흐름 만들기[^logicflow] · 연결 실패 해결[^failures]

[^architecture]: **Connectors architecture** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/connectors/connector-architecture> (2026-11-02 확인). 작업과 트리거, 자격 증명과 메타데이터 저장소.
[^solution]: **Understand the benefits of using solution-aware cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/understand-benefits-solution-aware-flows> (2026-11-02 확인). 연결과 연결 참조의 구분, 연결에 인증 정보가 들어 있다는 것.
[^actions]: **Actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/actions-introduction> (2026-11-02 확인, 한국어판 미번역). 작업 추가 창의 네 구역.
[^work]: **Work with triggers and actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/work-with-triggers-actions> (2026-11-02 확인, 한국어판 미번역). 작업 찾기와 **더 보기**.
[^overview]: **Connectors overview** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/connectors/overview> (2026-11-02 확인). 미리 만든 커넥터와 사용자 지정 커넥터.
[^licenses]: **Types of Power Automate licenses** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-platform/admin/power-automate-licensing/types> (2026-11-02 확인). 표준 · 프리미엄 · 사용자 지정 커넥터 권한.
[^trouble]: **Troubleshoot Power Automate trigger problems and errors** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/troubleshoot/power-platform/power-automate/flow-run-issues/triggers-troubleshoot> (2026-11-02 확인). 프리미엄 표시 확인, 사용자별 라이선스, 연결 유지, DLP 정책.
[^approvals]: **Standard approvals** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/approvals/> (2026-11-02 확인). 등급과 계정당 연결 수.
[^standard]: **List of all Standard tier connectors** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/connectors/connector-reference/connector-reference-standard-connectors> (2026-11-02 확인). SharePoint · Office 365 Outlook · Microsoft Teams · Excel Online (Business) 의 등급.
[^premium]: **List of all Premium tier connectors** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/connectors/connector-reference/connector-reference-premium-connectors> (2026-11-02 확인). 프리미엄 커넥터 예.
[^connections]: **Manage connections in Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/add-manage-connections> (2026-11-02 확인). 연결 추가 · 삭제 · 수정 · 사용 흐름 찾기, Power Apps 공유, 다른 계정의 연결.
[^logicflow]: **Create a cloud flow in Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/get-started-logic-flow> (2026-11-02 확인). 커넥터의 인증 유형.
[^failures]: **Fix connection failures in cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/fix-connection-failures> (2026-11-02 확인, 문서 끝에 AI 도움 표기). 연결이 깨지는 원인, 401 · 403, 재인증, 다른 사람 소유의 연결.
