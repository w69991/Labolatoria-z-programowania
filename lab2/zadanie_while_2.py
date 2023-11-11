print("Obliczanie wartosci funkcji y=2*x*2-5x-8, dla x = [-4,4] co 0,5 kroku")

poczatek = -4
koniec = 4
krok = 0.5

x = poczatek
while x <= koniec:
    y = 2*x**2-5*x-8
    print(f"f({x} = {y})")
    x += krok
