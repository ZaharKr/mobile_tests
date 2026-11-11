# Jenkins job `ZaharKr_mobile_tests`

1. New Item → Freestyle → `ZaharKr_mobile_tests` (если ещё нет)
2. Label: `python`
3. Git: `https://github.com/ZaharKr/mobile_tests.git`, `*/main`
4. Create Text File → `.env`:

```
CONTEXT=bstack
BROWSERSTACK_USERNAME=<from BrowserStack>
BROWSERSTACK_ACCESS_KEY=<from BrowserStack>
```

5. Execute shell:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --context=bstack
```

6. Allure Report → `allure-results`
7. Save → Build Now

Блокер: без BS username/key сборка на BrowserStack не пройдёт. Local context — только если на агенте есть Appium + эмулятор.
