class Config(object):
    # todo support yaml
    # todo support json
    # todo support conf
    # todo support env
    # todo support merging of confs
    def __init__(self, conf_path):
        # todo env
        # todo file
        self.conf = conf_path

    def get(self, key: str):
        # todo type
        return self.conf.get(key)
