import random

start = int(input("Podaj początek zakresu: "))
end = int(input("Podaj koniec zakresu: "))

numery = tuple(random.uniform(start, end) for _ in range(10))
print(numery)
iloczyn = 1

for liczba in numery:
    iloczyn *= liczba

srednia_geo = iloczyn ** (1/10)

print(f"Średnia geometryczna wylosowanych numerów to: {round(srednia_geo, 2)}")