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
