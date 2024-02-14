import time
from config.utils.override import override
from core.interface.finance.Banco.IBAnco import IBanco,BancoEntity
from providers.Db.PostgresConection import Psql,ResponseInternalEntity,ResponseInternal,Logs
class BancoDAO(IBanco,Psql):
    def __init__(self):
        super().__init__()
    @override
    def crearBanco (self, Banco: BancoEntity) -> ResponseInternalEntity:
        try:
            Banco.id = time.time()
            Banco.nombre=Banco.nombre.upper()
            conection =  self.connect()
            if conection.status != True:
                Logs.Error("Error de conexion a la base de datos")
                return ResponseInternal.responseInternal(ResponseInternalEntity(status= False ,message="Erro de conexion al servidor BD"),None)
            with self.conn.cursor() as cur:
                cur.execute(f" insert into bancos(id,nombre) values('{Banco.id}','{Banco.nombre}');")
                self.conn.commit()
            return ResponseInternal.responseInternal(ResponseInternalEntity(status=True,message="Banco REgistrado con exito",response=Banco))
        except self.INTEGRIDAD_ERROR as e:
            Logs.Error(f"Error de integridad en la base de datos  as [{e}]")
            return  ResponseInternal.responseInternal(ResponseInternalEntity(status= False,message="Estas Registrando un banco el cual ya etsa registrado",response=None))
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
    def getAllBanco(self) -> ResponseInternalEntity:
        """

        :rtype: object
        """
        try:
            data=[]
            conection =  self.connect()
            if conection.status != True:
                Logs.Error("Error de conexion a la base de datos")
                return ResponseInternal.responseInternal(ResponseInternalEntity(status= False ,message="Erro de conexion al servidor BD"),None)
            with self.conn.cursor() as cur:
                cur.execute(f"select * from bancos")
                count = cur.rowcount
                if count <= 0:
                    Logs.Warnings("no se encontro ningun Banco registrado")
                for i in cur:
                    data.append(BancoEntity(id=i[0],nombre=i[1]))
            return ResponseInternal.responseInternal(ResponseInternalEntity(status=True,message="Banco REgistrado con exito",response=data))
        except self.INTEGRIDAD_ERROR as e:
            Logs.Error(f"Error de integridad en la base de datos  as [{e}]")
            return  ResponseInternal.responseInternal(ResponseInternalEntity(status= False,message="Estas Registrando un banco el cual ya etsa registrado",response=None))
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




