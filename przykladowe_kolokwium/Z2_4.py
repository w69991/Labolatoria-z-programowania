import random
x = int(input("Podaj przedział: "))
lista1 = random.sample(range(-x,x), 10)
lista2 = []
print(lista1)
for i in lista1:
    if i>=0:
        lista2.append(True)
    else:
        lista2.append(False)
print(lista2)

