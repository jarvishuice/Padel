import configparser
from configparser import ConfigParser


class CredentialKeys:
    __config:ConfigParser = configparser.ConfigParser()
    __config.read("/home/jarvis/PycharmProjects/Padel/config/keys/config.ini")
    __user = __config.get("USER", "key")

    def __init__(self):
        pass

    @property
    def getKeysUser(self) -> object:
        return self.__user
