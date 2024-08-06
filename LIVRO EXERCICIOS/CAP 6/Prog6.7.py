ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f'\nExistem {len(fila)} clientes na filla')
    print(f'Fila Atual: {fila}')
    print('Digite F para adicionar um cliente ao fim da fila,\nou A para para realizar o atendimento. S para sair.')
    op = input('Operação: (F, A ou S): ')
    if op.lower() == 'a':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f'Cliente {atendido} atendido!')
        else:
            print('Fila vazia! Ninguem para atender')
    elif op.lower() == 'f':
        ultimo += 1 #incrementa o ticket do novo cliente
        fila.append(ultimo)

    elif op.lower() == 's':
        break
    else:
        print('Operação inválida!')
