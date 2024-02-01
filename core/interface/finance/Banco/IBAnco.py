from abc import ABC,abstractmethod

from core.Entities.ResponseINternalEntity import ResponseInternalEntity
from core.Entities.finance.BancoEntity import BancoEntity
class IBanco(ABC):
    @abstractmethod
    def crearBanco(self,Banco: BancoEntity) -> ResponseInternalEntity: ...
    @abstractmethod
    def getAllBanco(self) -> ResponseInternalEntity: ...
