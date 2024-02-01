from core.Entities.ResponseINternalEntity import ResponseInternalEntity
from core.Entities.finance.BancoEntity import BancoEntity
from core.Implements.finance.banco.BancoDAO import BancoDAO
from core.Implements.finance.planDeCuentas.PlanDeCuentasDAO import PlanDeCuentaDAO,PlanDeCuentaEntity

class FinanceServices():
    coreBanco: BancoDAO = None
    corePlanCuentas:PlanDeCuentaDAO = None
    def __init__(self):
        self.coreBanco = BancoDAO()
        self.corePlanCuentas = PlanDeCuentaDAO()
    def insertarBanco(self, Banco: BancoEntity) -> ResponseInternalEntity:
        """
        servicio encargado de registrar los nuevos bancos

        :param :Banco: BancoEntity
        :return: ResponserInternal
        """
        return self.coreBanco.crearBanco(Banco)
    @property
    def leerTodosBancos(self) -> ResponseInternalEntity:
        """

        :return:
        :rtype: ResponseInternalEntity
        """
        return self.coreBanco.getAllBanco()
    def insertarCuenta(self,cuenta:PlanDeCuentaEntity) -> ResponseInternalEntity:
        """

        :param cuenta:
        :return:
        """
        return self.corePlanCuentas.crearCuenta(cuenta=cuenta)
    @property
    def leerTodasLasCuentas(self) -> ResponseInternalEntity:
        """

        :retype: ResponseInternalEntity
        """
        return self.corePlanCuentas.getAllPlanDECuenta()