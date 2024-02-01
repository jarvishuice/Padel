from pydantic import BaseModel
from typing import Optional

class ConceptosPagosEntity(BaseModel):
    id:int
    nombre:str
    descripcion:Optional[str]

