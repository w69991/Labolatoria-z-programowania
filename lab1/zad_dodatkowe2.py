print("Obliczanie pola trójkąta o podanych bokach a,b,c")

a = (int(input("Podaj bok a: ")))
b = (int(input("Podaj bok b: ")))
c = (int(input("Podaj bok c: ")))

p = (a+b+c)/2

P = (p*(p-a)*(p-b)*(p-c))**(1/2)

print(f"Pole tego trojkata wynosi: {P}")
