estoque = {}

def adicionar_produto():
    nome = input("Digite o nome do produto: ").strip()
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))

    estoque[nome] = {"preco": preco, "quantidade": quantidade}
    print(f'✅ Produto {nome} adicionado com sucesso')


def menu():
    while True:
        print("\n=== 🛍️ MENU - CONTROLE DE ESTOQUE ===")
        print("1️⃣ Adicionar Produto")
        print("2️⃣ Atualizar Produto")
        print("3️⃣ Excluir Produto")
        print("4️⃣ Visualizar Estoque")
        print("5️⃣ Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            print("Você deseja atualizar um produto...")
        elif opcao == "3":
            print("Você deseja excluir um produto...")
        elif opcao == "4":
            print("Você deseja visualizar o estoque...")
        elif opcao == "5":
            print("👋 Saindo... Até mais!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

menu()