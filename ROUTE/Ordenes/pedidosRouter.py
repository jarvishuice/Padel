from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
from services.ordenes.pedidosServices import PedidosServices,PedidosEntity

core = PedidosServices()

URL = '/Padel/Pedidos'
PEDIDOS = APIRouter(prefix=URL,tags=["PEDIDOS"])
@PEDIDOS.post("/registrar/")
async def registrarPedido(pedido:PedidosEntity)->PedidosEntity:
    trigger = core.registrarPedido(pedido)
    if trigger.status:
        return  trigger.response
    raise HTTPException (400, trigger.message)

