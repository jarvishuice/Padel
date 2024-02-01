from core.Implements.productos.productosDAO import ProductosDAO,Logs,ResponseInternalEntity,ProductosEntity


class ProductosServices(Logs):

    def __init__(self):
        self.Core = ProductosDAO()