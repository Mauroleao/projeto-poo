import sqlite3

# 1 - conectando no BD
def conecta_db():
    conexao = sqlite3.connect('titulo.db')
    return conexao

# 2 - Inserir dados
def insere_dados(nome, ano, nota):
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO filmes (nome, ano, nota)
        VALUES (?, ?, ?)
    """, (nome, ano, nota))
    conexao.commit()  # Salva as alterações
    conexao.close()   # Fecha a conexão

# 3 - Ler dados
def obter_dados():
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute(" SELECT * FROM filmes")
    dados = cursor.fetchall()
    conexao.close()
    return dados




