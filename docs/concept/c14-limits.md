---
title: "C14. 건수 제한과 페이지 매김"
parent: "개념 2. 자료형과 식"
nav_order: 14
concept:
  id: C14
  grade: B
  used_in: "Lab 1 ⑥ 예약 트리거와 식 · Lab 2 ④ 행 읽기"
  tokens: ["항목 가져오기(2개 이상)", "테이블에 있는 행 나열", "원본행"]
  sample: false
---

# C14. 건수 제한과 페이지 매김

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안. 샘플 없음.
     ⚠️ 실측할 것: 설정 탭의 페이지 매김 · 임계값 라벨, 상위 개수 칸의 라벨,
     상위 개수를 비웠을 때 실제 건수(심층 문서는 100, 커넥터 참조는 「default = all」로 어긋난다. Excel 도 256 과 「default = all」로 어긋난다),
     상위 개수 5,001 을 넣었을 때의 오류 화면, 교육 계정의 성능 프로필.
     랩은 상한 안이다. Lab 1 목록은 두 건, Lab 2 표는 64행이다. -->

> **다루는 것**: 목록과 표를 읽는 작업이 한 번에 돌려주는 건수의 상한과 페이지 매김
>
> **쓰는 곳**: Lab 1 `항목 가져오기(2개 이상)` · Lab 2 `원본행` 의 `테이블에 있는 행 나열`. 두 랩은 상한 안의 건수를 읽고, 건수 칸과 페이지 매김은 쓰지 않음

---

## 기본 상한

| 작업 | 기본 건수 | 늘리는 칸 | 칸의 최대 | 그 위로 |
|---|---|---|---|---|
| 항목 가져오기(2개 이상) | 100 | 상위 개수 | 5,000 | 페이지 매김 |
| 파일 가져오기 | 100 | 상위 개수 | 5,000 | 페이지 매김 |
| 테이블에 있는 행 나열 | 256 | 상위 개수 | 적혀 있지 않음 | 페이지 매김 |

항목이 상한보다 많으면 작업은 첫 페이지만 돌려줍니다.[^pagination] 값은 앞쪽 건수만 담기고, 뒤 카드도 그 건수로 처리합니다. 상위 개수에 5,000을 넘겨 넣으면 흐름이 실패합니다.[^items]

SharePoint 목록의 5,000은 목록 보기 임계값입니다.[^items]

문서끼리 어긋나는 값이 하나 있습니다. 심층 문서와 알려진 제한 표는 기본 건수를 100 · 256으로 적고, 두 커넥터 참조의 매개 변수 표는 상위 개수의 기본값을 「모두」로 적습니다.[^connector] 실제 건수는 실행 기록의 출력으로 확인합니다.

아래 식은 앞 작업이 돌려준 건수를 셉니다. 카드 이름은 실제 이름으로 바꿉니다.[^cookbook]

```
length(body('원본행')?['value'])
```

---

## 건수를 정하는 칸

| 칸 | 영문 | 내용 | 작업 |
|---|---|---|---|
| 상위 개수 | Top Count | 돌려줄 건수 | 항목 가져오기 · 행 나열 |
| 개수 건너뛰기 | Skip Count | 건너뛸 건수. 기본 0 | 행 나열 |

칸은 카드의 **고급 매개 변수**에 있습니다. SharePoint 목록 항목에는 건너뛰기 쿼리가 동작하지 않습니다.[^rest]

---

## 페이지 매김

페이지 매김을 켜면 흐름 엔진이 모든 항목을 가져오거나 임계값에 닿을 때까지 서비스를 계속 호출합니다.[^known]

| 칸 | 위치 | 내용 |
|---|---|---|
| 페이지 매김 | 구성 창 **설정** 탭 | 끔 · 켬 |
| 임계값 | 페이지 매김 아래 | 받으려는 결과 수 |

페이지 단위로 가져오므로 결과가 임계값보다 많을 수 있습니다. 문서의 SQL 예는 페이지 크기 2048, 임계값 5000에서 6144건을 돌려줍니다.[^pagination] 전체 항목이 임계값보다 적으면 전체를 돌려줍니다.[^pagination]

켜면 카드의 **코드 보기**에 아래 설정이 들어갑니다. `minimumItemCount` 가 임계값입니다.[^pagination]

```
"runtimeConfiguration": {
  "paginationPolicy": {
    "minimumItemCount": 1000
  }
}
```

페이지 매김으로 받는 항목 수에도 상한이 있습니다. 페이지 매김 요청은 Power Platform 요청 수에 들어갑니다.[^limits]

