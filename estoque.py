import json

"""PERSISTÊNCIA DE DADOS"""
ARQUIVO_ESTOQUE = "estoque.json"

try:
    with open(ARQUIVO_ESTOQUE, "r") as file:
        estoque = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    estoque = {}

def salvar_estoque():
    with open(ARQUIVO_ESTOQUE, "w") as file:
        json.dump(estoque, file, indent=4)


"""Permite o usuário tentar novamente"""
def tentar_novamente(mensagem):
    resposta = input(mensagem).strip().lower()
    if resposta == "s":
        return True
    else:
        print("\n⬅ Voltando ao menu...")
        return False

"""FUNÇÕES BÁSICAS DO SISTEMA"""
def adicionar_produto():
    while True:  
      nome = input("\n➕ Digite o nome do produto: ").strip()
      
      if not any(c.isalpha() for c in nome):
          print("❌ Nome Inválido! O produto deve conter pelo menos uma letra.")
          continue
      
      if nome in estoque:
          print("❌ Produto já cadastrado! Use a opção de atualizar.")
          if not tentar_novamente("\n🔁 Gostaria de adicionar outro produto? (s/n) "):
            return
      else:
        try:
            preco = float(input("💲 Digite o preço do produto: "))
            quantidade = int(input("📦 Digite a quantidade em estoque: "))

            if preco < 0 or quantidade < 0:
                print("❌ Preço e quantidade devem ser valores positivos, tente novamente:")
                continue

            estoque[nome] = {"preco": preco, "quantidade": quantidade}
            salvar_estoque()
            print(f'✅ Produto {nome} adicionado com sucesso!')

        except ValueError:
            print("❌ Erro! Insira valores numéricos para preço e quantidade!")

      if not tentar_novamente("\n🔁 Gostaria de adicionar outro produto? (s/n) "):
        return

def atualizar_produto():
    while True:
        nome = input("\n🔎 Digite o nome do produto que você deseja atualizar: ").strip()

        if nome not in estoque:
            print(f'❌ Não encontramos esse produto em estoque!')
            resposta= input("\n🔁 Deseja tentar com outro produto? (s/n) ").strip().lower()
            if resposta != "s":
                print("\n⬅ Voltando ao menu...")
                return
            continue

        else:
            try:
                preco = float(input("💲 Novo preço do produto: "))
                quantidade = int(input("📦 Nova quantidade em estoque: "))

                if preco < 0 or quantidade < 0:
                    print("❌ Preço e quantidade devem ser números positivos.")
                    continue
                
                estoque[nome]["preco"] = preco
                estoque[nome]["quantidade"] = quantidade
                salvar_estoque()
                print(f'✅ Produto {nome} atualizado com sucesso!')
                return

            except ValueError:
                print("❌ Erro! Insira valores numéricos válidos")
    
def excluir_produto():
    while True:    
        nome = input("\n☠ Digite o nome do produto que deseja excluir: ").strip()

        if nome in estoque:
            del estoque[nome]
            salvar_estoque()
            print(f'✅ Produto {nome} exlcuído com sucesso!\n')
            print("⬅ Voltando ao menu...")
            return
        
        else:
            resposta = input(f'❌ Produto não localizado!\n🔁 Gostaria de tentar com um outro produto? (s/n) ').strip().lower()
            if resposta != "s":
                print("⬅ Voltando ao menu...")
                return

def visualizar_estoque():
    if not estoque:
        print("\n📭 Estoque vazio!")
    else:
        print("\n📦 Estoque Atual:\n")
        print("-" * 100)
        for nome, info in estoque.items():
            print(f'🛒 Produto: {nome} | Preço: R${info['preco']:.2f} | Quantidade: {info['quantidade']}')
        print("-" * 100)


"""MENU VISUAL DO SISTEMA"""
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