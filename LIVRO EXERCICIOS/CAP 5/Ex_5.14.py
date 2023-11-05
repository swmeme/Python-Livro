soma = 0
quantidade = 0
while True:
    n = int(input('Insira o próximo número ou 0 para sair: '))
    soma = soma + n
    if n == 0:
        break
    quantidade += 1
media = soma / quantidade
print(f'A quantidade de números foi: {quantidade}.\nO total da soma é: {soma}. \nA média é {media:.2f}.')