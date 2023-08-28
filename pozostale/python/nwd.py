def nwd(liczba1, liczba2):
    while liczba2 != 0:
        liczba1, liczba2 = liczba2, liczba1 % liczba2
    return liczba1


if __name__ == "__main__":
    print(nwd(27, 1960))
