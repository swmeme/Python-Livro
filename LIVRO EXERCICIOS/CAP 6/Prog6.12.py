'''
Aqui não tem muito o que falar não, é um algoritmo simples pra percorrer uma lista e separar em
duas novas listas os numeros pares e os impares
'''
L = [7, 5, 8, 2, 27, 42, 50, 1, 2, 3, 56]
par = []
impar = []

for e in L:
    if e % 2 == 0:
        par.append(e)
    else:
        impar.append(e)
    
print('Pares: ', par)
print('Impares: ', impar)
