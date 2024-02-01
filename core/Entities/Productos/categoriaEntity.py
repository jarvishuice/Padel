from pydantic import BaseModel


class CategoriaEntity(BaseModel):
    id: int
    nombre: str
    descripcion: str

