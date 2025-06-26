import sqlite3

# 1 - conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Lendo os dados
dados = cursor.execute("SELECT * FROM  filmes")

# 3 - Imprimindo os dados
print(dados.fetchall())

