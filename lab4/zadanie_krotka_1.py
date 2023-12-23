import random
import string
n = int(input("Podaj liczbę elementów listy: "))
x = int(input("Podaj długość ciągów znakowych: "))
lista_ciagow = [''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, x))) for _ in range(n)] #generowanie listy z n wyrazami z x znakami

krotka_ciagow = tuple(lista_ciagow)
print(krotka_ciagow)
#a
suma_wyrazow = sum(len(ciag) for ciag in krotka_ciagow)
print(f"Ilość znaków w liście: {suma_wyrazow}")
#b
ilosc_k = sum(ciag.count('k') for ciag in krotka_ciagow) #liczenie liter k
print(f"Ilość liter 'k' w liście: {ilosc_k}")
#c
ilosc_kt = sum(ciag.count('kt') for ciag in krotka_ciagow)
print(f"Ilość ciągów 'kt' w liście: {ilosc_kt}")
#d
s = int(input("Ilość ciągów dłuższych niż (podaj długość): "))
wieksze_od_s = sum(1 for ciag in krotka_ciagow if len(ciag) > s) #wyrazy większe od s
print(f"Ilość ciągów dłuższych niż {s}: {wieksze_od_s}")