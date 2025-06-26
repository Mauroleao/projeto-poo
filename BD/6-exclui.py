import sqlite3

# 1 - conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Excluindo os dados
id = (1, 2)

cursor.execute("""
    DELETE FROM filmes
    WHERE id IN (?, ?)
""", 
id
)

conexao.commit()  # Salva as alterações
print("Dados excluídos com sucesso!")