

from config.LOGS.LogsSystem import Logs
from core.interface.productos.Icategoria import ICategoria,CategoriaEntity
from providers.Db.PostgresConection import Psql,ResponseInternalEntity


class CategoriaDAO(Psql,ICategoria,Logs):

    def __init__(self):
        super().__init__()

    @property
    def getAllCategorias (self) -> ResponseInternalEntity:
        try:
            data = []
            conexion = self.connect()
            if conexion.status == False:
                self.Error("error de conexion a la base de datos")
                return ResponseInternalEntity(status=False,
                                              message="error de conexion a la base de datos",
                                              response=None)
            with self.conn.cursor() as cur:
                cur.execute("select  * from categorias order by id desc;")
                count  = cur.rowcount
                if count  <= 0:
                    self.Warnings("NO se encontraron Registros de cartegorias")
                    ResponseInternalEntity(status=True,
                                           message="no se encontraron regstors de catgorias ",
                                           response=data)
                for i in cur:
                    data.append(CategoriaEntity(id=int(i[0]),
                                                nombre=i[1],
                                                descripcion=i[2]))
                return ResponseInternalEntity(status=True,
                                              message="categorias leidas con exito",
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
            Logs.Error (f"Error de operaciones detail [{e}]")
            return ResponseInternalEntity(status=False,
                                          message="Error de operaciones en la base de datos",
                                          response=None)
        finally:
            self.disconnect()
    def crearCategoria(self,categoria:CategoriaEntity):
        """

        :type categoria: object
        """
        try:

            conexion = self.connect()
            if conexion.status == False:
                self.Error ("error de conexion a la base de datos")
                return ResponseInternalEntity (status=False,
                                               message="error de conexion a la base de datos",
                                               response=None)
            with self.conn.cursor () as cur:
                cur.execute(f"""INSERT INTO public.categorias (id, nombre, descripcion) 
                VALUES((SELECT max(id) + 1 as nuevoID FROM categorias), '{categoria.nombre}', 
                '{categoria.descripcion}');""")
                self.conn.commit()


                return ResponseInternalEntity (status=True,
                                               message="categorias leidas con exito",
                                               response=categoria)
        except self.DATABASE_ERROR as e:
            Logs.Error (f"Error de base de datos  detail[{e}]")
            return ResponseInternalEntity (status=False,
                                           message=f"error de base de datos detalles[{e}]",
                                           response=None)
        except self.INTERFACE_ERROR as e:
            Logs.Error (f"Error de interface detail {e}")
            return ResponseInternalEntity (status=False,
                                           message="Error de interface en base de datos",
                                           response=None)
        except self.OPERATIONAL_ERROR as e:
            Logs.Error (f"Error de operaciones detail [{e}]")
            return ResponseInternalEntity (status=False,
                                           message="Error de operaciones en la base de datos",
                                           response=None)
        finally:
            self.disconnect()


