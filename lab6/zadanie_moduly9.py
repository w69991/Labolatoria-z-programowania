import random
print("Zgadnij numer z podanego przez siebie przedziału (3 próby)")
a = int(input("Podaj początek przdziału numeru: "))
b = int(input("Podaj koniec przedziału numeru: "))

if b-a > 1:
    numer = random.randint(a, b)
    ilosc_prob = 3
    while ilosc_prob > 0:
            twoja_liczba = int(input("Zgadnij liczbę: "))
            if twoja_liczba < numer:
                print("Za mała liczba!")
            elif twoja_liczba > numer:
                print("Za duża liczba!")
            else:
                print(f"Gratulacje! Zgadłeś liczbę {numer}.")
                break
            ilosc_prob -= 1
            if ilosc_prob > 0:
                print(f"Pozostało Ci {ilosc_prob} prób.")
            else:
                print(f"Koniec gry! Szukana liczba to {numer}.")
                break
else:
    print("Za mały lub niewłaściwy przedział")