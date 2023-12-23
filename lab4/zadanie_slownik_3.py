rachunki = {"styczeń" : 144, "luty":141, "marzec":136, "kwiecień":132, "maj":135, "czerwiec":148, "lipiec":137}
print(rachunki)
lista = rachunki.values()
#a
print(f"Największy rachunek: {max(lista)}")
print(f"Najmniejszy rachunek: {min(lista)}")
print(f"Suma rachunków: {sum(lista)}")
print(f"Średnia rachunków: {sum(lista)/len(lista)}")
#b
if sum(lista)/len(lista) > rachunki["lipiec"]:
    print("Jesteś bezpieczny")
else:
    print("Zacznij oszczędzać")
