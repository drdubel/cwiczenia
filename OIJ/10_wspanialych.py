def ktorzy_muszkieterzy(il_kandydatow, moce):
    moce.sort(reverse=True)
    wynik = moce[0:10]
    return wynik


def main():
    il_kandydatow = int(input())
    moce = list(map(int, input().split()))
    wynik = ktorzy_muszkieterzy(il_kandydatow, moce)
    wynik = list(map(str, wynik))
    wynik = ' '.join(wynik)
    print(wynik)

if __name__ == "__main__":
    main()