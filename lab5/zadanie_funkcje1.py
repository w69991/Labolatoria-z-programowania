
def kolo(a):
    if r>0:
        print(3.14 * r ** 2)
    else:
        print("Nie poprawna długość promienia!")

r = float(input("Podaj promień koła: "))

kolo(r)

def kolov2():
    r2 = float(input("Podaj promien r2: "))
    p = 3.14 * r2 ** 2
    return p

print(kolov2())