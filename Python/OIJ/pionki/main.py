import sys


def najszybsze_zebranie(il_pionkow, plansza, plansza_przewrocona, najgestsza_kolumna):
    najgestszy_wiersz = max([kolumna.count("#") for kolumna in plansza_przewrocona])
    wynik = il_pionkow * 2 - (najgestsza_kolumna + najgestszy_wiersz)
    return wynik


def main(indata):
    wielkosc, _ = map(int, next(indata).split())
    plansza = []
    il_pionkow = 0
    pionki_w_kolumnach = []
    for wiersz in indata:
        plansza.append(wiersz)
        pionki_w_wierszu = wiersz.count("#")
        il_pionkow += pionki_w_wierszu
        pionki_w_kolumnach.append(pionki_w_wierszu)
    najgestsza_kolumna = max(pionki_w_kolumnach)
    return [
        najszybsze_zebranie(
            il_pionkow, plansza, list(zip(*plansza)), najgestsza_kolumna
        )
    ]


def run():
    for line in main((line.rstrip() for line in sys.stdin)):
        print(line)


if __name__ == "__main__":
    run()
