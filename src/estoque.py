import json

"""PERSISTÊNCIA DE DADOS"""
ARQUIVO_ESTOQUE = "data/estoque.json"

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
    while True:
        resposta = input(mensagem).strip().lower()

        if resposta == "s":
            return True
        
        if resposta == "n":
            print("\n⬅ Voltando ao menu...")
            return False
        
        print(f'\n❌ Opção {resposta} inválida! Digite "s" para continuar ou "n" para voltar ao menu.')

"""FUNÇÕES BÁSICAS DO SISTEMA"""
def adicionar_produto():
    while True:  
        nome = input("\n➕ Digite o nome do produto: ").strip()
        
        if not any(c.isalpha() for c in nome):
            print("❌ Nome Inválido! O produto deve conter pelo menos uma letra.")
            continue
        
        if nome in estoque:
            print("❌ Produto já cadastrado! Use a opção de atualizar para esse produto caso necessite")
            if not tentar_novamente("\n🔁 Gostaria de adicionar outro produto? (s/n) "):
                return

        try:
            preco = float(input("💲 Digite o preço do produto: "))
            quantidade = int(input("📦 Digite a quantidade em estoque: "))

            if preco < 0 or quantidade < 0:
                print("❌ Preço e quantidade devem ser valores positivos, tente novamente:\n")
                continue

            novo_id = str(max(map(int, estoque.keys()), default=0) + 1)

            estoque[novo_id] ={"nome": nome, "preco": preco, "quantidade": quantidade}
            salvar_estoque()
            print(f'✅ Produto {nome} (ID: {novo_id}) adicionado com sucesso!')

        except ValueError:
            print("❌ Erro! Insira valores numéricos para preço e quantidade!")
            continue

        if not tentar_novamente("\n🔁 Gostaria de adicionar outro produto? (s/n) "):
            return

def atualizar_produto():
    while True:
        id_produto = input("\n🔎 Digite o ID do produto que você deseja atualizar: ").strip()

        if id_produto not in estoque:
            print(f'❌ Não encontramos esse produto no estoque!')
            if not tentar_novamente("\n🔁 Deseja tentar com outro produto? (s/n) "):
                return
            continue

        try:
            if tentar_novamente("\n🖋 Deseja alterar o nome do produto? (s/n)"):
                novo_nome = input("🖋 Digite o novo nome do produto: ")
                if not any(c.isalpha() for c in novo_nome):
                    print("❌ Nome Inválido! O produto deve conter pelo menos uma letra.")
                    continue
                
                estoque[id_produto]["nome"] = novo_nome

            preco = float(input("💲 Novo preço do produto: "))
            quantidade = int(input("📦 Nova quantidade em estoque: "))

            if preco < 0 or quantidade < 0:
                print("❌ Preço e quantidade devem ser números positivos.")
                continue
            
            estoque[id_produto]["preco"] = preco
            estoque[id_produto]["quantidade"] = quantidade
            salvar_estoque()
            print(f'✅ Produto {estoque[id_produto]["nome"]} (ID: {id_produto}) atualizado com sucesso!')
            return

        except ValueError:
            print("❌ Erro! Insira valores numéricos válidos")

        if not tentar_novamente("\n🔁 Gostaria de alterar outro produto? (s/n) "):
            return
    
def excluir_produto():
    while True:    
        id_produto = input("\n☠ Digite o ID do produto que deseja excluir: ").strip()

        if id_produto in estoque:
            nome_produto = estoque[id_produto]["nome"]
            del estoque[id_produto]

            novo_estoque = {}
            for novo_id, (_, dados) in enumerate(sorted(estoque.items(), key=lambda x: int(x[0])), start=1):
                novo_estoque[str(novo_id)] = dados.copy()

            estoque.clear()
            estoque.update(novo_estoque)
            salvar_estoque()

            print(f'✅ Produto {nome_produto} (ID: {id_produto}) excluído com sucesso!\n')
            print("⬅ Voltando ao menu...")
            return

        if not tentar_novamente(f'❌ ID do produto não localizado!\n🔁 Gostaria de tentar com um outro produto? (s/n) '):
            return

def visualizar_estoque():
    if not estoque:
        print("\n📭 Estoque vazio!")
    else:
        print("\n📦 Estoque Atual:\n")
        print("-" * 100)
        print(f'{"🆔":<8} {"🛒 Produto":<20} {"💰 Valor":<15} {"📦 Quantidade"}')
        print("-" * 100)

        for id_produto, info in estoque.items():
            print(f' {id_produto:<8} {info["nome"]:<21} {info["preco"]:<16.2f} {info["quantidade"]:<10}')
            
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