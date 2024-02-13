from core.Implements.ordenes.PedidosDAO import PedidosDAO,PedidosEntity,ResponseInternalEntity,Logs
from services.productos.ProductosServices import ProductosServices
class PedidosServices(Logs):
    def __init__(self):
        self.__core = PedidosDAO()
        self.__integracion = ProductosServices()
        super().__init__()
    def registrarPedido(self,pedido:PedidosEntity)->ResponseInternalEntity:
         pedido.total = pedido.precio * pedido.cantidad
         if pedido.iterable:
             descuento =self.__integracion.descuentoInventario(pedido.idProducto,pedido.cantidad)
             self.Warnings(f"mostrando el status de descuento de inventario en reegistro pedidos services\n[{descuento.status}]")
         trigger = self.__core.crearPedido(pedido)
         if trigger.status == True:
             self.WirterTask("Pedido registrado con exito ")

         return trigger


