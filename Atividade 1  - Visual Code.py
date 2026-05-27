def poupanca(valor):
    taxa = 0.07
    resultado = valor + (valor * taxa)
    return resultado

def tesouro_direto(valor):
    taxa = 0.12
    resultado = valor + (valor * taxa)
    return resultado

opcao = input(
    "Investimentos Disponíveis: \n"
    "poupanca \n"
    "tesouro \n"
    "Digite o investimento desejado: "
)

match(opcao):
    
    case "poupanca":
        valor = float(input("Digite o valor que deseja investir: R$ "))
        rendimento = poupanca(valor)
        print("Após 1 ano, seu dinheiro na Poupança será: R$", rendimento)
    case "tesouro":
        valor = float(input("Digite o valor que deseja investir: R$ "))
        rendimento = tesouro_direto(valor)
        print("Após 1 ano, seu dinheiro no Tesouro Direto será: R$", rendimento)
    case _:
        print("Opção inválida!")
        