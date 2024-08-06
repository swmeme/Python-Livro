'''********************************************************************************************
Programa 6.6 - Adição de elementos a uma lista.

Em loop peço números ao usuário, quando o usuário tecla 0 o loop para e imprime na tela a 
lista que foi criada
********************************************************************************************'''

L = []
while True:
    n = int(input('Digite um número (0 p/ sair): '))
    if n == 0:
        break
    L.append(n)
x = 0
while x < len(L):
    print(L[x])
    x += 1

'''********************************************************************************************
No exercício 6.11 é pedido para modificarmos o programa para um loop for. aí segue a solução:
********************************************************************************************'''

for e in L:
    print(e)
