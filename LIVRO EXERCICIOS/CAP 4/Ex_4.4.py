salario = float(input('Qual o valor do salario? '))

if salario > 1250:
    aumento = (0.10 * salario)
    salario = (aumento + salario)
    print(f'Parabens!!! \nVocê recebeu um aumento de 10%. \nSeu novo salário é de: R$ {salario:.2f}')
else:
    aumento = (0.15 * salario)
    salario = (aumento + salario)
    print(f'Parabéns!!!\nVocê recebeu um aumento de 15%. \nSeu novo salário é de: R$ {salario:.2f}')

