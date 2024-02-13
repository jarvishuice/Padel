from abc import ABC,abstractmethod

from core.Entities.pagos.PagosEntity import PagosEntity


class IPagos(ABC):
    @abstractmethod
    def registrarPago(self,pago:PagosEntity): ...
    