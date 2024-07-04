'''
# Dada uma lista de temperaturas imprima a menor e a maior temperatura
'''

T = [-10, -8, 0, -1, 2, 5, -2, -4]
maximo = T[0] 
minimo = T[0]
soma = 0 #acumulador

for e in T:
    if e > maximo:
        maximo = e
    if e < minimo:
        minimo = e
    soma += e

media = soma / len(T)
print(f'A temperatura media foi de: {media:.2f} °C')
print(f'A temperatura mais alta é: {maximo} °C')
print(f'A temperatura mais baixa é: {minimo} °C')
