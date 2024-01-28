import pandas as pd
pierwszy_termin = {'Nr_albumu': [60001, 60005, 60020, 60007, 60042, 60023, 60201],
 'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Maciek', 'Paweł', 'Monika'],
 'Nazwisko': ['Jabłońska', 'Kowalski', 'Bielecka', 'Kielar', 'Szpunar', 'Kolek', 'Czerwonka'],
 'Wiek': [22, 21, 24, 23, 20, 25, 22],
 'Ocena': [4.5, 5.0, 3.5, 4.0, 2.0, 3.0, 5.0]}
df1 = pd.DataFrame(pierwszy_termin)

print(df1)
print()
#a
for row in df1.itertuples():
  if row.Ocena > 4.0:
   print(row.Imię, row.Nazwisko, row.Ocena)
#b
print()
print(df1.sort_values(['Wiek']))
print()
#c
print("Średnia wieku dla osób z 5.0: ", df1.groupby('Ocena').get_group(5.0)['Wiek'].mean())
print("Średnia wieku dla osób z 4.5: ", df1.groupby('Ocena').get_group(4.5)['Wiek'].mean())
print("Średnia wieku dla osób z 4.0: ", df1.groupby('Ocena').get_group(4.0)['Wiek'].mean())
print("Średnia wieku dla osób z 3.5: ", df1.groupby('Ocena').get_group(3.5)['Wiek'].mean())
print("Średnia wieku dla osób z 3.0: ", df1.groupby('Ocena').get_group(3.0)['Wiek'].mean())
print("Średnia wieku dla osób z 2.0: ", df1.groupby('Ocena').get_group(2.0)['Wiek'].mean())
print()

#d
poprawa = {'Nr_albumu': [60042, 60023],
 'Ocena': [4.0, 5.0]}
df2 = pd.DataFrame(poprawa)

df1.set_index('Nr_albumu', inplace=True)
df2.set_index('Nr_albumu', inplace=True)
df1.update(df2)
print(df1)
print()

#e
df1.to_csv('oceny_z_kolokwium')

#f
df = pd.read_csv('oceny_z_kolokwium')
print(df)
print()
#g
nowy_uczeń = pd.DataFrame([[60013, 'Julia', 'Bar', 21, 3.5]],
                          columns=['Nr_albumu', 'Imię', 'Nazwisko', 'Wiek', 'Ocena'])
df = pd.concat([df, nowy_uczeń], ignore_index=True) #ignore_index żeby indexy zostały zresetowane
print(df)
print()

#h
unikalne_wartości = df['Ocena'].unique()
print("Unikalne oceny to:", (unikalne_wartości))

#i
oceny_5 = df['Ocena'].value_counts().get(5.0, 0)
print("Liczba uczniów z ocenami 5.0: ", oceny_5)

#do zadania z matplotlib
df1.to_csv('poprawa')
df.set_index('Nr_albumu', inplace=True)
df.to_csv('ostateczne')
df0 = pd.DataFrame(pierwszy_termin)
df0.set_index('Nr_albumu', inplace=True)
df0.to_csv('pierwszy_termin')
