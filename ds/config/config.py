from typing import Any
from typing import Tuple

from .config_base import ConfigBase
from .config_env import ConfigEnv


class Config(object):
    # todo use args ?
    def __init__(self, order: Tuple[ConfigBase] = (ConfigEnv(),)) -> None:
        """

        Args:
            order (tuple): tuple of ConfigBase instances defining the order
            of config files
        """
        if order is None:
            order = (ConfigEnv(),)
        self.__configs = order
        for c in self.__configs:
            assert isinstance(c, ConfigBase)

    def __get(self, key: str, return_type: type = None) -> Any:
        v = None
        for c in self.__configs:
            if isinstance(c, ConfigEnv):
                v = c.get("{}_{}".format(self.__class__.__name__, key))
            else:
                v = c.get(key)

        if v is None:
            return

        if return_type:
            return return_type(v)
        return v

    def configure(self) -> None:
        """
            Configures object based on its initialization
        """
        for i in vars(self):
            if i.startswith("_"):
                continue
            val = self.__get(i, return_type=type(getattr(self, i)))
            if val is not None:
                setattr(self, i, val)

    def __str__(self):
        s = ""
        for i in vars(self):
            if i.startswith("_"):
                continue
            s += "{}\t{}\n".format(i, getattr(self, i))
        return s
