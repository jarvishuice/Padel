import time

from config.utils.override import override
from core.Entities.finance.planDeCuentas import PlanDeCuentaEntity
from core.interface.finance.planDeCuentas.IPlanDeCuentas import IPlandDeCuentas
from providers.Db.PostgresConection import Psql,ResponseInternalEntity,ResponseInternal,Logs

class PlanDeCuentaDAO(IPlandDeCuentas,Psql):

    def __init__(self):
        super().__init__()
    @override
    def crearCuenta(self, cuenta: PlanDeCuentaEntity) -> ResponseInternalEntity:
        try:
            cuenta.id = time.time()
            cuenta.metodo = cuenta.metodo.upper()

            conection:object = self.connect()
            if conection.status != True:
                Logs.Error("Error de conexion a la base de datos")
                return ResponseInternal.responseInternal(ResponseInternalEntity(status=False, message="Erro de conexion al servidor BD"), None)
            with self.conn.cursor() as cur:
                cur.execute(f" insert into plan_de_cuentas(id,metodo,n_cuenta,id_banco) values('{cuenta.id}','{cuenta.metodo}','{cuenta.nCuenta}','{cuenta.id_banco}');")
                self.conn.commit()
            return ResponseInternal.responseInternal(ResponseInternalEntity(status=True, message="Banco REgistrado con exito", response=cuenta))
        except self.INTEGRIDAD_ERROR as e:
            Logs.Error(f"Error de integridad en la base de datos  as [{e}]")
            return  ResponseInternal.responseInternal(ResponseInternalEntity(status=False,  message="Estas Registrando una la cual ya esta registrada", response=None))
        except self.DATABASE_ERROR as e:
            Logs.Error(f"Error de base de datos  detail[{e}]")
            return ResponseInternal.responseInternal(ResponseInternalEntity(status=False, message="error de base de datos", response=None))
        except self.INTERFACE_ERROR as e:
            Logs.Error(f"Error de interface detail {e}")
            return ResponseInternal.responseInternal(ResponseInternalEntity(status=False, message="Error de interface en base de datos", response=None))
        except self.OPERATIONAL_ERROR as e:
            Logs.Error(f"Error de operaciones detail [{e}]")
            return ResponseInternal.responseInternal(ResponseInternalEntity(status=False, message="Error de operaciones en la base de datos", response=None))
        finally:
            self.disconnect()

    @override
    def getAllPlanDECuenta(self) -> ResponseInternalEntity:
        """

        :rtype: object
        """
        try:
            data = []
            conection = self.connect()
            if conection.status != True:
                Logs.Error("Error de conexion a la base de datos")
                return ResponseInternal.responseInternal(
                    ResponseInternalEntity(status=False, message="Erro de conexion al servidor BD", response=None))
            with self.conn.cursor() as cur:
                cur.execute(f"select * from plan_de_cuentas")
                count = cur.rowcount
                if count <= 0:
                    Logs.Warnings("no se encontro ningun Banco registrado")
                for i in cur:
                    data.append(PlanDeCuentaEntity(id=str(i[0]), metodo=str(i[1]), nCuenta=str(i[2]), idBanco=str(i[3])))
            return ResponseInternal.responseInternal(
                ResponseInternalEntity(status=True, message="Banco REgistrado con exito", response=data))
        except self.INTEGRIDAD_ERROR as e:
            Logs.Error(f"Error de integridad en la base de datos  as [{e}]")
            return ResponseInternal.responseInternal(
                ResponseInternalEntity(status=False, message="Estas Registrando un banco el cual ya etsa registrado", response=None))
        except self.DATABASE_ERROR as e:
            Logs.Error(f"Error de base de datos  detail[{e}]")
            return ResponseInternal.responseInternal(
                ResponseInternalEntity(status=False, message="error de base de datos", response=None))
        except self.INTERFACE_ERROR as e:
            Logs.Error(f"Error de interface detail {e}")
            return ResponseInternal.responseInternal(
                ResponseInternalEntity(status=False, message="Error de interface en base de datos", response=None))
        except self.OPERATIONAL_ERROR as e:
            Logs.Error(f"Error de operaciones detail [{e}]")
            return ResponseInternal.responseInternal(
                ResponseInternalEntity(status=False, message="Error de operaciones en la base de datos", response=None))
        finally:
            self.disconnect()