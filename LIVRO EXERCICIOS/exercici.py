a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

if a == b or b == c:
    print('Valores iguais!')
else:
    if a > b and a > c:                # A é maior que B e C
        if b > c:                      # B está no meio e C é o menor
            print(a, b, c)
        else:                          # Nega B ser maior, logo ele é o menor e C está no meio
            print(a, c, b)

    elif b > a and b > c:              # B agora é maior que A e C
        if a > c:                      # Colocamos A no meio e C é o menor
            print(b, a, c)             
        else:                          # Naga A ser maior, logo é menor que C
            print(b, c, a)
    elif c > a and c > b:
        if a > b:
            print(c, a, b)
        else:
            print(c, b, a)

