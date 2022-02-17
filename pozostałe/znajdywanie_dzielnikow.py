def znajdywanie_dzielnikow(n):
    wynik = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n/i == i:
                wynik += 1
            else:
                wynik += 2
            print(i)
        if wynik > 3:
            return
    return wynik


print(znajdywanie_dzielnikow(80089))
