def kolejna(liczba, d):
    while d > 0:
        liczba += 1
        if "3" not in str(liczba):
            d -= 1
    return liczba


print(kolejna(28, 5))
