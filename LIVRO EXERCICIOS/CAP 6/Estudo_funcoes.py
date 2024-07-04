'''
# Podemos percorrer listas facilmente com a função loop for, exemplo:
'''
lista = [8, 9, 15]
contador = 0

while contador < len(lista):
    item = lista[contador]
    print(item)
    contador += 1

print()
'''
# veja agora o mesmo algoritmo usando o loop for:
'''
for item in lista:
    print(item)

print()
'''
# Normalmente vamos usar o for quando quisermos processar elementos de uma lista um a um.
  O loop while é indicado para quando não sabemos quantas vezes a condição irá se repetir, ou
  quando manipulamos os índices de forma não sequencial.
'''
'''
# Função Range
  
  A função range retorna um generator, uma função para imprimir uma sequencia de 0 a 9 seria:
'''
for item in range(10):
    print(item)

print()
'''
# Podemos também informar onde vamos iniciar a sequencia, como tambem a frequencia como se fosse
um salto, por exemplo:
'''
# for item in range(3, 33, 3):
    # print(item, end=' ') (esta comentado senao interfere no resultado abaixo)


'''
# No exemplo acima o algoritmo imprimiu iniciando no número 3 até 30 de 3 em 3.
  Existe outra função chamada enumerate onde podemos aumentar a funcionalidade do loop for,
  caso queiramos imprimir uma lista onde teremos o indice também presente:
'''
contador2 = 0
for item in lista:
    print(f'[{contador2}] {item}')
    contador += 1
print()
'''
# Com enumerate ficaria assim: 
'''
for indice, item in enumerate(lista):
    print(f'[{indice + 1}] {item}')