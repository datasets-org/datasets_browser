import abc


class ConfigBase(abc.ABC):
    @abc.abstractmethod
    def get(self, key: str):
        pass
