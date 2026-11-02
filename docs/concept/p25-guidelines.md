---
title: "P25. 코딩 지침"
parent: "개념 9. 실행과 운영"
nav_order: 25
concept:
  id: P25
  grade: B
  used_in: "Lab 4 ④ 30번 하위 흐름 · Lab 6 ③ 15번 변수 이름 · ⑧ 46~48번 오류 재시도 · Lab 7 ② 10번 응용 프로그램 로드 대기"
  tokens: ["하위 흐름", "재시도 정책", "로드 대기"]
  sample: true
---

# P25. 코딩 지침

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. 근거는 desktop-flow-coding-guidelines 영어판 네 문서다. readable · overview 는 한국어판이 없다.
     작업 이름 설명 · 지역 · 종료 지역 · 하위 흐름 실행 · 데스크톱 흐름 실행 · 로그 메시지 · 블록 오류 시 · 마지막 오류 보기 · 흐름 중지 · 대기 계열은 이 PC 의 PAD 한국어 리소스에서 확인했다.
     ko-kr flowcontrol 문서는 Comment 를 그대로 두고 Region 절 제목을 「하위 지역」, End region 을 「End 지역」 · 「End 영역」 · 「끝 지역」으로 섞어 적는다. 리소스는 설명 · 지역 · 종료 지역이다.
     ⚠️ 실측할 것: 작업 검색 칸에 설명 · 지역을 넣었을 때 결과에 뜨는 이름, 지역 줄을 접는 표시의 모양, 사용되지 않는 UI 요소 제거의 메뉴 위치. 「웹 서비스 호출」은 리소스에서 찾지 못한 라벨이다.
     ⚠️ 문서에 없는 것: 작업 대화 상자 맨 위 「메모 추가」 칸(Lab 7 15번 화면). 지침 문서에 언급이 없어 본문에 넣지 않았다. 변수 접두사 예시 표기는 문서 그림이 아니라 이 페이지에서 정한 예다. -->

> **다루는 것**: 데스크톱 흐름을 읽고 고치기 쉽게 만드는 지침 — 이름 · 설명 · 지역 · 모듈화 · 작업 선택 · 오류 처리 · 대기 · 정리 · 반복 · 모니터링
>
> **쓰는 곳**: Lab 4 30번 하위 흐름 `Basic` · Lab 6 15번 `ExcelInstance2` 이름 바꾸기 · 46~48번 재시도 정책 · Lab 7 10번 **응용 프로그램 로드 대기**

---

## 이름

하위 흐름 · 변수 · UI 요소 · 이미지에 뜻이 드러나는 이름을 붙입니다.[^readable]

| 대상 | 규칙 | 예 |
|---|---|---|
| 변수 | camelCase · PascalCase · 밑줄로 낱말을 구분 | `orderCount` · `OrderCount` · `order_count` |
| 변수 | 앞에 자료형 접두사 | `txtVendor` · `numOrderCount` · `dtOrders` |
| 입력 · 출력 변수 | 변수 이름과 외부 이름 모두에 접두사. 흐름 변수와 구분 | `inVendor` · `outResult` |

- 이름은 변수 창에서 바꿉니다. 모든 사용처가 함께 바뀝니다.[^vars]
- 이미 있는 이름으로 바꾸면 두 변수의 병합을 확인합니다.
- 흐름 검사기는 40자를 넘는 변수 이름을 경고합니다.[^checker]

---

## 설명

**설명** 작업은 흐름에 글을 남깁니다. 실행에 영향을 주지 않는 줄입니다.[^flowcontrol]

| 위치 | 적을 내용 |
|---|---|
| **Main** 맨 앞 | 프로세스의 짧은 설명 · 대상 사용자 · 관련 흐름 |
| 각 하위 흐름 맨 앞 | 그 하위 흐름의 목적 |
| 버그를 고친 줄 | 고친 이유 |

설명을 쓸 때 Copilot 의 작업 · 하위 흐름 요약 기능을 쓸 수 있습니다.[^readable] 이 기능은 대한민국을 포함한 지역에서 회사 또는 학교 계정으로 쓸 수 있습니다.[^copilot]

---

## 지역

