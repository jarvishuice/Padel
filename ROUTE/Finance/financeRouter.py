from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
from services.finance.financeServices import FinanceServices,BancoEntity,PlanDeCuentaEntity
core =FinanceServices()
URL = '/Padel/Finance'
FINANCE = APIRouter(prefix=URL,tags=["FINANCE"])
@FINANCE.get("/bancos/getAll")
async def getAll() -> BancoEntity | object :

    trigger = core.leerTodosBancos
    if trigger.status == False:
        raise HTTPException(400, trigger.message)
    return trigger.response
@FINANCE.get("/cuentas/getAll")
async def getAll() -> PlanDeCuentaEntity | object:
    trigger= core.leerTodasLasCuentas
    if trigger.status ==False:
        raise HTTPException (400, trigger.message)
    return trigger.response
@FINANCE.post("/cuentas/")
async def crearCuenta(cuenta:PlanDeCuentaEntity) -> PlanDeCuentaEntity | object:
    trigger = core.insertarCuenta(cuenta)
    if trigger.status ==False:
        raise HTTPException (400, trigger.message)
    return trigger.response
@FINANCE.post("/banco/")
async def crearBanco(banco:BancoEntity) -> BancoEntity | object:
    trigger = core.insertarBanco(banco)
    if trigger.status == False :
        raise HTTPException(400, trigger.message)
    return trigger.response
