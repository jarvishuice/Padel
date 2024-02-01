from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response
from services.clients.clientesServices import ClientesServices,PersonaEntity
core = ClientesServices()
URL = 'Padel/client'
CLIENTES = APIRouter(prefix=f'/{URL}',tags=["Clientes"])
@CLIENTES.post("/")
async def CrearCliente(client:PersonaEntity):
    trigger =core.RegistraCliente(client)
    if trigger.status == False :
        raise HTTPException(400,trigger.message)
    return trigger.response
@CLIENTES.get("/test")
async def Hello():
    return "hello"
@CLIENTES.get("/getAll")
async def GetAllCLient():
    trigger= core.ObetenerClientes()
    if trigger.status == False :
        raise HTTPException(400, trigger.message)
    return trigger.response
@CLIENTES.get("/search/by/ci/{ci}")
async def SerachClientByCi(ci:str):
    trigger = core.BuscarClienteByCi(ci)
    if trigger.status == False :
        raise HTTPException(400, trigger.message)
    return trigger.response