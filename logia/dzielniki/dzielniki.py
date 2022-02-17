def sito_erastotenesa(do_ilu):
    liczby_pier = [i for i in range(2, do_ilu+1)]
    n = 2
    i = 0
    while n < do_ilu**0.5:
        if liczby_pier[i]:
            for j in range(2*n, do_ilu+1, n):
                liczby_pier[j-2] = 0
        i += 1
        while not liczby_pier[i]:
            i += 1
        n = liczby_pier[i]
    while 0 in liczby_pier:
        liczby_pier.remove(0)
    return liczby_pier


def dzielniki(a, b):
    wynik = 0
    if b < 4:
        return 0
    liczby_piewsze = sito_erastotenesa(int(b**0.5))
    for liczba in liczby_piewsze:
        if liczba**2 >= a:
            wynik += 1
    return wynik


print(dzielniki(1, 1000000000))
