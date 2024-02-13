import configparser
from configparser import ConfigParser
from config.LOGS.LogsSystem import Logs


class CredentialKeys(Logs):
    __config:ConfigParser = configparser.ConfigParser()
    __config.read("/home/jarvis/PycharmProjects/Padel/config/keys/config.ini")
    __user = __config.get("USER", "key")

    def __init__(self):
        super().__init__()

    @property
    def getKeysUser(self) -> object:
        self.Warnings('utilizando la  llave de seguridad')
        return self.__user
