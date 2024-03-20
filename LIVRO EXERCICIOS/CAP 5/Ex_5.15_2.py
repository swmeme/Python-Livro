#programa de controle de maquina registradora.
#primeiramente vamos dar um alou ao usuário:
print('Olá, bem-vindo.')

#declaramos a variavel valor = 0 que vai ser atrelada ao  um produto assim que o mesmo for iserido pelo usuario
valor = float(0.0)

#depois pedimos qual produto ele deseja inserir na lista de compras dentro de um loop:
while True:
    produto = int(input('Insira o código do produto ou 0 para finalizar: '))
    if produto == 1:
        valor += 0.50
    elif produto == 2:
        valor += 1
    elif produto == 3:
        valor += 4
    elif produto == 5:
        valor += 7
    elif produto == 9:
        valor += 8
    elif produto == 0:
        break

print(f'O valor total das compras foi: R$ {valor:8.2f}')
