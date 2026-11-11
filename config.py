"""Pydantic configs: local emulator + BrowserStack (diploma wiki)."""

from __future__ import annotations

import os
from typing import Literal

from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


def _env(name: str, default: str = "") -> str:
    raw = os.environ.get(name)
    if raw is None or not raw.strip():
        return default
    return raw.strip()


class LocalConfig(BaseModel):
    """Appium local / emulator."""

    context: Literal["local"] = "local"
    remote_url: str = Field(default_factory=lambda: _env("URL_LOCAL", "http://127.0.0.1:4723"))
    udid: str = Field(default_factory=lambda: _env("DEVICE_NAME_EMULATE", "emulator-5554"))
    app: str = Field(default_factory=lambda: _env("APP_LOCAL", ""))
    timeout: float = Field(default_factory=lambda: float(_env("TIMEOUT", "30")))


class BrowserStackConfig(BaseModel):
    """BrowserStack App Automate."""

    context: Literal["bstack"] = "bstack"
    user: str = Field(default_factory=lambda: _env("BROWSERSTACK_USERNAME") or _env("BROWSERSTACK_USER"))
    key: str = Field(
        default_factory=lambda: _env("BROWSERSTACK_ACCESS_KEY") or _env("BROWSERSTACK_KEY")
    )
    app: str = Field(default_factory=lambda: _env("BROWSERSTACK_APP", "bs://sample.app"))
    device: str = Field(default_factory=lambda: _env("BROWSERSTACK_DEVICE", "Google Pixel 3"))
    os_version: str = Field(default_factory=lambda: _env("BROWSERSTACK_OS_VERSION", "9.0"))
    timeout: float = Field(default_factory=lambda: float(_env("TIMEOUT", "30")))

    def model_post_init(self, __context) -> None:
        if not self.user or not self.key:
            raise ValueError(
                "Set BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY (see .env.example)"
            )


def load_config(context: str | None = None) -> LocalConfig | BrowserStackConfig:
    ctx = (context or _env("CONTEXT", "bstack")).lower()
    if ctx in ("local", "local_emulator"):
        return LocalConfig()
    return BrowserStackConfig()


# Back-compat alias used in older imports
TestConfig = BrowserStackConfig
