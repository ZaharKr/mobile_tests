from __future__ import annotations

from urllib.parse import quote

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.webdriver import WebDriver

from config import BrowserStackConfig


def create_browserstack_driver(config: BrowserStackConfig) -> WebDriver:
    options = UiAutomator2Options()
    options.set_capability("platformName", "android")
    options.set_capability("app", config.app)
    options.set_capability(
        "bstack:options",
        {
            "userName": config.user,
            "accessKey": config.key,
            "deviceName": config.device,
            "osVersion": config.os_version,
            "projectName": "ZaharKr mobile_tests",
            "buildName": "browserstack-build-1",
            "sessionName": "android_wikipedia",
        },
    )
    user = quote(config.user, safe="")
    key = quote(config.key, safe="")
    remote_url = f"https://{user}:{key}@hub.browserstack.com/wd/hub"
    return webdriver.Remote(remote_url, options=options)


# back-compat
def create_driver(config: BrowserStackConfig) -> WebDriver:
    return create_browserstack_driver(config)
