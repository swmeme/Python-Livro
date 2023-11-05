preco = 0
soma = 0
quantidade = 0
while True:
    codigo = int(input('Insira o código do produto: '))
    soma = soma + preco
    if codigo == 0:
        break
    quantidade += 1
    if codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1
    elif codigo == 3:
        preco = 4
    elif codigo == 5:
        preco = 7
        
    elif codigo == 9:
        preco = 8
        
    else:
        print('Código inválido')
soma = soma + preco
print(f'A quantidade de produtos foi: {quantidade} \n'
    f'Num total de R$ {soma:.2f}')
