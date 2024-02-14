import time

from core.Implements.productos.productosDAO import ProductosDAO,Logs,ResponseInternalEntity,ProductosEntity
from core.Implements.productos.inventarioDAO import InventarioDAO,InventarioEntity

class ProductosServices(Logs):

    def __init__(self) -> object:
        self.Core = ProductosDAO()
        self.CoreInventario = InventarioDAO()
    def RegistrarProducto(self, producto: ProductosEntity) -> ResponseInternalEntity:
        if producto.id == 'default':
            producto.id = time.time()
            self.Warnings(f"se genero un id para el producto que tiene por nombre {producto.nombre.upper()} \n recuenrda que hay que poner su codigo de barras ")
        #Colocando el nombre del producto en mayuscula
        producto.nombre = producto.nombre.upper()
        if producto.precio <= 0:
            return ResponseInternalEntity(status=False,
                                          message="Error estas registrando un precio nulo ",
                                          response=None)
        if producto.urlImg is None or producto.urlImg == ' ':
            self.Warnings(f'hay que agregar la imagen del producto {producto.id}')
            producto.urlImg= 'inserta  la imgen del producto '
        trigger= self.Core.CrearProducto(producto=producto)
        if trigger.status == False:
            self.Error(f"El servicio Productos en el hilo crear Productos ha recibido un status False detail [{trigger.message}]")

        return trigger
    def EnviarInventario(self, idProducto: str, cantidad: float = 0)-> ResponseInternalEntity:
        """

        :type cantidad: object
        """
        Inventor=InventarioEntity(idProducto=idProducto,cantidad=cantidad)
        trigger: ResponseInternalEntity =  self.CoreInventario.registrar(Inventor)
        if trigger.status :
            return trigger
        self.Error(f"el core Productos a recibido un error en hilo de EnviarInventario detail [{trigger.message}]")
        return trigger

    @property
    def leerProductos(self) -> ResponseInternalEntity:
        return self.Core.GetAllProductos

    @property
    def ObtenerInventario(self) -> ResponseInternalEntity:
        return self.CoreInventario.Obtenernventario
    def descuentoInventario(self, idProducto: str, cantidad: float) -> ResponseInternalEntity:
        return self.CoreInventario.decontarInventario(idProducto,cantidad)