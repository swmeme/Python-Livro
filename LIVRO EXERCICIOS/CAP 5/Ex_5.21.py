
while True:
    valor = int(input('Digite o valor a pagar: '))
    cedulas = 0 #contador
    atual = 50 #valor atual da maior cédula
    apagar = valor #atrelando o valor a pagar ao valor inserido pelo usuário
    while True:
        if atual <= apagar: #se a cedula atual for menor ou igual ao valor a pagar:
            apagar -= atual #digo que a variável a pagar será igual a ela subtraida da cedula atual
            cedulas += 1 # somo uma cédula
        else:
            print(f'{cedulas} de R${atual}')
            if apagar == 0:
                break
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
            cedulas = 0

