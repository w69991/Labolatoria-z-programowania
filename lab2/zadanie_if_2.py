print("Kalkulator dla dwoch wybranych liczb")

a = (float(input("Podaj pierwsza liczbe: ")))
b = (float(input("Podaj druga liczbe: ")))

print("Jaka operacje chcesz wykonac: ")
print("1. Dodawanie \n2. Odejmowanie \n3. Mnozenie \n4. Dzielenie")

x = int(input("Twoj wybor: "))

if x == 1:
    print(f"Wynik dodawania podanych liczb: {a+b}")
elif x == 2:
    print(f"Wynik odejmowania podanych liczb: {a-b}")
elif x == 3:
    print(f"Wynik mnozenia podanych liczb: {a*b}")
elif x == 4:
    print(f"Wynik dzielenia podanych liczb: {a/b}")
else:
    print("Podano nieprawidlowy numer dzialania")
