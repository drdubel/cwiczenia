klucz = {
    21: 'a',
    22: 'b',
    23: 'c',
    24: 'd',
    25: 'e',
    26: 'f',
    27: 'g',
    28: 'h',
    29: 'i',
    30: 'j',
    31: 'k',
    32: 'l',
    33: 'm',
    41: 'n',
    42: 'o',
    43: 'p',
    44: 'q',
    45: 'r',
    46: 's',
    47: 't',
    48: 'u',
    49: 'v',
    50: 'w',
    51: 'x',
    52: 'y',
    53: 'z',
}


def deszyfr(lista):
    lista = list(map(str, lista))
    wynik = []
    for i in range(len(lista)):
        wynik.append('')
        for j in range(0, len(lista[i]), 2):
            wynik[i] = wynik[i] + klucz[int(lista[i][j:j+2])]
    return(wynik)


def main():
    lista = input().split()
    print(deszyfr(lista))


if __name__ == "__main__":
    main()
