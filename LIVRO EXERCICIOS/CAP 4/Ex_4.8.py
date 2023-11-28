num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))

operacao = str(input('Qual operação deseja fazer?'))

if operacao.lower() == ('soma'):
    print(f'O resultado da soma é: {num1 + num2}')
elif operacao.lower() == ('subtracao'):
    print(f'O resultado da soma é: {num1 - num2}')
elif operacao.lower() == ('multiplicacao'):
    print(f'O resultado da soma é: {num1 * num2}')
elif operacao.lower() == ('divisao'):
    print(f'O resultado da soma é: {num1 / num2}')
else:
    print('Tente digitar novamente a operação sem caracteres especiais. \nEx: (~, ç, etc)')
