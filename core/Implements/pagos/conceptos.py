from config.LOGS.LogsSystem import Logs
from config.utils.override import override
from core.Entities.ResponseINternalEntity import ResponseInternalEntity
from core.Entities.pagos.conceptos import ConceptosPagosEntity
from core.ROOM.ResponseInternal import ResponseInternal
from core.interface.pagos.IConceptos import IConceptos
from providers.Db.PostgresConection import Psql


class ConceptosDAO(IConceptos,Psql):
    def __init__(self):
        super().__init__()
    @override
    def crearConcepto(self, Concepto: ConceptosPagosEntity) -> ResponseInternalEntity :
       try:
           Concepto.nombre = Concepto.nombre.upper()
           conection:ResponseInternalEntity  = self.connect()
           if conection.status == False :
                return ResponseInternal.responseInternal (
                ResponseInternalEntity (status=False, message="Erro de conexion al servidor BD", response=None))
           with self.conn.cursor() as cur :
               cur.execute(f"insert into conceptos_pagos (id,nombre,descripcion) values((SELECT max(id) + 1 as nuevoID FROM conceptos_pagos),'{Concepto.nombre}','{Concepto.descripcion}')")
           self.conn.commit()
           return ResponseInternal.responseInternal(ResponseInternalEntity(status=True,message="exito al registrar concepto de pago",response=Concepto))
       except self.INTEGRIDAD_ERROR as e :
           Logs.Error (f"Error de integridad en la base de datos  as [{e}]")
           return ResponseInternal.responseInternal (
               ResponseInternalEntity (status=False, message="Estas Registrando un concepto el cual ya etsa registrado",
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
               ResponseInternalEntity (status=False, message="Error de operaciones en la base de datos", response=None))
       finally :
           self.disconnect ()

    @property
    def getAllConceptos(self) -> ResponseInternalEntity :
        try:
            data = []
            conection: ResponseInternalEntity = self.connect()
            if conection.status != True:
                Logs.Error("Error de conexion a la base de datos")
                return ResponseInternal.responseInternal(
                    ResponseInternalEntity(status=False, message="Error de conexion al servidor BD", response=None))
            with self.conn.cursor() as cur:
                cur.execute(f"select * from conceptos_pagos order by id asc;")
                count = cur.rowcount
                if count <= 0:
                    Logs.Warnings("no se encontro ningun Banco registrado")
                for i in cur:
                    data.append(ConceptosPagosEntity(id=int(i[0]), nombre=str(i[1]), descripcion=str(i[2])))
            return ResponseInternal.responseInternal(
                ResponseInternalEntity(status=True, message="Conceptos leidos con exito", response=data))
        except self.INTEGRIDAD_ERROR as e:
            Logs.Error(f"Error de integridad en la base de datos  as [{e}]")
            return ResponseInternal.responseInternal(
                ResponseInternalEntity(status=False, message="Estas Registrando un banco el cual ya etsa registrado", response=None))
        except self.DATABASE_ERROR as e:
            Logs.Error(f"Error de base de datos  detail[{e}]")
            return ResponseInternal.responseInternal(
                ResponseInternalEntity(status=False, message="error de base de datos", response=None))
        except self.INTERFACE_ERROR as e:
            Logs.Error(f"Error de interface detail {e}")
            return ResponseInternal.responseInternal(
                ResponseInternalEntity(status=False, message="Error de interface en base de datos", response=None))
        except self.OPERATIONAL_ERROR as e:
            Logs.Error(f"Error de operaciones detail [{e}]")
            return ResponseInternal.responseInternal(
                ResponseInternalEntity(status=False, message="Error de operaciones en la base de datos", response=None))
        finally:
            self.disconnect()