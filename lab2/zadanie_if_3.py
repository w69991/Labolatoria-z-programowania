print("Obliczanie rownania kwadratowego ax**2 + bx + c = 0")

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = b**2 - 4*a*c
print(f"Delta wynosi: {delta}")

if delta < 0:
    print("Rownanie nie ma rozwiazan")
elif delta == 0:
    print(f"Rownanie ma rozwiazanie: {-b/2*a}")
else:
    x1 = ((-b) + (delta ** (1 / 2))) / 2 * a
    x2 = ((-b) - (delta ** (1 / 2))) / 2 * a
    print(f"Rownanie ma 2 rozwiazania: {x1} i {x2}")
