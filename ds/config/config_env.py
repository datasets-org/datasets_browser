import os

from .config_base import ConfigBase


class ConfigEnv(ConfigBase):
    def get(self, key: str) -> str:
        v = os.environ.get(key)
        if not v:
            v = os.environ.get(key.lower())
        if not v:
            v = os.environ.get(key.upper())
        return v
