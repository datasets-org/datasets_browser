import requests
from .config import Config
from .urljoin import url_path_join


class Datasets(object):
    def __init__(self, conf: Config):
        self.conf = conf

    def list_projects(self) -> dict:
        # todo try
        return requests.get(self._get_address()).json()

    def project_details(self, ds_id: str) -> dict:
        # todo try
        return requests.get(
            url_path_join(self._get_address(), "detail", ds_id)).json()

    def _get_address(self) -> str:
        return self.conf.get("address")
