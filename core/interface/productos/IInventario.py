from abc import ABC,abstractmethod

from core.Entities.Productos.inventarioEntity import InventarioEntity
from core.Entities.ResponseINternalEntity import ResponseInternalEntity


class IInventario(ABC):
    @abstractmethod
    def registrar(self,producto:InventarioEntity) -> ResponseInternalEntity: ...
    @abstractmethod
    def Obtenernventario(self) -> ResponseInternalEntity: ...

    @abstractmethod
    def decontarInventario(self,idProducto:str,cantidad:float) -> ResponseInternalEntity: ...

