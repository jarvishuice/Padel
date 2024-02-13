from config.LOGS.LogsSystem import Logs
from config.utils.override import override
from core.interface.productos.IInventario import IInventario,InventarioEntity
from providers.Db.PostgresConection import Psql,ResponseInternalEntity


class InventarioDAO(Psql,Logs,IInventario):
    def __init__(self):
        super().__init__()
    @override
    def registrar (self, producto: InventarioEntity) -> ResponseInternalEntity :
        try:
            conexion  = self.connect()
            if conexion == False:
                return  ResponseInternalEntity(status=False,message='Error de conexion al servidor de base de datos',response=None)
            with self.conn.cursor() as cur:
                cur.execute(f""" INSERT INTO public.inventario (id_producto, cantidad) VALUES('{producto.idProducto}', {producto.cantidad});""")
            self.conn.commit()
            return ResponseInternalEntity(status= True,message="Exito al registrar el inventario",response=producto)
        except self.INTEGRIDAD_ERROR as e:
            Logs.Error(f"Error de integridad en la base de datos  as [{e}]")
            return ResponseInternalEntity(status=False,message="Puedes que estes regiuitrando un cliente cuyos datos ya existen en nuestra base de datos verifica y si el problema persite comuniquese con el equipo de soporte",response=None)
        except self.DATABASE_ERROR as e:
            Logs.Error(f"Error de base de datos  detail[{e}]")
            return ResponseInternalEntity(status=False,message="error de base de datos",response=None)
        except self.INTERFACE_ERROR as e :
            Logs.Error(f"Error de interface detail {e}")
            return ResponseInternalEntity(status=False,message="Error de interface en base de datos",response=None)
        except self.OPERATIONAL_ERROR as e :
            Logs.Error(f"Error de operaciones detail [{e}]")
            return ResponseInternalEntity(status=False,message="Error de operaciones en la base de datos",response= None)
        finally:
            Logs.WirterTask("ha finaliado la ejecucion del registros de productos DAO")
            self.disconnect()


    @override
    def Obtenernventario (self) :
        pass
    @override
    def decontarInventario (self, idProducto: str, cantidad: float) -> ResponseInternalEntity :
        pass