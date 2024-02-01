from pydantic import BaseModel

class TipoPersonaEntity(BaseModel):
    """
    :
        TIPO DE PERSONA SE EXPONE LOS TIPOS DE PERSONALIDADES QUE HACEN VIDA DENTRO DEL SITEMA (CLIENTES,SOCIOS,OPERADORES ENRE OTROS)

        :Attributes:
            :var id :str identificador de l tipo de persona .
           :var nombre :str The nombre del tipo de persona.
    """
    id:int
    nombre:str