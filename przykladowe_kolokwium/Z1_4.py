i = 0
while True:
    print(f"Znaków różnych od a lub b: {i}")
    a = input("Podaj znak: ")
    if a == "a" or a == 'b':
        continue
    else:
        i+=1
        continue

