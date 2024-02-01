import configparser
from configparser import ConfigParser
import os

class CredentialDb() :
    __config: ConfigParser = configparser.ConfigParser()
    __config.read("/home/jarvis/PycharmProjects/Padel/config/DB/config.ini")
    user = __config.get("POSTGRESQL", "user")
    port = __config.get("POSTGRESQL", 'port')
    db = __config.get("POSTGRESQL", 'data_base')
    host = __config.get("POSTGRESQL", 'host')
    password = __config.get("POSTGRESQL", 'password')
    #print(user)



    def __init__ (self) :


        self.keys = self.__config.options("POSTGRESQL")
        self.pru = self.__config.get("POSTGRESQL",'host')
    def getDatos (self):
        conection = (
                'dbname=' + self.db + ' ' + 'user=' + self.user + ' ' + 'password=' + self.password + ' ' + 'host=' + self.host + ' ' + 'port=' + self.port)
        return conection


#p = CredentialDb()
#print(p.getDatos())
