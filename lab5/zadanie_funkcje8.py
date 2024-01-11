def obliczanie_potegi(liczba, potega):
    if potega == 0:
        return 1
    elif potega < 0:
        return 1 / obliczanie_potegi(liczba, -potega)
    else:
        return liczba * obliczanie_potegi(liczba, potega - 1)


liczba = float(input("Podaj liczbę: "))
potega = float(input("Podaj potęge: "))
wynik = obliczanie_potegi(liczba, potega)
print(f"Wynik potęgowania {liczba} do potęgi {potega}, to {wynik}")
