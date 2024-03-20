#Ex 6.8 - Modificar o programa 6.9 sem utilizar a variavel 'achou'

lista = [15, 7, 27, 39]
p = int(input('Digite o valor a procurar: '))
v = int(input('Digite o segundo valor a procurar: '))

x = 0

while x < len(lista):
    if lista[x] == p:
        print(f'{p} achado na posição {x}')
        break
    x += 1
else:
    print(f'{p} não encontrado')
