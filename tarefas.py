import mysql.connector
import tkinter as tk
from tkinter import messagebox 
from tkinter import *


conexao = mysql.connector.connect(
    host = 'localhost', 
    user = 'root', 
    password = 'root', 
    database = 'tarefas'
)
cursor = conexao.cursor()
root = tk.Tk()

def membros():
    cpf = entry_cpf.get()
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    data_nascimento = entry_data_nascimento.get()

    if cpf and nome and telefone and email and data_nascimento:
        cursor.execute('INSERT INTO membro(cpf, nome, telefone, email, data_nascimento) VALUES(%s, %s, %s, %s, %s)', (cpf, nome, telefone, email, data_nascimento))
        conexao.commit()
        messagebox.showinfo("Cadastro realizado com sucesso")
    else:
        messagebox.showwarning("Por favor, preencha tudo antes de enviar")


def tarefas():
    titulo = entry_titulo.get()
    descricao = entry_descricao.get()
    status = entry_status.get().upper()
    prazo = entry_prazo.get()
    membro = entry_membro.get()

    if titulo and descricao and status and prazo and membro:
        cursor.execute('INSERT INTO tarefas(titulo, descricao, status, prazo, membro) VALUES (%s, %s, %s, %s, %s)', (titulo, descricao, status, prazo, membro))
        conexao.commit()
        messagebox.showinfo("Cadastro realizado com sucesso")
    else:
        messagebox.showwarning("Por favor, preencha tudo antes de enviar")

def membros_tarefas():
    # Executa a consulta para buscar membros e suas tarefas
    cursor.execute('SELECT m.nome, t.titulo, t.descricao, t.prazo FROM membro m JOIN tarefas t ON t.membro = m.cpf;')
    resultados = cursor.fetchall()

    # Cria uma nova janela para exibir os resultados
    janela_resultados = tk.Toplevel(root)
    janela_resultados.title("Resultados da Pesquisa")
    
    # Adiciona um título
    Label(janela_resultados, text="Nome | Tarefa | Descrição | Prazo", font=("Arial", 12, "bold")).pack(pady=10)

    # Exibe os resultados em labels
    for resultado in resultados:
        texto = f"{resultado[0]} | {resultado[1]} | {resultado[2]} | {resultado[3]}"
        Label(janela_resultados, text=texto, anchor="w", justify="left").pack()

# Botão de pesquisa
botao_pesquisar = tk.Button(root,text="Pesquisar", command=membros_tarefas)
botao_pesquisar.grid(row=11, column=0, columnspan=2, pady=10)

    

def fechar_conexao():
    cursor.close()
    conexao.close()
    root.destroy()   



root.title("Cadastro de membros da família e suas tarefas")

Label_cpf = tk.Label(root, text = "CPF")
Label_cpf.grid(row = 0, column = 0, pady = 10)

entry_cpf = tk.Entry(root)
entry_cpf.grid(row = 1, column = 0, pady = 10)
#---------------------------------------------------------------

Label_nome = tk.Label(root, text = "Nome")
Label_nome.grid(row = 2, column = 0, pady = 10)

entry_nome = tk.Entry(root)
entry_nome.grid(row = 3, column = 0, pady = 10)
#---------------------------------------------------------------

Label_telefone = tk.Label(root, text = "telefone")
Label_telefone.grid(row = 4, column = 0, pady = 10)

entry_telefone = tk.Entry(root)
entry_telefone.grid(row = 5, column = 0, pady = 10)
#---------------------------------------------------------------
Label_email = tk.Label(root, text = "e-mail")
Label_email.grid(row = 6, column = 0, pady = 10)

entry_email = tk.Entry(root)
entry_email.grid(row = 7, column = 0, pady = 10)

#---------------------------------------------------------------

Label_data_nascimento = tk.Label(root, text = "Data de nascimento (yyyy/mm/dd)")
Label_data_nascimento.grid(row = 8, column = 0, pady = 10)

entry_data_nascimento = tk.Entry(root)
entry_data_nascimento.grid(row = 9, column = 0, pady = 10)

botao = tk.Button(root, text = "Salvar", command = membros)
botao.grid(row = 10, column = 0, columnspan = 1, pady = 10)
#---------------------------------------------------------------

Label_titulo = tk.Label(root, text = "Tarefa")
Label_titulo.grid(row = 0, column = 1, pady = 10, padx= 20)

entry_titulo = tk.Entry(root)
entry_titulo.grid(row = 1, column = 1, pady = 10, padx= 20)
#---------------------------------------------------------------

Label_descricao = tk.Label(root, text = "Descrição")
Label_descricao.grid(row = 2, column = 1, pady = 10, padx= 20)

entry_descricao = tk.Entry(root)
entry_descricao.grid(row = 3, column = 1, pady = 10, padx=20)

#---------------------------------------------------------------

Label_status = tk.Label(root, text = "Status(Pendente, Em progresso, Realizada)")
Label_status.grid(row = 4, column = 1, pady = 10, padx= 20)

entry_status = tk.Entry(root)
entry_status.grid(row = 5, column = 1, pady = 10, padx= 20)

#---------------------------------------------------------------

Label_prazo = tk.Label(root, text = "Prazo (yyyy/mm/dd)")
Label_prazo.grid(row = 6, column = 1, pady = 10, padx= 20)

entry_prazo = tk.Entry(root)
entry_prazo.grid(row = 7, column = 1, pady = 10, padx= 20)

#---------------------------------------------------------------

Label_membro = tk.Label(root, text = "Membro da tarefa")
Label_membro.grid(row = 8, column = 1, pady = 10, padx= 20)

entry_membro = tk.Entry(root)
entry_membro.grid(row = 9, column = 1, pady = 10, padx= 20)

botao2 = tk.Button(root, text = "Salvar", command = tarefas)
botao2.grid(row = 10, column = 1, columnspan = 1, pady = 10, padx= 20)

#-----------------------------------------------------------------------------


root.protocol("WM_DELETE_WINDOW", fechar_conexao)

tk.mainloop()