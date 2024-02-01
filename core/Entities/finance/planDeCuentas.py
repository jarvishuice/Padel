from pydantic import BaseModel
class PlanDeCuentaEntity(BaseModel):
    id:str
    metodo:str
    nCuenta:str
    idBanco:str

