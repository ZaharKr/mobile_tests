"""Урок: поиск в Wikipedia sample app на BrowserStack."""

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers.search import open_search, search_field


@allure.epic("Wikipedia Mobile")
@allure.feature("Search")
@allure.title("Successful Wikipedia search")
@allure.tag("mobile", "smoke")
@allure.label("owner", "ZaharKr")
@allure.label("layer", "mobile")
@allure.severity("critical")
def test_successful_search(driver, config):
    wait = WebDriverWait(driver, config.timeout)

    with allure.step("Open search"):
        open_search(driver, config.timeout)

    with allure.step("Type query"):
        search_field(driver, config.timeout).send_keys("Appium")

    with allure.step("Verify results found"):
        results = wait.until(
            EC.presence_of_all_elements_located(
                (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
            )
        )
        assert len(results) > 0, "Expected at least one search result"
        allure.attach(
            results[0].text or "",
            name="first_result",
            attachment_type=allure.attachment_type.TEXT,
        )
