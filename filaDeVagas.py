from Apartamento import Apartamento
class FilaDeVagas:

    def __init__(self) -> None:
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add(self, apartamento):
        if self.inicio == None:
            self.inicio = apartamento
            
        else:
            self.fim.proximo = apartamento
        self.fim = apartamento
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        print("----------Fila de vagas----------")
        if self.inicio == None:
            print( "Fila de vagas vazia" )
        else:
            print( self.tamanho,  " elementos na Lista" )
            aux = self.inicio
            while aux:
                texto += aux.dado + " - "
                aux = aux.proximo
            print(texto)
    
    def remover(self):
        if self.inicio:
            apRemovido = self.inicio
            if self.inicio.prox == None:
                self.inicio = None
                self.fim = None
            else:
                self.inicio = self.inicio.proximo
            
            apRemovido.proximo = None
            return apRemovido
        else:
            print( "Fila de vagas vazia" )