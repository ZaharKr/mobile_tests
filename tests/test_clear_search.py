"""Третий mobile-сценарий: очистка поисковой строки."""

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers.search import open_search, search_field


@allure.title("Clear Wikipedia search field")
@allure.tag("mobile", "smoke")
@allure.label("owner", "ZaharKr")
@allure.label("layer", "mobile")
def test_clear_search(driver, config):
    wait = WebDriverWait(driver, config.timeout)

    with allure.step("Open search"):
        open_search(driver, config.timeout)

    with allure.step("Type query"):
        field = search_field(driver, config.timeout)
        field.send_keys("Selenium")

    with allure.step("Clear search"):
        close_buttons = driver.find_elements(
            AppiumBy.ID, "org.wikipedia.alpha:id/search_close_btn"
        )
        if not close_buttons:
            close_buttons = driver.find_elements(
                AppiumBy.ID, "org.wikipedia:id/search_close_btn"
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
        assert not text or text.startswith("Search"), f"Search not cleared: {text!r}"
