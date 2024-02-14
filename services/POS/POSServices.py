from config.LOGS.LogsSystem import Logs
from core.Entities.Operacion.OPeracionEntity import OperacionEntity
from core.Entities.ResponseINternalEntity import ResponseInternalEntity
from core.interface.POS.IPOS import IPOS


class POSServices(IPOS,Logs):

    def GenerarVenta(self, invoice: OperacionEntity) -> ResponseInternalEntity | OperacionEntity:
        return invoice
    @property
    def ventasToday(self) -> ResponseInternalEntity | list[OperacionEntity]:
        pass