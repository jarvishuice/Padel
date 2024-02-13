from fastapi import APIRouter, HTTPException
from services.productos.ProductosServices import ProductosEntity, ProductosServices

core =ProductosServices()
URL: str = 'Padel/Productos'
PRODUCTOS = APIRouter(prefix=f'/{URL}', tags=[ "Productos" ])

@PRODUCTOS.post('/crear',description="Servicio que crea un producto dentro del sistema")
async def CrearProducto(producto:ProductosEntity)->ProductosEntity:
    trigger  = core.RegistrarProducto(producto=producto)
    if trigger.status == True:
        return trigger.response
    raise HTTPException (400, trigger.message)
@PRODUCTOS.get("/crear/Inventario/{idProducto}/{cantidad}")
async  def  crearInventario(idPorducto:str,cantidad:float):
    trigger=core.EnviarInventario(idPorducto,cantidad)
    if trigger.status:
        return trigger.response
    raise HTTPException (400, trigger.message)

@PRODUCTOS.get("/get/all")
async def getAllProductos() -> list[ProductosEntity]:
    trigger = core.leerProductos
    if trigger.status :
        return trigger.response
    raise HTTPException (400, trigger.message)
