import tkinter as tk
import orm
from tkinter import messagebox

def adiciona_filme():
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.adiciona_filme(nome, ano, nota)
    messagebox.showinfo("Sucesso", "Filme adicionado com sucesso!")

def atualiza_filme():
    id = entry_id.get()
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.atualiza_filme(id, nome, ano, nota)
    messagebox.showinfo("Sucesso", "Filme atualizado com sucesso!")

def remover_filme():
    id = entry_id.get()
    orm.remover_filme(id)
    messagebox.showinfo("Sucesso", "Filme removido com sucesso!")

#Interface Grafica

root = tk.Tk()
root.title("Gerenciador de filmes")


#Rótulos e campos de entrada
label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=1, column=0)
entry_nome = tk.Entry(root, width=50)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

label_ano = tk.Label(root, text="Ano:")
label_ano.grid(row=2, column=0)
entry_ano = tk.Entry(root, width=50)
entry_ano.grid(row=2, column=1, padx=10, pady=5)

label_nota = tk.Label(root, text="Nota:")
label_nota.grid(row=3, column=0)
entry_nota = tk.Entry(root, width=50)
entry_nota.grid(row=3, column=1, padx=10, pady=5)

button_adicionar = tk.Button(root, text="Adicionar Filme", command=adiciona_filme)
button_adicionar.grid(row=4, column=0, padx=10, pady=5)

button_atualizar = tk.Button(root, text="Atualizar Filme", command=atualiza_filme)
button_atualizar.grid(row=4, column=1, padx=10, pady=5)

button_remover = tk.Button(root, text="Remover Filme", command=remover_filme)
button_remover.grid(row=4, column=2, padx=10, pady=5)

root.mainloop()