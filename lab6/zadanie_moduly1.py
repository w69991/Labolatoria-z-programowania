import random
#a
print("Szczęśliwy numerek to:", random.randint(1, 30))
#b
roczniki = [2000, 2001, 2002, 2003, 2004]
print(random.choice(roczniki))
#c
print("Losowanie 6 numerów lotto: ", random.sample(range(1, 49), 6))
