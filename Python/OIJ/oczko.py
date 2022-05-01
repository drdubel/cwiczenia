def oczko(karty_graczy, il_graczy):
    il_wyg = 0
    wyg = []
    max_wyn = 0
    wartosci = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": [1, 11],
    }
    for gracz, karty in enumerate(karty_graczy, 1):
        wynik_1 = 0
        wynik_2 = 0
        for karta in karty:
            if karta == "A":
                wynik_1 += 1
                wynik_2 += 11
            else:
                wynik_1 += wartosci[karta]
                wynik_2 += wartosci[karta]
        if wynik_2 > 21 and wynik_1 > 21:
            wynik = 0
        elif wynik_2 > 21 and wynik_1 <= 21:
            wynik = wynik_1
        elif wynik_1 > 21 and wynik_2 <= 21:
            wynik = wynik_2
        else:
            wynik = max(wynik_1, wynik_2)
        if wynik > max_wyn:
            il_wyg = 1
            wyg = [gracz]
            max_wyn = wynik
        elif wynik == max_wyn and wynik != 0:
            il_wyg += 1
            wyg.append(gracz)
    return il_wyg, wyg


def main():
    il_graczy = int(input())
    karty_graczy = []
    for _ in range(il_graczy):
        karty_graczy.append(input())
    wynik = oczko(karty_graczy, il_graczy)
    print(wynik[0])
    print(' '.join(list(map(str, wynik[1]))))


if __name__ == "__main__":
    main()
