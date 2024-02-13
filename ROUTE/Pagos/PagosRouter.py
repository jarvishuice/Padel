from fastapi import APIRouter, Request, HTTPException, UploadFile, File, Response
from services.pagos.pagosServices import PagosServices,PagosEntity,DetallesPagosEntity

core = PagosServices()
URL = '/Padel/pagos'
PAGOS = APIRouter(prefix=URL, tags=["PAGOS"])

@PAGOS.post("/")
async def crearPago(pago:PagosEntity) -> PagosEntity:
    trigger = core.registrarPago(pago)
    if trigger.status == False:
        raise HTTPException(400, trigger.message)
    return trigger.response

@PAGOS.post("/Detalle")
async def crearDetalle(detalle:DetallesPagosEntity):
    trigger = core.registrarDetallePago(detalle=detalle)
    if  trigger.status == False:
        raise HTTPException(400, trigger.message)
    return trigger.response