'''
Exercício 6.17 - A partir do programa 6.22, solicitar ao usuário o produto e 
a quantidade vendida. Verificar se o produto digitado existe no dicionário.
'''

estoque = {
    'TOMATE': [1000, 2.30],
    'ALFACE': [ 500, 0.45],
    'BATATA': [2001, 1.20],
    'FEIJAO': [ 100, 1.50]
    }

# Função para exibir o estoque
def exibir_estoque(estoque):
    print('Estoque Atualizado:\n')
    for key, data in estoque.items():
        print('Produto: ', key, '\n')
        print('Quantidade: ', data[0])
        print(f'Preço: R$ {data[1]:6.2f}', 2 * '\n')

total = 0
vendas = []

# Exibir estoque inicial
exibir_estoque(estoque)

print("Vendas:\n")
while True:
    produto = input('Selecione qual o produto, fim para terminar: ').upper()
    if produto == 'FIM':
        break
    if produto in estoque:
        try:
            venda = int(input('Quantos vendidos? '))
            if venda <= estoque[produto][0]:
                preço = estoque[produto][1]
                custo = preço * venda
                vendas.append([produto, venda, preço, custo])
                print(f'{produto.capitalize():12s}: {venda:3d} x R$ {preço:6.2f} = R$ {custo:6.2f}')
                estoque[produto][0] -= venda
                total += custo
            else:
                print('Quantidade vendida excede o estoque disponível.')
        except ValueError:
            print('Por favor, insira uma quantidade válida.')
    else:
        print('Produto não encontrado!')   

print('\nVendas\n')
for operacao in vendas:
    produto, quantidade, preço, custo = operacao
    print(f'{produto.capitalize():12s}: {venda:3d} x R$ {preço:6.2f} = R$ {custo:6.2f}')

print(f'\n   Custo total: R$ {total:15.2f}\n')

exibir_estoque(estoque)