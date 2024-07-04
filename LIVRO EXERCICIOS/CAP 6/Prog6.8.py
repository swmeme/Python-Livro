#Programa 6.8 - Pilha de pratos

prato = 5
pilha = list(range(1, prato + 1))

while True:
    print(f'\nExistem {len(pilha)} pratos na pilha')
    print(f'Pilha atual: {pilha}')
    print('Digite E para empilhar um novo prato. \nou D para desempilhar. S para sair.')
    
    op = input('Operação (E, D ou S)')
    if op.lower() == 'd':
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f'Prato {lavado} lavado.')
        else:
            print('Pilha vazia! BLEBLKELEB')
    elif op.lower() == 'e':
        prato += 1
        pilha.append(prato)
    elif op.lower() == 's':
        break
    else:
        print('Operação inválida! Digite apenas E, D ou S!')
