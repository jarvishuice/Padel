from abc import ABC,abstractmethod
from core.Entities.users.userEntity import UserEntity


class IUser(ABC):
    @abstractmethod
    def crearUser(self,user:UserEntity)-> object: ...
    @abstractmethod
    def getAllUsers(self)-> object: ...
    @abstractmethod
    def searchUserBYId(self,id:str): ...
    @abstractmethod
    def searcUserByUserName(self,userName:str): ...
    @abstractmethod
    def searchUserBytoken(self,token:str): ...
    @abstractmethod
    def actulizarContrasena(self,password:str): ...
    @abstractmethod
    def actualizar(self,user:UserEntity): ...
    





