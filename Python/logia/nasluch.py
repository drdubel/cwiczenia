def nasluch(sygnaly):
    wynik = 0
    for lic_1, lic_2 in zip(sygnaly[0], sygnaly[1]):
        if lic_1 == lic_2:
            wynik += 10
        elif lic_1 in sygnaly[1]:
            wynik += 1
    return wynik


def main():
    sygnaly = list(map(str, input().split()))
    print(nasluch(sygnaly))


if __name__ == "__main__":
    main()
