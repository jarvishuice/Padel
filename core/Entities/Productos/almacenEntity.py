from pydantic import BaseModel


class AlmacenEntity(BaseModel):
    id: int
    nombre = str