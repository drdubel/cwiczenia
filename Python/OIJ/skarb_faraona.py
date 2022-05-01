def skarb_faraona(il_przed, maks_suma_wag, waga, wartosc):
    tabl_wyn = [
        [0 for i in range(maks_suma_wag + 1)]
        for j in range(il_przed + 1)
        ]
    for i in range(1, il_przed + 1):
        p = i-1
        for j in range(1, maks_suma_wag + 1):
            if waga[p] <= j:
                tabl_wyn[i][j] = max(
                    tabl_wyn[i-1][j],
                    wartosc[p] + tabl_wyn[i-1][j-waga[p]]
                )
            else:
                tabl_wyn[i][j] = tabl_wyn[i-1][j]
    return tabl_wyn[il_przed][maks_suma_wag]


def main():
    il_przed, maks_suma_wag = list(map(int, input().split()))
    waga = []
    wartosc = []
    for i in range(il_przed):
        wejsc = input().split()
        waga.append(int(wejsc[0]))
        wartosc.append(int(wejsc[1]))
    print(skarb_faraona(il_przed, maks_suma_wag, waga, wartosc))


if __name__ == "__main__":
    main()
