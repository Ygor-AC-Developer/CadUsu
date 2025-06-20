from C4SubPasta.Funcoes import *

usuarios = {}

opcao = perguntar()

while opcao != "S":
    if opcao == "I":
        inserir(usuarios)
    elif opcao == "P":
        pesquisar(usuarios)
    elif opcao == "E":
        excluir(usuarios)
    elif opcao == "L":
        listar(usuarios)
    else:
        print("Opção inválida. Tente novamente.\n")

    opcao = perguntar()

print("Programa encerrado.")
