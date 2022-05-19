import math


def zygzak(sekw_ruch):
    # poz = []
    dl = sekw_ruch.count("P")
    wys = sekw_ruch.count("G")
    nwd = math.gcd(wys, dl)
    akt_wys = 0
    akt_dl = 0
    wyk = 0
    for ruch in sekw_ruch:
        if ruch == "P":
            akt_dl += 1
        else:
            akt_wys += 1
        if wys/dl*akt_dl < akt_wys:
            return "NIE"
        if wys/dl*akt_dl-1 > akt_wys and sekw_ruch[wyk+1] != "G":
            return "NIE"
        wyk += 1
    wys //= nwd
    dl //= nwd
    return f'{wys}/{dl}'


if __name__ == '__main__':
    zygzak('PG'*500000) == '1/1'
