print("Wypisywanie wszystkich liczb parzystych miedzy podanymi liczbami")

a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))
if a >= b:
    x = b
    y = a
elif b > a:
    x = a
    y = b

if y > x:
    while y >= x:
        if x % 2 == 0:
            print(x)
            x += 1
            continue
        else:
            x += 1
            continue

else:
    print("Nie mozna odliczyc")
