def ile(lista):
    wynik = 0
    for liczba in lista:
        if liczba > 1000000:
            raise ValueError("value too high, it has to be less than 1000000")
        if liczba < 0:
            raise ValueError("value has to be positive")
        a = str(liczba)
        suma = 0
        iloczyn = 1
        for cyfra in a:
            suma += int(cyfra)
            iloczyn = int(cyfra) * iloczyn
        if suma == iloczyn:
            wynik += 1
    return wynik

print(ile([134, 7, 123, 321]))
