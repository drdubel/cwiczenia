def kradniemy_filary(il_filarow, wartosci):
    wynik = [0] * il_filarow
    wynik[0] = wartosci[0]
    wynik[1] = wartosci[0] + wartosci[1]
    for i in range(3, il_filarow):
        wynik[i] = max(
            wynik[i - 1],
            wynik[i - 2] + wartosci[i],
            wynik[i - 3] + wartosci[i - 1] + wartosci[i],
        )
    return max(wynik)


def main():
    il_filarow = int(input())
    if not il_filarow:
        return 0
    wartosci = []
    for i in range(il_filarow):
        wartosci.append(int(input()))
    if il_filarow == 1:
        return wartosci[0]
    return kradniemy_filary(il_filarow, wartosci)


if __name__ == "__main__":
    print(main())
