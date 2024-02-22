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

    @property
    def GetAllProductos (self) :
        try:
            data = []
            conexion = self.connect()
            if conexion.status ==False:
                self.Error("Error de conexion a la base de datos")
                return ResponseInternalEntity(status=False,message="Error de conexion a la base de datos ",response=None)
            with self.conn.cursor() as cur:
                cur.execute("select * from productos order by nombre asc  ")
                count = cur.rowcount
                if count <= 0:
                    self.Warnings("No se encontraron registros en la tabla productos ")
                    return ResponseInternalEntity(status=True,message="No se encontraron registros ",response =data)
                for i in cur:
                    data.append(ProductosEntity(id=str(i[0]),
                                                nombre=i[1],
                                                urlImg=i[2],
                                                costo=float(i[3]),
                                                precio=float(i[4]),
                                                idCategoria=int(i[5]),
                                                idAlmacen=int(i[6]),
                                                descontable=bool(i[7])
                                                ))
                return ResponseInternalEntity(status=True,message="Exito al leer todos los productos",response=data)
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
            self.disconnect()


    def getProductByCategoria (self, idCategoria: int) :
        try:
            data = []
            conexion = self.connect()
            if conexion.status ==False:
                self.Error("Error de conexion a la base de datos")
                return ResponseInternalEntity(status=False,message="Error de conexion a la base de datos ",response=None)
            with self.conn.cursor() as cur:
                cur.execute(f"select * from productos where id_categoria={idCategoria} order by nombre asc  ")
                count = cur.rowcount
                if count <= 0:
                    self.Warnings("No se encontraron registros en la tabla productos ")
                    return ResponseInternalEntity(status=True,message="No se encontraron registros ",response =data)
                for i in cur:
                    data.append(ProductosEntity(id=str(i[0]),
                                                nombre=i[1],
                                                urlImg=i[2],
                                                costo=float(i[3]),
                                                precio=float(i[4]),
                                                idCategoria=int(i[5]),
                                                idAlmacen=int(i[6]),
                                                descontable=bool(i[7])
                                                ))
                return ResponseInternalEntity(status=True,message="Exito al leer todos los productos",response=data)
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
            self.disconnect()

    def getProductosByAlmacen (self, idAlmacen: int) :
        try:
            data = []
            conexion = self.connect()
            if conexion.status ==False:
                self.Error("Error de conexion a la base de datos")
                return ResponseInternalEntity(status=False,message="Error de conexion a la base de datos ",response=None)
            with self.conn.cursor() as cur:
                cur.execute(f"select * from productos where id_almacen={idAlmacen} order by nombre asc  ")
                count = cur.rowcount
                if count <= 0:
                    self.Warnings("No se encontraron registros en la tabla productos ")
                    return ResponseInternalEntity(status=True,message="No se encontraron registros ",response =data)
                for i in cur:
                    data.append(ProductosEntity(id=str(i[0]),
                                                nombre=i[1],
                                                urlImg=i[2],
                                                costo=float(i[3]),
                                                precio=float(i[4]),
                                                idCategoria=int(i[5]),
                                                idAlmacen=int(i[6]),
                                                descontable=bool(i[7])
                                                ))
                return ResponseInternalEntity(status=True,message="Exito al leer todos los productos",response=data)
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
            self.disconnect()
    def editProduct(self,producto:ProductosEntity):
        try :
            conexion = self.connect ()
            if conexion.status == False :
                self.Error ("error al conectarse al servidpor de base de datos")
                return ResponseInternalEntity (status=False,
                                               message="error de conexion  a la base de datos",
                                               response=None)
            with self.conn.cursor () as cur :
                cur.execute (f"""UPDATE public.productos SET nombre='{producto.nombre}', urlimg='{producto.urlImg}', 
                costo={producto.costo}, precio={producto.precio},id_categoria={producto.idCategoria}, 
                id_almacen={producto.idAlmacen}, descontable={producto.descontable} WHERE id='{producto.id}';""")
                self.conn.commit ()
            return ResponseInternalEntity (status=True,
                                           message="Producto actualizado de manera correcta",
                                           response=producto)
        except self.INTEGRIDAD_ERROR as e :
            Logs.Error (f"Error de integridad en la base de datos  as [{e}]")
            return ResponseInternalEntity (status=False,
                                           message=f"error de integridad detalle[{e}] ",
                                           response=None)
        except self.DATABASE_ERROR as e :
            Logs.Error (f"Error de base de datos  detail[{e}]")
            return ResponseInternalEntity (status=False, message="error de base de datos", response=None)
        except self.INTERFACE_ERROR as e :
            Logs.Error (f"Error de interface detail {e}")
            return ResponseInternalEntity (status=False, message="Error de interface en base de datos", response=None)
        except self.OPERATIONAL_ERROR as e :
            Logs.Error (f"Error de operaciones detail [{e}]")
            return ResponseInternalEntity (status=False, message="Error de operaciones en la base de datos",
                                           response=None)
        finally :
            Logs.WirterTask ("ha finaliado la ejecucion de edicion  de productos DAO")
            self.disconnect ()

