"""Dismiss Wikipedia first-run onboarding and promo sheets."""

from __future__ import annotations

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

_STEP_LOCATORS = (
    (AppiumBy.ACCESSIBILITY_ID, "Forward"),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Forward")'),
    (AppiumBy.ACCESSIBILITY_ID, "Close"),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Close")'),
    (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button"),
    (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button"),
    (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button"),
    (AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_skip_button"),
    (AppiumBy.ID, "org.wikipedia.alpha:id/closeButton"),
    (AppiumBy.ID, "org.wikipedia.alpha:id/view_announcement_action_negative"),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Skip")'),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Get started")'),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")'),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Got it")'),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Not now")'),
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("No thanks")'),
)


def skip_onboarding(driver: WebDriver, timeout: float = 8.0) -> None:
    """Advance through onboarding / promo sheets until home is free."""
    wait = WebDriverWait(driver, min(3.0, timeout))
    for _ in range(12):
        clicked = False
        for by, value in _STEP_LOCATORS:
            try:
                wait.until(EC.element_to_be_clickable((by, value))).click()
                clicked = True
                break
            except TimeoutException:
                continue
        if not clicked:
            return
