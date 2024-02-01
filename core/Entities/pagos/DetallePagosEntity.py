from pydantic import BaseModel

class DetallesPagosEntity(BaseModel):
    """
    Detalles de los pagos persividos '
    :Attributes:
      :var id :str  Identificador único .
      :var idPago:str identificador del encabezad de pago relacionado
      :var idFormaPago: str form en que se percibe o s eenvia el dinero
      :var monto: float  cantidad
      :var idTasa: Identificador d ela tasa del dolar bcv en obtenida en el momento dle pago

    """
    id:str
    idPago:str
    idFormaPago:str
    monto:float
    idTasa:str