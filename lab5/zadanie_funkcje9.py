def ciag_fibonacciego(n):
    if n == 1 or n == 2:
        return 1
    elif n <= 0:
        return None
    else:
        return ciag_fibonacciego(n-1) + ciag_fibonacciego(n-2)


wyraz = int(input("Podaj numer wyrazu: "))
wynik = ciag_fibonacciego(wyraz)
print(f"{wyraz} wyraz ciągu Fibonacciego to {wynik}")
