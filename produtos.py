from bancoprod import bancoprod
class grande(Exception):
    def __init__(self,msg):
        Exception.__init__(self,msg)
    def diminua(nomeproduto):
        if len(nomeproduto)>=19:
            raise grande("limite de 19 caracteres")

class produtos(object):


    def __init__(self, codproduto = 0, nomeproduto = "", preco = 0):
        self.info = {}
        self.codproduto = codproduto
        self.nomeproduto = nomeproduto
        self.preco = preco


    def insertProd(self):

        bp = bancoprod()
        try:

            c = bp.conexao.cursor()

            c.execute("insert into produtos (nomeproduto, preco) values ('" + self.nomeproduto + "', '" +self.preco + "')")
            testa = grande.diminua(self.nomeproduto)

            bp.conexao.commit()
            c.close()

            return "Produto cadastrado com sucesso!"
        except grande:
            return "O produto deve ter menos de 19 caracteres"
        except:
            return "Ocorreu um erro na inserção do produto"

    def updateProd(self):

        bp = bancoprod()
        try:

            c = bp.conexao.cursor()

            c.execute("update produtos set nomeproduto = '" + self.nomeproduto + "',preco = '" + self.preco + "' where codproduto = "+self.codproduto+"")

            bp.conexao.commit()
            c.close()

            return "produto atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do produto"

    def deleteProd(self):

        bp = bancoprod()
        try:
            c = bp.conexao.cursor()

            c.execute("delete from produtos where codproduto = " + self.codproduto + " ")

            bp.conexao.commit()
            c.close()

            return "Produto excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do produto"

    def selectProd(self, codproduto):
      bp = bancoprod()
      try:

          c = bp.conexao.cursor()

          c.execute("select * from produtos where codproduto = " + codproduto + "  ")

          for linha in c:
              self.codproduto = linha[0]
              self.nomeproduto = linha[1]
              self.preco = linha[2]
          c.close()

          return "Busca feita com sucesso!"
      except:
          return "Ocorreu um erro na busca do produto"

