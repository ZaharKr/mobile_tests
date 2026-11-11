"""Урок: поиск в Wikipedia sample app на BrowserStack."""

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.title("Successful Wikipedia search")
def test_successful_search(driver, config):
    wait = WebDriverWait(driver, config.timeout)

    with allure.step("Open search"):
        wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
        ).click()

    with allure.step("Type query"):
        wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
            )
        ).send_keys("Appium")

    with allure.step("Verify results found"):
        items = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
        assert len(items) > 0
