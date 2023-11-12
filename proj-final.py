
#importndo as bibliotecas
import sqlite3
from produtos import produtos
from tkinter import *
import tkinter as tk
from tkinter import ttk

#Construção da classe de interface
class Page(tk.Frame):
    def __init__(self, *args):
        tk.Frame.__init__(self, *args)
    def show(self):
        self.lift()

#Construção da página de cadastro
class Application2(Page):

    def __init__(self,master=None):
        Page.__init__(self, master)
        self.fonte = ("Verdana", "16")
        # Construção dos frames que compõem a seção de cadastro da interface
        self.container1 = tk.Frame(self)
        self.container1["pady"] = 10
        self.container1.pack()


        self.container3 = tk.Frame(self)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = tk.Frame(self)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = tk.Frame(self)
        self.container5["padx"] = 20
        self.container5["pady"] = 10
        self.container5.pack()

        self.container6 = tk.Frame(self)
        self.container6["pady"] = 15
        self.container6.pack()

        self.container7 = tk.Frame(self)
        self.container7["pady"] = 60
        self.container7.pack()

        self.container9 = tk.Frame(self)
        self.container9["padx"] = 100
        self.container9["pady"] = 100
        self.container9.pack()

        #elaboração de elementos da interface (títulos, botões e etc)
        self.titulo = tk.Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "20", "bold")
        self.titulo.pack ()

        self.lblnome = tk.Label(self.container3, text="Nome do produto:",
        font=self.fonte, width=20,height=3)
        self.lblnome.pack(side=LEFT)

        self.txtnome = tk.Entry(self.container3)
        self.txtnome["width"] = 30
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblpreco = tk.Label(self.container4, text="preco:",
        font=self.fonte, width=10)
        self.lblpreco.pack(side=LEFT)

        self.txtprec = tk.Entry(self.container4)
        self.txtprec["width"] = 25
        self.txtprec["font"] = self.fonte
        self.txtprec.pack(side=LEFT)


        self.bntInsert = tk.Button(self.container5, text="Inserir",font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirProd
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = tk.Button(self.container5, text="Alterar",font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarProd
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = tk.Button(self.container5, text="Excluir",font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirProd
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = tk.Label(self.container6, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

        #abertura de conexão com o banco de dados
        banco = sqlite3.connect('prod.db')
        cursor = banco.cursor()
        self.memoria = []
        self.menu = []

        cursor.execute("SELECT*FROM produtos")
        a = cursor.fetchall()
        self.nomeProd = {}
        self.precoProd = {}

        for a in a:
            self.memoria.append(a)

        ite = 0
        for ite in range(len(self.memoria)):
            self.menu.append(self.memoria[ite][1])
            self.nomeProd[self.memoria[ite][1]] = self.memoria[ite][0]
            self.precoProd[self.memoria[ite][1]] = self.memoria[ite][2]
        self.menu.sort()

        self.combb = ttk.Combobox(self.container9, values=self.menu, font=16, width=30)
        self.combb.set("")
        self.combb.pack()
        self.combb.bind("<<ComboboxSelected>>", self.CallbackFunc)
    #Função de ação do combobox
    def CallbackFunc(self,event):

        self.txtnome.delete(0,END)
        self.txtprec.delete(0,END)
        self.txtnome.insert(tk.END,event.widget.get())
        self.txtprec.insert(tk.END, self.precoProd[event.widget.get()])

    # Função para inserir novo produto
    def inserirProd(self):


        prod = produtos()

        prod.nomeproduto = self.txtnome.get()
        prod.preco = self.txtprec.get()


        self.lblmsg["text"] = prod.insertProd()
        self.txtnome.delete(0, END)
        self.txtprec.delete(0, END)

        banco = sqlite3.connect('prod.db')
        cursor = banco.cursor()
        memoria = []
        menu = []

        cursor.execute("SELECT*FROM produtos")
        a = cursor.fetchall()

        for a in a:
            memoria.append(a)

        ite = 0
        for ite in range(len(memoria)):
            menu.append(memoria[ite][1])
        menu.sort()
        print(menu)

        self.combb["values"]=menu
        self.combb.pack()

   #Função para alterar preço e nome de produtos já existentes
    def alterarProd(self):


        prod = produtos()

        prod.codproduto = str(self.nomeProd[self.txtnome.get()])
        prod.nomeproduto = self.txtnome.get()
        prod.preco = self.txtprec.get()

        self.lblmsg["text"] = prod.updateProd()


        self.txtnome.delete(0, END)
        self.txtprec.delete(0, END)

        banco = sqlite3.connect('prod.db')
        cursor = banco.cursor()
        self.memoria = []
        menu = []

        cursor.execute("SELECT*FROM produtos")
        a = cursor.fetchall()

        for a in a:
            self.memoria.append(a)

        ite = 0
        for ite in range(len(self.memoria)):
            menu.append(self.memoria[ite][1])

        menu.sort()
        print(menu)
        self.combb["values"] = menu
        self.combb.pack()

   #Função para excluir determinado produto
    def excluirProd(self):


        prod = produtos()

        prod.codproduto = str(self.nomeProd[self.txtnome.get()])

        self.lblmsg["text"] = prod.deleteProd()


        self.txtnome.delete(0, END)
        self.txtprec.delete(0, END)

        banco = sqlite3.connect('prod.db')
        cursor = banco.cursor()
        memoria = []
        menu = []

        cursor.execute("SELECT*FROM produtos")
        a = cursor.fetchall()

        for a in a:
            memoria.append(a)

        ite = 0
        for ite in range(len(memoria)):
            menu.append(memoria[ite][1])
        menu.sort()
       

        self.combb["values"] = menu
        self.combb.pack()

    
# Página de operaçõo de compra do aplicativo
class aplicativo(Page):
    # Anunciação do construtor e objetos da classe
    def __init__(self, master=None):
        Page.__init__(self,master)
        global fonte
        global txtcampo1
        self.notaPed = []
        self.adicao = 0
        self.precoPed = []
        self.ordemPedido = 0


        self.nom=[]
        self.pre=[]

        self.container1=Frame(self)
        self.container1["padx"]=10
        self.container1["pady"]=20
        self.container1.pack()

        self.container2 = Frame(self)
        self.container2["padx"] = 50
        self.container2["pady"] = 20
        self.container2.pack()

        self.container7=Frame(self)
        self.container7["padx"]=50
        self.container7["pady"]=200
        self.container7.pack()

        fonte = ("Verdana", "16")

        # Construção dos frames da seção de compra da interface
        lbltexto1 = Label(self.container1,text="produto:", font=fonte, width=10)
        lbltexto1.pack(side=LEFT)





        btncalc=Button(self.container2,text="comprar", font=fonte, width=14)
        btncalc.pack(side=LEFT)
        btncalc["command"]=self.comprar


        btnretirar=Button(self.container2,text="retirar", font=fonte, width=14)
        btnretirar.pack(side=LEFT)
        btnretirar["command"]=self.apagar


        banco = sqlite3.connect('prod.db')
        cursor = banco.cursor()
        self.memoria = []
        self.menu = []
        self.gends={}

        cursor.execute("SELECT*FROM produtos")
        a = cursor.fetchall()
        agenda={}

        for a in a:
            self.memoria.append(a)

        ite = 0
        for ite in range(len(self.memoria)):
            self.menu.append(self.memoria[ite][1])
            self.gends[self.memoria[ite][1]] = self.memoria[ite][0]

        self.combo_box = ttk.Combobox(self.container1)
        self.combo_box['values'] = self.menu
        self.combo_box['width']=30
        self.combo_box['font'] = 16
        self.combo_box.bind('<KeyRelease>', self.check_input)
        self.combo_box.pack()


    def check_input(self,event):
        value = event.widget.get()

        if value == '':
            self.combo_box['values'] = self.menu
        else:
            data = []
            for item in self.menu:
                if value.lower() in item.lower():
                    data.append(item)

            self.combo_box['values'] = data

    #Criação da função comprar
    def comprar(self,master=None):
        container3 = Frame(self)
        container3["padx"] = 10

        container4 = Frame(self)
        container4["padx"] = 10

        prod=produtos()

        codproduto = str(self.gends[self.combo_box.get()])
        prod.selectProd(codproduto)

        global lbltexto2
        global ite
        banco = sqlite3.connect('prod.db')
        cursor = banco.cursor()
        listinha = []
        cursor.execute("SELECT*FROM produtos")
        a = cursor.fetchall()
        agenda = {}
        ite = 0
        for a in a:
            listinha.append(a)

        for ite in range(len(listinha)):
            agenda[listinha[ite][0]] = [listinha[ite][1], listinha[ite][2]]
        b = agenda[int(codproduto)]



        self.ordemPedido= self.ordemPedido + 1
        container3.place(x=20, y=20+30*self.ordemPedido)
        container4.place(x=1300,y=300)
        self.precoPed.append(b[1])
        self.adicao= self.adicao + self.precoPed[self.ordemPedido - 1]
        cx=30-len(str(prod.nomeproduto))
        lbltexto2 = Label(container3, text=str(prod.nomeproduto)+cx*"_"+"R$"+str(prod.preco), font=fonte, width=40)
        lbltexto2.pack(side=LEFT)
        lbltexto3=Label(container4, text="O total é "+str(self.adicao), font=fonte)
        lbltexto3.pack()
        self.notaPed.append(lbltexto2)
        self.nom.append(str(prod.nomeproduto))
        self.pre.append(str(prod.preco))

    #Criação da função para apagar pedido anterior
    def apagar(self):
        container4 = Frame(self)
        container4["padx"] = 10
        container4.place(x=1300, y=300)

        self.notaPed[len(self.notaPed) - 1].destroy()
        self.notaPed.remove(self.notaPed[len(self.notaPed) - 1])
        self.adicao= self.adicao - self.precoPed[len(self.precoPed) - 1]
        self.precoPed.remove(self.precoPed[len(self.precoPed) - 1])
        self.nom.remove(self.nom[len(self.nom)-1])
        self.pre.remove(self.pre[len(self.pre)-1])
        self.ordemPedido= self.ordemPedido - 1
        lbltexto3 = Label(container4, text="O total é " + str(self.adicao), font=fonte)
        lbltexto3.pack()






#Cliar a classe responsável por fazer a permuta entre as páginas
class MainView(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        p2 = Application2(self)
        p3 = aplicativo(self)

        buttonframe = tk.Frame(self)
        conte = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        conte.pack(side="top", fill="both", expand=True)


        p2.place(in_=conte, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=conte, x=0, y=0, relwidth=1, relheight=1)


        b2 = tk.Button(buttonframe, text="Cadastro de produtos", command=p2.lift,width=17,height=3)
        b3 = tk.Button(buttonframe, text="Área de Venda", command=p3.lift,width=17,height=3)


        b2.pack(side="left")
        b3.pack(side="left")
        p2.show()
#parâmetros da tela
root = tk.Tk()
root.title("Bom mercado")
root.iconbitmap(default='favicon.ico')
main = MainView(root)
root.state('zoomed')
main.pack(side="top", fill="both", expand=1)
root.wm_geometry("400x400")
root.mainloop()
