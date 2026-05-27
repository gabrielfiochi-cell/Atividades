produtos = []

# 1. CREATE (Adicionar)

def adicionar_produto(nome):
    produtos.append(nome)
    print(f" Produto '{nome}' adicionado com sucesso!")


# 2. READ (Listar)

def listar_produtos():
    if not produtos:
        print("A lista de produtos está vazia.")
        return

    print("\n--- LISTA DE PRODUTOS ---")
    for i, nome in enumerate(produtos, start=1):
        print(f"{i}. {nome}")
    print("-------------------------")

# 3. UPDATE (Atualizar)

def atualizar_produto(nome_antigo, nome_novo):
    if nome_antigo in produtos:
        # Descobre a posição (índice) da primeira ocorrência do produto
        indice = produtos.index(nome_antigo)
        produtos[indice] = nome_novo
        print(f" Produto '{nome_antigo}' atualizado para '{nome_novo}'!")
    else:
        print(f" Erro: Produto '{nome_antigo}' não encontrado.")

# 4. DELETE (Deletar)

def deletar_produto(nome):
    if nome in produtos:
        produtos.remove(nome)
        print(f" Produto '{nome}' removido com sucesso!")
    else:
        print(f" Erro: Produto '{nome}' não encontrado.")

# PROGRAMA PRINCIPAL 
 
while True:
    print("\n===== MENU =====")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("4 - Deletar produto")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        adicionar_produto(nome)

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        nome_antigo = input("Digite o nome do produto que deseja atualizar: ")
        nome_novo = input("Digite o novo nome do produto: ")
        atualizar_produto(nome_antigo, nome_novo)

    elif opcao == "4":
        nome = input("Digite o nome do produto que deseja deletar: ")
        deletar_produto(nome)

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
