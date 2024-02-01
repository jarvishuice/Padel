"""Interface The Conections dataBase
posgresql tha operating system

    Returns:
method tha operations the systems
erential connect and disconect
the methods this override

    """
#@author
#jarvisHuice
from abc import ABC, abstractmethod


class ConectionDbInterface(ABC):
    ERROR="\033[0;31m"
    NOTE="\033[0;33m"
    DATABASE_ERROR=None
    INTEGRIDAD_ERROR=None
    INTERFACE_ERROR=None
    OPERATIONAL_ERROR=None
    #conect DataBase
    @abstractmethod
    def connect(self): ...


    @abstractmethod
    def disconnect(self): ...
    #create register
