from core.Entities.pagos.conceptos import ConceptosPagosEntity
from core.Implements.pagos.conceptos import ConceptosDAO


class ConceptoServices:
    core = None
    def __init__(self):
        self.core = ConceptosDAO()
    @property
    def leerConceptos(self) -> object | ConceptosPagosEntity:
        return self.core.getAllConceptos

    def crearConcepto(self,Concepto:ConceptosPagosEntity) -> object | ConceptosPagosEntity:
        """

        :param Concepto:
        :return:
        """
        return self.core.crearConcepto(Concepto)