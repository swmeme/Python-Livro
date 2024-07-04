'''
# Programa 6.13 - Controle da utilização das salas de cinema.
**************************************************************
'''
# Aqui a temos as salas 1, 2, 3, 4 e 5 com as seguintes vagas respectivamente:
lugares_vagos =  [10, 2, 1, 3, 0]
'''
# 1: Enquanto o usuario não digitar 0 o programa ira pedir o numero da sala
# 2: Se o numero da sala for maior que a quantidade de itens na lista de vagas por sala print 
sala inválida
# 3: Se a sala indicada pelo usuario conter o valor zero print sala lotada
# 4: Os casos restantes quando validados pede ao usuario quantas vagas ele deseja da sala 
solicitada 
# 5: Se os lugares solicitados pelo usuario forem maiores que o numero de lugares vagos da lista
print numero maior que a qtd de vagas blablabla...
# 6: '''
while True:
    sala = int(input('Sala (0 sai): ')) #1
    if sala == 0:
        print('Fim!')
        break
    if sala > len(lugares_vagos): #2
        print('Sala Inválida!')
    elif lugares_vagos[sala - 1] == 0: #2
        print('Sala lotada!')
    else: #4
        lugares = int(input(f'Quantos lugares vc deseja? ({lugares_vagos[sala - 1]} vagos)'))
        
        if lugares > lugares_vagos[sala - 1]: #5
            print('Número maior que a quantidade de vagas disponiveis.')
        elif lugares < 0:
            print('Número invalido!')
        else:
            lugares_vagos[sala - 1] -= lugares

print('*'*30)
print('Utilização da sala: ')
for x, l in enumerate(lugares_vagos):
    print(f'Sala {x + 1} - {l} lugar(es) vazio(s)')
