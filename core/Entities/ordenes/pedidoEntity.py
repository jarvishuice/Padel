from pydantic import BaseModel


class PedidosEntity(BaseModel):
    idOrden: str
    total: float
    idProducto: str
    cantidad:float
    costo: float
    precio: float
    total:float = precio * cantidad
