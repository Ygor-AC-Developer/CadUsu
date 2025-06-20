def perguntar():
    return (
        input(
            "\n<I> - Para Inserir um usuário\n"
            + "<P> - Para Pesquisar um usuário\n"
            + "<E> - Para Excluir um usuário\n"
            + "<L> - Para Listar um usuário\n"
            + "\nO que deseja realizar? "
        )
        .strip()
        .upper()
    )


def inserir(dicionario):
    while True:
        chave = input("\nDigite o login do usuário: ").strip().upper()
        if chave in dicionario:
            print("Usuário já existe")
        else:
            nome = input("Digite o nome do usuário: ")
            dicionario[chave] = nome
            print(f"Usuário '{nome}' inserido com sucesso\n")

        repetir = input("\nDeseja inserir outro usuário? (S/N): ").strip().upper()
        if repetir != "S":
            break


def pesquisar(dicionario):
    while True:
        chave = input("\nDigite o login a ser pesquisado: ").strip().upper()
        if chave in dicionario:
            print(f"Usuário encontrado: {dicionario[chave]}\n")
        else:
            print("Usuário não encontrado\n")

        repetir = input("\nDeseja pesquisar outro usuário? (S/N): ").strip().upper()
        if repetir != "S":
            break


def excluir(dicionario):
    while True:
        chave = input("\nDigite o login a ser excluído: ").strip().upper()
        if chave in dicionario:
            del dicionario[chave]
            print("Usuário excluído com sucesso\n")
        else:
            print("Usuário não encontrado para exclusão\n")

        repetir = input("\nDeseja excluir outro usuário? (S/N): ").strip().upper()
        if repetir != "S":
            break


def listar(dicionario):
    if dicionario:
        print("=== Lista de Usuários ===")
        for chave, nome in dicionario.items():
            print(f"Login: {chave} | Nome: {nome}")
    else:
        print("Nenhum usuário cadastrado.\n")

    qtd = len(dicionario)
    if qtd > 1:
        print(f"\nUsuários cadastrados: {qtd}")
