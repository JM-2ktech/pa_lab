---
title: "C24. 보안 입력과 출력"
parent: "더 읽을거리 · Cloud Flow"
nav_order: 24
concept:
  id: C24
  grade: C
  used_in: "랩에서 쓰지 않음"
  tokens: []
  sample: true
---

# C24. 보안 입력과 출력

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행.
     ⚠️ 실측할 것: 작업 구성 창 설정 탭의 보안 묶음 · 보안 입력 · 보안 출력 라벨(한국어판 코딩 지침 표기), 작성 카드에 보안 출력 토글이 있는지, 실행 화면에서 값 대신 보이는 문구(영어판 화면은 Content not shown due to security configuration)
     ⚠️ 하위 작업에 가려지는 범위와 지원하지 않는 작업 목록은 Azure Logic Apps 문서에만 있다. Power Automate 문서는 켜는 방법까지만 적는다. Power Automate 에서 같게 동작하는지 실측한다.
     ⚠️ how-tos-use-sensitive-input 은 구 디자이너 경로만 적어 페이지에 옮기지 않았다. -->

> **다루는 것**: 실행 기록에 남는 입력과 출력을 가리는 설정, 민감한 값을 흐름에 직접 넣지 않는 방법
>
> **쓰는 곳**: 랩에서 쓰지 않음

---

## 실행 기록에 남는 값

흐름에 접근할 수 있는 사람은 실행 기록에서 트리거와 작업의 입력 · 출력을 볼 수 있습니다. 비밀번호나 API 키를 흐름에 직접 적으면 이 사람들에게 값이 보입니다.[^secure]

| 방법 | 하는 일 | 조건 |
|---|---|---|
| 보안 입력 · 보안 출력 | 실행 기록과 감사 로그에서 값을 가림 | 작업마다 설정 |
| 환경 변수 | 값을 흐름 밖에서 관리 | 솔루션 흐름. [C23](c23-solutions.html) |
| 환경 변수의 비밀 형식 · Azure Key Vault 커넥터 | 실행 중에 비밀을 가져옴. 흐름 정의에 값이 드러나지 않음 | Azure Key Vault 필요 |
| HTTP 요청 트리거의 Microsoft Entra ID 토큰 | 흐름을 시작할 수 있는 사용자를 테넌트나 특정 사용자로 제한 | HTTP 요청을 받을 때 트리거 |
| 데스크톱 흐름 입력의 Secure Text | 데스크톱 흐름으로 넘기는 값을 가림[^sensitive] | 데스크톱 흐름 호출. [P26](p26-sensitive.html) |

---

## 켜는 경로

새 디자이너에서 작업을 고르고 **설정** 탭의 보안 묶음에서 켭니다.[^secure] 켠 작업의 오른쪽 위에 자물쇠 아이콘이 붙습니다.[^sensitive]

| 토글 | 가리는 값 |
|---|---|
| 보안 입력 | 그 작업에 들어간 값 |
| 보안 출력 | 그 작업이 내놓은 값 |

작업의 **코드 보기**에서는 아래 설정으로 보입니다.[^logicapps]

```
"runtimeConfiguration": {
  "secureData": {
    "properties": [
      "inputs",
      "outputs"
    ]
  }
}
```

---

## 가려지는 범위

아래는 Azure Logic Apps 문서의 내용입니다. Power Automate 문서에는 이 범위를 적은 표가 없습니다.[^logicapps]

| 켠 설정 | 켠 작업 | 그 값을 입력으로 쓰는 다음 작업 |
|---|---|---|
| 보안 출력 | 출력을 가림 | 입력을 가림. 다음 작업의 설정은 켜지지 않음 |
| 보안 입력 | 입력을 가림 | 입력을 가림. 다음 작업의 출력은 보임 |
| 작성 · JSON 구문 분석 · 응답의 보안 입력 | 입력과 출력을 모두 가림 | 입력과 출력이 모두 보임 |

작성 카드를 거친 값은 다음 작업에서 다시 보입니다. 다음 작업에도 보이지 않아야 하면 그 작업에서 직접 설정을 켭니다. 앞 작업의 가려진 출력을 나타내는 칩에도 자물쇠 아이콘이 붙습니다.

---

## 지원하지 않는 작업

커넥터 작업과 사용자 지정 커넥터 작업은 모두 지원합니다. 아래 기본 제공 작업은 지원하지 않습니다.[^logicapps]

| 설정 | 지원하지 않는 작업 |
|---|---|
| 보안 입력 | 변수 초기화 · 변수 설정 · 변수 증가 · 변수 감소 · 배열 변수에 추가 · 문자열 변수에 추가 · For each · If · Recurrence · Scope · Switch · Terminate · Until |
| 보안 출력 | 위 작업 전부 · Compose · Parse JSON · Response · Wait |

---

## 샘플

흐름 `식 연습장_HGD` 를 씁니다. 없으면 [C7](c07-types.html)의 샘플로 만듭니다.

1. `식 연습장_HGD` 의 **편집**을 눌러 디자이너를 엽니다.
2. **작성** 카드를 누릅니다. **입력** 칸을 비우고 아래를 입력합니다.

    ```
    시험값-1234
    ```

3. 구성 창의 **설정** 탭을 누릅니다. 보안 묶음에서 **보안 입력**을 켭니다.

    **완료 기준**: **작성** 카드 오른쪽 위에 자물쇠 아이콘이 보인다.

4. **저장**을 누르고 **테스트** › **수동** › **테스트**를 누릅니다. **흐름 실행**을 누르고 **완료**를 누릅니다.
5. 실행 화면에서 **작성** 카드를 누릅니다.

    **완료 기준**: 입력과 출력에 `시험값-1234` 대신 보안 구성 때문에 표시하지 않는다는 문구가 보인다.

6. 실행 화면 오른쪽 위 **편집**을 눌러 디자이너로 돌아옵니다. **작성** 카드의 **설정** 탭에서 **보안 입력**을 끄고 **저장**을 누릅니다. 이 흐름은 다른 페이지의 샘플에서도 씁니다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: 민감한 입력 관리[^sensitive] · 클라우드 흐름의 데이터 보호[^secure] · Azure Logic Apps 보안[^logicapps]

[^sensitive]: **Manage sensitive input like passwords** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/how-tos-use-sensitive-input> (2026-11-02 영어판 확인). 자물쇠 아이콘, 데스크톱 흐름으로 넘길 때의 Secure Text.
[^secure]: **Secure data used in cloud flows** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/guidance/coding-guidelines/use-secure-inputs-outputs-triggers> (2026-11-02 확인). 하드코딩의 위험, 환경 변수, Azure Key Vault, 새 디자이너의 토글 경로, HTTP 트리거 보호.
[^logicapps]: **Secure access and data for workflows in Azure Logic Apps** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/azure/logic-apps/set-up-security-permissions> (2026-11-02 영어판 확인). 하위 작업에 미치는 범위, 지원하지 않는 작업, 코드 보기의 secureData. Power Automate 가 아닌 Azure Logic Apps 문서다.