**지역** 작업과 「종료 지역」 작업 사이의 작업을 한 묶음으로 접고 펼칩니다. 두 작업은 동작에 영향을 주지 않습니다.[^flowcontrol]

| 규칙 | 내용 |
|---|---|
| 짝 | **지역**과 **종료 지역**을 짝으로만 씀 |
| 범위 | 둘이 같은 범위에 있어야 함. 하나만 반복이나 조건 안에 있으면 지역이 되지 않음 |
| 짝 맺기 | 정해진 매핑이 없음. 마지막 **지역**이 다음에 나오는 **종료 지역**과 짝을 이룸 |
| 이름 | **지역**에 이름을 붙임 |

---

## 모듈화

| 단위 | 부르는 작업 | 쓰는 곳 | 만드는 방법 |
|---|---|---|---|
| 하위 흐름 | **하위 흐름 실행** | 한 흐름 안에서 관련 작업 묶기, 되풀이 작업 | 탭 줄 오른쪽 **+ 새로운** |
| 재사용 흐름 | **데스크톱 흐름 실행** | 여러 흐름에서 쓰는 작업 | 전용 흐름을 만들어 공유. 하위 흐름의 작업을 복사해 새 흐름에 붙여넣어도 됨 |

**하위 흐름 실행**은 현재 하위 흐름을 멈추고 다른 하위 흐름을 실행한 뒤 돌아옵니다.[^flowcontrol] 변수 범위는 [P19](p19-subflows.html)에서 다룹니다.

**데스크톱 흐름 실행**의 조건은 아래와 같습니다.[^runflow]

| 항목 | 내용 |
|---|---|
| 완료 대기 켬 | 부모가 멈추고 자식이 끝나면 이어감. 출력 변수를 돌려받음 |
| 완료 대기 끔 | 병렬 실행. 출력 변수 없음 |
| 병렬 수 | 루트 흐름과 함께 최대 6개. 자식이 부른 병렬 흐름도 포함 |
| 부모 종료 | 병렬 자식을 취소. 자식 로그가 일부 또는 전부 없을 수 있음 |
| 재귀 | 두 흐름이 직접 또는 간접으로 서로 부를 수 없음 |
| 의존 수 | 최대 150개. 넘거나 빠지면 부모가 실행되지 않음 |

---

## 작업을 고르는 순서

앱이나 서비스를 자동화할 때 위에서부터 찾습니다.[^performance]

| 순서 | 작업 | 예 |
|---:|---|---|
| 1 | 클라우드 커넥터 작업 | SharePoint 작업 |
| 2 | 앱 · 파일 전용 작업 | Excel · PDF · 파일 · 폴더 |
| 3 | UI 자동화 · 브라우저 자동화 | 창에서 텍스트 필드 채우기 · 웹 페이지 버튼 누르기 |
| 4 | 이미지 인식 · 마우스 및 키보드 · 클립보드 | 이미지로 마우스 이동 · OCR을 포함한 텍스트 추출 · 키 보내기 · 마우스 클릭 보내기 |
| 고급 | 스크립팅 · HTTP | VBScript 실행 · Python 스크립트 실행 · 웹 서비스 호출 |

OCR 대신 AI Builder 커넥터 작업 「이미지 또는 PDF 문서의 텍스트 인식」으로 데이터를 뽑을 수도 있습니다.

---

## 오류 처리

실패할 수 있는 작업을 찾아 제품의 오류 처리 기능으로 다룹니다.[^performance] 동작은 [P18](p18-errors.html)에서 다룹니다.

| 도구 | 범위 |
|---|---|
| 작업 대화 상자 왼쪽 아래 **오류** | 작업 하나 |
| **블록 오류 시** | 작업 묶음 |
| **마지막 오류 보기** | 가장 최근 오류를 변수로 받음 |
| **흐름 중지** | 흐름을 정상 종료 또는 오류와 함께 종료 |
| **로그 메시지** 또는 외부에 글을 쓰는 작업 | 메시지 기록 |

---

## 대기와 시간 제한

