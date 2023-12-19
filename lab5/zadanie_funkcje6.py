def poletrojkata():
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    c = float(input("Podaj bok c: "))
    if a>0 and b>0 and c>0:
        if a+b>c and a+c>b and c+b>a:
            p = (a + b + c) / 2
            P = (p*(p-a)*(p-b)*(p-c))**(1/2)
            print("Pole trójkąta to:", P)
        else:
            print("Niepoprawna długość boku!")
    else:
        print("Niepoprawna długość boku!")

poletrojkata()