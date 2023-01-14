def ciaganie_neonow(slowo_1, slowo_2):
    wynik = [[]]
    for i in range(len(slowo_1)):
        for j in range(len(slowo_2)):
            wynik[i].append(0)
            if slowo_1[i] == slowo_2[j]:
                wynik[i][j] = wynik[i - 1][j - 1] + 1
            else:
                wynik[i][j] = max(wynik[i - 1][j], wynik[i][j - 1])
        wynik.append([])
    return wynik[i][j]


def main():
    slowo_1, slowo_2 = input().split()
    print(ciaganie_neonow(slowo_1, slowo_2))


if __name__ == "__main__":
    main()
