a = int(input('Insira o primeiro numero: '))
b = int(input('Insira o segundo numero: '))
c = int(input('Insira o terceiro numero: '))

maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

menor = a

if c < a and c < b:
    menor = c
if b < a and b < c:
    menor = c


print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')


