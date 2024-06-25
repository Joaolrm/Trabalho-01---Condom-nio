from Apartamento import Apartamento
from Torre import Torre

t1 = Torre("Villagio", "Rua 2")
t1.cadastrar()
t2 = Torre("Villagio 2", "Rua 4")
t2.cadastrar()
t1.imprimir()
ap1 = Apartamento("1813", t1)
ap1.cadastrar()
ap1.imprimir()
