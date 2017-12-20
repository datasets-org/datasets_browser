import yaml
from typing import Any

from .config_base import ConfigBase


class ConfigYaml(ConfigBase):
    def __init__(self, path) -> None:
        self.__conf = yaml.load(path)

    def get(self, key: str) -> Any:
        return self.__conf.get(key)
