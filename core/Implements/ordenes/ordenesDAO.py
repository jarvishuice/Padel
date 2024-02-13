import datetime

from providers.helpers.hash import HashHelper
from providers.Db.PostgresConection import Psql,ResponseInternal,Logs,ResponseInternalEntity,override
from core.interface.ordenes.IOrdenes import IOrdenes,OrdenEntity
import time

class OrdenesDAO(IOrdenes,Psql):

    def __init__(self):
        super().__init__()
    @override
    def registrarOrden(self, orden: OrdenEntity) -> ResponseInternalEntity:
        try:
            orden.id = time.time()
            orden.fechaApertura = str(datetime.datetime.now())

            conection =  self.connect()
            if conection.status ==False:
                return ResponseInternalEntity(status=False,message="error de conecioin al servidor de DB ",response=None)
            with self.conn.cursor() as cur:
                cur.execute(f"insert into ordenes(id,total,id_persona,fecha_apertura,fecha_pago,iva,igtf,sub_total,status,id_concepto) values('{orden.id}',{orden.total},'{orden.idCliente}','{orden.fechaApertura}','{orden.fechaPago}',{orden.IVA},{orden.IGTF},{orden.subTotal},'{orden.status}','{orden.idConcepto}')")
                self.conn.commit()
            Logs.WirterTask(f"ORDEN #[{orden.id}] -> registrada con exito !!!")
            return ResponseInternalEntity(status = True, message= "exito al registrar la nueva orden ",response = orden)
        except self.INTEGRIDAD_ERROR as e:
            Logs.Error(f"Error de integridad en la base de datos  as [{e}]")
            return  ResponseInternal.responseInternal(ResponseInternalEntity(status= False,message="Puedes que estes registrando una orden cuyos datos ya existen en nuestra base de datos verifica y si el problema persite comuniquese con el equipo de soporte",response=None))
        except self.DATABASE_ERROR as e:
            Logs.Error(f"Error de base de datos  detail[{e}]")
            print({e})
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
    def getAllOrden(self):

            try :
                data = []
                conection = self.connect ()
                if conection.status == False :
                    return ResponseInternalEntity (status=False, message="error de conecioin al servidor de DB ",
                                                   response=None)
                with self.conn.cursor () as cur :
                    cur.execute ("select * from ordenes order by id Desc")
                    count = cur.rowcount
                    if count <=0 :
                        Logs.Warnings("no se encontraron ordenes")
                        return ResponseInternalEntity(status=True,message="no se encontraro prdenes",response=data)
                    for i in cur:
                        data.append(
                                    OrdenEntity(
                                                id=i[0],
                                                total=float(i[1]),
                                                idCliente=i[2],
                                                fechaApertura=str(i[3]),
                                                fechaPago=i[4],
                                                IVA=float(i[5]),
                                                IGTF=float(i[6]),
                                                subTotal=float(i[7]),
                                                status=i[8],
                                                idConcepto=int(i[9])
                                                ))
                    return ResponseInternalEntity(status=True,message= "Ordenes leidas con exito",response=data)
            except self.INTEGRIDAD_ERROR as e:
                Logs.Error(f"Error de integridad en la base de datos  as [{e}]")
                return ResponseInternal.responseInternal (ResponseInternalEntity (status=False,
                                                                                  message="Puedes que estes registrando una orden cuyos datos ya existen en nuestra base de datos verifica y si el problema persite comuniquese con el equipo de soporte",
                                                                                  response=None))
            except self.DATABASE_ERROR as e:
                Logs.Error(f"Error de base de datos  detail[{e}]")
                print({e})
                return ResponseInternal.responseInternal(
                    ResponseInternalEntity(status=False, message="error de base de datos", response=None))
            except self.INTERFACE_ERROR as e :
                Logs.Error (f"Error de interface detail {e}")
                return ResponseInternal.responseInternal (
                    ResponseInternalEntity (status=False, message="Error de interface en base de datos", response=None))
            except self.OPERATIONAL_ERROR as e :
                Logs.Error (f"Error de operaciones detail [{e}]")
                return ResponseInternal.responseInternal (
                    ResponseInternalEntity (status=False, message="Error de operaciones en la base de datos",
                                            response=None))
            finally:
                self.disconnect()