import sqlite3

# 1- conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2- Atualizando os dados
id = 1
cursor.execute("""
    UPDATE filmes SET nota = ?
    WHERE id = ?
    """,
    ('10', id)
)

conexao.commit()  # Salva as alterações
print("Dados atualizados com sucesso!")
