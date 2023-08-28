from math import sqrt


def dzie(liczba):
    dzielniki = [1]
    for i in range(2, int(sqrt(liczba)) + 1):
        if liczba % i == 0:
            dzielniki.append(i)
            dzielniki.append(liczba // i)
    return sorted(dzielniki)


def liczby_janka(liczba):
    liczby = []
    while len(liczby) < 5:
        liczba += 1
        dzielniki = dzie(liczba)
        if len(dzielniki) == 1:
            pass
        elif sum(dzielniki) / len(dzielniki) <= sqrt(liczba):
            liczby.append(str(liczba))
    return " ".join(liczby)


def main():
    liczba = int(input())
    print(liczby_janka(liczba))


if __name__ == "__main__":
    main()
