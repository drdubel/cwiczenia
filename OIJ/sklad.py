def sklad(il_wagonow, wym_il_cementu, cem_w_wag):
    min_wynik = 0
    for _ in range(il_wagonow):
        il_wag_uz = 0
        wynik = 0
        for cement in cem_w_wag:
            il_wag_uz += cement
            wynik += 1
            if il_wag_uz > wym_il_cementu:
                break
            if il_wag_uz == wym_il_cementu:
                if wynik < min_wynik or not min_wynik:
                    min_wynik = wynik
        cem_w_wag = cem_w_wag[1:]
    if not min_wynik:
        return "N"
    return min_wynik


def main():
    il_wagonow, wym_il_cementu = list(map(int, input().split()))
    cem_w_wag = list(map(int, input().split()))
    print(sklad(il_wagonow, wym_il_cementu, cem_w_wag))

if __name__ == "__main__":
    main()