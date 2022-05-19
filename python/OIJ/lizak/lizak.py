def lizak(il_segmentow, segmenty):
    mozliwe = []
    for segment in segmenty:
        if segment not in mozliwe:
            if segmenty.count(segment) >= 3:
                mozliwe.append(segment)
    if not mozliwe:
        return "NIE"
    polozenia = {}
    for mozliwa in mozliwe:
        i = 0
        polozenia.update([[mozliwa, []]])
        for _ in range(segmenty.count(mozliwa)):
            i = segmenty.index(mozliwa, i) + 1
            polozenia[mozliwa].append(i - 1)
    wynik = 5*10**5
    for liczba in polozenia:
        polozenia_liczby = polozenia[liczba]
        for i in range(2, len(polozenia_liczby)):
            dlugosc = polozenia_liczby[i] - polozenia_liczby[i-2] + 1
            if wynik > dlugosc:
                wynik = dlugosc
    return wynik


def main():
    n = int(input())
    segmenty = list(map(int, input().split()))
    print(lizak(n, segmenty))


if __name__ == "__main__":
    main()
