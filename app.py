from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

biblioteca_cidade = Biblioteca("Biblioteca da cidade")
biblioteca_shopping = Biblioteca("Biblioteca do shopping")
""
livro1 = Livro("O Senhor dos Anéis", "J. R. R. Tolkien", 40.0, "9788532511017")
livro2 = Livro("1984", "George Orwell", 30.0, "9788532522921")
revista1 = Revista("Revista de Tecnologia", "Tech Magazine", 15.0, "Quinta")


livro1.aplicar_desconto()
revista1.aplicar_desconto()

biblioteca_cidade.adicionar_item(livro1)
biblioteca_cidade.adicionar_item(livro2)
biblioteca_cidade.adicionar_item(revista1)




# biblioteca_cidade.alterna_estado()
# biblioteca_cidade.receber_avaliacao("João", 5)
# biblioteca_cidade.receber_avaliacao("Maria", 4)
# biblioteca_cidade.receber_avaliacao("Pedro", 10)

def main():
    #Biblioteca.listar_bibliotecas()
    print(vars(livro1))
    print(vars(revista1))
    biblioteca_cidade.exibir_itens()
    

if __name__ == "__main__":
    main()

