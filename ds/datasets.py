import requests

from .datasets_config import DatasetsConfig
from .urljoin import url_path_join


class Datasets(object):
    # todo support python2
    # todo docstrings
    def __init__(self, conf: DatasetsConfig = DatasetsConfig()):
        self.conf = conf

    def list_projects(self) -> dict:
        # todo try
        return requests.get(self._get_address()).json()

    def project_details(self, ds_id: str) -> dict:
        # todo try
        return requests.get(
            url_path_join(self._get_address(), "detail", ds_id)).json()

    def _get_address(self) -> str:
        return "{}://{}:{}".format("https" if self.conf.ssl else "http",
                                   self.conf.host,
                                   self.conf.port)
