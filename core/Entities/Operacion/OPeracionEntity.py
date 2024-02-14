from pydantic import BaseModel
from typing import Optional

from core.Entities.ordenes import pedidoEntity
from core.Entities.ordenes.ordenEnity import OrdenEntity
from core.Entities.pagos import DetallePagosEntity
from core.Entities.pagos.PagosEntity import PagosEntity


class OperacionEntity(BaseModel):
    encabezado:Optional[OrdenEntity]
    detalle:Optional[list[pedidoEntity]]
    pagos:Optional[PagosEntity]
    detallesPagos: Optional[DetallePagosEntity]

