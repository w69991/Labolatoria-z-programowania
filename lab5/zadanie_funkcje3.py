def imie_i_wiek(imie,wiek=20):
    "Funkcja wczytująca i wyświetlająca podane imie oraz wiek"
    print(f"Imię to {imie}, wiek to {wiek}")


print(imie_i_wiek.__doc__)
imie_i_wiek("Adam")
imie_i_wiek("Kuba",25)

