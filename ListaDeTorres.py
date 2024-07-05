from Torre import Torre
class ListaDeTorres:
	def __init__(self):
		self.inicio = None
		self.torres = 0

	def getTorres(self):
		return self.torres

	def add(self, torre):
		if self.inicio == None:
			self.inicio = torre
		else:
			if torre.id < self.inicio.id:
				torre.proximo = self.inicio
				self.inicio = torre
			else:
				ant = self.inicio
				aux = self.inicio.proximo
				while aux:
					if torre.id < aux.id:
						torre.proximo = ant.proximo
						ant.proximo = torre
						break
					else:
						ant = aux
						aux = aux.proximo
				if aux == None and torre.id >= ant.id:
					ant.proximo = torre
		self.torres += 1

	def imprimir(self):
		print("Lista de torres disponiveis: ")
		if self.inicio == None:
			print( "Lista Vazia" )
		else:
			print( self.torres,  " elementos na Lista" )
			aux = self.inicio
			while aux:
				print( aux )
				aux = aux.proximo

	def remover(self, numid):
		tamInicial = self.torres
		apRemovido = None
		if self.inicio != None:

			if self.inicio.proximo == None and self.inicio.id == numid:
				apRemovido = self.inicio
				self.inicio = None
				self.torres = 0

			elif self.inicio.id == numid:
				apRemovido = self.inicio
				self.inicio = self.inicio.proximo
				self.torres -= 1

			else:
				ant = self.inicio
				aux = self.inicio.proximo
				while aux:
					if aux.id == numid:
						apRemovido = aux
						ant.proximo = aux.proximo
						self.torres -= 1
						break
					else:
						ant = aux
						aux = aux.proximo
			if apRemovido:
				apRemovido.proximo = None
				return apRemovido
		if tamInicial == self.torres:
			print( "Número da id não encontrado")


	def getTorreById(self, numId):
		if self.inicio != None:

			if self.inicio.proximo == None and self.inicio.id == numId:
				return self.inicio


			elif self.inicio.id == numId:
				return self.inicio


			else:
				ant = self.inicio
				aux = self.inicio.proximo
				while aux:
					if aux.id == numId:
						return aux
					else:
						ant = aux
						aux = aux.proximo


		
		

		


				