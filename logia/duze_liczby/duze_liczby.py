def liczba(a, n):
    while a**(1/n) % 1 != 0:
        a -= 1
    return int(a**(1/n))


def main():
    a, n = list(map(int, input().split()))
    print(liczba(a, int(n)))


if __name__ == "__main__":
    main()
