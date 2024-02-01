from pydantic import BaseModel
from typing import Optional


class ClienteEntity (BaseModel):
    """
    :
       The ClienteEntity entity represents a client in the system.

       Attributes:
           :var id :str The unique identifier of the client.
           :var ci :str The identity card of the client.
           :var nombre :str: The name of the client.
           :var telefono :str: The phone number of the client.
           :var correo :Optional[str]: The email of the client. It can be None.
           :var direccion (Optional[str]): The address of the client. It can be None.
           :var fechaIngreso (Optional[str]): The date the client entered the system. It can be None.
           :var  urlImagen (Optional[str]): The URL of the client's profile image. It can be None.
           :var deuda (Optional[float]): The current debt of the client. It can be None.
       """
    id: str
    ci: str
    nombre: str
    telefono: str
    correo: Optional[str]
    direccion: Optional[str]
    fechaIngreso: Optional[str]
    urlImagen: Optional[str]
    deuda: Optional[float]
