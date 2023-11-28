while True:
    materia = input('Insira a materia (ou digite s p/sair): ')
    if materia.lower == 's':
        break
    else:
        nota1 = float(input('Insira a nota do primeiro bimestre: \n'))
        nota2 = float(input('Insira a nota do segundo bimestre: \n'))
        nota3 = float(input('Insira a nota do terceiro bimestre: \n'))
        peso1 = 1
        peso2 = 2
        peso3 = 3
        notas = [nota1 * peso1, nota2 * peso2, nota3 * peso3]
        calc = sum(notas) / 10
        print(f'Sua média em {materia} atualmente é de {calc.__round__(2)} pontos\n')

    if calc < 3.0:
        falta = 0
        print(f'Sinto muito, voce está de recuperação em {materia}.\n')
    else:
        falta = ((7 - calc) / 4) * 10
        print(f'Pra passar em {materia} vc precisa ter a média do 4º bimestre igual a: {falta.__round__(2)}\n')