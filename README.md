# Mobile — Wikipedia (Appium)

Автотесты Android Wikipedia: Appium, Pytest, Allure.  
Два окружения — **local** (эмулятор) и **BrowserStack**, конфиги на **pydantic** (`LocalConfig` / `BrowserStackConfig`).

### Используемые инструменты

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="Python">
  <img src="https://img.shields.io/badge/Appium-4.x-green" alt="Appium">
  <img src="https://img.shields.io/badge/BrowserStack-App%20Automate-orange" alt="BrowserStack">
  <img src="https://img.shields.io/badge/Pytest-8.x-red" alt="Pytest">
  <img src="https://img.shields.io/badge/Allure-2.x-orange" alt="Allure">
  <img src="https://img.shields.io/badge/Jenkins-CI-yellow" alt="Jenkins">
  <img src="https://img.shields.io/badge/Telegram-notifications-blue" alt="Telegram">
</p>

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" height="40" alt="Python"/>
  &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/android/android-original.svg" width="40" height="40" alt="Android"/>
  &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jenkins/jenkins-original.svg" width="40" height="40" alt="Jenkins"/>
  &nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="40" height="40" alt="GitHub"/>
</p>

| | |
|---|---|
| GitHub | https://github.com/ZaharKr/mobile_tests |
| Jenkins | https://jenkins.qa.guru/job/ZaharKr_mobile_tests/ |
| Allure | https://jenkins.qa.guru/job/ZaharKr_mobile_tests/10/allure |
| TestOps | https://allure.qa.guru/project/5432/test-cases |
| Jira | https://jira.qa.guru/browse/MUL-80 |
| UI + API | [toolshop_diploma](https://github.com/ZaharKr/toolshop_diploma) |

## Список проверок

1. Успешный поиск в Wikipedia.
2. Открытие статьи из результатов поиска.
3. Очистка поля поиска.

## Конфиги

- `LocalConfig` — Appium local (`CONTEXT=local` / `--context=local`)
- `BrowserStackConfig` — BrowserStack (`CONTEXT=bstack` / `--context=bstack`)

Credentials — только `.env` (dotenv), в git не коммитятся.

## Установка

```bash
git clone https://github.com/ZaharKr/mobile_tests.git
cd mobile_tests
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

В `.env` указать `BROWSERSTACK_USERNAME` / `BROWSERSTACK_ACCESS_KEY` и `BROWSERSTACK_APP`.

## Запуск

BrowserStack:

```bash
pytest --context=bstack
```

Local:

```bash
pytest --context=local
```

```bash
allure serve allure-results
```

В Allure: steps, screenshot, page source, video (BrowserStack).

## Jenkins

> [Ссылка на сборку в Jenkins](https://jenkins.qa.guru/job/ZaharKr_mobile_tests/)

Freestyle, label `python`, Git на этот репозиторий.

1. Create Text File → `.env` с `BROWSERSTACK_*`
2. Shell:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --context=bstack
```

3. Allure Report → `allure-results`
4. Telegram: allure-notifications **4.11.1**

Последняя успешная сборка: [#10 SUCCESS — 3 passed](https://jenkins.qa.guru/job/ZaharKr_mobile_tests/10/)

<img src="media/jenkins-success.png" width="720" alt="Jenkins mobile SUCCESS">

## Allure Report

<img src="media/allure-overview.png" width="720" alt="Allure overview 3 passed">

## Allure TestOps / Jira

TestOps: https://allure.qa.guru/project/5432/test-cases  
Jira: [MUL-80](https://jira.qa.guru/browse/MUL-80)

## Прохождение автотеста

Поиск → статья → очистка поля:

<img src="media/wikipedia_flow.gif" width="360" alt="Wikipedia mobile flow">

Скрин шага (BrowserStack):

<img src="media/test-step.png" width="360" alt="Wikipedia search step">

## Telegram

Уведомление бота после прогона (Allure chart → Telegram):

<img src="media/telegram.png" width="360" alt="Telegram notification">

## UI + API

Веб/API часть того же диплома: [toolshop_diploma](https://github.com/ZaharKr/toolshop_diploma).
