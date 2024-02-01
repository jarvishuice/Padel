from abc import ABC, abstractmethod
from core.Entities.users.loginEnity import LoginEntity


class ILogin(ABC):
    """
    Interfaz para el inicio de sesión.
    :
    """
    @abstractmethod
    def validarUsuario(self, userName: str) -> object:
        """
               Método abstracto para validar si el usuario existe.

               :param userName:

               """
        ...

    @abstractmethod
    def Login(self, login: LoginEntity):
        """
        Método abstracto para iniciar sesión.

        :param login: Entidad que contiene los detalles del inicio de sesión.

        """
        ...
    @abstractmethod
    def logout(self, idUser: str) -> object:
        """

        :param idUser:
        :rtype: object
        """
        ...