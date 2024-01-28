import matplotlib.pyplot as plt
import pandas as pd
#1
kategorie = ['Odzież', 'Elektronika', 'Książki', 'Sprzęt_sportowy']
ilosc_sprzedanych = [320, 260, 145, 290]

plt.bar(kategorie, ilosc_sprzedanych, color='green')

plt.title('Ilość sprzedanych produktów w różnych kategoriach')
plt.xlabel('Kategoria')
plt.ylabel('Ilość sprzedanych')

plt.show()

#2
plt.pie(ilosc_sprzedanych, labels=kategorie,
autopct='%1.f%%', startangle=90,
colors=['blue', 'green',
'red', 'yellow'])
plt.title('Udział w kategoriach')

plt.show()

#3
czas = [0, 1, 2, 3, 4, 5, 6, 7, 8]
predkosc = [0, 15, 25, 30, 20, 40, 60, 80, 70]

plt.scatter(czas, predkosc, color='lightblue')

plt.title('Prędkość chwilowa pojazdu')
plt.xlabel('Czas [s]')
plt.ylabel('Prędkość [km/h]')

plt.show()

#4
oceny = pd.read_csv('ostateczne')
print(oceny)

plt.hist(oceny['Ocena'], bins=5, color='purple', edgecolor='black')
plt.title('Rozkład ocen')
plt.xlabel('Ocena')
plt.ylabel('Liczba wystąpień')

plt.show()

#5
termin_1 = pd.read_csv('pierwszy_termin')
termin_2 = pd.read_csv('poprawa')

plt.figure(figsize=(10, 5))
plt.plot(termin_1['Imię'], termin_1['Ocena'], marker='o', linestyle='-', color='blue', label='Termin 1')
plt.plot(termin_2['Imię'], termin_2['Ocena'], marker='s', linestyle='--', color='green', label='Termin 2')
plt.title('Oceny z poszczególnych terminów')
plt.xlabel('Imię')
plt.ylabel('Ocena')
plt.legend()

plt.show()
