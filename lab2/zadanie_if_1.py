print("Automatyczny cennik biletowy")

wiek = int(input("Podaj swoj wiek: "))

if wiek < 0:
    print("Podałeś niewlasciwy wiek!")
elif wiek < 4:
    print("Wstep bezplatny")
elif wiek <= 18:
    print("Bilet kosztuje 10 zl")
else:
    print("Bilet kosztuje 20 zl")