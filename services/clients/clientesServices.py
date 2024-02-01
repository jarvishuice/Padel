from core.Implements.clients.clientesDAO import ClientesDAO,PersonaEntity,ResponseInternalEntity
class ClientesServices():
    def __init__(self):
        super().__init__()
    def RegistraCliente(self, Client: PersonaEntity) -> PersonaEntity | ResponseInternalEntity:
        """
                Este método registra un nuevo cliente en la base de datos.

                Args:
                    Client: Objeto de tipo `PersonaEntity` que contiene los datos del cliente a registrar.

                Returns:
                    Un objeto de tipo `PersonaEntity` que contiene los datos del cliente registrado, o un objeto de tipo `ResponseInternalEntity` en caso de error.
                """
        core = ClientesDAO()
        return core.crearCliente(Client)

    def ObetenerClientes(self) -> list[PersonaEntity ] | ResponseInternalEntity:
        """
               Este método obtiene todos los clientes registrados en la base de datos.

               Returns:
                   Una lista de objetos de tipo `PersonaEntity` que contienen los datos de los clientes registrados,
                    o un objeto de tipo `ResponseInternalEntity` en caso de error.
               """
        core = ClientesDAO()
        return core.getAllClientes()
    def BuscarClienteByCi(self,ci:str):
        core = ClientesDAO()
        return core.searchClienteByCi(ci)
