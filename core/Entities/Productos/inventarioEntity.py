from pydantic import BaseModel


class InventarioEntity(BaseModel):
    idProducto:str
    cantidad: float

class inventarioEntityOut(BaseModel):
    idProducto: str
    nombre: str
    cantidad: str