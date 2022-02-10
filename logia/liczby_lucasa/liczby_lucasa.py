def lucas(n):
    liczby = [2, 1]
    for _ in range(2, n, 1):
        stara_liczba = liczby[1]
        liczby[1] = sum(liczby)
        liczby[0] = stara_liczba
    if n < 3:
        return liczby[n-1]
    liczba_lucasa = str(liczby[1])
    liczba_lucasa = int(liczba_lucasa[len(liczba_lucasa)-2:])
    return liczba_lucasa



def main():
    n = int(input())
    print(lucas(n))


if __name__ == "__main__":
    main()
