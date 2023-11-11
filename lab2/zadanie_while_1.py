print("Wypisywanie wszystkich liczb miedzy podanymi liczbami")

a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))

if a > b:
    while a >= b:
        print(b)
        b += 1
    print("Koniec")
elif b > a:
    while b >= a:
        print(a)
        a += 1
    print("Koniec")
else:
    print("Nie mozna odliczyc")
