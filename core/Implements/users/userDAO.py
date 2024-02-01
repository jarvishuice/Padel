from providers.helpers.hash import HashHelper
from providers.Db.PostgresConection import Psql,ResponseInternal,Logs,ResponseInternalEntity,override
from core.interface.users.Iuser import IUser,UserEntity
import time
class UserDAO(Psql,IUser,Logs):


    __cifrador: HashHelper = HashHelper()
    def __init__(self):
        """

        :rtype: object
        """
        #self.__cifrador = HashHelper()
        super().__init__()

    def crearUser(self, user: UserEntity) -> object :
        """

        :rtype: object
        """
        try:
            user.password = self.__cifrador.cifrar(user.password)
            user.id = time.time()
            user.nombre = user.nombre.upper()
            user.token = self.__cifrador.cifrar(user.password)
            conection:ResponseInternalEntity= self.connect()
            if conection == False :
                self.Error(f"error de conexion al sevidor DB {conection.message}")
                return ResponseInternal.responseInternal(ResponseInternalEntity(status=False,message=conection.message,response=None))

            with self.conn.cursor()  as cur:
                cur.execute(f"""INSERT INTO public.usuarios (id, nombre, cedula, correo, tipo_usuario, "token", status, 
                "password",url_imagen) VALUES('{user.id}', '{user.nombre}', '{user.cedula}', '{user.correo}', {user.tipoUsuario}, '{user.token}', 'desconectado'::character varying, '{user.password}','{user.urlImg}');""")
            self.conn.commit()
            user.password = "🖕🖕"
            return ResponseInternal.responseInternal(ResponseInternalEntity(status=True,message=f"Usuario registrado con exito detail [{user}]",response=user))
        except self.INTEGRIDAD_ERROR as e:
            Logs.Error(f"Error de integridad en la base de datos  as [{e}]")
            return  ResponseInternal.responseInternal(ResponseInternalEntity(status= False,message="Puedes que estes registrando un usuario cuyos datos ya existen en nuestra base de datos verifica y si el problema persite comuniquese con el equipo de soporte",response=None))
        except self.DATABASE_ERROR as e:
            Logs.Error(f"Error de base de datos  detail[{e}]")
            return ResponseInternal.responseInternal(ResponseInternalEntity(status=False,message="error de base de datos",response=None))
        except self.INTERFACE_ERROR as e :
            Logs.Error(f"Error de interface detail {e}")
            return ResponseInternal.responseInternal(ResponseInternalEntity(status=False,message="Error de interface en base de datos",response=None))
        except self.OPERATIONAL_ERROR as e :
            Logs.Error(f"Error de operaciones detail [{e}]")
            return ResponseInternal.responseInternal(ResponseInternalEntity(status=False,message="Error de operaciones en la base de datos",response= None))
        finally:
            self.disconnect()


    @property
    def getAllUsers (self) -> object :
        try :
            data = []
            conection: ResponseInternalEntity = self.connect ()
            if conection == False :
                self.Error (f"error de conexion al sevidor DB {conection.message}")
                return ResponseInternal.responseInternal (
                    ResponseInternalEntity (status=False, message=conection.message, response=None))

            with self.conn.cursor () as cur :
                cur.execute(f""" select * from usuarios;""")
                if cur.rowcount <= 0:
                    self.Warnings("no se encontraron Usuarios")
                for i in cur:
                    data.append(UserEntity(id=i[0],nombre=i[1],cedula=i[2],correo=i[3],tipoUsuario=int(i[4]),token=i[5],status=i[6],password="🖕🖕",urlImg=i[8]))

                return ResponseInternal.responseInternal(ResponseInternalEntity (status=True, message=f"Usuarios leidos con exito detail [{data}]",
                                        response=data))
        except self.INTEGRIDAD_ERROR as e :
            Logs.Error (f"Error de integridad en la base de datos  as [{e}]")
            return ResponseInternal.responseInternal (ResponseInternalEntity (status=False,
                                                                              message="Puedes que estes registrando un usuario cuyos datos ya existen en nuestra base de datos verifica y si el problema persite comuniquese con el equipo de soporte",
                                                                              response=None))
        except self.DATABASE_ERROR as e :
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


    def searchUserBYId (self, id: str) :
        try :
            data = [ ]
            conection: ResponseInternalEntity = self.connect ()
            if conection == False :
                self.Error (f"error de conexion al sevidor DB {conection.message}")
                return ResponseInternal.responseInternal (
                    ResponseInternalEntity (status=False, message=conection.message, response=None))

            with self.conn.cursor () as cur :
                cur.execute(f""" select * from usuarios where id = '{id}';""")
                if cur.rowcount <= 0 :
                    self.Warnings ("no se encontraron Usuarios")
                for i in cur :
                    data.append (
                        UserEntity (id=i[ 0 ], nombre=i[ 1 ], cedula=i[ 2 ], correo=i[ 3 ], tipoUsuario=int (i[ 4 ]),
                                    token=i[ 5 ], status=i[ 6 ], password="🖕🖕", urlImg=i[ 8 ]))

                return ResponseInternal.responseInternal (
                    ResponseInternalEntity (status=True, message=f"Usuarios leidos con exito detail [{data}]",
                                            response=data))
        except self.INTEGRIDAD_ERROR as e :
            Logs.Error (f"Error de integridad en la base de datos  as [{e}]")
            return ResponseInternal.responseInternal (ResponseInternalEntity (status=False,
                                                                              message="Puedes que estes registrando un usuario cuyos datos ya existen en nuestra base de datos verifica y si el problema persite comuniquese con el equipo de soporte",
                                                                              response=None))
        except self.DATABASE_ERROR as e :
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

    def searchUserBytoken (self, token: str) :
        try :
            data = []
            conection: ResponseInternalEntity = self.connect ()
            if conection == False :
                self.Error (f"error de conexion al sevidor DB {conection.message}")
                return ResponseInternal.responseInternal (
                    ResponseInternalEntity (status=False, message=conection.message, response=None))

            with self.conn.cursor () as cur :
                cur.execute (f""" select * from usuarios where token = '{token}';""")
                if cur.rowcount <= 0 :
                    self.Warnings ("no se encontraron Usuarios")
                for i in cur :
                    data.append (
                        UserEntity (id=i[ 0 ], nombre=i[ 1 ], cedula=i[ 2 ], correo=i[ 3 ], tipoUsuario=int (i[ 4 ]),
                                    token=i[ 5 ], status=i[ 6 ], password="🖕🖕", urlImg=i[ 8 ]))

                return ResponseInternal.responseInternal (
                    ResponseInternalEntity (status=True, message=f"Usuarios leidos con exito detail [{data}]",
                                            response=data))
        except self.INTEGRIDAD_ERROR as e :
            Logs.Error (f"Error de integridad en la base de datos  as [{e}]")
            return ResponseInternal.responseInternal (ResponseInternalEntity (status=False,
                                                                              message="Puedes que estes registrando un usuario cuyos datos ya existen en nuestra base de datos verifica y si el problema persite comuniquese con el equipo de soporte",
                                                                              response=None))
        except self.DATABASE_ERROR as e :
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
    def searcUserByUserName(self, userName: str):
        try :
            data = []
            conection: ResponseInternalEntity = self.connect()
            if conection == False:
                self.Error(f"error de conexion al sevidor DB {conection.message}")
                return ResponseInternal.responseInternal(
                    ResponseInternalEntity(status=False, message=conection.message, response=None))

            with self.conn.cursor() as cur:
                cur.execute(f""" select * from usuarios where cedula = '{userName}';""")
                if cur.rowcount <= 0:
                    self.Warnings("no se encontraron Usuarios")
                for i in cur:
                    data.append(
                        UserEntity (id=i[0], nombre=i[1], cedula=i[2], correo=i[3], tipoUsuario=int (i[4]),
                                    token=i[5], status=i[6], password=i[7], urlImg=i[8]))

                return ResponseInternal.responseInternal(
                    ResponseInternalEntity(status=True, message=f"Usuarios leidos con exito detail [{data}]",
                                            response=data))
        except self.INTEGRIDAD_ERROR as e :
            Logs.Error(f"Error de integridad en la base de datos  as [{e}]")
            return ResponseInternal.responseInternal(ResponseInternalEntity (status=False,
                                                                              message="Puedes que estes registrando un usuario cuyos datos ya existen en nuestra base de datos verifica y si el problema persite comuniquese con el equipo de soporte",
                                                                              response=None))
        except self.DATABASE_ERROR as e :
            Logs.Error (f"Error de base de datos  detail[{e}]")
            return ResponseInternal.responseInternal(
                ResponseInternalEntity(status=False, message="error de base de datos", response=None))
        except self.INTERFACE_ERROR as e:
            Logs.Error (f"Error de interface detail {e}")
            return ResponseInternal.responseInternal(
                ResponseInternalEntity (status=False, message="Error de interface en base de datos", response=None))
        except self.OPERATIONAL_ERROR as e :
            Logs.Error (f"Error de operaciones detail [{e}]")
            return ResponseInternal.responseInternal(
                ResponseInternalEntity(status=False, message="Error de operaciones en la base de datos",
                                        response=None))
        finally:
            self.disconnect()
    def actulizarContrasena (self, password: str) :
        pass

    def actualizar (self, user: UserEntity) :
        """

                :rtype: object
                """
        try :
            user.password = self.__cifrador.cifrar (user.password)
            user.id = time.time ()
            user.nombre = user.nombre.upper ()
           # user.token = self.__cifrador.cifrar (user.password)
            conection: ResponseInternalEntity = self.connect ()
            if conection == False :
                self.Error (f"error de conexion al sevidor DB {conection.message}")
                return ResponseInternal.responseInternal (
                    ResponseInternalEntity (status=False, message=conection.message, response=None))

            with self.conn.cursor () as cur :
                cur.execute(f"""UPDATE public.usuarios SET nombre='{user.nombre}',cedula ='{user.cedula}',correo= '{user.correo}',tipo_usuario= {user.tipoUsuario},token= '{user.token}', status='{user.status}' where id='{user.id}';""")
            self.conn.commit()
            user.password = "🖕🖕"
            return ResponseInternal.responseInternal (
                ResponseInternalEntity (status=True, message=f"Usuario registrado con exito detail [{user}]",
                                        response=user))
        except self.INTEGRIDAD_ERROR as e :
            Logs.Error (f"Error de integridad en la base de datos  as [{e}]")
            return ResponseInternal.responseInternal (ResponseInternalEntity (status=False,
                                                                              message="Puedes que estes registrando un usuario cuyos datos ya existen en nuestra base de datos verifica y si el problema persite comuniquese con el equipo de soporte",
                                                                              response=None))
        except self.DATABASE_ERROR as e :
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



