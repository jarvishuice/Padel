from abc import ABC,abstractmethod

from core.Entities.Productos.categoriaEntity import CategoriaEntity


class ICategoria(ABC):
    @abstractmethod
    def getAllCategorias(self): ...
    @abstractmethod
    def crearCategoria(self,categoria:CategoriaEntity): ...


