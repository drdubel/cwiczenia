def bisekcja(lista, szukana):
    lista_poczatkowa = lista.copy()
    koniec = False
    wynik = [1, 1]
    while not koniec:
        pol_dl_listy = len(lista) // 2
        if pol_dl_listy == 0:
            srodek = [1, lista[pol_dl_listy - 1]]
        else:
            srodek = [lista[pol_dl_listy - 1] + 1, lista[pol_dl_listy]]
        if szukana > srodek[1]:
            lista = lista[pol_dl_listy:]
        elif szukana < srodek[0]:
            lista = lista[:pol_dl_listy]
        else:
            wynik = [
                srodek[1] - srodek[0] + szukana - srodek[1] + 1,
                lista_poczatkowa.index(srodek[1]) + 1,
            ]
            koniec = True
    return wynik


def do_arbuzan(dzien, miesiac, il_mies_A, il_mies_B, dl_mies_A, dl_mies_B):
    if miesiac == 1:
        dni_minelo = dzien
    else:
        dni_minelo = dl_mies_B[miesiac - 2] + dzien
    jak_dalej = bisekcja(dl_mies_A, dni_minelo)
    return f"{jak_dalej[0]} {jak_dalej[1]}"


def do_bananitow(dzien, miesiac, il_mies_A, il_mies_B, dl_mies_A, dl_mies_B):
    if miesiac == 1:
        dni_minelo = dzien
    else:
        dni_minelo = dl_mies_A[miesiac - 2] + dzien
    jak_dalej = bisekcja(dl_mies_B, dni_minelo)
    return f"{jak_dalej[0]} {jak_dalej[1]}"


def main():
    il_mies_A, il_mies_B = list(map(int, input().split()))
    dl_mies_A = list(map(int, input().split()))
    dl_mies_B = list(map(int, input().split()))
    for i in range(1, il_mies_A):
        dl_mies_A[i] = dl_mies_A[i] + dl_mies_A[i - 1]
    for i in range(1, il_mies_B):
        dl_mies_B[i] = dl_mies_B[i] + dl_mies_B[i - 1]
    lic_zap = int(input())
    wynik = []
    for _ in range(lic_zap):
        zap = input().split()
        if zap[2] == "A":
            wynik.append(
                do_bananitow(
                    int(zap[0]), int(zap[1]), il_mies_A, il_mies_B, dl_mies_A, dl_mies_B
                )
            )
        else:
            wynik.append(
                do_arbuzan(
                    int(zap[0]), int(zap[1]), il_mies_A, il_mies_B, dl_mies_A, dl_mies_B
                )
            )
    return "\n".join(wynik)


if __name__ == "__main__":
    print(main())
