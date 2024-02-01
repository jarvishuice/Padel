from pydantic import BaseModel


class OrdenEntity(BaseModel):
    """
        :
        Encabezado de lAS ORDENES


        :Attributes:
           :var id :str  Identificador único de la orden.
           :var total :float  Total de la orden.
           :var idCliente :str Identificador único del cliente.
           :var fechaApertura :str: Fecha de apertura de la orden.
           :var fechaPago: str: Fecha de pago de la orden.
           :var IVA :float: Impuesto al Valor Agregado de la orden.
           :var IGTF :float: Impuesto a las Grandes Transacciones Financieras de la orden.
           :var subTotal :float: Subtotal de la orden.
           :var status :str: Estado de la orden.
           :var idConcepto :int: Concepto de la orden.

       """

    id: str
    total: float
    idCliente: str
    fechaApertura: str
    fechaPago: str
    IVA: float
    IGTF: float
    subTotal: float
    status: str
    idConcepto: int