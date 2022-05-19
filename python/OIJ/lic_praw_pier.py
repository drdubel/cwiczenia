def czy_pierw(lic):
    lic = lic**0.5
    if lic > 1 and lic%1 == 0:
        lic = int(lic)
        for i in range(2, int(lic/2)+1):
            if (lic % i) == 0:
                return "NIE"
        else:
            return "TAK"
    else:
        return "NIE"

def lic_praw_pier(il_liczb, liczby):
    wynik = []
    for liczba in liczby:
        wynik.append(czy_pierw(liczba))
    return wynik

def main():
    il = int(input())
    liczby = [int(i) for i in input().split()]
    assert len(liczby) == il
    wynik = lic_praw_pier(il, liczby)
    for i in wynik:
        print(i)
    #print(wynik)

if __name__ == "__main__":
    main()