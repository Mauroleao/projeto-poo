from modelos.biblioteca import Biblioteca

biblioteca_cidade = Biblioteca("Biblioteca da cidade")
biblioteca_shopping = Biblioteca("Biblioteca do shopping")

biblioteca_cidade.alterna_estado()

def main():
    Biblioteca.listar_bibliotecas()

if __name__ == "__main__":
    main()

