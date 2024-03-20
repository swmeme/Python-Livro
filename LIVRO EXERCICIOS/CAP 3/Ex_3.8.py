
try:
    num = int(input('Insira um número inteiro: '))
    if num % 2 == 0:
        print(f'O numero {num:4.2f} é par')
    else:
        print(f'O numero {num:4.2f} é impar')

except:
    print('Um erro ocorreu. Insira caracteres válidos!')
