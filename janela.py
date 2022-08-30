from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox

class Janela():
    def __init__(self, controller):
        self.controller = controller
        self.interface = Tk()
        self.interface.geometry("800x600+270+100")
        self.interface.title("CRUD")
        self.tela_conexao()

    def abrir_tela(self):
        self.interface.mainloop()

    def tela_conexao(self):
        telaPrincipal = Frame(self.interface, bg="#353535")
        telaPrincipal.place(x=0, y=0, width=800, height=600)
        titulo = Label(self.interface, text="Loja de Suplementos", font=("Arial", 20), bg="#353535", fg="white")
        titulo.place(x=280, y=20)
        botaoConectar = Button(self.interface, width=15, text="CONECTAR", font=("Arial", 10), bg="green", fg="black", command=self.controller.chamar_comando_conexao)
        botaoConectar.place(x=332, y=300)

    def trocar_tela(self):
        self.interface.withdraw()
        self.interface.destroy()

    def mensagem_conexao(self):
        MessageBox.showinfo("SUCESSO!", "Conexão realizada!")

class JanelaPrincipal():
    def __init__(self, controller, banco):
        self.controller = controller
        self.banco = banco
        self.interface = Tk()
        self.interface.geometry("800x600+270+100")
        self.interface.title("CRUD")
        self.tela_principal()
        self.tela_campo_digitacao()
        self.tela_botao()
        self.tela_banco(self.banco)

    def mostrar_tela(self):
        self.interface.mainloop()

    def atualizar_tela(self):
        self.interface.withdraw()
        self.interface.destroy()

    def tela_principal(self):
        telaPrincipal = Frame(self.interface, bg="#353535")
        telaPrincipal.place(x=0, y=0, width=800, height=600)
        titulo = Label(self.interface, text="Loja de Suplementos", font=("Arial", 20), bg="#353535", fg="white")
        titulo.place(x=280, y=20)

    def tela_campo_digitacao(self):
        textoDescricao = Label(self.interface, text="Descricao:", font=("Arial", 20), bg="#353535", fg="white")
        textoDescricao.place(x=5, y=445)
        self.recebeDescricao = Entry(self.interface, width=25, font=1)
        self.recebeDescricao.place(x=150, y=450)
        textoEstoque = Label(self.interface, text="Estoque:", font=("Arial", 20), bg="#353535", fg="white")
        textoEstoque.place(x=25, y=485)
        self.recebeEstoque = Entry(self.interface, width=25, font=1)
        self.recebeEstoque.place(x=150, y=490)
        textoValor = Label(self.interface, text="Valor:", font=("Arial", 20), bg="#353535", fg="white")
        textoValor.place(x=60, y=525)
        self.recebeValor = Entry(self.interface, width=25, font=1)
        self.recebeValor.place(x=150, y=530)

    def tela_botao(self):
        self.botaoInserir = Button(self.interface, width=10, text="Inserir", font=("Arial", 10), bg="#353535", fg="white", command=self.controller.recebe_campos_inserir)
        self.botaoInserir.place(x=450, y=440)
        self.botaoRemover = Button(self.interface, width=10, text="Remover", font=("Arial", 10), bg="#353535", fg="white", command=self.controller.recebe_campos_remover)
        self.botaoRemover.place(x=450, y=490)
        self.botaoAtualizar = Button(self.interface, width=10, text="Atualizar", font=("Arial", 10), bg="#353535", fg="white", command=self.controller.recebe_campos_atualizar)
        self.botaoAtualizar.place(x=450, y=540)
        self.botaoDesconectar = Button(self.interface, width=15, text="DESCONECTAR", font=("Arial", 10), bg="red", fg="black", command=self.interface.destroy)
        self.botaoDesconectar.place(x=600, y=490)

    def tela_banco(self, linhas):
        self.telaBanco = ttk.Treeview(self.interface, columns=("id", "descricao", "estoque", "valor"), show='headings')
        self.scroll = ttk.Scrollbar(orient="vertical", command=self.telaBanco.yview)
        self.scroll.place(x=43+695+2,y=120, height=280)
        self.telaBanco.configure(yscrollcommand=self.scroll.set)
        self.telaBanco.place(x=43, y=100, height=300)
        self.telaBanco.column('id', minwidth=0, width=70)
        self.telaBanco.column('descricao', minwidth=0, width=400)
        self.telaBanco.column('estoque', minwidth=0, width=110)
        self.telaBanco.column('valor', minwidth=0, width=130)
        self.telaBanco.heading('id', text='ID')
        self.telaBanco.heading('descricao', text='Descrição')
        self.telaBanco.heading('estoque', text='Estoque')
        self.telaBanco.heading('valor', text='Valor')
        for self.linha in linhas:
            self.telaBanco.insert("","end",values=self.linha)
        self.telaBanco.bind('<Double-1>', self.valor_tela)

    def valor_tela(self, event):
        self.recebeDescricao.delete(0, END)
        self.recebeEstoque.delete(0, END)
        self.recebeValor.delete(0, END)

        self.coluna = self.telaBanco.selection()[0]
        self.selecionar = self.telaBanco.set(self.coluna)
        self.recebeDescricao.insert(0, self.selecionar['descricao'])
        self.recebeEstoque.insert(0, self.selecionar['estoque'])
        self.recebeValor.insert(0, self.selecionar['valor'])

    def pegar_descricao(self):
        return self.recebeDescricao.get()

    def pegar_estoque(self):
        return self.recebeEstoque.get()

    def pegar_valor(self):
        return self.recebeValor.get()

    def pegar_id(self):
        self.coluna = self.telaBanco.selection()[0]
        self.selecionar = self.telaBanco.set(self.coluna)
        self.id = list(self.selecionar.values())[0]
        return self.id

    def mensagem_inserir(self):
        MessageBox.showinfo("SUCESSO!", "Suplemento inserido com sucesso!")

    def mensagem_falha(self):
        MessageBox.showinfo("ERRO!", "Todos os campos são obrigatórios!")

    def mensagem_atualizar(self):
        MessageBox.showinfo("SUCESSO!", "Suplemento atualizado com sucesso!")

    def mensagem_falha_remover(self):
        MessageBox.showinfo("ERRO!", "Não foi possível remover o produto!")

    def mensagem_remover(self):
        MessageBox.showinfo("SUCESSO!", "Suplemento removido com sucesso!")