def gdzie_przyczepic_lampy(lampy, il_lamp, il_lamp_do_kupienia, dlugosc):
    odleglosci_miedzy = [i - i_przed for i_przed, i in zip(lampy[:-1], lampy[1:])]
    odleglosci_miedzy2 = odleglosci_miedzy.copy()
    il_nowych_lamp = [0] * (il_lamp - 1)
    for i in range(il_lamp_do_kupienia):
        indeks = odleglosci_miedzy2.index(max(odleglosci_miedzy2))
        il_nowych_lamp[indeks] += 1
        odleglosci_miedzy2[indeks] /= il_nowych_lamp[indeks] + 1
    pole_nieoswietlone = sum((odleglosc / (lampa + 1))**2 / 4 * (lampa + 1) for odleglosc, lampa in zip(odleglosci_miedzy, il_nowych_lamp))
    return pole_nieoswietlone


def main():
    il_lamp, il_lamp_do_kupienia, dlugosc = map(int, input().split())
    lampy = list(map(int, input().split()))
    print(gdzie_przyczepic_lampy(lampy, il_lamp, il_lamp_do_kupienia, dlugosc))


if __name__ == '__main__':
    main()
