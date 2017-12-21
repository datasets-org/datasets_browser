import requests

from .datasets_config import DatasetsConfig
from urljoin import url_path_join


# todo support python2
class Datasets(object):
    """
        Library for datasets browsing and management
    """
    def __init__(self, conf: DatasetsConfig = DatasetsConfig()) -> None:
        """

        Args:
            conf (DatasetsConfig): instance of Datasets configuration class
        """
        self.conf = conf

    def list(self) -> dict:
        """
        Get all projects
        Returns:
            dict: list of all datasets
        """
        return requests.get(self.get_address()).json()

    def project_details(self, ds_id: str) -> dict:
        """
        Get project details
        Args:
            ds_id (str): dataset id

        Returns:
            dict: Dataset details
        """
        return requests.get(
            url_path_join(self.get_address(), "detail", ds_id)).json()

    def get_address(self) -> str:
        """

        Returns:
            str: server address
        """
        return "{}://{}:{}".format("https" if self.conf.ssl else "http",
                                   self.conf.host,
                                   self.conf.port)
