"""ДЗ: клик по результату поиска (открытие статьи).

На sample.app BrowserStack статья может не открыться полностью —
в задании достаточно реализовать клик по найденному элементу.
"""

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.title("Open Wikipedia article from search results")
def test_open_article_from_search(driver, config):
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
        ).send_keys("Python")

    with allure.step("Click first search result"):
        # sample app: item title in results list
        first_result = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
            )
        )
        title = first_result.text
        first_result.click()
        allure.attach(title or "", name="clicked_title", attachment_type=allure.attachment_type.TEXT)