- 일반 **대기** 작업을 피하고, 조건을 기다리는 대기 작업에 시간 제한을 둡니다.[^performance]
- 흐름 전체의 최대 실행 시간은 흐름 속성의 **흐름 시간 제한**으로 정합니다.
- UI 자동화와 브라우저 자동화의 시간 제한은 상황별로 조정합니다. [P16](p16-wait-timeout.html)에서 다룹니다.

조건을 기다리는 작업에는 파일 대기 · 서비스 대기 · 마우스 대기 · 바로 가기 키 대기 · 화면에서 텍스트 대기(OCR) 등이 있습니다. **응용 프로그램 실행**의 응용 프로그램 로드 대기도 같은 목적의 설정입니다.

---

## 쓰지 않는 구성 요소 정리

사용 안 함으로 둔 작업을 지우고, 쓰지 않는 UI 요소와 이미지를 제거합니다. 흐름 크기가 줄고 저장 · 불러오기 시간이 줄어듭니다.[^performance]

---

## 불필요한 반복 피하기

수천 행의 Excel 파일처럼 큰 데이터를 반복으로 돌지 않습니다.[^performance]

| 대안 | 다루는 페이지 |
|---|---|
| 데이터 테이블 작업 · 데이터베이스 작업 | [P20](p20-datatable.html) |
| Power Fx 함수 | [P30](p30-powerfx.html) |
| 스크립팅 작업 | VBScript 실행 · Python 스크립트 실행 |

---

## 모니터링

실행을 추적하는 수단입니다.[^monitor]

| 수단 | 내용 |
|---|---|
| 작업 로그 V2 | 각 작업의 입출력 값 · 오류 · 경고. Elastic Table 사용, 자동 보존, 실행당 기가바이트 규모, 거의 실시간 갱신. 관리 센터에서 설정 |
| **로그 메시지** | 정보 · 경고 · 오류 수준의 메시지. 프리미엄 기능. 최대 128자. 디자이너 실행의 작업 로그는 올라가지 않음[^log] |
| **메시지 표시** | 화면에 표시하고 실행 세부 정보에도 남음 |
| 자체 기록 | Dataverse · SharePoint · 파일 작업으로 원하는 곳에 기록 |
| **마지막 오류 보기** | 마지막 오류를 받아 기록 |
| 자동화 센터 보고서 | 환경 수준. 클라우드 흐름 활동 · 데스크톱 흐름 활동 · 데스크톱 흐름 실행 · 용량 사용률 |
| 모니터 페이지 | 테넌트 수준. Power Platform 관리 센터 |
| Microsoft Fabric | Power Platform 의 Fabric 연결로 OneLake 데이터를 직접 조회 |

로그에는 진행 상황과 입력 · 출력 값, 중간 결과, 오류 메시지를 남깁니다. 민감한 값은 [P26](p26-sensitive.html)의 규칙을 따릅니다.

---

## 샘플

설명 · 지역 · 하위 흐름을 한 흐름에 넣습니다.

흐름 `개념 연습_HGD` 를 씁니다. 없으면 [P2](p02-types.html)의 1·2번으로 만듭니다.

1. 콘솔 왼쪽 막대의 **흐름**을 누르고 `개념 연습_HGD` 의 **편집**을 누릅니다.
2. 작업 영역의 빈 곳을 한 번 누르고 `Ctrl` + `A` 로 전체를 선택합니다. 선택한 줄을 마우스 오른쪽 단추로 눌러 **삭제**를 고릅니다.
3. 작업 검색 칸에 `설명` 을 입력하고 **흐름 제어** 아래 **설명**을 끌어다 놓습니다. **설명** 칸에 아래를 넣고 **저장**을 누릅니다.

    ```
    개념 연습 흐름. 코딩 지침 샘플. 대상 사용자 수강생. 관련 흐름 없음.
    ```

4. 작업 검색 칸에 `지역` 을 입력하고 **지역**을 1번 줄 아래로 끌어다 놓습니다. **이름**에 아래를 넣고 **저장**을 누릅니다.

    ```
    변수 준비
    ```

5. 작업 검색 칸에 `변수 설정` 을 입력하고 **변수 설정**을 2번 줄 아래로 끌어다 놓습니다. **변수**와 **값**에 아래를 차례로 넣고 **저장**을 누릅니다.

    ```
    txtCourse
    ```

    ```
    PA 실습
    ```

