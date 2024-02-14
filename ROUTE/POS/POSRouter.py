from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
from services.POS.POSServices import POSServices,OperacionEntity

core = POSServices()

URL = '/Padel/POS'
POS = APIRouter(prefix=URL,tags=["POS"])

@POS.post("/")
async def crearOrden(operacion:OperacionEntity):
    trigger = core.GenerarVenta(operacion)
    if trigger.status == True :
        return trigger.response
    raise HTTPException(400, trigger.message)
