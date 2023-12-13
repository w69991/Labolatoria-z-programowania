lista_imion = ["Bartek", "Asia", "Zosia", "Waldek"]
#a
print(lista_imion)
posortowana_lista_imion = sorted(lista_imion)
#b
posortowana_lista_imion.append("Mati")
posortowana_lista_imion.append("Dorota")
print(posortowana_lista_imion)
posortowana_lista_imion.pop()
print(posortowana_lista_imion)
#c
posortowana_lista_imion.insert(3, "Kasia")
print(posortowana_lista_imion)
#d
posortowana_lista_imion.reverse()
print(posortowana_lista_imion)
listax2 = posortowana_lista_imion*2
print(listax2)
listax2.sort()
print(listax2)
