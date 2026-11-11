from __future__ import annotations

import pytest
from appium.webdriver.webdriver import WebDriver

from config import BrowserStackConfig, LocalConfig, load_config
from drivers import create_driver
from helpers import attach


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        action="store",
        default="",
        help="local | bstack (default from CONTEXT env / bstack)",
    )


@pytest.fixture(scope="session")
def config(request) -> LocalConfig | BrowserStackConfig:
    ctx = request.config.getoption("--context") or None
    return load_config(ctx)


@pytest.fixture
def driver(config: LocalConfig | BrowserStackConfig) -> WebDriver:
    drv = create_driver(config)
    yield drv
    session_id = drv.session_id
    attach.screenshot(drv)
    attach.page_source(drv)
    drv.quit()
    attach.video(config, session_id)
