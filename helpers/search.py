"""Open Wikipedia search (sample.app + real alpha)."""

from __future__ import annotations

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

_OPEN_SEARCH = (
    (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"),
    (AppiumBy.ID, "org.wikipedia.alpha:id/search_container"),
    (AppiumBy.ID, "org.wikipedia:id/search_container"),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Search Wikipedia")'),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Search")'),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Search")'),
)

_SEARCH_FIELD = (
    (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"),
    (AppiumBy.ID, "org.wikipedia:id/search_src_text"),
)


def open_search(driver: WebDriver, timeout: float) -> None:
    wait = WebDriverWait(driver, timeout)
    last: Exception | None = None
    for by, value in _OPEN_SEARCH:
        try:
            wait.until(EC.element_to_be_clickable((by, value))).click()
            return
        except TimeoutException as exc:
            last = exc
    raise last or TimeoutException("Search entry not found")


def search_field(driver: WebDriver, timeout: float):
    wait = WebDriverWait(driver, timeout)
    last: Exception | None = None
    for by, value in _SEARCH_FIELD:
        try:
            return wait.until(EC.element_to_be_clickable((by, value)))
        except TimeoutException as exc:
            last = exc
    raise last or TimeoutException("Search field not found")
