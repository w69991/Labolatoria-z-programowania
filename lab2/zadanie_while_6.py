print("Obliczanie srednia ocen studentow")

suma = 0
x = 1
while x > 0:
    suma = suma + int(input(f"Liczba punktow studenta {x}: "))
    if suma > 100:
        break
    else:
        srednia = suma / x
        x += 1
        continue
print(f"Srednia studentow jest rowna {srednia}")
