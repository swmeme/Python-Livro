'''
Exercício 6.3: 
Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos:
***********************************************************************************************
Inicio criando as 4 listas, sendo: 
'''
#↓ duas delas as listas com os numeros inseridos pelo usuário; ↓
lista_1 = []
lista_2 = []

while True:
    item = int(input("Digite um valor para a primeira lista (0 para terminar):"))
    if item == 0:
        break
    lista_1.append(item)
while True:
    item = int(input("Digite um valor para a segunda lista (0 para terminar):"))
    if item == 0:
        break
    lista_2.append(item)

#↓ uma lista vazia (a que o algoritmo ira anexar os itens não repetidos) ↓
final = []
#↓ uma delas sendo a soma dos objetos das primeiras duas; ↓
lista_3 = lista_1[:]
lista_3.extend(lista_2)
'''
Bom, aqui inicia o trabalho, quero que seja armazenada na memoria cada item da lista conjunta, 
logo:
'''
#1crio o indice para percorrer a lista conjunta
#2depois disso inicio o loop enquanto o indice for menor ao tamanho da lista 3 faça isso:
#3Agora vamos criar o indice_da_lista_final 
#4e o loop para que a lista final percorra cada objeto na lista final.
#5se o objeto da lista conjunta for igual ao da lista final pare.
#6somo +1 ao indice_da_lista_final para continuar percorrendo a lista final.
#7Aqui é onde finalmente pego o objeto da lista conjunta e coloco na lista final
#8somo 1 pro loop while continuar percorrendo a lista conjunta.

x = 0 #1
while x < len(lista_3):#2
    y = 0 #3
    while y < len(final):#4
        if lista_3[x] == final[y]:#5
            break
        y += 1#6
    if y == len(final): #7
        final.append(lista_3[x])

    x += 1 #8
#↓ Agora crio outro loop para imprimir cada objeto/item da lista final: ↓
x = 0
while x < len(final):
    print(f"{x + 1}: {final[x]}")
    x = x + 1
'''
o pensamento é o seguinte: 
enquanto o indice da lista for menor que o tamanho da lista final faço a verificação:
o item do atual indice da lista conjunta é igual ao item do indice atual da lista final?
se sim paro
se não vou para o proximo indice da lista final
Depois disso faço a segunda verificação:
o indice da lista final está igual ao tamanho da lista final?
se sim insiro o item referente ao indice da lista conjunta
e depois sigo somando 1 ao indice da lista conjunta prosseguindo para o próximo item/indice
'''