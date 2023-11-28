valor_casa = float(input('Insira o valor da casa: R$ '))
salario = float(input('Qual o valor da sua renda mensal? '))
anos = int(input('Em quantos anos deseja quitar o valor da casa? '))
meses = anos * 12
parcela = float(valor_casa / meses)

if parcela > 0.3 * salario:
    print(f'Infelizmente o valor da parcela é R$ {parcela} e é superior a 30% do seu salário. \nPor este motivo não aprovamos seu crédito.')
else:
    print(f'Parabéns, sua renda é compativel e o financiamento ficará com uma parcela de R$ {parcela:.2f} \nEnviaremos uma lista com a documentação necessária.')

