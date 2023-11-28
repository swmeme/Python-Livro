distancia = int(input('Quantos km deseja percorrer? '))

if distancia <= 200:
    passagem = (0.50 * distancia)
    print(f'O valor da passagem é de R$ {passagem:.2f}')
else:
    passagem = (0.45 * distancia)
    print(f'O valor da passagem é de R$ {passagem:.2f}')

