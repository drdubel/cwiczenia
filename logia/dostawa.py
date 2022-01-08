def il_liter(slowo):
    a = 0
    b = 0
    c = 0
    for litera in slowo:
        if litera == 'a':
            a += 1
        if litera == 'b':
            b += 1
        if litera == 'c':
            c += 1
    return a, b, c

def dostawa(zamowienia, zapas):
    wynik = 0
    a = 0
    b = 0
    c = 0
    for zamowienie in zamowienia:
        a1, b1, c1 = il_liter(zamowienie)
        if a1 + a <= zapas and b1 + b <= zapas and c1 + c <= zapas:
            a += a1
            b += b1
            c += c1
            wynik += 1
    return wynik

print(dostawa(["abc","abaa", "caa", "bbbcc", "cac","abc"], 5))
