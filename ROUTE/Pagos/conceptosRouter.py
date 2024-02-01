from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
from services.pagos.conceptosServices import ConceptoServices,ConceptosPagosEntity
core =ConceptoServices()
URL = '/Padel/pagos/conceptos'
CONCEPTOS = APIRouter(prefix=URL, tags=[ "CONCEPTOS" ])
@CONCEPTOS.get("/getAll")
async def getAll() -> ConceptosPagosEntity | object:

    trigger = core.leerConceptos
    if trigger.status == False:
        raise HTTPException(400, trigger.message)
    return trigger.response

@CONCEPTOS.post("/")
async def crearConcepto(Concepto:ConceptosPagosEntity) -> ConceptosPagosEntity | object:
    trigger = core.crearConcepto(Concepto=Concepto)
    if trigger.status == False :
        raise HTTPException (400, trigger.message)
    return trigger.response
