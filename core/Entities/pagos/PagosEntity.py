from pydantic import BaseModel

class PagosEntity(BaseModel):

    id:str
    idOrden:str
    idPersona:str
    total:float
    IVA:float
    IGTF:float
    idConcepto:int
