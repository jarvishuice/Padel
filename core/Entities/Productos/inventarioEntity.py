from pydantic import BaseModel


class InventarioEntity(BaseModel):
    idProducto:str
    cantidad:  float

class inventarioEntityOut(BaseModel):
    idProducto: str
    nombre:     str
    precio:     float
    costo:      float
    cantidad:   float

