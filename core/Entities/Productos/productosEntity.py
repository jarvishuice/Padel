from pydantic import BaseModel
from typing import Optional

class ProductosEntity(BaseModel):
    """
    :var id identiificador del producto
    """
    #este se gebnera con :time.time()
    id: str
    nombre: str
    urlImg:Optional[str]
    # precio de compra
    costo :float
    # precio de venta
    precio : float
    idCategoria: int
    idAlmacen:  int
    # bandera para saber si se descuenta del inventario
    descontable : bool

