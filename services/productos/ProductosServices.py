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
            return ResponseInternalEntity(status=False,message="Error estas registrando un precio nulo ",response=None)
        if producto.urlImg is None or producto.urlImg == ' ':
            self.Warnings(f'hay que agregar la imagen del producto {producto.id}')
            producto.urlImg= 'inserta  la imgen del producto '
        trigger= self.Core.CrearProducto(producto=producto)
        inventario = self.CoreInventario.registrar(inventarioEntity)
        if trigger.status == False:
            self.Error(f"El servicio Productos en el hilo crear Productos ha recibido un status False detail [{trigger.message}]")
            return trigger
        return trigger