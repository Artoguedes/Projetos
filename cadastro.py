usuarios = []

while True:
    print("\n1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")

        usuario = {
            "nome": nome,
            "idade": idade
        }

        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        print("\nUsuários cadastrados:")
        for u in usuarios:
            print(f"Nome: {u['nome']} | Idade: {u['idade']}")

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")