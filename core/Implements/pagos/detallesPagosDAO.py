import time
from config.LOGS.LogsSystem import Logs
from core.interface.pagos.IDetallesPagos import IDetallesPagos,DetallesPagosEntity
from providers.Db.PostgresConection import Psql,ResponseInternalEntity


class DetallesPagosDAO(Psql,IDetallesPagos,Logs):
    def __init__(self):
        self.Warnings("instanciando detalles Pagos")
        super().__init__()

    def RegistrarDetalle(self, detalle:DetallesPagosEntity) -> ResponseInternalEntity:
        try:
            conexion:ResponseInternalEntity = self.connect()
            detalle.id = time.time()
            if not conexion.status:
                self.Error("error de conexion a la base de datos")
                return ResponseInternalEntity(status=False,
                                              message="error de conexion a la base de datos ",
                                              response=None
                                              )
            with self.conn.cursor() as cur:
                cur.execute(f"""
                INSERT INTO public.detalles_pagos (id, id_pago, id_forma_pago, monto, id_tasa)
                 VALUES('{detalle.id}', '{detalle.idPago}', '{detalle.idFormaPago}', {detalle.monto}, 
                 '{detalle.idTasa}');
                """)
                self.conn.commit()
            return ResponseInternalEntity(status=True,
                                          message="detalle registrado de manera orrecta ",
                                          response=detalle)
        except self.INTEGRIDAD_ERROR as e:
            self.Error(f"Error de integridad en la base de datos  as [{e}]")
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
            Logs.WirterTask("ha finaliado la ejecucion registro detalles de pagos [deatllesPagosDAO]")
            self.disconnect()
