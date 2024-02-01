from core.Entities.ResponseINternalEntity import ResponseInternalEntity
from core.Entities.pagos.conceptos import ConceptosPagosEntity
from abc import abstractmethod,ABC
class IConceptos(ABC):
    @abstractmethod
    def crearConcepto(self,Concepto:ConceptosPagosEntity) -> ResponseInternalEntity: ...
    @abstractmethod
    def getAllConceptos(self) -> ResponseInternalEntity: ...