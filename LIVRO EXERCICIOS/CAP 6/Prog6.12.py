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
