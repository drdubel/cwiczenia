from functools import reduce
from operator import mul


class MalformedDigit(Exception):
    pass


def trzy_mnożniki(n):
    l = 1
    liczby = []
    if n < 111:
        raise MalformedDigit("za mała liczba, nie mniej niż 111")
    if n > 10**20 - 1:
        raise MalformedDigit("za duża liczba, nie więcej niż 10**20-1")
    cyfry = [int(i) for i in str(n)]
    if 0 in cyfry:
        raise MalformedDigit("nieprafidłowa cyfra, nie może być 0")
    for i in range(len(cyfry) - 2):
        liczby.append(reduce(mul, cyfry[i : 3 + i]))
    return max(liczby)


def main():
    liczba_str = input()
    try:
        liczba = int(liczba_str)
    except ValueError:
        raise MalformedDigit("To nie jest liczba")
    print(trzy_mnożniki(liczba))


if __name__ == "__main__":
    main()
