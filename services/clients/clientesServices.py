from core.Implements.clients.clientesDAO import ClientesDAO,ClienteEntity,ResponseInternalEntity
class ClientesServices():
    def __init__(self):
        super().__init__()
    def RegistraCliente(self, Client: ClienteEntity) -> ClienteEntity | ResponseInternalEntity:
        """
                Este método registra un nuevo cliente en la base de datos.

                Args:
                    Client: Objeto de tipo `ClienteEntity` que contiene los datos del cliente a registrar.

                Returns:
                    Un objeto de tipo `ClienteEntity` que contiene los datos del cliente registrado, o un objeto de tipo `ResponseInternalEntity` en caso de error.
                """
        core = ClientesDAO()
        return core.crearCliente(Client)

    def ObetenerClientes(self) -> list[ClienteEntity] | ResponseInternalEntity:
        """
               Este método obtiene todos los clientes registrados en la base de datos.

               Returns:
                   Una lista de objetos de tipo `ClienteEntity` que contienen los datos de los clientes registrados,
                    o un objeto de tipo `ResponseInternalEntity` en caso de error.
               """
        core = ClientesDAO()
        return core.getAllClientes()
    def BuscarClienteByCi(self,ci:str):
        core = ClientesDAO()
        return core.searchClienteByCi(ci)
