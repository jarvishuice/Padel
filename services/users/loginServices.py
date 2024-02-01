from core.Entities.users.loginEnity import LoginEntity
from core.Implements.users.loginDAO import LoginDAO
class LoginServices:
    def __init__ (self) :
        self.__core = LoginDAO()
        super ().__init__ ()
    def ingresar(self, login: LoginEntity) -> object:
        return self.__core.Login(login)
    def salir(self, idUser:str):
        return self.__core.logout(idUser)
