def zamiana_klucza(klucz):
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    kolejnosc = ''
    klucz_posortowany = sorted(klucz)
    i = 0
    for lit in klucz:
        polozenie = klucz_posortowany.index(lit) + klucz[:i].count(lit)
        kolejnosc = kolejnosc + str(polozenie)
        i += 1
    return kolejnosc

def szyfrator_kolumnowy(wiadomosc, klucz):
    klucz_cyfr = zamiana_klucza(klucz)
    lista_liter = ['']*len(klucz)
    zaszyf_wiad = ''
    i = 0
    for litera in wiadomosc:
        lista_liter[i%len(klucz)] = lista_liter[i%len(klucz)] + litera
        i += 1
    for miejsce in klucz_cyfr:
        zaszyf_wiad = zaszyf_wiad + lista_liter[int(miejsce)]
    return zaszyf_wiad


def main():
    wiadomosc, klucz = input().split()
    print(szyfrator_kolumnowy(wiadomosc, klucz))


if __name__ == "__main__":
    main()
