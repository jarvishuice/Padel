from fastapi import APIRouter, HTTPException

from core.Entities.Productos.inventarioEntity import inventarioEntityOut
from services.productos.ProductosServices import ProductosEntity, ProductosServices,CategoriaEntity

core =ProductosServices()
URL: str = 'Padel/Productos'
PRODUCTOS = APIRouter(prefix=f'/{URL}', tags=[ "Productos" ])

@PRODUCTOS.post('/crear',description="Servicio que crea un producto dentro del sistema")
async def CrearProducto(producto:ProductosEntity)->ProductosEntity:
    trigger  = core.RegistrarProducto(producto=producto)
    if trigger.status == True:
        return trigger.response
    raise HTTPException (400, trigger.message)
@PRODUCTOS.get("/filter/almacen/{idAlmacen}")
async def filterProductosByAlmacen(idAlmacen:int)-> list[ProductosEntity]:
    trigger = core.productosByAlmacen(idAlmacen)
    if trigger.status == True:
        return trigger.response
    raise HTTPException(400, trigger.message)
@PRODUCTOS.get("/filter/categoria/{idCategoria}")
async def filterProductosByCategoria(idCategoria:int):
    trigger = core.productosByCategorias(idCategoria)
    if trigger.status == True:
        return trigger.response
    raise HTTPException (400, trigger.message)
@PRODUCTOS.put("/edit/")
async def EditarProducto(producto:ProductosEntity):
    trigger = core.editProductos(producto)
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
@PRODUCTOS.get("/inventario/all",description="retorna el inmventario actual",response_model=list[inventarioEntityOut])
async def getInventario():
    trigger = core.ObtenerInventario
    if trigger.status:
        return trigger.response
    raise HTTPException(400, trigger.message)

@PRODUCTOS.get("/categorias/all",
               description="obtener todas las categorias de los productos ",
               response_model= list[CategoriaEntity])
async def getAllCategorias():
    trigger = core.getCategorias
    if trigger.status:
        return trigger.response
    raise HTTPException(400, trigger.message)
@PRODUCTOS.post("/categorias/")
async def crearCategoria(categoria:CategoriaEntity):
    trigger = core.crearCategoria(categoria)
    if trigger.status:
        return trigger.response
    raise HTTPException(400, trigger.message)
