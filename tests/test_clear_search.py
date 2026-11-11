"""Третий mobile-сценарий: очистка поисковой строки."""

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.title("Clear Wikipedia search field")
@allure.tag("mobile", "smoke")
@allure.label("owner", "ZaharKr")
@allure.label("layer", "mobile")
def test_clear_search(driver, config):
    wait = WebDriverWait(driver, config.timeout)

    with allure.step("Open search"):
        wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
        ).click()

    with allure.step("Type query"):
        field = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
            )
        )
        field.send_keys("Selenium")

    with allure.step("Clear search"):
        # sample app: close/clear often via close button or empty field
        close_buttons = driver.find_elements(
            AppiumBy.ID, "org.wikipedia.alpha:id/search_close_btn"
        )
        if close_buttons:
            close_buttons[0].click()
        else:
            field.clear()

        text = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
            )
        ).text
        assert text in ("", "Search Wikipedia"), f"Search not cleared: {text!r}"
