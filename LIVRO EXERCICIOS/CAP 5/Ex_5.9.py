num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
x = num1  
quo = 0   #contador

while x >= num2:
    x -= num2
    quo = quo + 1
resto = x

print(f'{num1} x {num2} = {x}')