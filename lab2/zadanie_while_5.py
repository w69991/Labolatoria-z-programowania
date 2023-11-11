print("Obliczanie srednia ocen studentow")

n = int(input("Wprowadz ilosc studentow: "))
x = 1
suma = 0
while n >= x:
    suma = suma + int(input(f"Liczba punktow studenta {x}: "))
    x += 1
srednia = suma/n
print(f"Srednia studentow jest rowna {srednia}")
