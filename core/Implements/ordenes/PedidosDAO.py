from config.LOGS.LogsSystem import Logs
from core.Entities.ordenes.pedidoEntity import PedidosEntity
from core.interface.ordenes.Ipedidos import IPedidos
from providers.Db.PostgresConection import Psql,ResponseInternalEntity,override


class PedidosDAO(Psql,IPedidos,Logs):
    def __init__ (self) :
        super ().__init__ ()

    @override
    def crearPedido(self, pedido: PedidosEntity) -> ResponseInternalEntity:
        try:
            conexion = self.connect()
            if conexion.status  == False:
                self.Error("Error de conexion al serviodr de base de datos ")
                return ResponseInternalEntity(status = False,messagge="error de cponexion al servidor db", response=None)
            with self.conn.cursor() as cur:
                cur.execute(f"""INSERT INTO public.pedidos (id_orden, id_producto, cantidad, costo, precio, total,iterable) 
                VALUES('{pedido.idOrden}', '{pedido.idProducto}', {pedido.cantidad}, {pedido.costo}, {pedido.precio}, {pedido.total},{pedido.iterable});
                """)
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
            Logs.WirterTask("ha finaliado la ejecucion del registros de pedidosDAO")
            self.disconnect()


