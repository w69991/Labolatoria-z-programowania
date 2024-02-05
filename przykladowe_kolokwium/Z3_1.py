def wypelnianie_krotki(a,b,c):
    lista1 = []
    for _ in range(a):
        lista1.append(b)
        b += c
    print(lista1)

a = int(input("Podaj liczbę elementów: "))
b = int(input("Podaj początek przedziału: "))
c = int(input("Podaj skok: "))

wypelnianie_krotki(a,b,c)