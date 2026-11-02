---
title: "C23. 환경 · 솔루션 · 환경 변수"
parent: "더 읽을거리 · Cloud Flow"
nav_order: 23
concept:
  id: C23
  grade: C
  used_in: "Lab 1 ② 인스턴트 흐름"
  tokens: ["환경 선택", "site.pa.environment"]
  sample: true
---

# C23. 환경 · 솔루션 · 환경 변수

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. 교육 계정 역할(Environment Maker · 기본 사용자)로 솔루션과 환경 변수를 만들 수 있는지는 문서로만 확인했다.
     ⚠️ 실측할 것: 왼쪽 메뉴의 솔루션 위치, 새 솔루션 창의 게시자 기본값, 신규 메뉴의 환경 변수 라벨(영어판 + New > More > Environment variable, 한국어판 없음), 환경 변수 창의 칸 이름(표시 이름 · 데이터 형식 · 기본값 · 현재 값은 영어판을 옮긴 것), 동적 콘텐츠 창의 환경 변수 묶음 이름, 솔루션 흐름의 초안 저장 · 게시 단추
     ⚠️ 문서 사이 차이: use-environment-variables 문서는 환경 변수를 @{variables('API_Base_URL')} 로 쓰는 예를 적는데, environment-variables 문서는 동적 콘텐츠에서 고르라고 적는다. 변수 작업 식처럼 보여 페이지에 옮기지 않았다. 데이터 형식 이름도 Yes/No 와 Two options 로 문서마다 다르다. -->

> **다루는 것**: 흐름이 들어 있는 환경, 흐름을 묶어 옮기는 솔루션, 환경마다 다른 값을 담는 환경 변수
>
> **쓰는 곳**: Lab 1 ② `{{ site.pa.environment }}` 환경 확인. 솔루션과 환경 변수는 랩에서 쓰지 않음

---

## 환경

환경은 앱 · 챗봇 · 흐름 · 업무 데이터를 저장하고 관리하는 공간입니다. 역할이나 보안 요구, 대상이 다른 앱을 나누는 단위이기도 합니다.[^env]

| 항목 | 내용 |
|---|---|
| 소속 | Microsoft Entra 테넌트 아래. 그 테넌트 사용자만 접근 |
| 지역 | 환경마다 지역이 정해짐. 연결 · 게이트웨이 · 흐름도 그 지역에 묶임 |
| 데이터베이스 | Dataverse 데이터베이스 0개 또는 1개 |
| 연결 범위 | 앱은 같은 환경의 연결 · 게이트웨이 · 흐름 · Dataverse에만 연결 |
| 지역 변경 | 지원 요청 필요[^regions] |

환경의 유형입니다.

| 유형 | 용도 | 특징 |
|---|---|---|
| 프로덕션 | 조직의 상시 업무 | 1GB 이상의 데이터베이스 용량 필요 |
| 기본값 | 실험 · 탐색 · 가벼운 개발 | 테넌트마다 하나. 삭제 불가. 라이선스 사용자 모두 환경 메이커. 운영용 아님 |
| 샌드박스 | 개발과 테스트 | 복사 · 재설정 기능 |
| 평가판 | 단기 테스트 | 30일 후 만료. 사용자당 1개 |
| 개발자 | 소유자 전용 | 관리되지 않는 개발자 환경은 2026-11-15부터 새로 만들 수 없고 2026-12-15부터 일시 중단 |
| Dataverse for Teams | Teams 안의 앱 | 2026-11-15부터 새로 만들 수 없고 2027-10-30에 폐기 |

교육 환경은 샌드박스이고 Dataverse 데이터베이스가 있습니다.

환경의 기본 역할은 두 가지입니다.

| 역할 | 할 수 있는 일 |
|---|---|
| 환경 관리자 | 역할 배정, Dataverse 프로비저닝, 환경의 모든 리소스 관리, DLP 정책 설정 |
| 환경 메이커 | 앱 · 연결 · 사용자 지정 커넥터 · 흐름 만들기 |

두 역할 모두 환경의 데이터베이스 접근 권한을 자동으로 주지 않습니다.

---

## 솔루션

솔루션은 흐름과 그 흐름에 필요한 연결 · 구성 요소를 묶은 패키지입니다. 환경 사이에서 옮기는 단위이고 ALM(애플리케이션 수명 주기 관리)의 수단입니다.[^aware] 솔루션을 만들려면 Dataverse가 있는 버전 9.1.0.267 이상의 환경이 필요합니다.[^solution]

솔루션에서 만들거나 솔루션에 추가한 흐름을 솔루션 흐름이라고 합니다.

