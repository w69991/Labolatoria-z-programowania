import datetime

ostatnie_lab = datetime.datetime(2023, 12, 19)
kolokwium = datetime.datetime(2024, 2, 12)
dzisiejszy_dzien = datetime.datetime.now()

print(f"Od ostatnich labolatoriów upłynęło {dzisiejszy_dzien - ostatnie_lab}")
print(f"Do kolokwium zostało {kolokwium - dzisiejszy_dzien}")
