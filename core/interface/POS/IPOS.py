from abc import ABC,abstractmethod

from core.Entities.Operacion.OPeracionEntity import OperacionEntity
from core.Entities.ResponseINternalEntity import ResponseInternalEntity


class IPOS(ABC):

    @abstractmethod
    def GenerarVenta(self,invoice:OperacionEntity): ...
    @abstractmethod
    def ventasToday(self) -> ResponseInternalEntity | list[OperacionEntity]:...
