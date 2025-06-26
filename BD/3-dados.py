import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Criando a tabela
cursor.execute('''

        INSERT INTO filmes (nome, ano, nota)
        VALUES ('Momento de Glória', 2023, 8.5)

''')

conexao.commit()  # Salva as alterações
conexao.close()
print("Dados inseridos com sucesso!")