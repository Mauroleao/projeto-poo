from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///banco.db', echo=True)
Base = declarative_base()

class Filme(Base):
    __tablename__ = 'filmes'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)

Base.metadata.create_all(engine)


# Inserir dados

def adiciona_filme(nome, ano, nota):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme =Filme(nome=nome, ano=ano, nota=nota)
    session.add(filme)
    session.commit()
    session.close()

# adiciona_filme('O Poderoso Chefão', 1972, 9.2)
# adiciona_filme('O Senhor dos Anéis: O Retorno do Rei', 2003, 9.0) 

#Atualiza dados

def atualiza_filme(id, nome=None, ano=None, nota=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter(Filme.id == id).first()
    if filme:
        if nome:
            filme.nome = nome
        if ano:
            filme.ano = ano
        if nota:
            filme.nota = nota
        session.commit()
    session.close()

atualiza_filme(1, nome='O Poderoso Chefão: Parte II', ano=1974, nota=9.0)


#Excluir dados

def remover_filme(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter(Filme.id == id).first()
    if filme:
        session.delete(filme)
        session.commit()
    session.close()

remover_filme(2)    
