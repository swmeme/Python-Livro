estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50],
}

# Função para exibir o estoque
def exibir_estoque(estoque):
    print("Estoque:\n")
    for chave, dados in estoque.items():
        print(f"Descrição: {chave.capitalize()}")
        print(f"Quantidade: {dados[0]}")
        print(f"Preço: R$ {dados[1]:6.2f}\n")

total = 0
vendas = []

# Exibir estoque inicial
exibir_estoque(estoque)


while True:
    produto = input("Nome do produto (fim para sair): ").lower()
    if produto == "fim":
        break
    if produto in estoque:
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade <= estoque[produto][0]:
                preço = estoque[produto][1]
                custo = preço * quantidade
                vendas.append([produto, quantidade, preço, custo])
                print(f"{produto.capitalize():12s}: {quantidade:3d} x R$ {preço:6.2f} = R$ {custo:6.2f}")
                estoque[produto][0] -= quantidade
                total += custo
            else:
                print("Quantidade solicitada não disponível.")
        except ValueError:
            print("Por favor, insira uma quantidade válida.")
    else:
        print("Nome de produto inválido.")

# Exibir resumo das vendas
print("\nResumo das Vendas:\n")
for venda in vendas:
    produto, quantidade, preço, custo = venda
    print(f"{produto.capitalize():12s}: {quantidade:3d} x R$ {preço:6.2f} = R$ {custo:6.2f}")

print(f"\nCusto total: R$ {total:21.2f}\n")

# Exibir estoque atualizado
exibir_estoque(estoque)