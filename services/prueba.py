from providers.Db.PostgresConection import Psql
class Prueba(Psql):
    def __init__(self):
        super().__init__()
    def probando(self) -> object:
        conexion = self.connect()
        if conexion.status :
            with self.conn.cursor() as cur :
                cur.execute("INSERT INTO public.prueba (id) VALUES('dddsa');")
                self.conn.commit()
            return True
        else :
            return False

probadera = Prueba()
print(probadera.probando())