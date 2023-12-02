n = int(input('Insira o número: '))

if n < 0:
    print("Número inválido. Digite apenas valores positivos")

elif n == 0 or n == 1:
    print("0 e 1 não são primos.")

else:
    if n == 2:
        print("2 é o único primo par")
    elif n % 2 == 0:
        print(f"{n} não é primo, pois 2 é o único número par primo.")
    else:
        x = 3
        while(x < n):
            if n % x == 0:
                break
            print(x)
            x = x + 2

        if x == n:
            print(f"{n} é primo")
        else:
            print(f"{n} não é primo, pois é divisível por {x}")