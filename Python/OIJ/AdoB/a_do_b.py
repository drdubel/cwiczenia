def odAdoB(start, drogi, koniec):
    wynik = 10**24
    il_krokow = 0
    wie_ter = start
    bylo = []
    while len(bylo) != len(drogi):
        bylo.append(wie_ter)
        dalej = drogi[wie_ter]
        dalej_2 = []
        for i in dalej:
            if i not in bylo:
                dalej_2.append(i)
        if dalej_2 and wie_ter != koniec:
            if koniec in dalej_2:
                if il_krokow+1 < wynik:
                    wynik = il_krokow+1
                    dalej_2.remove(koniec)
            if dalej_2:
                wie_ter = dalej_2[0]
                il_krokow += 1
        else:
            if wie_ter == koniec:
                if il_krokow < wynik:
                    wynik = il_krokow
            wie_ter = bylo[len(bylo)-2]
            il_krokow -= 1
    if wynik == 10**24:
        return "niestety"
    return wynik


def main():
    il_miast, il_autos = list(map(int, input().split()))
    skad, dokad = list(map(int, input().split()))
    drogi = {}
    for i in range(1, il_miast+1):
        drogi.update([[i, []]])
    for _ in range(il_autos):
        droga = list(map(int, input().split()))
        drogi[droga[0]].append(droga[1])
    if skad == dokad:
        return 0
    return odAdoB(skad, drogi, dokad)


if __name__ == "__main__":
    print(main())
