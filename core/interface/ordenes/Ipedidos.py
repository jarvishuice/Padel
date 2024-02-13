from abc import ABC,abstractmethod

from core.Entities.ResponseINternalEntity import ResponseInternalEntity
from core.Entities.ordenes.pedidoEntity import PedidosEntity


class IPedidos(ABC):
    @abstractmethod
    def crearPedido(self,pedido:PedidosEntity)-> ResponseInternalEntity:...
    