'''
programa que calcula a média dos 5 primeiros números
digitados pelo usuário, para estudo de acumuladores:
'''

x = 1
soma = 0
while x <= 5:
    n = int(input(f'{x}. Digite o número: '))
    soma = soma + n #acumulador
    x = x + 1 #contador
print(f'Média: {soma / 5:5.2f}')
