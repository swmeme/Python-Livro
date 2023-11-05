tipo_instalacao = str(input('Qual seu tipo de instalação? \n(R: Residencial; I: Industrial; C: Comercial) '))
faixa_consumo = int(input('Qual sua faixa de consumo em kWh? '))

if tipo_instalacao.upper() == 'R':
    if faixa_consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo_instalacao.upper() == 'C':
    if faixa_consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo_instalacao.upper() == 'I':
    if faixa_consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    print('Tipo de instalação inválida')
print(f'O valor total a pagar é de: R$ {(preco * faixa_consumo):.2f}')
