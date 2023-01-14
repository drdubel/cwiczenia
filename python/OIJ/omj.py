def sumy(liczby, przedzial):
    wynik = sum(liczby[(przedzial[0] - 1) : (przedzial[1])])
    return f"{wynik}\n"


def main():
    il_liczb, il_pytan = list(map(int, input().split()))
    lista = list(map(int, input().split()))
    wynik = ""
    for _ in range(il_pytan):
        przedzial = list(map(int, input().split()))
        wynik += sumy(lista, przedzial)
    return wynik


if __name__ == "__main__":
    print(main())
