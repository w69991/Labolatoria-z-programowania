for i in range(100000):
    liczba = int(input("Podaj liczbe calkowita: "))
    if liczba >= 0:
        print(f"Pierwsiastek kwadratowy z twojej liczby {liczba} to: {liczba ** (1 / 2)}")
    else:
        break
print("Dziekujemy za skorzystanie z naszej aplikacji")