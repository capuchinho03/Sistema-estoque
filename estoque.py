import customtkinter
from tkinter import ttk
import mysql.connector

conexao = mysql.connector.connect(
    host='',
    user='',
    password='',
    database='',
)

cursor = conexao.cursor()

# funcoes

def popular():
    tv.delete(* tv.get_children())
    comando = 'SELECT * FROM produtos'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for db in resultado:
        tv.insert("", "end", values=db)


def cadastrar():
    nome = nome_entry.get()
    quantidade = qtn_entry.get()
    valor = valor_entry.get()

    comando = f'INSERT INTO produtos (produto, valor, quantidade) VALUES ("{nome}", {valor}, {quantidade})'
    cursor.execute(comando)
    conexao.commit()

    popular()

    nome_entry.delete(0, 100)
    qtn_entry.delete(0, 100)
    valor_entry.delete(0, 100)

# tela

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

janela = customtkinter.CTk()
janela.title('Estoque')
janela.geometry('600x300')

# frame
frame1 = customtkinter.CTkFrame(janela, width= 300, height=300,)
frame1.place(x=0, y=0)

# elementos

# nome
nome_text = customtkinter.CTkLabel(frame1, text='Nome do Produto')
nome_text.place(x=50, y=10)

nome_entry = customtkinter.CTkEntry(frame1)
nome_entry.place(x=50, y=40)

# quantidade
qtn_text = customtkinter.CTkLabel(frame1, text='Quantidade')
qtn_text.place(x=50, y=90)

qtn_entry = customtkinter.CTkEntry(frame1)
qtn_entry.place(x=50, y=120)

# valor 
valor_text = customtkinter.CTkLabel(frame1, text='Valor')
valor_text.place(x=50, y=170)

valor_entry = customtkinter.CTkEntry(frame1)
valor_entry.place(x=50, y=200)

# botao 
botao_cadastrar = customtkinter.CTkButton(frame1, text='Cadastrar', command=cadastrar)
botao_cadastrar.place(x=50, y=250)

# frame2

frame2 = customtkinter.CTkFrame(janela, width=290, height=300)
frame2.place(x=310, y=0)

tv = ttk.Treeview(frame2,height=13, columns=("id", "Nome_Produto","Valor", "Quantidade"), show='headings')
tv.column('id', minwidth=0, width=50)
tv.column('Nome_Produto', minwidth=0, width=110)
tv.column('Valor', minwidth=0, width=70)
tv.column('Quantidade', minwidth=0, width=50)

tv.heading('id', text='ID')
tv.heading('Nome_Produto', text='NOME_PRODUTO')
tv.heading('Valor', text='Valor')
tv.heading('Quantidade', text='QTND')
tv.pack()
popular()





if janela.mainloop():
    cursor.close()
    conexao.close()

