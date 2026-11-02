---
title: "C29. Copilot으로 만들기"
parent: "더 읽을거리 · Cloud Flow"
nav_order: 29
concept:
  id: C29
  grade: C
  used_in: "랩에서 쓰지 않음"
  tokens: []
  sample: true
---

# C29. Copilot으로 만들기

<!-- 저작 메모(학생 비노출) — 2026-11-02 초안.
     ⚠️ 샘플 미실행. 2026-10-05 촬영 화면에 디자이너의 Copilot 단추와 식 편집기의 Copilot으로 식 만들기 단추가 보인다(assets/lab2/lab2-13b.png). 동작은 확인하지 않았다.
     ⚠️ 실측할 것: 식 도우미의 식 만들기 · 확인 라벨, 홈의 Copilot으로 만들기 라벨, Copilot 창의 입력 칸과 보내기 단추, 한국어 프롬프트의 품질
     ⚠️ 프리뷰로 적은 것은 문서에 preview 로 표시된 것만이다. Copilot 결과는 실행마다 달라져 완료 기준을 넓게 적었다.
     copilot-cloud-flows-tips 는 문서 끝에 AI 도움을 받아 썼다고 적혀 있다. -->

> **다루는 것**: Power Automate의 Copilot 기능과 프리뷰 구분, 흐름을 자연어로 만들고 고치는 방법, 식 도우미
>
> **쓰는 곳**: 랩에서 쓰지 않음

---

## 기능 지도

프리뷰 기능은 운영에 쓰도록 나온 기능이 아니고 기능이 제한될 수 있습니다.[^expr]

| 영역 | 기능 | 상태 |
|---|---|---|
| 클라우드 흐름[^overview] | 자연어로 흐름 만들기 | 프리뷰 표시 없음 |
| 클라우드 흐름 | 디자이너 Copilot 창으로 편집 · 질문 | 프리뷰 표시 없음 |
| 클라우드 흐름[^fixflow] | 실행 오류를 요약하고 수정 제안(문제 해결) | 프리뷰 표시 없음 |
| 클라우드 흐름 | Copilot Studio 에이전트 호출 | 프리뷰 표시 없음 |
| 클라우드 흐름[^expr] | 식 도우미(Copilot으로 식 만들기) | 프리뷰 |
| 클라우드 흐름 | Microsoft 365 Copilot의 플러그인으로 흐름 사용 | 프리뷰 |
| 데스크톱 흐름 | Power Automate for desktop의 Copilot | 프리뷰 |
| 데스크톱 흐름 | Copilot으로 기록(Record with Copilot) | 프리뷰 |
| 데스크톱 흐름 | 자연어로 스크립트 작성 | 프리뷰 |
| 데스크톱 흐름 | 런타임 오류 복구 | 프리뷰 |
| 데스크톱 흐름 | 데스크톱 흐름 활동 분석 | 프리뷰 |
| 데스크톱 흐름 | 제품 질문 답변 | 프리뷰 표시 없음 |
| 프로세스 마이닝 | 수집 안내, 프로세스 분석 | 프리뷰 표시 없음 |
| 자동화 센터 | 실행 기록 · 작업 큐 · 제품 질문 답변 | 프리뷰 표시 없음 |

문서가 적는 사용 조건입니다.

| 조건 | 내용 |
|---|---|
| 디자이너 | 새 디자이너에서만 사용[^create] |
| 언어 | 영어에 최적화. 다른 언어는 지원이 제한되고 일부가 영어로 보일 수 있음[^create] |
| 계정 | 조직 계정. 개인 Microsoft 계정은 사용 불가[^regions] |
| 지역 | 미국 · 호주 · 영국 · 인도는 기본 켜짐. 그 외 지역은 지역 간 데이터 공유를 통해 기본 켜짐[^regions] |
| 끄기 | GPU가 있는 지역은 관리자가 지원에 요청해 테넌트 단위로 끔. 그 외 지역은 관리 센터에서 지역 간 데이터 공유를 끔. 환경 단위는 없음[^overview] |
| 모델 | Azure OpenAI 서비스 사용[^create] |

