class Torre:
    idGenerator = 0

    def __init__(self, nome, endereco):
        Torre.idGenerator += 1
        self.id = Torre.idGenerator
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        return f"""\tId: {self.id}\n\tNome: {self.nome}\n\tEndereco: {self.endereco}\n"""

    def cadastrar(self):
        print(f"Torre cadastrada:\n{self}")

    def imprimir(self):
        print(f"Torre:\n{self}\n")

        
        
        