6. 작업 검색 칸에 `종료 지역` 을 입력하고 **종료 지역**을 맨 아래로 끌어다 놓습니다.
7. 2번 줄 **지역**의 접기 표시를 누릅니다.

    **완료 기준**: **변수 설정** 줄이 가려지고, 다시 누르면 보인다.

8. 작업 영역 위 탭 줄 오른쪽의 **+ 새로운**을 누릅니다. **하위 흐름 이름**에 아래를 넣고, **범위**는 **전역** 그대로 **저장**을 누릅니다.

    ```
    결과표시
    ```

9. **결과표시** 탭을 누릅니다. **설명**을 끌어다 놓고 아래를 넣은 뒤 **저장**을 누릅니다.

    ```
    과정 이름을 메시지로 표시합니다.
    ```

10. 작업 검색 칸에 `메시지 표시` 를 입력하고 **메시지 표시**를 1번 줄 아래로 끌어다 놓습니다. **표시할 메시지**에 아래를 넣고 **저장**을 누릅니다.

    ```
    %txtCourse%
    ```

11. **Main** 탭을 누릅니다. 작업 검색 칸에 `하위 흐름 실행` 을 입력하고 **하위 흐름 실행**을 맨 아래로 끌어다 놓습니다. **하위 흐름 이름**에서 `결과표시` 를 고르고 **저장**을 누릅니다.
12. 도구 모음의 **실행**(▶)을 누릅니다.

    **완료 기준**: 메시지 창에 `PA 실습` 이 뜬다.

13. 메시지 창의 **확인**을 누르고 도구 모음의 **저장**을 누릅니다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다. 지침 문서 일부는 한국어판이 없어 링크가 영어로 열립니다.

- **문헌**: 지침 개요[^overview] · 읽기 쉬운 흐름[^readable] · 성능 최적화[^performance] · 모니터링[^monitor] · 흐름 제어 작업[^flowcontrol] · 다른 흐름 실행[^runflow] · 로그 메시지[^log] · 변수 창[^vars] · 흐름 검사기[^checker] · Copilot[^copilot]

[^overview]: **Power Automate coding guidelines: Desktop flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/desktop-flow-coding-guidelines/> (2026-11-02 확인). 지침의 네 갈래. 데이터 보호 갈래는 P26 에서 다룬다.
[^readable]: **Build readable and maintainable flow scripts** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/desktop-flow-coding-guidelines/build-readable-flow-scripts> (2026-11-02 확인). 이름 · 설명 · 지역 · 하위 흐름 · 재사용 흐름.
[^performance]: **Optimize flow performance** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/desktop-flow-coding-guidelines/optimize-flow-performance> (2026-11-02 확인). 작업 선택 순서 · 오류 처리 · 대기 · 정리 · 반복.
[^monitor]: **Monitor and troubleshoot automation processes** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/desktop-flow-coding-guidelines/monitor-automation> (2026-11-02 확인). 작업 로그 V2 · 보고서 · Fabric.
[^flowcontrol]: **Flow control actions** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/flowcontrol> (2026-11-02 확인). 설명 · 지역의 규칙 · 하위 흐름 실행. 한국어판의 작업 이름 표기가 섞여 있어 영어판과 대조했다.
[^runflow]: **Run desktop flow from other desktop flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/how-to/run-desktop-flow-action> (2026-11-02 확인). 병렬 실행 · 출력 변수 · 재귀 금지 · 의존 수.
[^log]: **Log message action** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/actions-reference/logging> (2026-11-02 확인). 프리미엄 기능 · 128자 · 디자이너 실행의 로그.
[^vars]: **Manage variables and the variables pane** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/manage-variables> (2026-11-02 확인). 변수 이름 바꾸기와 병합.
[^checker]: **Flow checker** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/static-analysis> (2026-11-02 확인). 변수 이름 길이 규칙.
[^copilot]: **Get started with Copilot in Power Automate for desktop** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/desktop-flows/copilot-in-power-automate-for-desktop> (2026-11-02 확인). 요약 기능의 지역과 계정 조건.
