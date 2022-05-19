def ogien(czas_ognia, czas, farma, wymiary):
    nowa_farma = farma.copy()
    print(id(nowa_farma) == id(farma))
    if czas/czas_ognia % 1 == 0 and czas != 0:
        for wys in range(wymiary[0]):
            for szer in range(wymiary[1]):
                if farma[wys][szer] == '.':
                    if wys != 0 and farma[wys-1][szer] == '*':
                        nowa_farma[wys][szer] = '*'
                    if wys != wymiary[0]-1 and farma[wys+1][szer] == '*':
                        nowa_farma[wys][szer] = '*'
                    if szer != wymiary[1]-1 and farma[wys][szer+1] == '*':
                        nowa_farma[wys][szer] = '*'
                    if szer != 0 and farma[wys][szer-1] == '*':
                        nowa_farma[wys][szer] = '*'
    print(nowa_farma == farma)
    return farma


def main():
    wys, szer, czas_ognia = list(map(int, input().split()))
    wymiary = [wys, szer]
    farma = []
    for _ in range(wys):
        farma.append(list(input()))
    wynik = ogien(czas_ognia, 6, farma.copy(), wymiary)
    for lista in wynik:
        print(''.join(lista))


main()
