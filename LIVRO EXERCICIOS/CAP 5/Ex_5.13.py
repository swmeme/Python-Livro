divida = float(input('Qual o valor inicial da dívida? '))
juros = float(input('Qual o valor do juro? ')) / 100
mes = 1
amort = float(input('Qual o valor a amortizar? '))
if (divida * juros > amort):
    print('Sua dívida jamais será paga pois os juros sao superiores ao pagamento mensal')
else:
    saldo = divida
    juros_pago = 0
    while saldo > amort:
        tx = saldo * juros
        saldo = saldo + tx - amort #acumulador
        juros_pago = juros_pago + tx #acumulador
        print(f'Saldo da dívida no mes {mes} é de R${saldo:.2f}')
        mes += 1 #contador
    print(f'Para pagar uma dívida de R$ {divida:.2f}, a {(juros*100):.2f}% '
          'de juros ao mes, serao necessários: \n'
          f'{mes - 1} meses, pagando um total de R${juros_pago:.2f} de juros.\n'
          f'No ultimo mes voce tera um saldo residual de R$ {saldo:.2f} a pagar.')
