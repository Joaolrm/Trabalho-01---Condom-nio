class Apartamento:
    idGenerator = 0

    def __init__(self, numero, torre):
        Apartamento.idGenerator += 1
        self.id = Apartamento.idGenerator
        self.numero = numero
        self.torre = torre
        self.vaga = "Sem vaga"
        self.proximo = None

    def __str__(self):
        return f"""Apartamento:\nId do apartamento: {self.id}\nNúmero do apartamento: {self.numero}\nNúmero da vaga: {self.vaga}\nTorre: \n{self.torre}\n"""

    def cadastrar(self):
        print(f"Apartamento cadastrado:\n{self}")
    
    def imprimir(self):
        print(f"Apartamento: {self}\n")

    def setVaga(self, vaga):
        self.vaga = vaga
        