| 항목 | 솔루션 밖 흐름 | 솔루션 흐름 |
|---|---|---|
| 연결 | 연결을 직접 사용. 바꾸면 해당 작업을 모두 수정 | 연결 참조를 사용. 참조만 바꿈 |
| 초안과 버전 기록 | 없음 | 있음. [C30](c30-child-versions.html) |
| 환경 변수 | 쓸 수 없음 | 사용 |
| 하위 흐름 | 쓸 수 없음 | 사용. [C30](c30-child-versions.html) |
| 소유 개수 | 최대 600개 | 제한 없음 |
| Dataverse의 실행 기록 | 없음 | FlowRun 테이블. 기본 28일(2,419,200초) |
| 파이프라인 배포 | 없음 | 사용 |
| Process 라이선스 | 배정 불가[^limitguide] | 배정 가능 |

솔루션은 관리 여부로 나뉩니다.

| 종류 | 쓰는 환경 | 수정 |
|---|---|---|
| 비관리형 | 개발 · 테스트 | 구성 요소 수정 가능 |
| 관리형 | 테스트 · 운영에 배포 | 배포 후 수정 불가 |

ALM 권장 사항입니다.[^aware]

- 테스트와 운영 환경에는 관리형 솔루션만 배포합니다.
- 흐름은 개발 환경에서만 편집합니다.
- 운영 환경의 흐름은 서비스 주체가 소유합니다.
- 운영 환경의 변경은 모두 ALM 절차를 거칩니다.

솔루션을 쓸 때의 조작입니다.[^flowsol]

| 하는 일 | 경로 | 조건 |
|---|---|---|
| 흐름 만들기 | 솔루션 열기 › 신규 › 자동화 › 클라우드 흐름 | 솔루션이 있어야 함 |
| 기존 흐름 추가 | 기존 항목 추가 › 자동화 › 클라우드 흐름 | 추가할 수 없는 흐름도 있음 |
| 구성 요소 보기 | 솔루션의 개체 탭 | 연결 참조 · 환경 변수 · 하위 흐름 표시 |
| 흐름이 든 솔루션 찾기 | 흐름 세부 정보의 솔루션 카드 | 솔루션 흐름만 |
| 환경 이동 | 내보내기 후 다른 환경에서 가져오기 | 마지막으로 게시한 버전만 내보냄[^drafts] |

솔루션 패키지의 최대 크기는 95MB입니다.[^envvar]

---

## 환경 변수

환경 변수는 URL · 메일 주소 · 연결 문자열처럼 환경마다 달라지는 값을 흐름 밖에 두는 구성 요소입니다.[^envflow] 값을 바꿀 때 흐름을 수정하지 않습니다. 하나의 환경 변수를 여러 흐름과 앱이 함께 씁니다.[^envvar]

| 쓰임 | 환경 변수 예 | 값 |
|---|---|---|
| API 호출 | `API_Base_URL` | 개발 · 운영 주소 |
| 메일 알림 | `SupportEmail` | 환경별 담당 팀 주소 |
| SharePoint | `SP_Site_URL` | 환경별 사이트 주소 |

칸과 값의 규칙입니다.

| 칸 | 내용 |
|---|---|
| 표시 이름 | 화면에 보이는 이름. 최대 100자 |
| 이름 | 고유 이름. 표시 이름에서 자동 생성되며 변경 가능. 최대 100자 |
| 데이터 형식 | 10진수 · JSON · 텍스트 · 예/아니요 · 데이터 원본 · 비밀 |
| 기본값 | 현재 값이 없을 때 사용. 최대 2,000자 |
| 현재 값 | 있으면 기본값보다 우선. 최대 2,000자 |

운영 조건입니다.[^envvar]

| 항목 | 내용 |
|---|---|
| 값 변경 반영 | 앱과 흐름에 비동기로 전달되어 최대 1시간 소요 |
| 값이 없을 때 | 알림 표시. 값 없이 쓰면 구성 요소가 실패할 수 있음 |
| 가져올 때 | 솔루션 가져오기 화면에서 값 입력 |
| 값의 위치 | 정의는 솔루션에 넣고 값은 대상 환경에서 입력 |
| 라이선스 | 프리미엄 불필요. Dataverse 커넥터로 환경 변수 레코드를 직접 다룰 때만 예외 |
| 예약 이름 | `$authentication` · `$connection` 은 저장 불가 |
| 표시 이름을 바꿀 때 | 디자이너에 옛 이름과 새 이름이 함께 보임. 참조를 지우고 다시 넣음 |
| 사용처 확인 | 솔루션에서 종속성 표시 |
| 삭제된 값 | 실행은 마지막 값을 사용 |

민감한 값은 텍스트 형식에 직접 넣지 않고 비밀 형식으로 Azure Key Vault를 참조합니다.[^envguide] 민감 정보를 다루는 다른 방법은 [C24](c24-secure.html)에 있습니다.

데이터 원본 형식은 커넥터의 매개 변수를 담습니다. SharePoint는 사이트와 목록에 환경 변수를 하나씩 둡니다. 환경 변수에 연결은 저장되지 않으며 흐름에는 연결이 따로 필요합니다.[^envvar]

---

## 샘플

솔루션 하나와 환경 변수 하나를 만들고 솔루션 흐름에서 값을 읽습니다. 이 솔루션은 [C30](c30-child-versions.html)의 샘플에서도 씁니다.

