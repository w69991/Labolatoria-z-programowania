print("Wyznaczanie wartosci 3 funkcji dla argumentow rzeczywistych")

x = float(input("Wprowadz argument x: "))

if x > 0:
    a = 2*x
elif x == 0:
    a = 0
else:
    a = -3*x
print(f"a(x) = {a}")

if x >= 1:
    b = x**2
else:
    b = x
print(f"b(x) = {b}")

if x > 2:
    c = 2+x
elif x == 2:
    c = 8
else:
    c = x - 4
print(f"c(x) = {c}")
