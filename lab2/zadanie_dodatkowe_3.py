print("Test logiczny")

warunek1 = input("Czy pada deszcz? tak/nie \n")
warunek2 = input("Czy jest autobus na przystanku? tak/nie \n")

if warunek1 == "tak":
    warunek1 = True
elif warunek1 == "nie":
    warunek1 = False
else:
    print("Blad")

if warunek2 == "tak":
    warunek2 = True
elif warunek2 == "nie":
    warunek2 = False
else:
    print("Blad")

if warunek1 and warunek2:
    print("Wez parasol. " + "Dostaniesz sie na uczelnie.")
elif warunek1 and not warunek2:
    print("Nie dostaniesz sie na uczelnie")
else:
    print("Dostaniesz sie na uczelnie. " + "Miłego dnia i pieknej pogody.")
