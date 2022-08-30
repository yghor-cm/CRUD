import mysql.connector

class Comandos():
    def __init__(self):
        try:
            self.conexao = mysql.connector.connect(
                host='localhost',
                database='LojaSuplementos',
                user='root',
                password='password'
            )
            self.cursor = self.conexao.cursor()
            self.conexao.close()
        except ConnectionError:
            raise RuntimeError('Conexão falhou!')

    def inserir(self, produto, estoque, valor):
        self.produto = produto
        self.estoque = estoque
        self.valor = valor
        self.insert = f'insert into suplementos (descricao, estoque, valor) ' \
                       f'values ("{self.produto}", "{self.estoque}", "{self.valor}")'

        try:
            self.conexao = mysql.connector.connect(
                host='localhost',
                database='LojaSuplementos',
                user='root',
                password='password'
            )
            self.cursor = self.conexao.cursor()
            try:
                self.cursor.execute(self.insert)
                self.conexao.commit()
            except ConnectionError:
                raise RuntimeError('Conexão falhou!')

        except ConnectionError:
            raise RuntimeError('Conexão falhou!')

        self.conexao.close()

    def atualizar_banco(self, idProd, produto, estoque, valor):
        self.idProd = idProd
        self.produto = produto
        self.estoque = estoque
        self.valor = valor
        self.atualizar ="update suplementos set descricao='"+ self.produto + "', estoque='"+ self.estoque + "', valor='"+ self.valor + "' where id_sup='"+ self.idProd +"'"

        try:
            self.conexao = mysql.connector.connect(
                host='localhost',
                database='LojaSuplementos',
                user='root',
                password='password'
            )
            self.cursor = self.conexao.cursor()
            try:
                self.cursor.execute(self.atualizar)
                self.conexao.commit()
            except ConnectionError:
                raise RuntimeError('Conexão falhou!')

        except ConnectionError:
            raise RuntimeError('Conexão falhou!')

        self.conexao.close()

    def remover(self, idProd):
        self.idProd = idProd
        self.delete = f'delete from suplementos where id_sup={self.idProd}'

        try:
            self.conexao = mysql.connector.connect(
                host='localhost',
                database='LojaSuplementos',
                user='root',
                password='password'
            )
            self.cursor = self.conexao.cursor()
            try:
                self.cursor.execute(self.delete)
                self.conexao.commit()
            except ConnectionError:
                raise RuntimeError('Conexão falhou!')

        except ConnectionError:
            raise RuntimeError('Conexão falhou!')

        self.conexao.close()


    def listagem(self):
        try:
            self.conexao = mysql.connector.connect(
                host='localhost',
                database='LojaSuplementos',
                user='root',
                password='password'
            )
            self.cursor = self.conexao.cursor()
            self.comando = 'select * from suplementos'
            self.cursor.execute(self.comando)
            self.linhas = self.cursor.fetchall()
            self.conexao.close()
        except ConnectionError:
            raise RuntimeError('Conexão falhou!')
        return self.linhas