교육 환경의 디자이너 명령 모음에는 Copilot 단추가, 식 편집기에는 **Copilot으로 식 만들기** 단추가 보입니다(2026-10-05 화면).

---

## 자연어로 흐름 만들기

| 순서 | 화면 | 하는 일 |
|---:|---|---|
| 1 | 홈 | 자연어로 흐름을 설명하고 보내기 |
| 2 | 제안된 구조 | 트리거와 작업 확인. 다르면 내용을 더 적어 다시 생성 |
| 3 | 연결 확인 | 초록 체크는 정상, 빨간 느낌표는 설정 필요 |
| 4 | 디자이너 | 흐름 만들기를 누르면 오른쪽에 Copilot 창이 열림 |
| 5 | Copilot 창 | 남은 설정, 질문, 수정 |
| 6 | 명령 모음 | 저장 후 테스트 |

프롬프트를 쓰는 기준입니다.[^create]

| 기준 | 예 |
|---|---|
| 「X가 일어나면 Y를 한다」 형식 | `When an email arrives from contoso@gmail.com, post in Teams.` |
| 구체적으로 | `When an email arrives, I want to post the subject of the email to 'Contoso' Teams General channel` |
| 커넥터 이름 포함 | Outlook · Teams · Forms |
| 결과가 다르면 고쳐서 다시 실행 | 문구를 바꿔 비교 |

---

## 디자이너에서 고치기

디자이너의 Copilot은 범위가 분명한 지시에서 잘 동작합니다.[^tips]

| 할 수 있는 일 | 예 |
|---|---|
| 작업 추가 | `Add a condition after the Get Items action that checks if the Status column equals 'Approved'.` |
| 작업 수정 | `Change the trigger to run every Monday at 9:00 AM Pacific Time.` |
| 흐름 설명 | `Explain what this flow does step by step.` |
| 간단한 식 | `Write an expression that formats today's date as YYYY-MM-DD.` |
| 오류 처리 구성 | `Add error handling to the HTTP action. If it fails, send me an email with the error details and then terminate the flow as failed.` |
| 다음 단계 제안 | 트리거를 넣은 뒤 다음 작업 추천 |

지금 하지 못하는 일입니다.[^tips]

| 하지 못하는 일 | 대신 |
|---|---|
| 디자이너에서 런타임 오류 디버깅 | 실행 기록을 직접 봄. 흐름 실행 화면의 문제 해결 사용 |
| 실제 데이터 읽기(열 이름 · 값 확인) | 데이터를 직접 보고 필드 이름을 프롬프트에 적음 |
| 연결 문제 수정 | 다시 인증하거나 관리자 작업. [C22](c22-error-codes.html) |
| 복잡한 중첩 논리의 안정적 수정 | 요청을 잘게 나눔 |
| 다른 흐름과의 종속 관계 이해 | 흐름마다 따로 지시 |
| 복잡한 식 생성 | 결과를 [C10](c10-expressions.html)과 대조 |

결과를 좋게 하는 방법입니다.[^tips]

| 방법 | 내용 |
|---|---|
| 메시지 하나에 지시 하나 | 여러 단계를 한 번에 적으면 정확도가 떨어짐 |
| 동사로 시작 | Add · Change · Remove · Explain · Move |
| 필드 이름과 값을 적음 | 추측하지 않게 정확한 이름 명시 |
| 저장 전 검토 | 생성된 작업의 매개 변수와 동적 값 확인 |
| 작게 진행 | 트리거, 첫 작업 순서로 하나씩 확인 |
| 설명으로 검증 | 수정 후 흐름 설명을 시켜 의도와 비교 |
| 큰 수정 전 저장 | 원치 않는 변경이면 저장한 버전으로 되돌림 |

---

## 식 도우미

**프리뷰** 기능입니다. Copilot이 켜진 테넌트의 새 디자이너에서 씁니다. 식 편집기의 Copilot으로 식 만들기 단추로 엽니다.[^expr]