| 성능 프로필 | 해당 요금제 | 페이지 매김 항목 |
|---|---|---|
| Low | 무료 · Microsoft 365 요금제 · Power Automate Plan 1 · 평가판 등 | 5,000 |
| Medium | Power Automate Premium · Power Automate Plan 2 등 | 100,000 |
| High | Power Automate Process · 흐름별 요금제 | 100,000 |
| Unlimited Extended | 종량제 흐름 등 | 100,000 |

클라우드 흐름은 소유자의 요금제를 따릅니다.[^limits]

---

## 배열 필터링과 건수

**배열 필터링**은 앞 작업이 돌려준 항목만 거릅니다. 목록이 상한보다 크면 뒤쪽 항목은 입력에 들어오지 않습니다. 원본의 필터 쿼리는 서버에서 거르므로 이 조건을 받지 않습니다. 두 방식의 차이는 [C13](c13-filter.html)에서 다룹니다.

---

## 건수에서 생기는 증상

| 증상 | 원인 | 조치 |
|---|---|---|
| 출력이 100건에서 끝남 | 항목 가져오기 기본 상한 | 상위 개수 · 페이지 매김 |
| 출력이 256행에서 끝남 | 행 나열 기본 상한 | 페이지 매김[^excel] |
| 5,000건 넘는 목록에서 필터 쿼리 결과가 없음 | 앞 5,000건 안에 맞는 항목이 없음 | 페이지 매김[^items] |
| `exceeds the list view threshold` 메시지 | 5,000건 초과 | OData 필터 · 인덱스 열 · 페이지 매김[^trouble] |
| `WorkflowRunActionRepetitionQuotaExceeded` | 각각에 적용 항목 수 초과 | 원본에서 거름 · 배열 필터링 · 선택[^errors] |

각각에 적용이 처리하는 항목 수는 Low 5,000, 그 밖의 프로필 100,000입니다.[^limits] 반복은 [C18](c18-loops.html)에서 다룹니다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다.

- **문헌**: 항목 가져오기와 파일 가져오기[^items] · SharePoint 커넥터[^connector] · Excel Online (Business) 커넥터[^excel] · 커넥터 알려진 문제[^known] · 페이지 매김 설정[^pagination] · 흐름 제한[^limits] · SharePoint REST OData[^rest] · 문제 해결[^trouble] · 오류 코드 참조[^errors] · 식 요리책[^cookbook]

[^items]: **In-depth analysis into Get items and Get files SharePoint actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/sharepoint/dev/business-apps/power-automate/guidance/working-with-get-items-and-get-files> (2026-11-02 확인, 한국어판 미번역). 기본 100건, 최대 5,000건, 초과 시 실패, 5,000건 넘는 목록의 필터 쿼리 제한.
[^connector]: **SharePoint** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/sharepointonline/> (2026-11-02 확인). 상위 개수 설명의 기본값 「모두」. Excel 커넥터 참조의 매개 변수 표도 같게 적는다.
[^excel]: **Excel Online (Business)** — Microsoft Learn 커넥터 참조. <https://learn.microsoft.com/ko-kr/connectors/excelonlinebusiness/> (2026-11-02 확인). 행 나열 기본 256행과 페이지 매김, 상위 개수 · 개수 건너뛰기 칸.
[^known]: **Known issues and limitations for connectors** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/connectors/common/known-issues> (2026-11-02 확인). 설정의 페이지 매김과 임계값 동작.
[^pagination]: **Set up pagination to get more data than the page size limit** — Microsoft Learn (Azure Logic Apps). <https://learn.microsoft.com/ko-kr/azure/logic-apps/logic-apps-exceed-default-page-size-with-pagination> (2026-11-02 확인). 첫 페이지만 돌려주는 동작, 임계값보다 많이 받는 경우, `paginationPolicy` 정의.
[^limits]: **Limits of automated, scheduled, and instant flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/limits-and-config> (2026-11-02 확인). 성능 프로필과 요금제, 페이지 매김 항목 수, 각각에 적용 항목 수, 페이지 매김 요청이 요청 수에 들어간다는 것.
[^rest]: **Use OData query operations in SharePoint REST requests** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/sharepoint/dev/sp-add-ins/use-odata-query-operations-in-sharepoint-rest-requests> (2026-11-02 확인). `$skip` 이 목록 항목 쿼리에서 동작하지 않는다는 것.
[^trouble]: **Troubleshoot cloud flow errors** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/troubleshoot-flow-errors> (2026-11-02 확인). 목록 보기 임계값 오류 메시지와 조치.
[^errors]: **Cloud flow error code reference** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/error-reference> (2026-11-02 확인). `WorkflowRunActionRepetitionQuotaExceeded` 의 원인과 조치.
[^cookbook]: **Expression cookbook for cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/expression-cookbook> (2026-11-02 확인). 15번 패턴. `length()` 로 쿼리 결과 건수를 세는 식.
