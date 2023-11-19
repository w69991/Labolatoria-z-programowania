wysokosc = int(input("Podaj wysokosc choinki: "))

for gwiazdka in range(1, wysokosc+1):
    print((gwiazdka) * "* ")

for i in range(1, wysokosc+1):
    gwiazdka = "* " * i
    spacja = " " * (wysokosc - i)
    print(spacja + gwiazdka)
