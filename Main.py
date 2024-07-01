from Apartamento import Apartamento
from Torre import Torre
from ListaDeApComVaga import ListaDeApComVaga
from filaDeVagas import FilaDeVagas

t1 = Torre("Villagio", "Rua 2")
t2 = Torre("Villagio 2", "Rua 4")
ap1 = Apartamento("101", t1)
ap2 = Apartamento("101", t2)
ap3 = Apartamento("102", t1)
ap4 = Apartamento("103", t1)
ap5 = Apartamento("104", t1)
ap6 = Apartamento("105", t1)



lv1 = ListaDeApComVaga()
lv1.add(ap3)
lv1.add(ap1)
lv1.add(ap2)
lv1.add(ap4)
print(lv1.remover(2))
lv1.add(ap1)
lv1.add(ap5)
lv1.add(ap6)
lv1.remover(2)
print(lv1.getOcupacao())
lv1.remover(3)
lv1.remover(1)
lv1.remover(4)
lv1.remover(5)
lv1.remover(5)
lv1.remover(6)
fv1= FilaDeVagas()
fv1.remover()






