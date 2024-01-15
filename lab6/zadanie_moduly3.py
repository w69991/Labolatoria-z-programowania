import time

a = int(input("Podaj sekundy do odliczenia: "))

while a > 0:
    print(f"Zostało: {a} sekund")
    a -= 1
    time.sleep(1)
print("Odliczanie zakończone")