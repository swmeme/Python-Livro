
deposito_init = float(input('Qual o valor do depósito inicial? '))
taxa = float(input('Qual a taxa de juros? ')) / 100
mes = 1
saldo = deposito_init
while mes <= 24:
    deposito_mens = float(input('Qual o valor do depósito mensal?'))
    saldo = saldo + deposito_mens + (saldo * taxa) #acumulador
    print(f'Saldo do mês {mes} é de R$ {saldo:5.2f}')
    mes += 1 #contador
print(f'O ganho obtido foi de R$ {saldo - deposito_init:8.2f}.')

