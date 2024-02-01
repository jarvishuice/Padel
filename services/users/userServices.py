from core.Implements.users.userDAO import UserDAO,UserEntity,ResponseInternalEntity,ResponseInternal,Logs
class UserServices(Logs):
     __core= None
     def __init__(self):
         self.__core = UserDAO()
         super().__init__()
     def CrearUsuario(self,user:UserEntity) -> object  | ResponseInternalEntity:
         """

         :param user:
         :return: object
         """
         return self.__core.crearUser(user)
     @property
     def leerTodosLosUsuarios(self):
         return self.__core.getAllUsers

     def buscarUsuarioPorId(self,id:str):
         """

         :param id
         :return:
         """
         return self.__core.searchUserBYId(id)
     def buscarUsuarioPorToken(self, token: str) -> object:
         """
         :return:
         :rtype: object
         :param token:
         :return:
         """
         return self.__core.searchUserBytoken(token)