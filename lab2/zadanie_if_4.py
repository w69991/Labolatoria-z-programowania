print("Ukladanie 3 podanych liczb od najmniejszej do najwiekszej")

x = int(input("Podaj 1 liczbe: "))
y = int(input("Podaj 2 liczbe: "))
z = int(input("Podaj 3 liczbe: "))

if x >= y >= z:
    print(f"Liczby kolejno to {z}, {y}, {x}")
elif y >= z >= x:
    print(f"Liczby kolejno to {x}, {z}, {y}")
elif z >= y >= x:
    print(f"Liczby kolejno to {x}, {y}, {z}")
elif y >= x >= z:
    print(f"Liczby kolejno to {z}, {x}, {y}")
elif z >= x >= y:
    print(f"Liczby kolejno to {y}, {x}, {z}")
elif x >= z >= y:
    print(f"Liczby kolejno to {y}, {z}, {x}")
