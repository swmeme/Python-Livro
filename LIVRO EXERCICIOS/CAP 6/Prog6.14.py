# Programa 6.14 - Lendo e imprimindo uma lista de compras

compras = []
while True:
    produto = input("Produto: ")
    if produto.upper() == 'FIM':
        break
    compras.append(produto)

for p in compras:
    print(p)


