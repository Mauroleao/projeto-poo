class Biblioteca:
    bibliotecas = []
    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        Biblioteca.bibliotecas.append(self)
    def __str__(self):
        return self.nome
    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'Nome da biblioteca'} | {'status'}")
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome.ljust(25)} | {biblioteca.ativo}")


    def alterna_estado(self):
        self._ativo =  not self._ativo    

    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada"        


