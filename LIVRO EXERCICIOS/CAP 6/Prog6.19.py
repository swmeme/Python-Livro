# Programa 6.19 - Criaçao e impressão de listas de compras


compras = [] # inicio criando uma lista vazia onde inserirei minha lista de compras
while True: # crio um loop para inserir cada item detalhadamente até que não tenha finalizado
    produto = input('Produto: ')
    if produto.lower() == 'fim':
        break
    quantidade = int(input('Quantidade: '))
    price = float(input('Preço: '))
    compras.append([produto, quantidade, price]) 
'''
Ao final do loop eu digo ao programa para inserir uma lista dentro da lista compras, essa lista 
compras vai conter em cada item, sua quantidade, seu preço respectivamente.
'''

soma = 0.0 # como quero saber o total ao final do código crio a mesma variavel

for n in compras:
    print(f'{n[0]:10s} x {n[1]:5d} {n[2]:5.2f} {n[1] * n[2]:6.2f}')
    soma += n[1] * n[2]
'''
Esse novo loop diz: Para cada item (n) em compras quero que exiba na tela o nome do produto (item na
lista compras de indice n[0]) vezes a quantidade (item n[1]), o valor unitário (item nalista compras
de indice n[2]) e o valor total por item (n[1] * n[2]) e depois acumulo esses valores na variável
soma dizendo que o total (soma) é igual a quantidade vezes o preço somado ao valor anterior do total.
Esse loop será feito pra cada item da lista compras.
'''
print(f'Total : {soma:7.2f}')
# Ao final peço que o programa me retorne o valor total das compras, que está na variável soma.