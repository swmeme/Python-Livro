# Programa 6.1 -  calculo de media

notas = [6, 7, 5, 8, 9,]
soma = 0 # acumulador da soma
x = 0 #indice que vai percorrer os itens da lista
while x < len(notas):
    soma += notas[x]
    x += 1
print(f'Média: {soma / x:.2f}')
