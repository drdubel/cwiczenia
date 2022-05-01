def main():
    liczba_dni, liczba_miast, liczba_pytan = list(map(int, input().split()))
    opady_w_miastach = {}
    wynik = ''
    for i in range(liczba_miast):
        opady_w_miastach.update([[i+1, 0]])
    for _ in range(liczba_dni):
        dane = list(map(int, input().split()))
        for i in range(dane[0], dane[1]+1):
            opady_w_miastach.update([[i, dane[2]+opady_w_miastach[i]]])
    for _ in range(liczba_pytan):
        wynik += f"{opady_w_miastach[int(input())]}\n"
    return wynik


if __name__ == "__main__":
    print(main())
