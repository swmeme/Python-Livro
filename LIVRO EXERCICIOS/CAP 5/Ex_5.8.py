num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
x = 1 #contador
repeticao = 0

while x <= num2:
    repeticao = repeticao + num1
    x += 1

print(f'{num1} x {num2} = {repeticao}')