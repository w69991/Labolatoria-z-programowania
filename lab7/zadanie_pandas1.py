import pandas as pd
data = {'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz'],
 'Wiek': [22, 21, 24, 23],
 'Ocena': [4.5, 5.0, 3.5, 4.0]}
df = pd.DataFrame(data)
print(df)
#a
for row in df.itertuples():
  if row.Ocena > 4.0:
   print(row.Imię, row.Ocena)
#b
print(df.sort_values)
#c
print(df.groupby('Ocena').get_group(5.0))
print(df.groupby('Ocena')['Wiek'].min())

#ROZSZERZ TĄ FUNKCJE ADAS PROSZE W DOMU JAK TO PRZECZYTASZ NR ALBUMU I EWENTUALNE NAZWISKO (WIĘCEJ OSÓB MA BYĆ)


df_pop = {'Imię': ['Katarzyna', 'Aleksander'],
 'Ocena': [3.5, 4.0]}
print(df_pop['Ocena'])
print(pd.merge df_pop, on=) #idk coś tu źle jest
