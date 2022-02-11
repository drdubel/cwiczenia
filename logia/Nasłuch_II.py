def nasluch_II(slowa):
    wynik = 0
    i = 0
    for lit_0, lit_1 in zip(slowa[0], slowa[1]):
        if lit_0 == lit_1:
            wynik += 10
            slowa[0] = slowa[0][:i] + slowa[0][i+1:]
            slowa[1] = slowa[1][:i] + slowa[1][i+1:]
            i -= 1
        i += 1
    dlugosci = {
        len(slowa[0]): slowa[0],
        len(slowa[1]): slowa[1]
    }
    krotsze = slowa.index(dlugosci[min(len(slowa[0]), len(slowa[1]))])
    for lit_0, lit_1 in zip(slowa[0], slowa[1]):
        if krotsze == 0:
            if lit_0 in slowa[1]:
                wynik += 1
        else:
            if lit_1 in slowa[0]:
                wynik += 1
    return wynik


def main():
    slowa = input().split()
    print(nasluch_II(slowa))


if __name__ == "__main__":
    main()
