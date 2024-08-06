# Programa 6.20 - Ordenação pelo método de Bolhas (BubbleSort)
'''
O algoritmo de ordenação pelo método de bolhas (BubbleSort)
consiste em comparar dois elementos a cada vez que é chamado.
Se o primeiro valor for maior que o segundo, eles trocarão de posição.
Essa operação é então repetida para o próximo elemento até o fim da lista.
A idéia é percorrer um conjunto de elementos diversas vezes, e a cada passagem fazer
flutuar para o topo o maior elemento da sequência. Essa movimentação lembra a forma como
as bolhas procuram seu proprio nivel num recipiente, daí o nome do algoritmo.
Como o BubbleSort percorre a lista várias vezes vamos colocar um marcador
para saber se chegamos ao fim da lista trocando ou nao algum elemento.
'''

exemplo_lista = [7,4,3,12,8]
marcador_fim = 5
'''
Inicialmente temos a lista e a variável  que determina a quantidade 
de elementos na lista,que também poderia ser substituido por len(lista)
'''
while marcador_fim > 1: # 2 Aqui iniciamos a percorrer a lista, controlando quantos passos iremos dar
    trocou = False # 3 Esta é uma flag para verificar se houve alguma troca.
    indice_contador = 0 # 4 Este é o indice que vai iterar (percorrer) sobre  a lista
    while indice_contador < (marcador_fim - 1): 
        # 5 enquanto o indice for menor que o tamanho da lista iremos:
        if exemplo_lista[indice_contador] > exemplo_lista[indice_contador + 1]: 
            # aqui acontece a comparaçao, se o item da lista no respectivo indice for maior que
            # o item sucessivo então:
            trocou = True # Marcamos que sera efetuada uma troca,
            var_temp = exemplo_lista[indice_contador] # Uma variável temporaria é criada para 
            # armazenar o indice a trocar
            exemplo_lista[indice_contador] = exemplo_lista[indice_contador + 1] # Aqui ocorre a troca
            exemplo_lista[indice_contador + 1] = var_temp # aqui a variavel temp é deixada de lado
        indice_contador += 1 # Passo para continuar a iteração
    if not trocou: #Essa parte eu achei meio redundante talvez haja explicação no futuro
        break
    marcador_fim -= 1 # e retornamos o loop

for n in exemplo_lista: 
    print(n) # Agora que os elementos na lista foram trocados é só mostrar em tela.

'''
Como programamos em pyton essa linguagem tem algumas técnicas que podem
ser utilizadas: https://docs.python.org/3/howto/sorting.html#sortinghowto
Como os exemplos abaixo:
'''
lista2 = [3,2,17,4,5,49,11,21]
# Existe a função sorted:
print(sorted(lista2))
print(lista2)
# Que não modifica a lista original e retorna uma nova lista
# E existe o método .sort() que modifica a lista original substituindo-a
lista2.sort()
print(lista2)
