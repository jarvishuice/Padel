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