| 상황 | 하는 일 | 프롬프트 예 |
|---|---|---|
| 새 식 | 프롬프트로 식 생성. 흐름의 동적 콘텐츠 이름을 프롬프트에 적을 수 있음 | `Concatenate first name and last name.` |
| 기존 식 변경 | 열려 있는 식을 맥락으로 프롬프트대로 수정 | `Grab last four characters of Phone Number.` |
| 잘못된 식 수정 | 단추를 누르면 괄호 누락 같은 오류를 고친 식 제안 | 프롬프트 없음 |

제안을 적용하려면 식 만들기, 확인, 추가 순서로 누릅니다.

---

## 샘플

흐름 `식 연습장_HGD` 를 씁니다. 없으면 [C7](c07-types.html)의 샘플로 만듭니다. 식 도우미는 프리뷰 기능입니다. Copilot의 결과는 실행마다 달라질 수 있습니다.

1. `식 연습장_HGD` 의 **편집**을 눌러 디자이너를 엽니다.
2. **작성** 카드를 누릅니다. **입력** 칸을 비우고 ***fx*** 단추를 누릅니다.
3. 식 편집기에서 **Copilot으로 식 만들기**를 누릅니다. 프롬프트 칸에 아래를 붙여넣고 **식 만들기**를 누릅니다.

    ```
    Write an expression that formats today's date as YYYY-MM-DD.
    ```

    **완료 기준**: 날짜 형식을 지정하는 식이 제안된다.

4. **확인**을 누르고 **추가**를 누릅니다.
5. **저장**을 누르고 **테스트** › **수동** › **테스트**를 누릅니다. **흐름 실행**을 누르고 **완료**를 누릅니다.
6. 실행 화면에서 **작성** 카드를 누릅니다.

    **완료 기준**: 출력이 `2026-11-02` 같은 모양의 날짜다. 식에 시간대 변환이 없으면 UTC 날짜다. [C11](c11-datetime.html)

7. 실행 화면 오른쪽 위 **편집**을 눌러 디자이너로 돌아옵니다. 위쪽 명령 모음의 **Copilot**을 누릅니다.
8. Copilot 창의 입력 칸에 아래를 붙여넣고 보냅니다.

    ```
    What does my flow do?
    ```

    **완료 기준**: Copilot 창에 흐름을 요약한 답이 보인다.

---

## 출처

이 페이지는 아래 문서를 토대로 썼습니다. 샘플은 아직 실행하지 않았습니다.

- **문헌**: Power Automate의 Copilot[^overview] · Copilot으로 첫 흐름 만들기[^create] · 디자이너 Copilot 활용[^tips] · 식 도우미[^expr] · 클라우드 흐름 문제 해결[^fixflow] · 지역 개요[^regions]

[^overview]: **Copilot in Power Automate** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/copilot-overview> (2026-11-02 영어판 확인). 영역별 기능과 프리뷰 표시, 켜고 끄기.
[^create]: **Create your first cloud flow using Copilot** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/create-cloud-flow-using-copilot> (2026-11-02 영어판 확인). 만드는 순서, 프롬프트 기준, 언어, 새 디자이너 조건.
[^tips]: **Get the most from Copilot in Power Automate designer** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/copilot-cloud-flows-tips> (2026-11-02 영어판 확인). 할 수 있는 일과 하지 못하는 일, 프롬프트 예. 문서 끝에 AI 도움을 받아 썼다고 적혀 있다.
[^expr]: **Create, update, and fix expressions with Copilot expression assistant (preview)** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/expressions-copilot> (2026-11-02 영어판 확인). 프리뷰 조건, 세 가지 상황, 적용 순서.
[^fixflow]: **Troubleshoot a cloud flow** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/fix-flow-failures> (2026-11-02 영어판 확인). Copilot의 문제 해결.
[^regions]: **Power Automate regions overview** — Microsoft Learn. <https://learn.microsoft.com/ko-kr/power-automate/regions-overview> (2026-11-02 영어판 확인). 지역별 Copilot 제공, 개인 계정 제외.
