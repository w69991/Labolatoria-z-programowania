n = int(input("Ktory wyraz ciagu arytmetycznego obliczyc: "))
a = int(input("Podaj pierwszy wyraz ciagu arytmetycznego: "))
r = int(input("Podaj roznice ciagu arytmetycznego: "))

for i in range(n):
    x = a + i*r
    print(x)