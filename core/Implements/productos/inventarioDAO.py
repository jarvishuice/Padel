from config.LOGS.LogsSystem import Logs
from config.utils.override import override
from core.Entities.Productos.inventarioEntity import inventarioEntityOut
from core.interface.productos.IInventario import IInventario,InventarioEntity
from providers.Db.PostgresConection import Psql,ResponseInternalEntity


class InventarioDAO(IInventario,Psql,Logs):
    def __init__(self):
        super().__init__()

    @override
    def registrar(self, producto: InventarioEntity) -> ResponseInternalEntity :
        try:
            conexion = self.connect()
            if conexion == False:
                return ResponseInternalEntity(status=False,
                                              message='Error de conexion al servidor de base de datos',
                                              response=None)
            with self.conn.cursor() as cur:
                cur.execute(f""" INSERT INTO public.inventario (id_producto, cantidad) VALUES('{producto.idProducto}', {producto.cantidad});""")
            self.conn.commit()
            return ResponseInternalEntity(status=True,
                                          message="Exito al registrar el inventario",
                                          response=producto)
        except self.INTEGRIDAD_ERROR as e:
            Logs.Error(f"Error de integridad en la base de datos  as [{e}]")
            return ResponseInternalEntity(status=False,
                                          message=f"error de integridad de datos detalle [{e}]",
                                          response=None)
        except self.DATABASE_ERROR as e:
            Logs.Error(f"Error de base de datos  detail[{e}]")
            return ResponseInternalEntity(status=False,
                                          message="error de base de datos",
                                          response=None)
        except self.INTERFACE_ERROR as e:
            Logs.Error(f"Error de interface detail {e}")
            return ResponseInternalEntity(status=False,
                                          message="Error de interface en base de datos",response=None)
        except self.OPERATIONAL_ERROR as e:
            Logs.Error(f"Error de operaciones detail [{e}]")
            return ResponseInternalEntity(status=False,message="Error de operaciones en la base de datos",response= None)
        finally:
            Logs.WirterTask("ha finaliado la ejecucion del registros de productos DAO")
            self.disconnect()

    @property
    def Obtenernventario(self):
        try:
            data = []
            conexion = self.connect()
            if conexion.status ==False:
                self.Error("Error de conexion  al servidor de base de datos ")
                return ResponseInternalEntity(status=False,
                                              message="error de conexion a la base de datos",
                                              response=None)
            with self.conn.cursor() as cur:
                cur.execute("""select p.id ,p.nombre ,p.precio,p.costo ,i.cantidad 
                               from productos p 
                               inner join inventario i  on  i.cantidad =i.cantidad 
                               where p.id = i.id_producto """)
                count = cur.rowcount
                if count <= 0:
                    self.Warnings("no se encontraron productos en el inventario ")
                    return ResponseInternalEntity(status=True,
                                                  message="no  se ncontraron productos en el inventario",
                                                  response=data)
                for i in cur:
                    data.append(inventarioEntityOut(
                                                    idProducto=i[0],
                                                    nombre=i[1],
                                                    precio=float(i[2]),
                                                    costo=float(i[3]),
                                                    cantidad=float(i[4])

                    ))
                return ResponseInternalEntity(status=True,
                                              message=f"inventrario leido con exito se encontraton {count} productos",
                                              response=data)
        except self.DATABASE_ERROR as e:
            Logs.Error(f"Error de base de datos  detail[{e}]")
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
            self.disconnect()

    @override
    def decontarInventario(self, idProducto: str, cantidad: float) -> ResponseInternalEntity:
        try:
            conexion =  self.connect()
            if conexion.status == False:
                self.Error("Error de conexion a la bas e de datos")
                return ResponseInternalEntity(status=False,
                                              message="Error de conexion",
                                              response=None)
            with self.conn.cursor() as cur:
                cur.execute(f"""
                update inventario set cantidad = ((select cantidad 
                from inventario where id_producto  = '{idProducto}')-{cantidad}) 
                where id_producto ='{idProducto}';
                        """)
                self.conn.commit()
                count = cur.rowcount
                if count  <= 0:
                    self.Warnings("no s eactualizo ningun registro del inventario ....  ")
                    return ResponseInternalEntity(status=False,
                                                  message=f"no se pudo realizar el descuento de{cantidad} del producto {idProducto}",
                                                  response=False)
                return ResponseInternalEntity(status=True,
                                              message=f"descontado {cantidad} del producto {idProducto}",
                                              response=True)
        except self.INTEGRIDAD_ERROR as e:
            Logs.Error(f"Error de integridad en la base de datos  as [{e}]")
            return ResponseInternalEntity(status=False,
                                          message=f"Error de integrida en la bas e de datos  detalles[{e}]",
                                          response=None)
        except self.DATABASE_ERROR as e:
            Logs.Error(f"Error de base de datos  detail[{e}]")
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
            Logs.WirterTask("ha finaliado la ejecucion   descuento de inevntario  [InventarioDAO]")
            self.disconnect()
