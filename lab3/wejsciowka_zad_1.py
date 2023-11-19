a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
iloczyn = 1
if a > b:
    x = a
    y = b
elif b > a:
    x = b
    y = a

while x >= y:
    iloczyn = iloczyn * y
    y += 1
print(f"Iloczyn jest równy {iloczyn}")