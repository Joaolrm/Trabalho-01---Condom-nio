from Apartamento import Apartamento
class ListaDeApComVaga:
	def __init__(self):
		self.inicio = None
		self.ocupacao = 0

	def getOcupacao(self):
		return self.ocupacao

	def add(self, apartamento):
		numVaga = self.obterMenorVagaDisponivel()
		apartamento.setVaga(numVaga)
		if self.inicio == None:
			self.inicio = apartamento
		else:
			if apartamento.vaga < self.inicio.vaga:
				apartamento.proximo = self.inicio
				self.inicio = apartamento
			else:
				ant = self.inicio
				aux = self.inicio.proximo
				while aux:
					if apartamento.vaga < aux.vaga:
						apartamento.proximo = ant.proximo
						ant.proximo = apartamento
						break
					else:
						ant = aux
						aux = aux.proximo
				if aux == None and apartamento.vaga >= ant.vaga:
					ant.proximo = apartamento
		self.ocupacao += 1

	def imprimir(self):
		print("------Lista Encadeada---------")
		if self.inicio == None:
			print( "Lista Vazia" )
		else:
			print( self.ocupacao,  " elementos na Lista" )
			aux = self.inicio
			while aux:
				print( aux )
				aux = aux.proximo

	def remover(self, numVaga):
		tamInicial = self.ocupacao
		apRemovido = None
		if self.inicio != None:

			if self.inicio.proximo == None and self.inicio.vaga == numVaga:
				apRemovido = self.inicio
				self.inicio = None
				self.ocupacao = 0

			elif self.inicio.vaga == numVaga:
				apRemovido = self.inicio
				self.inicio = self.inicio.proximo
				self.ocupacao -= 1

			else:
				ant = self.inicio
				aux = self.inicio.proximo
				while aux:
					if aux.vaga == numVaga:
						apRemovido = aux
						ant.proximo = aux.proximo
						self.ocupacao -= 1
						break
					else:
						ant = aux
						aux = aux.proximo
			if apRemovido:
				apRemovido.setVaga("Sem vaga")
				apRemovido.proximo = None
				return apRemovido
		if tamInicial == self.ocupacao:
			print( "Número da vaga não encontrado")
		
		

	def obterMenorVagaDisponivel(self):
		numVaga = 1
		if self.inicio:
			ap = self.inicio
			pAp = self.inicio.proximo

			while pAp:
				difVaga = pAp.vaga - ap.vaga
				if difVaga != 1:
					numVaga = ap.vaga + 1
					return numVaga
				ap, pAp = pAp, pAp.proximo
				
			
			if ap.vaga != 1 and self.inicio.vaga != 1:
				numVaga = 1
			else: 
				numVaga = ap.vaga + 1

		return numVaga

		


				