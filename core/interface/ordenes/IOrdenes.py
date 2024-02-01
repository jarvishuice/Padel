from abc import ABC,abstractmethod

from core.Entities.ordenes.ordenEnity import OrdenEntity


class IOrdenes(ABC):
    @abstractmethod
    def registrarOrden(self, orden:OrdenEntity):
        """
        dd

        :param orden:
        """
        ...

