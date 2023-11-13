a = int(input("Podaj liczbe lini i gwiazdek: "))

for linia in range(a):
    for gwiazdka in range(a):
        print("* ", end="")
    print()
