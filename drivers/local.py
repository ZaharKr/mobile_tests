from __future__ import annotations

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.webdriver import WebDriver

from config import LocalConfig


def create_local_driver(config: LocalConfig) -> WebDriver:
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("udid", config.udid)
    if config.app:
        options.set_capability("app", config.app)
    options.set_capability("automationName", "UiAutomator2")
    return webdriver.Remote(config.remote_url, options=options)
