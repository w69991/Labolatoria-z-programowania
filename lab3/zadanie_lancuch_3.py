print("Wybierz zadanie: ")
print("1. Imie\n2. Wiek\n3. Inicjały\n4. 5 x Łancuch\n5. Połączenie Łańcuchów\n6. Połączenie połów łańcuchów")
x = int(input("Twój wybór: "))
if x == 1:
    imie = input("Podaj swoje imie: ")
    print("Witaj " + imie)
elif x == 2:
    wiek = input("Podaj swój wiek: ")
    print("Twoj wiek to: " + wiek)
elif x == 3:
    imie = input("Podaj swoje imie: ")
    nazwisko = input("Podaj swoje nazwisko: ")
    print("Twoje inicjały to: " + imie[0] + nazwisko[0])
elif x == 4:
    lancuch = input("Podaj łańcuch: ")
    print(5*lancuch)
elif x == 5:
    lancuch1 = input("Podaj łańcuch 1: ")
    print(lancuch1)
    lancuch2 = input("Podaj łańcuch 2: ")
    print(lancuch2)
    lancuch3 = lancuch1 + lancuch2
    print(lancuch3)
elif x == 6:
    lancuch1 = input("Podaj łańcuch 1: ")
    print(lancuch1)
    lancuch2 = input("Podaj łańcuch 2: ")
    print(lancuch2)
    polowa1 = len(lancuch1)//2                    #połowa długości łańcucha
    polowa2 = len(lancuch2)//2
    lancuch3 = lancuch1[0: polowa1] + lancuch2[polowa2:]
    print(lancuch3)
else:
    print("Niepoprawny wybór!")
