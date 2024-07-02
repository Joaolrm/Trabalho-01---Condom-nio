class Torre:
    idGenerator = 0

    def __init__(self, nome, endereco):
        Torre.idGenerator += 1
        self.id = Torre.idGenerator
        self.nome = nome
        self.endereco = endereco
        self.proximo = None

    def __str__(self):
        return f"""\tId da torre: {self.id}\n\tNome da torre: {self.nome}\n\tEndereço da torre: {self.endereco}\n"""

    def cadastrar(self):
        print(f"Torre cadastrada:\n{self}")

    def imprimir(self):
        print(f"Torre:\n{self}\n")

        
        
        