1. [Power Automate — {{ site.pa.environment }}]({{ site.pa.powerautomate_url }}){:target="_blank"}를 엽니다. 왼쪽 메뉴에서 **솔루션**을 누릅니다. 메뉴에 없으면 **더 보기**에서 찾습니다.
2. **새 솔루션**을 누릅니다. **표시 이름**에 아래를 입력합니다. `HGD` 대신 본인 이니셜을 넣습니다.

    ```
    개념 솔루션_HGD
    ```

3. **게시자**에서 목록의 기본 게시자를 고르고 **만들기**를 누릅니다.

    **완료 기준**: 솔루션 목록에 `개념 솔루션_HGD` 가 보인다.

4. 목록에서 `개념 솔루션_HGD` 를 눌러 엽니다. **신규** › **더 보기** › **환경 변수**를 누릅니다.
5. **표시 이름**에 아래를 입력합니다. **데이터 형식**은 **텍스트**를 고릅니다.

    ```
    실습 사이트_HGD
    ```

6. **기본값**에 아래를 붙여넣고 **저장**을 누릅니다.

    ```
    {{ site.pa.sharepoint_site }}
    ```

7. **신규** › **자동화** › **클라우드 흐름** › **인스턴트**를 누릅니다.
8. **흐름 이름**에 아래를 입력하고 트리거 목록에서 **수동으로 흐름 트리거**를 고른 뒤 **만들기**를 누릅니다.

    ```
    환경 변수 연습_HGD
    ```

9. 트리거 카드 아래 **+** › **작업 추가**에서 `작성` 을 검색해 **작성**을 고릅니다.
10. **입력** 칸을 누르고 번개 단추를 누릅니다. 동적 콘텐츠 창의 환경 변수 묶음에서 `실습 사이트_HGD` 를 고릅니다.
11. **초안 저장**을 누르고 **게시**를 누릅니다.
12. **테스트** › **수동** › **테스트**를 누릅니다. **흐름 실행**을 누르고 **완료**를 누릅니다.
13. 실행 화면에서 **작성** 카드를 누릅니다.

    **완료 기준**: 출력이 `{{ site.pa.sharepoint_site }}` 이다.

14. **솔루션**에서 `개념 솔루션_HGD` 를 열고 **개체** 탭을 누릅니다.

    **완료 기준**: `환경 변수 연습_HGD` 와 `실습 사이트_HGD` 가 함께 보인다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: 환경 개요[^env] · 지역 개요[^regions] · 솔루션 인식 흐름 개요[^solution] · 솔루션 흐름의 이점[^aware] · 솔루션에서 흐름 만들기[^flowsol] · 초안과 버전[^drafts] · 플랫폼 제한 이해[^limitguide] · 환경 변수 만들기[^envflow] · 환경 변수 사용[^envguide] · Power Platform 환경 변수 개요[^envvar]

[^env]: **Power Platform environments overview** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-platform/admin/environments-overview> (2026-11-02 영어판 확인). 환경의 범위, 유형, 역할, 개발자 · Dataverse for Teams 환경의 사용 중단 일정.
[^regions]: **Power Automate regions overview** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/regions-overview> (2026-11-02 영어판 확인). 환경 지역 변경은 지원 요청으로 한다는 것.
[^solution]: **Overview of solution-aware flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/overview-solution-flows> (2026-11-02 확인). 솔루션의 필수 조건과 새 솔루션 창의 칸.
[^aware]: **Understand the benefits of using solution-aware cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/understand-benefits-solution-aware-flows> (2026-11-02 영어판 확인). 연결과 연결 참조, 소유 개수, Dataverse 실행 기록, 파이프라인, 관리형 · 비관리형, ALM 권장 사항.
[^flowsol]: **Create a cloud flow in a solution** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/create-flow-solution> (2026-11-02 확인). 솔루션에서 만들기, 기존 흐름 추가, 개체 탭, 솔루션 카드.
[^drafts]: **Drafts and versioning for solution-aware cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/drafts-versioning> (2026-11-02 확인). 내보내는 버전.
[^limitguide]: **Understand platform limits and avoid throttling** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/understand-limits> (2026-11-02 영어판 확인). Process 라이선스를 배정하려면 흐름이 솔루션에 있어야 한다는 것.
[^envflow]: **Create environment variables** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/environment-variables> (2026-11-02 확인). 한국어 번역이 없어 영어로 열린다. 쓰임 표, 만드는 칸, 흐름에서 고르는 경로.
[^envguide]: **Use environment variables** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/use-environment-variables> (2026-11-02 영어판 확인). 민감한 데이터를 직접 저장하지 않는다는 권장 사항.
[^envvar]: **Environment variables for Power Platform overview** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-apps/maker/data-platform/environmentvariables> (2026-11-02 영어판 확인). 기본값과 현재 값, 길이 제한, 반영 시간, 라이선스, 예약 이름, 데이터 원본 형식, 솔루션 최대 크기.
