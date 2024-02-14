from pydantic import BaseModel
from typing import Optional

from core.Entities.ordenes.pedidoEntity import PedidosEntity
from core.Entities.ordenes.ordenEnity import OrdenEntity
from core.Entities.pagos.DetallePagosEntity import DetallesPagosEntity
from core.Entities.pagos.PagosEntity import PagosEntity


class OperacionEntity(BaseModel):
    """
    OPeraciones de compra o venta dentro del sistema
    :Attributes:
        :var encabezado: OrdenEntity: informacion del beneficiario y de la orden
        :var detalle: list [PedidosEntity]: detalle de lo consumido en la orden
        :var pagos : PagosEntity: encabezado de pago  con la fecha
        :var detallesPagos: list[DetallesPagosEntity]: Detalles que conforman los pagos como forma de pago , tasa del dollar y el monto
    """
    encabezado:Optional[OrdenEntity]
    detalle:Optional[list[PedidosEntity]]
    pagos:Optional[PagosEntity]
    detallesPagos: Optional[list[DetallesPagosEntity]]