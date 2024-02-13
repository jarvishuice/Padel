import time
from config.LOGS.LogsSystem import Logs
from config.utils.override import override
from core.Entities.pagos.PagosEntity import PagosEntity
from core.interface.pagos.IPagos import IPagos
from providers.Db.PostgresConection import Psql,ResponseInternalEntity


class PagosDAO(Psql,IPagos,Logs):
    def __init__(self):
        self.Warnings("Nueva Instacian de pagos ")
        super().__init__()

    def registrarPago(self, pago: PagosEntity) -> ResponseInternalEntity:
        try:
            #generando el id
            pago.id = time.time()
            conexion = self.connect()
            if conexion.status == False:
                self.Error("Error de conexion  a la Base de datos ")
                return ResponseInternalEntity(status=False,
                                              message="Error de conexion a la base de datos",
                                              response=None)
            with self.conn.cursor() as cur:
                cur.execute(f"""
                            INSERT INTO public.pagos (id, id_orden, id_persona, total, iva, igtf, id_concepto) 
                            VALUES('{pago.id}', '{pago.idOrden}', '{pago.idPersona}', {pago.total}, {pago.IVA}, 
                            {pago.IGTF}, {pago.idConcepto});
                            """)
                self.conn.commit()
            self.WirterTask(f"Psago registrado de manera exitosa con el id [{pago.id}]")
            return ResponseInternalEntity(status=True,
                                          message="Pago Registrado con exito ",
                                          response=pago)
        except self.INTEGRIDAD_ERROR as e:
            Logs.Error(f"Error de integridad en la base de datos  as [{e}]")
            return ResponseInternalEntity(status=False,
                                          message=f" Error de integridad en la base de datos detalles [{e}]",
                                          response=None)
        except self.DATABASE_ERROR as e:
            Logs.Error(f"Error de base de datos detail[{e}]")
            return ResponseInternalEntity(status=False,
                                          message="error de base de datos",
                                          response=None)
        except self.INTERFACE_ERROR as e:
            Logs.Error(f"Error de interface detail {e}")
            return ResponseInternalEntity(status=False,
                                          message="Error de interface en base de datos",
                                          response=None)
        except self.OPERATIONAL_ERROR as e:
            Logs.Error(f"Error de operaciones detail [{e}]")
            return ResponseInternalEntity(status=False,
                                          message="Error de operaciones en la base de datos",
                                          response=None)
        finally:
            Logs.WirterTask("ha finaliado la ejecucion    de registro de pago  [PagosDAO]")
            self.disconnect()