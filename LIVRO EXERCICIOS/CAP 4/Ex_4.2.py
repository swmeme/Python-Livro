velo = int(input('Insira a velocidade do carro: '))

if velo > 80:
    exces = float((velo - 80) * 5)
    print(f'Você foi multado, e o valor da multa é R$ {exces:.2f}')

if velo <= 80:
    print('Parabéns você não foi multado!')
