import os
from ds.config.config import Config
from ds.config.config_yaml import ConfigYaml
from ds.config.config_env import ConfigEnv
from ds.config.config_json import ConfigJson


class Conf(Config):
    def __init__(self):
        self.hello = "world"
        self.num = 42
        super().__init__()
        self.configure()


def test_config():
    os.environ["NUM"] = "52"
    conf = Conf()
    assert conf.hello == "world"
    assert conf.num == 52
    assert isinstance(conf.num, int)
    assert isinstance(conf.hello, str)
    del os.environ["NUM"]


class ConfYaml(Config):
    def __init__(self):
        self.hello = "world"
        self.num = 42
        super().__init__(order=(ConfigYaml(open("tests/test.yaml")),))
        self.configure()


def test_config_yaml():
    conf = ConfYaml()
    assert conf.hello == "universe"
    assert conf.num == 42
    assert isinstance(conf.num, int)
    assert isinstance(conf.hello, str)


class ConfYamlEnv(Config):
    def __init__(self):
        self.hello = "world"
        self.num = 42
        super().__init__(order=(ConfigYaml(open("tests/test.yaml")),
                                ConfigEnv()))
        self.configure()


def test_config_yaml_env():
    os.environ["hello"] = "conf"
    conf = ConfYamlEnv()
    assert conf.hello == "conf"
    assert conf.num == 42
    assert isinstance(conf.num, int)
    assert isinstance(conf.hello, str)
    del os.environ["hello"]


class ConfEnvYaml(Config):
    def __init__(self):
        self.hello = "world"
        self.num = 42
        super().__init__(order=(ConfigEnv(),
                                ConfigYaml(open("tests/test.yaml"))))
        self.configure()


def test_config_env_yaml():
    os.environ["hello"] = "conf"
    conf = ConfEnvYaml()
    assert conf.hello == "universe"
    assert conf.num == 42
    assert isinstance(conf.num, int)
    assert isinstance(conf.hello, str)
    del os.environ["hello"]


class ConfJson(Config):
    def __init__(self):
        self.hello = "world"
        self.num = 42
        super().__init__(order=(ConfigJson(open("tests/test.json")),))
        self.configure()


def test_config_json():
    conf = ConfJson()
    assert conf.hello == "json"
    assert conf.num == 42
    assert isinstance(conf.num, int)
    assert isinstance(conf.hello, str)
