import json
from os.path import abspath
from os import getcwd




class Configuration():
    def loadConfig(self):
        config = json.loads(
            open(abspath(getcwd() + '/configuration.json')).read())
        return config
