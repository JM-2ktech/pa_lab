---
title: 홈
nav_order: 1
---

<!-- 저작 메모(학생 비노출) — 2026-10-02 신설.
     ★ 랩 표의 시간은 _instructions/PA_설계.md §1 편성표와 같다. 랩 헤더의 「예상 시간」을 고치면 여기도 고친다.
     ★ 이 페이지는 랩이 실측으로 확정된 뒤에 다시 맞춘다(cs_lab §2 규칙). 지금은 초안 기준이다. -->

# Power Automate 업무 자동화 실습
{: .no_toc }

첫날은 Cloud Flow로 문서와 결재를 잇는 DPA를, 둘째 날은 Power Automate Desktop으로 PC와 웹을 다루는 RPA를 만듭니다.

---

## 1일차 — Cloud Flow

| 시간 | 랩 | 끝내고 나면 |
|---|---|---|
| 10:00 | [Lab 1. 첫 클라우드 흐름](docs/lab1.html) | 버튼으로 요청을 받아 목록에 적고, 긴급이면 Teams로 알립니다. 매일 아침 마감 건수를 메일로 받습니다 |
| 13:00 | [Lab 2. 정기점검 보고서 — 취합과 생성](docs/lab2.html) | 매월 지난달 점검 기록을 모아 보고서 파일을 SharePoint에 만듭니다 |
| 14:55 | [Lab 3. 정기점검 보고서 — 승인과 배포](docs/lab3.html) | 그 보고서가 승인을 거쳐 메일과 Teams로 나갑니다. 반려되면 의견이 돌아옵니다 |

## 2일차 — Power Automate Desktop

| 시간 | 랩 | 끝내고 나면 |
|---|---|---|
| 10:00 | [Lab 4. Desktop 흐름 기본](docs/lab4.html) | 변수·조건·반복으로 파일을 정리하고 Excel 표를 읽습니다 |
| 13:00 | [Lab 5. 웹 자동화](docs/lab5.html) | 웹에서 공고를 검색해 여러 쪽의 표를 Excel로 옮깁니다 |
| 14:35 | [Lab 6. 고객계약 발굴](docs/lab6.html) | 키워드 목록으로 공고를 훑어 조건에 맞는 건만 결과 파일에 남깁니다 |

## 준비물

- 강사가 배부한 **교육용 계정**. 본인 회사 계정으로 로그인하지 않습니다
- Windows 노트북, **Microsoft Edge**
- 2일차: Power Automate Desktop 설치와 Edge 확장 설치. 2일차 첫 시간(PAD 개요)에 설치를 확인합니다

수강생 전원이 한 환경과 한 SharePoint 사이트를 씁니다. 이름 있는 것을 만들 때는 **본인 이니셜**을 붙입니다.

## 실습 자료

- [점검기록.xlsx](assets/download/점검기록.xlsx) — Lab 2·3. 강사가 사이트에 올려 둡니다
- [PA실습.zip](assets/download/PA실습.zip) — Lab 4~6. `C:\` 에 풀어 `C:\PA실습` 을 만듭니다
- [모의 공고 조회](practice/bid/) — Lab 5·6의 웹 자동화 대상

자료의 회사·기관·공고·금액은 모두 가상입니다.
