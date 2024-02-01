from pydantic import BaseModel


class ProductosEntity(BaseModel):
    id: str
    nombre: str
    urlImg:str
    # precio de compra
    costo :float
    # precio de venta
    precio : float
    idCategoria: int
    idAlmacen:  int
    # bandera para saber si se descuenta del inventario
    descontable : bool

