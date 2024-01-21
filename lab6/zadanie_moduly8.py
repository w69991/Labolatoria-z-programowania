import math

a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
kat = int(input("Podaj kąt ostry między bokami a i b: "))


if a > 0 and b > 0:
    if 90 > kat > 0:
        kat_rad = math.radians(kat)
        pole_trojkata = 0.5 * a * b * math.sin(kat_rad)
        print(f"Pole trójkąta wynosi {pole_trojkata}")
    else:
        print("Podałeś niewłaściwy kąt")
else:
    print("Podałeś niewłaściwą długość boku")
