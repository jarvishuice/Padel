import time

from config.LOGS.LogsSystem import Logs
from config.utils.override import override
from core.interface.productos.IProductos import IProductos,ProductosEntity
from providers.Db.PostgresConection import Psql,ResponseInternalEntity


class ProductosDAO(IProductos,Psql,Logs):
    def __init__(self) -> object:
        super().__init__()
    @override
    def CrearProducto(self, producto: ProductosEntity) -> ResponseInternalEntity:
        try:
            conexion = self.connect()
            if producto.id is False:
                producto.id = time.time()
                Logs.Warnings("generando el id del producto ")
            Logs.WirterTask("Data correcta en los productos")

            if conexion.status ==False:
                self.Error("error al conectarse al servidpor de base de datos")
                return ResponseInternalEntity(status=False,message="error de conexion  a la base de datos",response=None)
            with self.conn.cursor() as cur:
                cur.execute(f"""INSERT INTO public.productos (id, nombre, urlimg, costo, precio, id_categoria, id_almacen, 
                descontable) VALUES('{producto.id}', '{producto.nombre}', NULL, {producto.costo},{producto.precio}, {producto.idCategoria},
                 {producto.idAlmacen}, {producto.descontable});""")
                self.conn.commit()
            return ResponseInternalEntity(status=True,message="Producto registrado de manera correcta",response=producto)
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

    def EditarProductos (self, producto: ProductosEntity) :
        pass

    def GetAllProductos (self) :
        ...

    def getProductByCategoria (self, idCategoria: int) :
        pass

    def getProductosByAlmacen (self, idAlmacen: int) :
        pass