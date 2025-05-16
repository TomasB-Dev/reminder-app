import sqlite3

class BaseDatos():
    def __init__(self,archivo_db = 'app.db'):
        self.conexion = sqlite3.connect(archivo_db)
        self.cursor = self.conexion.cursor()
    def consultar(self,consulta,parametros=()):
        self.cursor.execute(consulta,parametros)
        self.conexion.commit()
        return self.cursor
    def cerrar(self):
        self.conexion.close()