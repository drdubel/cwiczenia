def jakie_pozycje(szukana, posortowane_liczby, liczby):
    for liczba in posortowane_liczby:
        ind1 = posortowane_liczby.index(liczba)
        if szukana - liczba in posortowane_liczby[:ind1] + posortowane_liczby[ind1 + 1:]:
            ind1 = liczby.index(liczba)
            return ind1, (liczby[:ind1] + liczby[ind1 + 1:]).index(szukana - liczba)
        if liczba * 2 > szukana:
            break
    return "IMPOSSIBLE"


def main():
    _, szukana = list(map(int, input().split()))
    liczby = list(map(int, input().split()))
    posortowane_liczby = sorted(liczby)
    print(jakie_pozycje(szukana, posortowane_liczby, liczby))


if __name__ == '__main__':
    main()
