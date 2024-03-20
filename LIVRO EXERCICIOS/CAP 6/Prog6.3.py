#Programa 6.3 - Apresentação de números

num = [0] * 5
x = 0
while x < 5:
    num[x] = int(input(f"Número {x + 1}: "))
    x += 1
while True:
    escolhido = int(input('Qual posição vc quer imprimir (0 para sair):'))
    if escolhido == 0:
        break
    print(f'Voce escolheu o numero: {num[escolhido - 1]}')
