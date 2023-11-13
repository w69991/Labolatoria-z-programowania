print("Wypisywanie liczb")

print("Wybierz co chcesz wyswietlic:")
print("1. 1 -> 100\n2. 100 -> 0\n3. 7 -> 77 z krokiem co 7\n4. 20 -> 0 z krokiem co 2")
x = int(input("Twoj wybor: "))
if x == 1:
    for i in range(1, 101):
        print(i)
elif x == 2:
    for i in range(100, 0, -1):
        print(i)
elif x == 3:
    for i in range(7, 84, 7):
        print(i)
elif x == 4:
    for i in range(20, -2, -2):
        print(i)
else:
    print("Niewlasciwy wybor!")