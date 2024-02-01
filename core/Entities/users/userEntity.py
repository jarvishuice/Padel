from pydantic import BaseModel
class UserEntity(BaseModel):
    id:str
    nombre:str
    cedula:str
    correo:str
    tipoUsuario:int
    token:str
    status:str
    password:str
    urlImg:str