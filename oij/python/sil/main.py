import math
import bisect

silnie = [math.factorial(i) for i in range(1, 16)]
liczby_silne = []
sumy_liczb_silnych = []

for i in range(1, 16):
    kopia = liczby_silne.copy()
    liczby_silne.append(math.factorial(i))
    for j in kopia:
        liczby_silne.append(j + math.factorial(i))

liczby_silne.sort()
suma = 0

for ls in liczby_silne:
    suma += ls
    sumy_liczb_silnych.append(suma)


def suma_zakresu(a, b):
    najw_liczba_silna = bisect.bisect_right(liczby_silne, b) - 1
    najm_liczba_silna = bisect.bisect_left(liczby_silne, a) - 1
    if najm_liczba_silna < 0:
        return sumy_liczb_silnych[najw_liczba_silna]
    return sumy_liczb_silnych[najw_liczba_silna] - sumy_liczb_silnych[najm_liczba_silna]


def main():
    il_zakresow = int(input())
    wyniki = []
    for _ in range(il_zakresow):
        a, b = list(map(int, input().split()))
        wyniki.append(str(suma_zakresu(a, b)))
    print("\n".join(wyniki))


if __name__ == "__main__":
    main()
