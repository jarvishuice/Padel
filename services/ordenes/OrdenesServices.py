from core.Implements.ordenes.ordenesDAO import OrdenesDAO,OrdenEntity,ResponseInternalEntity,Logs


class OrdenesServices(Logs):
    def __init__(self):
        self.__core = OrdenesDAO()
        super().__init__()

    def crearOrden(self,orden:OrdenEntity):
        orden.IGTF = round(float(orden.IGTF),2)
        orden.IVA = round(float(orden.IVA), 2)
        orden.subTotal = round(float(orden.subTotal),2)
        orden.total = round(float(orden.subTotal + orden.IGTF + orden.IVA),2)
        self.Warnings( "claculando el total de una orden de ingreso "+str(orden.total))
        """VALIDACION CE CONCEPTO DE PAGO INGRESO O EGRESO TODO NUMERO MENOR A 3 ES EGRESO"""
        if orden.idConcepto == 2 or orden.idConcepto == 1:
            orden.total = orden.total * -1
            orden.subTotal = orden.subTotal * -1
        self.Warnings(  "calculando el total de l una orden de egreso "+str(orden.total))

        return self.__core.registrarOrden(orden)

    @property
    def leerOrdenes(self)-> ResponseInternalEntity:
        return self.__core.getAllOrden()