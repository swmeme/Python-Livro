# Programa 6.22 - Exemplo de dicionário com estoque e operações de venda

estoque = {'TOMATE': [1000, 2.30],
           'ALFACE': [ 500, 0.45],
           'BATATA': [2001, 1.20],
           'FEIJAO': [ 100, 1.50]}
venda = [['TOMATE', 5], ['BATATA', 10], ['ALFACE', 5]]
total = 0
print('Vendas\n')
for operacao in venda:
    produto, quantidade = operacao
    preço = estoque[produto][1]
    custo = preço * quantidade
    print(f'{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}')
    estoque[produto][0] -= quantidade
    total += custo
print(f' Custo total: R$ {total:15.2f}\n')
print('Estoque: \n')
for key, data in estoque.items():
    print('Produto: ', key)
    print('Quantidade: ', data[0])
    print(f'Preço: R$ {data[1]:6.2f}')