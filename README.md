# 삼쩜삼 웹 자동화 테스트 과제

## 1. 프로젝트 개요

본 프로젝트는 **삼쩜삼 웹 서비스**를 대상으로  
자동화 테스트를 작성하고,  
해당 테스트를 **GitHub Actions 기반 CI 환경에서 실행**하도록 구성한 과제입니다.

삼쩜삼 웹은 **카카오 OAuth 로그인만 제공하는 서비스**이므로,  
외부 OAuth 로그인 특성을 고려하여 자동화 테스트 범위를 명확히 정의하고  
로그인 이전의 핵심 사용자 흐름 위주로 테스트를 구성했습니다.

---

## 2. 사용 기술

- Playwright
- Python 3.10.1
- GitHub Actions
- Slack Webhook (테스트 결과 알림)

---

## 3. 테스트 시나리오

### 시나리오 설명

- TC-01: 사용자가 삼쩜삼 웹 랜딩 페이지에 진입하는 경우, '내 환급금 조회하기' 버튼이 조회되는지 확인한다.
- TC-02: 메인 CTA 버튼(“내 숨은 환급액 찾기”)을 클릭하면 로그인 화면으로 이동하는지 확인한다.
- TC-03: "카카오톡으로 로그인 하기" 버튼 클릭 시 카카오 로그인 페이지로 이동하는지 확인한다

### 테스트 범위 정의

삼쩜삼 웹은 **카카오 OAuth 로그인을 사용**하고 있어  
외부 로그인 과정은 보안 정책 및 서비스 구조상 자동화 대상에서 제외했습니다.

본 테스트에서는  
**사용자가 정상적으로 로그인 페이지까지 도달하는지 여부**를  
핵심 사용자 흐름으로 정의하여 검증했습니다.

실제 서비스 환경이라면 테스트 계정, 로그인 API,  
또는 OAuth Mock 방식을 활용해 테스트 할 예정입니다.

---

## 4. 프로젝트 구조

```text
Playwright_Project_251224/
├─ tests/
│  └─ test_landing_page.py
├─ src/
│  └─ browser.py
├─ reports/
│  └─ test_report.html
├─ .github/
│  └─ workflows/
│     └─ playwright.yml
├─ requirements.txt
└─ README.md
```
---

## 5. 실행 방법

### 1) 의존성 설치

    pip install -r requirements.txt

### 2) Playwright 브라우저 설치

    playwright install

### 3) 테스트 실행

    pytest -v --html=reports/test_report.html --self-contained-html
---

## 6. 테스트 리포트

- Playwright 기본 HTML 리포트 사용  
- 테스트 실행 후 `reports/test_report.html` 생성  

CI 환경에서는 GitHub Actions Artifact로 리포트가 업로드됩니다.

---

## 7. CI/CD 파이프라인 설명

### GitHub Actions 구성

- main 브랜치 push 또는 Pull Request 생성 시 자동 실행  
- 테스트 성공/실패 여부와 관계없이 리포트 업로드  
- 테스트 종료 후 Slack으로 결과 알림 전송  

### CI 실행 흐름

1. 코드 체크아웃  
2. python 환경 설정  
3. 의존성 설치  
4. Playwright 브라우저 설치  
5. 자동화 테스트 실행  
6. HTML 리포트 업로드  
7. Slack 알림 전송  

---

## 8. Slack 알림

- GitHub Actions 실행 결과(pass/fail)를 Slack으로 전송  
- Slack Webhook URL은 GitHub Secrets를 통해 관리  

---

## 9. 추가로 고민한 포인트

- OAuth 로그인 자동화는 과제 범위에서 제외했지만,  
  실제 환경에서는 로그인 상태 세션 주입 또는  
  테스트용 인증 API를 활용한 확장이 가능하다고 판단했습니다.

- 과제 특성상 테스트 개수보다는  
  **테스트 범위 정의, CI 연동 경험, 자동화 구조 이해**에 집중했습니다.

---

## 10. 개선 아이디어

- 로그인 이후 주요 사용자 시나리오 자동화  
- API 테스트와 E2E 테스트 분리 운영  
- 테스트 실패 시 스크린샷 자동 저장  
- Slack 알림 메시지에 실패 테스트 요약 추가
