pontos = 0
questão = 1
while questão <= 3:
    resposta = input(f"Resposta da questão {questão}: ")
    if questão == 1 and resposta.lower() == "b":
        pontos = pontos + 1
    if questão == 2 and resposta.lower() == "a":
        pontos = pontos + 1
    if questão == 3 and resposta.lower() == "d":
        pontos = pontos + 1
    questão = questão + 1
print(f'O aluno fez {pontos} ponto(s)')
