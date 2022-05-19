def najmniejsza_suma(cyfry, il_liczb):
    wynik = 0
    cyfry_bez_zer = [i for i in cyfry if i != 0]
    dlugosc_liczb = len(cyfry)//il_liczb
    il_liczb_dluzszych = len(cyfry) % il_liczb
    wynik += sum(
        cyfry_bez_zer[
            :il_liczb_dluzszych
            ]
        ) * 10**dlugosc_liczb
    il_zer = cyfry.count(0)
    cyfry_bez_zer = cyfry_bez_zer[il_liczb_dluzszych:]
    wynik += sum(
        cyfry_bez_zer[
            :il_liczb-il_liczb_dluzszych
            ]
        ) * 10**(dlugosc_liczb-1)
    cyfry_bez_zer = cyfry_bez_zer[il_liczb-il_liczb_dluzszych:]
    cyfry = [0 for _ in range(il_zer)]
    for cyfra in cyfry_bez_zer:
        cyfry.append(cyfra)
    wynik += sum(
        cyfry[
            :il_liczb_dluzszych
            ]
        ) * 10**(dlugosc_liczb-1)
    cyfry = cyfry[il_liczb_dluzszych:]
    for i in range(dlugosc_liczb-1):
        wynik += sum(cyfry[0:il_liczb]) * 10**(dlugosc_liczb - i - 2)
        cyfry = cyfry[il_liczb:]
        il_zer = cyfry.count(0)
    return wynik


def main():
    cyfry = list(map(int, sorted(input())))
    il_liczb = int(input())
    print(najmniejsza_suma(cyfry, il_liczb))


if __name__ == "__main__":
    main()
