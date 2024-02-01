import time

from core.Entities.users.userEntity import UserEntity
from providers.Db.PostgresConection import Psql,Logs,ResponseInternalEntity,ResponseInternal,override
from providers.helpers.hash import HashHelper
from core.interface.users.ILogin import ILogin,LoginEntity

class LoginDAO(Psql,ILogin,ResponseInternal,Logs):
    """

    """
    __helper = HashHelper()

    def __init__(self) :
        """

        :rtype: object
        """
        self.__helper = HashHelper()
        super ().__init__()
 

    def validarUsuario(self, userName: str) -> object:
        try:
            data= []
            conection:ResponseInternalEntity = self.connect()
            if conection.status != True :
                self.Error(f"Error de conexion al servidor de Db {conection.status} ")
                return self.responseInternal(ResponseInternalEntity(status=False,message=f"error de conexion al servidor de BD",response=None))
            with self.conn.cursor() as cur:
                cur.execute(f"""select * from usuarios where cedula = '{userName}' """)
                count = cur.rowcount
                if count <= 0:
                    return self.responseInternal(ResponseInternalEntity(status=False,message=f"error el usuario {userName}  no se encuentra registrado en el sistema",response=False))
                for i in cur:
                    data.append(UserEntity(id=i[0],nombre=i[1],cedula=i[2],correo=i[3],tipoUsuario=int(i[4]),token=i[5],status=i[6],password=i[7],urlImg=i[8]))
                return self.responseInternal(ResponseInternalEntity(status = True,message= "Usuario encontrado",response=data))
        except self.INTEGRIDAD_ERROR as e:
                Logs.Error (f"Error de integridad en la base de datos  as [{e}]")
                return ResponseInternal.responseInternal (ResponseInternalEntity (status=False,
                                                                                  message="Puedes que estes registrando un usuario cuyos datos ya existen en nuestra base de datos verifica y si el problema persite comuniquese con el equipo de soporte",
                                                                                  response=None))
        except self.DATABASE_ERROR as e:
            Logs.Error (f"Error de base de datos  detail[{e}]")
            return ResponseInternal.responseInternal (
                ResponseInternalEntity (status=False, message="error de base de datos", response=None))
        except self.INTERFACE_ERROR as e :
            Logs.Error (f"Error de interface detail {e}")
            return ResponseInternal.responseInternal (
                ResponseInternalEntity (status=False, message="Error de interface en base de datos", response=None))
        except self.OPERATIONAL_ERROR as e :
            Logs.Error (f"Error de operaciones detail [{e}]")
            return ResponseInternal.responseInternal (
                ResponseInternalEntity (status=False, message="Error de operaciones en la base de datos",
                                        response=None))
        finally :
            self.disconnect ()

    @override
    def Login(self, login: LoginEntity):
        """

        :param login:
        :return:
        """
        try:
            #token
            token  = self.__helper.cifrar(str(time.time()))
            #cifrado de la contrasena para validarla con la de base de datos
            password = self.__helper.cifrar(login.password)
            #llamada al metodo que valida la exitencia del usuario
            usuario:ResponseInternalEntity = self.validarUsuario(login.userName)

            #validacion del; usuario
            if usuario.status == False:
                self.Error("Error al autenticar el usuario")
                return self.responseInternal(ResponseInternalEntity(status=False,message=usuario.message,response=None))


            conection:ResponseInternalEntity = self.connect()
            print(password)
            print(usuario.response[0].password)
            if  usuario.response[0].password != self.__helper.decifrar(password,usuario.response[0].password):
                self.Error(f"fallo de login de parte del usuario [{usuario.response[0].nombre}] detail [Password Erroneo]")
                return self.responseInternal(ResponseInternalEntity(status=False,message="ha ingresado un password invalido ",response = None))
            self.Warnings(f"el usuario {usuario.response.nombre} ha sido validado  ......")
            if conection.status != True:
                self.Error(f"Error de conexion al servidor de Db {conection.status} ")
                return self.responseInternal(ResponseInternalEntity(status=False,message=f"error de conexion al servidor de BD",response=None))
            with self.conn.cursor() as cur:
                usuario.response.token = token
                usuario.response.status = "CONECTADO"
                cur.execute(f""" UPDATE public.usuarios SET token ='{usuario.response.token}', status = '{usuario.response.status}'""")

                count = cur.rowcount
                if count <= 0:
                    return self.responseInternal(ResponseInternalEntity(status=False,message=f"error no se pudo iniciar seccion"),response = None)
                return self.responseInternal (
                    ResponseInternalEntity (status=True, message=f"el usuario {usuario.response.nombre} ha iniciado seccion demanera correcta detail  [{usuario.response}]" ), response=usuario.response)
        except self.INTEGRIDAD_ERROR as e:
                Logs.Error (f"Error de integridad en la base de datos  as [{e}]")
                return ResponseInternal.responseInternal (ResponseInternalEntity (status=False,
                                                                                  message="Puedes que estes registrando un usuario cuyos datos ya existen en nuestra base de datos verifica y si el problema persite comuniquese con el equipo de soporte",
                                                                                  response=None))
        except self.DATABASE_ERROR as e:
            Logs.Error (f"Error de base de datos  detail[{e}]")
            return ResponseInternal.responseInternal (
                ResponseInternalEntity (status=False, message="error de base de datos", response=None))
        except self.INTERFACE_ERROR as e :
            Logs.Error (f"Error de interface detail {e}")
            return ResponseInternal.responseInternal (
                ResponseInternalEntity (status=False, message="Error de interface en base de datos", response=None))
        except self.OPERATIONAL_ERROR as e :
            Logs.Error (f"Error de operaciones detail [{e}]")
            return ResponseInternal.responseInternal (
                ResponseInternalEntity (status=False, message="Error de operaciones en la base de datos",
                                        response=None))
        finally :
            self.disconnect ()



    def logout (self, idUser: str) -> object :
        """

        :param idUser:
        :return:
        """
        pass

