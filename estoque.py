estoque = {}

def adicionar_produto():
    while True:  
      nome = input("Digite o nome do produto: ").strip()
      
      if not any(c.isalpha() for c in nome):
          print("❌ Nome Inválido! O produto deve conter pelo menos uma letra.")
          continue
      
      if nome in estoque:
          print("❌ Produto já cadastrado! Use a opção de atualizar.")
          return
      
      try:
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade em estoque: "))

        if preco < 0 or quantidade < 0:
            print("❌ Preço e quantidade devem ser valores positivos, tente novamente:")
            continue

        estoque[nome] = {"preco": preco, "quantidade": quantidade}
        print(f'✅ Produto {nome} adicionado com sucesso!')
        break

      except ValueError:
          print("❌ Erro! Insira valores numéricos para preço e quantidade!")

def atualizar_produto():
    while True:
        nome = input("Digite o nome do produto que você deseja atualizar: ").strip()

        if nome not in estoque:
            print(f'❌ Não encontramos esse produto em estoque. Tente com outro produto!')
            continue
        
        try:
            preco = float(input("Novo preço do produto: "))
            quantidade = int(input("Nova quantidade em estoque: "))

            if preco < 0 or quantidade < 0:
                print("❌ Preço e quantidade devem ser números positivos.")
                continue
            
            estoque[nome]["preco"] = preco
            estoque[nome]["quantidade"] = quantidade
            print(f'✅ Produto {nome} atualizado com sucesso!')
            return

        except ValueError:
            print("❌ Erro! Insira valores numéricos válidos")
    
def excluir_produto():
    nome = input("Digite o nome do produto que deseja excluir: ").strip()
    if nome in estoque:
        del estoque[nome]
        print(f'✅ Produto {nome} exlcuído com sucesso!')
    else:
        print(f'❌ Produto não localizado!')
        return

def visualizar_estoque():
    if not estoque:
        print("\n📭 Estoque vazio!")
    else:
        print("\n📦 Estoque Atual:")
        print("-" * 100)
        for nome, info in estoque.items():
            print(f'🛒 Produto: {nome} | Preço: R${info['preco']:.2f} | Quantidade: {info['quantidade']}')
        print("-" * 100)

def menu():
    while True:
        print("\n=== 🛍️ MENU - CONTROLE DE ESTOQUE ===")
        print("1️⃣ Adicionar Produto")
        print("2️⃣ Atualizar Produto")
        print("3️⃣ Excluir Produto")
        print("4️⃣ Visualizar Estoque")
        print("5️⃣ Sair")
        opcao = input("🔵 Escolha uma opção: ")
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            atualizar_produto()
        elif opcao == "3":
            excluir_produto()
        elif opcao == "4":
            visualizar_estoque()
        elif opcao == "5":
            print("👋 Saindo... Até mais!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

menu()