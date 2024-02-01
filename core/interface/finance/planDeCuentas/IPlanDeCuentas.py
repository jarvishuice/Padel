from core.Entities.finance.planDeCuentas import PlanDeCuentaEntity
from core.ROOM.ResponseInternal import ResponseInternalEntity
from abc import ABC,abstractmethod
class IPlandDeCuentas(ABC):
    @abstractmethod
    def crearCuenta(self,cuenta:PlanDeCuentaEntity) -> ResponseInternalEntity: ...
    @abstractmethod
    def getAllPlanDECuenta(self) -> ResponseInternalEntity: ...



