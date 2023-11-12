
import sqlite3
class bancoprod():

    def __init__(self):
        self.conexao = sqlite3.connect('prod.db')
        self.createTable()

    def createTable(self,lesta=[]):
        c = self.conexao.cursor()

        c.execute("""create table if not exists produtos (
                 codproduto integer primary key autoincrement ,
                 nomeproduto text,
                 preco float)""")
        self.conexao.commit()
        c.close()


