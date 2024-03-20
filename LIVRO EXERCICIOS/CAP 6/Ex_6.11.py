# Ex 6.11 - Modificar o prog 6.6 utilizando o for e explicar o motivo de nao conseguir usar o 
#for no lugar de alguns while.

L = []

while True:
    n = int(input('Digite um número (0 p/ sair): '))
    if n == 0:
        break
    L.append(n)

for x in L:
    print(x)

'''
Não se pode usar o for quando não se sabe o numero total de repetições no inicio.
'''