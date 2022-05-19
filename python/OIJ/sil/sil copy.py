import math
import bisect
import cProfile
from functools import wraps

test = open("/home/antek/zipy/sil6m.in").read().split()
zakresy = []

for i in range(1, len(test), 2):
    zakresy.append([int(test[i]), int(test[i + 1])])

silnie = [math.factorial(i) for i in range(1, 16)]
liczby_silne = []

for i in range(1, 16):
    for j in liczby_silne.copy():
        liczby_silne.append(j + math.factorial(i))
    liczby_silne.append(math.factorial(i))

liczby_silne.sort()


def bieda_cache(fn):
    cache = {}
    limit = 99999
    @wraps(fn)
    def cached_fn(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        try:
            return cache[key]
        except KeyError:
            result = fn(*args, **kwargs)
            if len(cache) > limit:
                cache.popitem()
            cache[key] = result
            return result
    return cached_fn


cache = {}

def suma_zakresu(a, b, cache=cache):
    try:
        return cache[(a, b)]
    except KeyError:
        res = sum(
            liczby_silne[
                bisect.bisect_left(liczby_silne, a) : bisect.bisect_right(liczby_silne, b)
            ])
        cache[(a, b)] = res
        return res


def main():
    wynik = []
    for a, b in zakresy:
        wynik.append(str(suma_zakresu(a, b)))
    print("\n".join(wynik))



if __name__ == "__main__":
    cProfile.run("main()") #main()