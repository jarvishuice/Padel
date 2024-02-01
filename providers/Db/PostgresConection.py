from typing_extensions import override
from core.interface.config.dataBAse.ConectionDbInterface import ConectionDbInterface
import psycopg2
from core.ROOM.ResponseInternal import ResponseInternal,ResponseInternalEntity
from config.LOGS.LogsSystem import Logs
from config.DB.datosConfig import CredentialDb


class Psql(ConectionDbInterface):
    OPERATIONAL_ERROR = psycopg2.OperationalError
    DATABASE_ERROR = psycopg2.DatabaseError
    INTEGRIDAD_ERROR = psycopg2.IntegrityError
    INTERFACE_ERROR = psycopg2.InternalError
    credenciales = CredentialDb()

    def __init__(self) -> object:
        self.conn = None

    @override
    def connect(self) -> object:
        """

        :rtype: object
        """
        try:
            self.conn = psycopg2.connect(self.credenciales.getDatos())

            return ResponseInternal.responseInternal(ResponseInternalEntity(status=True,message="Conexion realizada con exito",response=self.conn))
        except psycopg2.OperationalError as err:
            return ResponseInternal.responseInternal(ResponseInternalEntity(status=True,message=err,response=self.conn))
        except psycopg2.InterfaceError as err:
            return ResponseInternal.responseInternal(ResponseInternalEntity(status=True,message=err,response=self.conn))
        except psycopg2.DatabaseError as err:
            return ResponseInternal.responseInternal(ResponseInternalEntity(status=True,message=err,response=self.conn))

    @override
    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
            Logs.WirterTask("Desconexión exitosa de la base de datos")
            self.conn = None
        else:
            Logs.WirterTask(f"{self.NOTE}no tiene conexion aperturada en estos monetos ")
