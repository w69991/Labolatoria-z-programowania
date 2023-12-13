lista_zakupow = {"papryka":6.99, "ryż":9.99, "piwo":3}
print(lista_zakupow)
suma = 0

for key in lista_zakupow:
    suma += lista_zakupow[key]
    print(key)
    print(suma)
print(suma)