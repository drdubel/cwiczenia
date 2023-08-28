def ciag(do_ilu):
    wynik = 0
    i = 0
    while wynik <= do_ilu:
        i += 1
        wynik += i
    return wynik - i, i - 1


def nawiasowania(n):
    nawiasy = ""
    while n > 0:
        ile, il_nawiasow = ciag(n)
        nawiasy += "()" * il_nawiasow + "("
        n -= ile
    return nawiasy


def main():
    n = int(input())
    print(nawiasowania(n))


if __name__ == "__main__":
    main()
