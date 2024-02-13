from abc import ABC,abstractmethod

from core.Entities.pagos.DetallePagosEntity import DetallesPagosEntity


class IDetallesPagos(ABC):
    @abstractmethod
    def RegistrarDetalle(self, detalle: DetallesPagosEntity):...
