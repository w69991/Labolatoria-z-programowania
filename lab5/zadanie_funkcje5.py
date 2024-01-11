def obliczanie_BMI(waga, wzrost):
    BMI = waga / (wzrost ** 2)
    if BMI < 18.5:
        print("Niedowaga")
    elif 25 > BMI >= 18.5:
        print("Prawidłowa")
    elif 30 > BMI >= 25:
        print("Nadwaga")
    else:
        print("Otyłość")


waga = float(input("Podaj wage (w kg): "))
wzrost = float(input("Podaj wzrost (w metrach): "))

obliczanie_BMI(waga, wzrost)
