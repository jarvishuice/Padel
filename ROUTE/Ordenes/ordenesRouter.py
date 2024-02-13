from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
from services.ordenes.OrdenesServices import OrdenesServices,OrdenEntity

core = OrdenesServices()

URL = '/Padel/ordenes'
ORDENES = APIRouter(prefix=URL,tags=["ORDENES"])

@ORDENES.post("/")
async def crearOrden(orden:OrdenEntity):
    trigger = core.crearOrden(orden)
    if trigger.status == True :
        return trigger.response
    raise HTTPException(400, trigger.message)
@ORDENES.get("/get/All")
async def getAllOrdenes():
    trigger = core.leerOrdenes
    if trigger.status == True :
        return trigger.response
    raise HTTPException(400, trigger.message)