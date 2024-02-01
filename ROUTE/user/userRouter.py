from fastapi import APIRouter,Request,HTTPException,UploadFile,File,Response

from core.Entities.users.loginEnity import LoginEntity
from services.users.loginServices import LoginServices
from services.users.userServices import UserServices,UserEntity

core = UserServices()
loginCore = LoginServices()
URL = '/Padel/user'
USER = APIRouter(prefix=URL,tags=["USER"])
@USER.post("/")
async def RegitrarUsuario(user:UserEntity)-> UserEntity | object:
    trigger=core.CrearUsuario(user)
    if trigger.status == False:
        raise HTTPException(400, trigger.message)
    return trigger.response
@USER.get("/getAll")
async def getAll():
    trigger = core.leerTodosLosUsuarios
    if trigger.status == False:
        raise HTTPException(400, trigger.message)
    return trigger.response
@USER.get("/search/token/{token}")
async def BuscarPorToken(token: str) -> object| list[UserEntity]:
    trigger = core.buscarUsuarioPorToken(token=token)
    if trigger.status == False:
        raise HTTPException(400, trigger.message)
    return trigger.response
@USER.get("/search/id/{id}")
async def BuscarPorId(id:str):
    trigger = core.buscarUsuarioPorId(id=id)
    if trigger.status == False :
        raise HTTPException (400, trigger.message)
    return trigger.response
@USER.post("/Loggin/")
async def InicioSeccion(login:LoginEntity):
    trigger = loginCore.ingresar(login)

    return trigger.response
@USER.put("/logout/{idUser}")
async def salir(idUser:str):
    trigger = loginCore.salir(idUser)
    return trigger.response

