def speedrun(poziomy):
    poziomy_bez = [i for i in poziomy]
    for poziom in poziomy_bez:
        if poziom == poziomy.index(poziom)+1:
            return poziom

if __name__ == '__main__':
    liczba_poziomow = int(input())
    poziomy = [int(p) for p in input().split()]
    assert 1 < liczba_poziomow < 100000
    assert liczba_poziomow == len(poziomy)
    czas = speedrun(poziomy)
    print(czas)
