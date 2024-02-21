from config.LOGS.LogsSystem import Logs
from core.Entities.pagos.DetallePagosEntity import DetallesPagosEntity
from core.Implements.pagos.PagosDAO import PagosDAO,PagosEntity,ResponseInternalEntity
from core.Implements.pagos.detallesPagosDAO import DetallesPagosDAO


class PagosServices(Logs):
    def __init__(self):
        self.__core = PagosDAO()
        self.__coreDetalles = DetallesPagosDAO()
        super().__init__()

    def registrarPago(self,pago:PagosEntity) -> ResponseInternalEntity:
        """Registra un pago
        :type pago: object
        """
        if pago.total == 0:
            # validacion del monto
            return ResponseInternalEntity(status=False,
                                          message="error esta intentando ingresar  un pago por 0 ",
                                          response=None)
        return self.__core.registrarPago(pago=pago)
    def registrarDetallePago(self,detalle:DetallesPagosEntity):
        if detalle.monto == 0:
            return ResponseInternalEntity(status=False,
                                           message="error esta intentando ingreesar un pago por 0 ",
                                           response=None)
        return self.__coreDetalles.RegistrarDetalle(detalle=detalle)
