# Programa 5.1  - Contagem de Cédulas
valor = float(input('Digite o valor a pagar: '))
cedulas = 0 #contador
atual = 100 #valor atual da maior cédula
apagar = valor #atrelando o valor a pagar ao valor inserido pelo usuário
while True:
    if atual <= apagar: #se a cedula atual for menor ou igual ao valor a pagar:
        apagar -= atual #digo que a variável a pagar será igual a ela subtraida da cedula atual
        cedulas += 1 # somo uma cédula
    else:
        print(f'{cedulas} de R${atual: 3.2f}')
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
        elif atual == 1:
            atual = 0.5
        elif atual == 0.5:
            atual = 0.1
        elif atual == 0.1:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        cedulas = 0
