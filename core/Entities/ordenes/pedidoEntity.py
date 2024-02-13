from pydantic import BaseModel
from typing import Optional

class PedidosEntity(BaseModel):
    idOrden: str
    total: float
    idProducto: str
    cantidad:float
    costo: float
    precio: float
    total:Optional[float]
    iterable:bool
