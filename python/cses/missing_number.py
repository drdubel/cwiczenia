def brakujaca(n, liczby_podane):
    liczby = "1"
    for i in range(2, n):
        liczby += f" {i}"
    return liczby.strip(liczby_podane)


def main():
    n = int(input()) + 1
    liczby_podane = input()
    print(brakujaca(n, liczby_podane))


if __name__ == "__main__":
    main()
