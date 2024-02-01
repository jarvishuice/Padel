from abc import ABC,abstractmethod

from core.Entities.clients.clienteEntity import ClienteEntity
from core.ROOM.ResponseInternal import ResponseInternalEntity,ResponseInternal
class ICliente(ABC):
    @abstractmethod
    def crearCliente(self,client: ClienteEntity) -> ResponseInternalEntity:
        """

        :type ClienteEntity: c
        """
        ...
    @abstractmethod
    def getAllClientes(self) -> ResponseInternalEntity: ...
    @abstractmethod
    def searchClienteByCi(self,ci:str) -> ResponseInternalEntity: ...
    @abstractmethod
    def searchClienteByName(self,name:str) -> ResponseInternalEntity: ...
