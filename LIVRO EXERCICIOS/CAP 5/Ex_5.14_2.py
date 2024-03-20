#Quero um programa que leia numeros inteiros do teclado até que
#eu digite 0 para sair, depois disso exibir a quantidade de numeros digitados
#a soma e a media aritmetica desses numeros.

qtd = 0 #esse vai ser o contador dos numeros
soma = 0 #esse vai ser o acumulador dos numeros

while True:
    novo_numero = int(input('Insira um numero ou digite 0 p/ sair: '))
    soma = soma + novo_numero #pra acumular preciso avisar ao código que ele precisa juntar esses numeros
    if novo_numero == 0:
        break
    qtd += 1

media = soma/qtd

print(f'A quantidade de números foi: {qtd}. \nA soma foi {soma}. \nE a média foi: {media}')
