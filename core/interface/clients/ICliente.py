from abc import ABC,abstractmethod

from core.Entities.clients.personaEntity import PersonaEntity
from core.ROOM.ResponseInternal import ResponseInternalEntity,ResponseInternal
class ICliente(ABC):
    @abstractmethod
    def crearCliente(self, client: PersonaEntity) -> ResponseInternalEntity:
        """

        :type PersonaEntity: c
        """
        ...
    @abstractmethod
    def getAllClientes(self) -> ResponseInternalEntity: ...
    @abstractmethod
    def searchClienteByCi(self,ci:str) -> ResponseInternalEntity: ...
    @abstractmethod
    def searchClienteByName(self,name:str) -> ResponseInternalEntity: ...
