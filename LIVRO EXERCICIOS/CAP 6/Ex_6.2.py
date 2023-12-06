lista_1 = [] #1 define a primeira lista como uma lista vazia
lista_2 = [] #2 define a segunda lista como uma lista vazia

while True: #3 inicia o loop para preenchimento da lista, aqui precisamos criar o nome da variavel que se tornará os itens dentro da lista
    e = int(input('Digite um valor para a primeira lista (0 p/ sair): '))
    if e == 0:
        break
    lista_1.append(e) #4 este loop vai inserir um numero na lista até digitarmos 0

while True:
    e = int(input('Digite um valor para a segunda lista (0 p/ sair): '))
    if e == 0:
        break
    lista_2.append(e) #5 estamos simplesmente fazendo a mesma coisa que o loop anterior, só que pra segunda lista


lista_3 = lista_1[:] #6 criamos a variavel lista_3 sendo uma cópia da lista 1
lista_3.extend(lista_2) #7 aqui utilizamos o método extend pois estamos adicionando uma lista a outra, e se usássemos o método append este crearia um item na lista_3 no formato da lista a ser adicionada, no caso a lista_2

x = 0 #8 aqui teremos o nosso contador/indice para a lista_3
while x < len(lista_3):
    print(f'{x}: {lista_3[x]}') #9 aqui vai imprimir todos os itens da lista_3 informando o indice
    x += 1
