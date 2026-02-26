estoque = {}

while True:
    print("\n1 - Adicionar produto")
    print("2 - Atualizar quantidade")
    print("3 - Mostrar estoque")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        estoque[nome] = quantidade
        print("Produto adicionado!")

    elif opcao == "2":
        nome = input("Produto para atualizar: ")
        if nome in estoque:
            quantidade = int(input("Nova quantidade: "))
            estoque[nome] = quantidade
            print("Quantidade atualizada!")
        else:
            print("Produto não encontrado.")

    elif opcao == "3":
        print("\nEstoque atual:")
        for produto, qtd in estoque.items():
            print(f"{produto}: {qtd}")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")