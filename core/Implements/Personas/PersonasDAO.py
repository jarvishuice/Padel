import time

from config.utils.override import override
from providers.Db.PostgresConection import Psql
from config.LOGS.LogsSystem import Logs
from core.interface.personas.IPersona import IPersona,ResponseInternalEntity,PersonaEntity
class ClientesDAO(IPersona,Psql,Logs):

    def __init__(self):
        """

        :rtype: object
        """
        super().__init__()
    @override
    def crearCliente (self, client: PersonaEntity) -> ResponseInternalEntity:
        """

        :param client: PersonaEntity
        :return: ResponseInternalEntity
        """
        try:
            conexion = self.connect()
            client.id = str(time.time())
            if conexion.status != True:
                Logs.Error("Error de conexion la la base de datos ")
                return ResponseInternal.responseInternal(ResponseInternalEntity(status=False,message=str("error de conexion a la base de datos")))
            with self.conn.cursor() as cur:
                cur.execute(f"""INSERT INTO public.persona (id,ci, nombre, telefono, correo, direccion, fecha_ingreso, url_imagen, deuda,id_tipo_persona) VALUES( 
                '{client.id}','{client.ci}', '{client.nombre}', '{client.telefono}', '{client.correo}', '{client.direccion}','now()', 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fpreviews.123rf.com%2Fimages%2Fylivdesign%2Fylivdesign2101%2Fylivdesign210102017%2F162572026-icono-de-cliente-estilo-de-esquema.jpg&tbnid=qyxQPn0J7Mtr0M&vet=12ahUKEwj9983x4_iDAxVpYTABHTF6B-UQMygEegUIARCAAQ..i&imgrefurl=https%3A%2F%2Fes.123rf.com%2Fphoto_162572026_icono-de-cliente-estilo-de-esquema.html&docid=ngLMwSLUgWLwdM&w=1300&h=1300&q=clientes&hl=es-419&client=firefox-b-e&ved=2ahUKEwj9983x4_iDAxVpYTABHTF6B-UQMygEegUIARCAAQ'::character varying, 0.0,{client.idTIpoPersona});""")
                self.conn.commit()
            return ResponseInternal.responseInternal(ResponseInternalEntity(status=True,message="cliente regitrado con exito ",response=client))
        except self.INTEGRIDAD_ERROR as e:
            Logs.Error(f"Error de integridad en la base de datos  as [{e}]")
            return  ResponseInternal.responseInternal(ResponseInternalEntity(status= False,message="Puedes que estes regiuitrando un cliente cuyos datos ya existen en nuestra base de datos verifica y si el problema persite comuniquese con el equipo de soporte",response=None))
        except self.DATABASE_ERROR as e:
            Logs.Error(f"Error de base de datos  detail[{e}]")
            return ResponseInternal.responseInternal(ResponseInternalEntity(status=False,message="error de base de datos",response=None))
        except self.INTERFACE_ERROR as e :
            Logs.Error(f"Error de interface detail {e}")
            return ResponseInternalEntity(status=False,message="Error de interface en base de datos",response=None)
        except self.OPERATIONAL_ERROR as e :
            Logs.Error(f"Error de operaciones detail [{e}]")
            return ResponseInternal.responseInternal(ResponseInternalEntity(status=False,message="Error de operaciones en la base de datos",response= None))
        finally:
            self.disconnect()
    @override
    def getAllClientes (self) -> ResponseInternalEntity :
        try:
            data =[]
            conexion = self.connect()
            if conexion.status != True :
                Logs.Error("Error de conexion la la base de datos ")
                return ResponseInternal.responseInternal(
                    ResponseInternalEntity(status=False, message=str("error de conexion a la base de datos")))
            with self.conn.cursor() as cur :
                cur.execute(f"select  * from persona")
                count =  cur.rowcount
                if count <= 0:
                    Logs.Warnings("NO se encontraron registros en la tabla clientes puede que algo este mal por favor valida ")
                for items in cur:
                    data.append(PersonaEntity(id=items[8 ], ci=items[0 ], nombre=items[1 ], telefono=items[2 ],
                                              correo=items[3], direccion=items[4], fechaIngreso=str(items[5]),
                                              urlImagen=items[6], deuda=float(items[7]), idTIpoPersona=int(items[9])))
            return ResponseInternal.responseInternal(
                ResponseInternalEntity(status=True, message="cliente regitrado con exito ", response=data))

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

    @override
    def searchClienteByCi (self, ci: str) -> ResponseInternalEntity :
        try :
            data = []
            conexion = self.connect ()
            if conexion.status != True :
                Logs.Error ("Error de conexion la la base de datos ")
                return ResponseInternal.responseInternal (
                    ResponseInternalEntity (status=False, message=str ("error de conexion a la base de datos")))
            with self.conn.cursor() as cur:
                cur.execute (f"select  * from persona where ci = '{ci}'")
                count = cur.rowcount
                if count <= 0 :
                    Logs.Warnings (
                        "NO se encontraron registros en la tabla clientes puede que algo este mal por favor valida ")
                for items in cur :
                    data.append (PersonaEntity (id=items[8 ], ci=items[0 ], nombre=items[1 ], telefono=items[2 ],
                                                correo=items[3], direccion=items[4], fechaIngreso=str (items[5]),
                                                urlImagen=items[6], deuda=float (items[7]), idTIpoPersona=int(items[9])))
                return ResponseInternal.responseInternal (
                    ResponseInternalEntity (status=True, message="cliente regitrado con exito ", response=data))

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
    def searchClienteByName(self,name:str) -> ResponseInternalEntity: ...

