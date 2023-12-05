import sqlite3


class ModelConection():
    def conectBase(self):
        self.conn = sqlite3.connect(r'model\registros.db')
        self.cursor = self.conn.cursor()

        return print('Conectado ao banco.')
    
    def desconect(self):
        self.cursor.close()
        self.conn.close()

        return print('Desconectado do banco.')