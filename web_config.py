from confobj import Config
from confobj import ConfigBase
from typing import Tuple


class WebConfig(Config):
    def __init__(self, order: Tuple[ConfigBase] = None) -> None:
        self.host = "0.0.0.0"
        self.port = 5000
        self.date_format = "%d.%m.%Y %H:%M"
        self.processed = {'name', "usages", "maintainer", "paths", "tags",
                          "links", "markdowns", "_markdowns", "changelog",
                          "_paths", "_links", "internal", "data", "type", "url",
                          "from", "characteristics"}
        super().__init__(order=order)
        self.configure()
