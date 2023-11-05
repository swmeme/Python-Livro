while True:
    print('''
Menu
-------------
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair

-------------''')
    opcao = int(input('Insira a operação que deseja realizar: '))
    if opcao == 5:
        break
    elif opcao >= 1 and opcao < 5:
        num = int(input('Insira com qual numero deseja realizar a operação: '))
        x = 1
        while x <= 10:
            if opcao == 1:
                print(f'{num} + {x} = {num + x}')
            elif opcao == 2:
                print(f'{num} - {x} = {num - x}')
            elif opcao == 3:
                print(f'{num} * {x} = {num * x}')
            elif opcao == 4:
                print(f'{num} / {x} = {num / x:.2f}')
            x = x + 1
    else:
        print('Opção inválida!')

