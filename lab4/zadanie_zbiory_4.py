import random
a = random.randint(3, 7)
b = random.randint(3, 7)

X = {random.randint(0, 10) for _ in range(a)}
Y = {random.randint(0, 10) for _ in range(b)}

print(X)
print(Y)
print(f"Posortowane dla przejrzystości: {sorted(X)} i {sorted(Y)}")
#a
if 5 in X:
    print("Zbiór X zawiera liczbe 5")
else:
    print("Zbiór X nie zawiera liczby 5")
#b
if X.issubset(Y):
    print("Zbiór X jest podzbiorem Y")
else:
    print("Zbiór X nie jest podzbiorem Y")
#c
if Y.issubset(X):
    print("Zbiór Y jest podzbiorem X")
else:
    print("Zbiór Y nie jest podzbiorem X")
#d
if X.issuperset(Y):
    print("Zbiór X jest nadzbiorem Y")
else:
    print("Zbiór X nie jest nadzbiorem Y")
#e
if Y.issuperset(X):
    print("Zbiór Y jest nadzbiorem X")
else:
    print("Zbiór Y nie jest nadzbiorem X")
#f
suma_zbiorow = X.union(Y)
print(f"Suma zbiorów X i Y: {suma_zbiorow}")

#g
roznica_X_Y = X.difference(Y)
print(f"Różnica zbiorów X i Y: {roznica_X_Y}")

#h
roznica_Y_X = Y.difference(X)
print(f"Różnica zbiorów Y i X: {roznica_Y_X}")

#i
iloczyn_zbiorow = X.intersection(Y)
print(f"Iloczyn zbiorow X i Y: {iloczyn_zbiorow}")

#j
roznica_symetryczna_zbiorow = X.symmetric_difference(Y)
print(f"Różnica symetryczna zbiorów X i Y: {roznica_symetryczna_zbiorow}")

#k
print(f"Największa wartość w zbiorze X: {max(X)} i Y: {max(Y)}")

#l
pierwszy_element_X = X.pop()
Y.add(pierwszy_element_X)
print(f"Zbiór Y: {Y}")

#m
Y.update(X)
print(f"Po przekopiowianiu wszystkich elementów z X do Y: {Y}")

#n
X.clear()
Y.clear()
print("Wyczyszczenie zbiorów X i Y")