tabuada = int(input('Insira qual tabuada deseja saber: '))
inicio = int(input('Onde deseja que comece? '))
fim = int(input('E onde deseja que termine? '))

while inicio <= fim:
    print(f'{tabuada} x {inicio} = {tabuada * inicio}')
    inicio = inicio + 1
