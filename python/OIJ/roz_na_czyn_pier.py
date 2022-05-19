def rozklad(liczba):
    for dziel in range(2, liczba):
        wyn_dziel, reszta = divmod(liczba, dziel)
        if not reszta:
            return [dziel] + rozklad(wyn_dziel)
    return [liczba]

def czyn_pier_zad(liczba1, liczba2):
    wynik = ''
    for lic_ter in range(liczba1, liczba2+1):
        wynik += str(len(rozklad(lic_ter)))+' '
    return wynik

def main():
    #liczba1, liczba2 = [int(i) for i in input().split()]
    #print(czyn_pier_zad(liczba1, liczba2))
    a = int(input("DAJ LICZBE DO ROZŁOŻENIA: "))
    print(rozklad(a))

if __name__ == "__main__":
    main()
