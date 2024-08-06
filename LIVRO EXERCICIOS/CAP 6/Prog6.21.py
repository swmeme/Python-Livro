# Programa 6.21 - Obtenção do preço com um dicionário
'''
Este programa utiliza dicionários para exibir o preço de um produto
'''


tabela = {'Alface': 0.45,
          'Batata': 1.20,
          'Tomate': 2.30,
          'Feijão': 1.50}
while True:
    produto = input('Digite o nome do produto, fim para terminar: ')
    if produto.lower() == 'fim':
        break
    elif produto.capitalize() in tabela:
        print(f'Preço R$ {tabela[produto.capitalize()]:5.2f}')
    else:
        print('Produto não encontrado!')

