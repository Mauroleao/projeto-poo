from modelos.biblioteca import Biblioteca

biblioteca_cidade = Biblioteca("Biblioteca da cidade")
biblioteca_shopping = Biblioteca("Biblioteca do shopping")

biblioteca_cidade.alterna_estado()

biblioteca_cidade.receber_avaliacao("João", 5)
biblioteca_cidade.receber_avaliacao("Maria", 4)
biblioteca_cidade.receber_avaliacao("Pedro", 10)

def main():
    Biblioteca.listar_bibliotecas()

if __name__ == "__main__":
    main()

