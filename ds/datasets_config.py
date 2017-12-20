from typing import Tuple

from .config.config import Config
from .config.config_base import ConfigBase


class DatasetsConfig(Config):
    def __init__(self, order: Tuple[ConfigBase] = None) -> None:
        self.host = "localhost"
        self.port = 8000
        self.ssl = False
        super().__init__(order=order)
        self.configure()
