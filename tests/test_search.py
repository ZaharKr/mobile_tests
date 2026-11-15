"""Урок: поиск в Wikipedia sample app на BrowserStack."""

import allure
from appium.webdriver.common.appiumby import AppiumBy

from helpers.search import open_search, search_field


@allure.title("Successful Wikipedia search")
def test_successful_search(driver, config):
    with allure.step("Open search"):
        open_search(driver, config.timeout)

    with allure.step("Type query"):
        search_field(driver, config.timeout).send_keys("Appium")

    with allure.step("Verify results found"):
        items = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
        assert len(items) > 0
