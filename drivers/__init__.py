from config import BrowserStackConfig, LocalConfig
from drivers.browserstack import create_browserstack_driver
from drivers.local import create_local_driver


def create_driver(config: LocalConfig | BrowserStackConfig):
    if isinstance(config, LocalConfig):
        return create_local_driver(config)
    return create_browserstack_driver(config)


__all__ = ["create_driver"]
