import mysql.connector
from comandos import Comandos
from janela import Janela, JanelaPrincipal

class Controller():
    def __init__(self):
        self.janela = Janela(self)
        self.janela.abrir_tela()

    def chamar_comando_conexao(self):
        try:
            self.comandos = Comandos()
            self.janela.mensagem_conexao()
            self.janela.trocar_tela()
            self.janelaConectada = JanelaPrincipal(self, self.comandos.listagem())
            self.janelaConectada.mostrar_tela()
        except ConnectionError:
            raise RuntimeError

    def recebe_campos_inserir(self):
        try:
            descricao = self.janelaConectada.pegar_descricao()
            estoque = self.janelaConectada.pegar_estoque()
            valor = self.janelaConectada.pegar_valor()
            self.comandos.inserir(descricao, estoque, valor)
            self.janelaConectada.mensagem_inserir()
            self.janelaConectada.atualizar_tela()
            self.janelaConectada = JanelaPrincipal(self, self.comandos.listagem())
            self.janelaConectada.mostrar_tela()
        except mysql.connector.Error:
            self.janelaConectada.mensagem_falha()

    def recebe_campos_atualizar(self):
        try:
            descricao = self.janelaConectada.pegar_descricao()
            estoque = self.janelaConectada.pegar_estoque()
            valor = self.janelaConectada.pegar_valor()
            idProd = self.janelaConectada.pegar_id()
            self.comandos.atualizar_banco(idProd, descricao, estoque, valor)
            self.janelaConectada.mensagem_atualizar()
            self.janelaConectada.atualizar_tela()
            self.janelaConectada = JanelaPrincipal(self, self.comandos.listagem())
            self.janelaConectada.mostrar_tela()
        except mysql.connector.Error:
            self.janelaConectada.mensagem_falha()
        except IndexError:
            self.janelaConectada.mensagem_falha()

    def recebe_campos_remover(self):
        try:
            idProd = self.janelaConectada.pegar_id()
            self.comandos.remover(idProd)
            self.janelaConectada.mensagem_remover()
            self.janelaConectada.atualizar_tela()
            self.janelaConectada = JanelaPrincipal(self, self.comandos.listagem())
            self.janelaConectada.mostrar_tela()
        except mysql.connector.Error:
            self.janelaConectada.mensagem_falha_remover()