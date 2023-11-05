

deposito_init = float(input('Qual o valor do depósito inicial? '))
taxa = float(input('Qual a taxa de juros? ')) / 100
mes = 1
saldo = deposito_init
while mes <= 24:
    saldo = saldo + (saldo * taxa)
    print(f'Saldo do mês {mes} é de R$ {saldo:5.2f}')
    mes += 1
print(f'O ganho obtido foi de R$ {saldo - deposito_init:8.2f}.')
