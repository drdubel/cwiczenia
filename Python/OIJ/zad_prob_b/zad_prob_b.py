def dzielniki(lic):
    wynik = []
    i = 1
    while i*i <= lic:
        if lic % i == 0:
            wynik.append(i)
            if lic//i != i:
                wynik.append(lic//i)
        i += 1
    return wynik

def czekolada(liczby):
    liczby = liczby.split()
    a = int(liczby[0])
    b = int(liczby[1])
    c = int(liczby[2])
    d = int(liczby[3])
    if a*b < c*d:
        return "NIE"
    dzie_c = dzielniki(c)
    dzie_d = dzielniki(d)
    mnj_dzie, wcj_dzie = min(dzie_c, dzie_d), max(dzie_c, dzie_d)
    lic_nowe = [c, d]
    wcj_dzie_lic = c
    if wcj_dzie == dzie_d:
        wcj_dzie_lic = d
    for dzie in wcj_dzie:
        lic_nowe[lic_nowe.index(wcj_dzie_lic)] //= dzie
        if wcj_dzie_lic == d:
            lic_nowe[0] *= dzie
        else:
            lic_nowe[1] *= dzie
        if lic_nowe[0] <= a and lic_nowe[1] <= b or lic_nowe[1] <= a and lic_nowe[0] <= b:
            return "TAK"
        lic_nowe = [c, d]
    return "NIE"

def main():
    liczby = input()
    print(czekolada(liczby))

if __name__ == "__main__":
    main()