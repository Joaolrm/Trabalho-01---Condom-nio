from Apartamento import Apartamento
from Torre import Torre
from ListaDeApComVaga import ListaDeApComVaga
from filaDeVagas import FilaDeVagas
from ListaDeTorres import ListaDeTorres

listaDeTorres = ListaDeTorres()
listaDeApComVaga = ListaDeApComVaga()
filaDeVagas = FilaDeVagas()

def cadastrarTorre():
    print("-----------Cadastro de torres-----------")
    nome = input("Digite o nome da torre: ")
    endereco = input("Digite o endereço da torre: ")
    listaDeTorres.add(Torre(nome, endereco))

def cadastrarApartamento():
    if listaDeTorres.getTorres() >= 1:
        numAp = input("Digite o número do apartamento: ")
        listaDeTorres.imprimir()
        torre = listaDeTorres.getTorreById(int(input("Escolha uma torre pelo id: ")))
        apartamento = Apartamento(numAp, torre)
        if listaDeApComVaga.getOcupacao() < 10:
            listaDeApComVaga.add(apartamento)
        else:
            filaDeVagas.add(apartamento)

    else:
        print("Não existem torres para cadastrar um apartamento, você irá para o cadastro de torres, antes de cadastrar o apartamento.")
        cadastrarTorre()
        cadastrarApartamento()


def liberarVaga():
    if listaDeApComVaga.getOcupacao() == 10:
        vagaALiberar = int(input("Digite o número da vaga que você quer liberar: "))
        apDaVagaLiberada = listaDeApComVaga.remover(vagaALiberar)
        filaDeVagas.add(apDaVagaLiberada)
        primeiroApDaFila = filaDeVagas.remover()
        listaDeApComVaga.add(primeiroApDaFila)

    else:
        input("Você não deve liberar uma vaga sem que todas as vagas estejam ocupadas.")

def listarApsComVagas():
    listaDeApComVaga.imprimir()

def mostrarApsNaFila():
    filaDeVagas.imprimir()


menu = f"""a) - Cadastrar apartamento\nb) - Liberar vaga\nc) - Listar Ap's com vagas\nd) - Mostrar ap's na fila\ne) - Cadastrar torre\nf) - Finalizar programa"""
t1 = Torre("Villagio", "Rua 2")
t2 = Torre("Villagio 2", "Rua 4")
ap1 = Apartamento("101", t1)
ap2 = Apartamento("101", t2)
ap3 = Apartamento("102", t1)
ap4 = Apartamento("103", t1)
ap5 = Apartamento("104", t1)
ap6 = Apartamento("105", t1)
ap7 = Apartamento("106", t1)
ap8 = Apartamento("107", t1)
ap9 = Apartamento("108", t1)
ap10 = Apartamento("109", t1)
ap11 = Apartamento("110", t1)
listaDeTorres.add(t1)
listaDeTorres.add(t2)
listaDeApComVaga.add(ap1)
listaDeApComVaga.add(ap2)
listaDeApComVaga.add(ap3)
listaDeApComVaga.add(ap4)
listaDeApComVaga.add(ap5)
listaDeApComVaga.add(ap6)
listaDeApComVaga.add(ap7)
listaDeApComVaga.add(ap8)
listaDeApComVaga.add(ap9)


while True:
    print(menu)
    opSelect = input("Digite uma letra para prosseguir: ").lower()

    if opSelect == 'a':
        cadastrarApartamento()
    elif opSelect == 'b':
        liberarVaga()
    elif opSelect == 'c':
        listarApsComVagas()
    elif opSelect == 'd':
        mostrarApsNaFila()
    elif opSelect == 'e':
        cadastrarTorre()
    elif opSelect == 'f':
        print("Finalizando programa...")
        break
    else:
        print("Opção inválida!")

