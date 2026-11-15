"""ДЗ: клик по результату поиска (открытие статьи).

На sample.app BrowserStack статья может не открыться полностью —
в задании достаточно реализовать клик по найденному элементу.
"""

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers.search import open_search, search_field


@allure.title("Open Wikipedia article from search results")
def test_open_article_from_search(driver, config):
    wait = WebDriverWait(driver, config.timeout)

    with allure.step("Open search"):
        open_search(driver, config.timeout)

    with allure.step("Type query"):
        search_field(driver, config.timeout).send_keys("Python")

    with allure.step("Click first search result"):
        first_result = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
            )
        )
        title = first_result.text
        first_result.click()
        allure.attach(
            title or "",
            name="clicked_title",
            attachment_type=allure.attachment_type.TEXT,
        )
