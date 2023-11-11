print("Sprawdzanie czy litera jest duza czy mala")
litera = input("Wprowadz litere: ")
if litera.isupper():
    print("Wprowadzona litera jest duza")
elif litera.islower():
    print("Wprowadzona litera jest mala")
else:
    print("To nie jest litera lub jest litera specjalna")
