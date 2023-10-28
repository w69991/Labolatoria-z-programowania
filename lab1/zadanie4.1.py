import random
print("Liczenie zuzycia i kosztow na przypadkowej dlugosci drogi")

x = (float(input("Podaj srednie spalanie paliwa w litrach na 100km: ")))

d = random.randint(1, 100000)
zuzycie = d/100*x

print(f"Przewidywane zużycie paliwa na drodze {d} km to: {round(zuzycie, 2)} l")

koszt = zuzycie*6.5

print(f"Przewidywany koszt podrozy na {d} km to: {round(koszt, 2)} zl")
