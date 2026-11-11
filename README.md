# Mobile — Wikipedia (Appium)

Автотесты Android Wikipedia: Appium, Pytest, Allure.  
Два окружения — **local** (эмулятор) и **BrowserStack**, конфиги на pydantic.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Appium](https://img.shields.io/badge/Appium-4.x-green)
![BrowserStack](https://img.shields.io/badge/BrowserStack-App%20Automate-orange)
![Pytest](https://img.shields.io/badge/Pytest-8.x-red)
![Allure](https://img.shields.io/badge/Allure-2.x-orange)

- GitHub: https://github.com/ZaharKr/mobile_tests
- Jenkins: https://jenkins.qa.guru/job/ZaharKr_mobile_tests/

## Сценарии

| Файл | Что проверяет |
|------|---------------|
| `tests/test_search.py` | Поиск в Wikipedia |
| `tests/test_open_article.py` | Открытие статьи из выдачи |
| `tests/test_clear_search.py` | Очистка поля поиска |

## Конфиги

- `LocalConfig` — Appium local (`CONTEXT=local`)
- `BrowserStackConfig` — BrowserStack (`CONTEXT=bstack`)

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

В `.env` указать `BROWSERSTACK_USERNAME` / `BROWSERSTACK_ACCESS_KEY`.

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

## Jenkins

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

## UI + API

Веб/API часть того же диплома: [toolshop_diploma](https://github.com/ZaharKr/toolshop_diploma).
