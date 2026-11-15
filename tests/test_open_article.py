"""ДЗ: клик по результату поиска (открытие статьи).

На sample.app BrowserStack статья может не открыться полностью —
проверяем клик и переход: контейнер статьи или смена экрана поиска.
"""

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers.search import open_search, search_field


@allure.epic("Wikipedia Mobile")
@allure.feature("Article")
@allure.title("Open Wikipedia article from search results")
@allure.tag("mobile", "smoke")
@allure.label("owner", "ZaharKr")
@allure.label("layer", "mobile")
@allure.severity("critical")
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

    with allure.step("Verify article screen opened"):
        article_locators = (
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_contents_container"),
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_web_view"),
            (AppiumBy.ID, "org.wikipedia.alpha:id/content_frame"),
            (AppiumBy.CLASS_NAME, "android.webkit.WebView"),
        )
        opened = False
        for by, value in article_locators:
            try:
                WebDriverWait(driver, min(8, config.timeout)).until(
                    EC.presence_of_element_located((by, value))
                )
                opened = True
                break
            except TimeoutException:
                continue

        search_still = driver.find_elements(
            AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"
        )
        assert opened or not search_still, (
            "Article did not open and search results are still visible"
        )
