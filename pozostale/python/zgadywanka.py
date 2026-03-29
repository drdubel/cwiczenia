from random import randint


def zgaduj():
    n = randint(0, 10000)
    k = -1

    while k != n:
        k = int(input("Zgadnij liczbę od 0 do 100000: "))
        if k < n:
            print("Za mało!")
        elif k > n:
            print("Za dużo!")

    print("Zgadłeś! To była liczba", n)


if __name__ == "__main__":
    zgaduj()
