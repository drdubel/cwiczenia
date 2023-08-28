def prezenty(il_cuk):
    cukierki = [i for i in range(1, il_cuk + 1)]
    kombinacje = []
    il_osob = 0
    if il_cuk % 2 == 1:
        kombinacje.append(f"1 {il_cuk}")
        cukierki.remove(il_cuk)
        il_osob += 1
    for i in range(il_cuk // 2):
        kombinacje.append(f"2 {cukierki[i]} {cukierki[len(cukierki)-i-1]}")
    il_osob += il_cuk // 2
    return [str(il_osob), kombinacje]


def main():
    il_cuk = int(input())
    wynik = prezenty(il_cuk)
    print(wynik[0])
    print("\n".join(wynik[1]))


if __name__ == "__main__":
    main()
