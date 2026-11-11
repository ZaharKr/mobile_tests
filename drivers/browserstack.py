from __future__ import annotations

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.webdriver import WebDriver

from config import BrowserStackConfig


def create_browserstack_driver(config: BrowserStackConfig) -> WebDriver:
    options = UiAutomator2Options()
    options.set_capability("browserstack.user", config.user)
    options.set_capability("browserstack.key", config.key)
    options.set_capability("app", config.app)
    options.set_capability("device", config.device)
    options.set_capability("os_version", config.os_version)
    options.set_capability("project", "ZaharKr mobile_tests")
    options.set_capability("build", "browserstack-build-1")
    options.set_capability("name", "android_wikipedia")
    return webdriver.Remote("https://hub.browserstack.com/wd/hub", options=options)


# back-compat
def create_driver(config: BrowserStackConfig) -> WebDriver:
    return create_browserstack_driver(config)
