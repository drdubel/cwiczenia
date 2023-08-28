import sys
import numpy as np


def przeladunek(nes_x, nes_v, ciezarowki, poprzedni_czas, cel):
    if nes_v:
        eta = abs(cel - nes_x) / nes_v
    else:
        eta = 2**31 - 1
    szybsze = []
    najlepsza = (eta, -nes_v, nes_x)
    if len(ciezarowki):
        for c_x, c_v in ciezarowki:
            if c_v <= nes_v:
                continue
            if nes_x < c_x:
                c_x -= poprzedni_czas * c_v
            else:
                c_x += poprzedni_czas * c_v
            if nes_x < c_x:
                if nes_x < cel:
                    do_spotkania = (c_x - nes_x) / (c_v + nes_v)
                else:
                    do_spotkania = (c_x - nes_x) / (c_v - nes_v)
            elif c_x < nes_x:
                if cel < nes_x:
                    do_spotkania = (nes_x - c_x) / (c_v + nes_v)
                else:
                    do_spotkania = (nes_x - c_x) / (c_v - nes_v)
            else:
                do_spotkania = 0
            if do_spotkania > eta:
                continue
            if (do_spotkania, -c_v) < najlepsza:
                najlepsza = (do_spotkania, -c_v, c_x)
            szybsze.append((c_x, c_v))
    do_spotkania, mnes_v, _nes_x = najlepsza
    if nes_v:
        if nes_x < cel:
            nes_x += do_spotkania * nes_v
        else:
            nes_x -= do_spotkania * nes_v
    return do_spotkania, nes_x, -mnes_v, szybsze


def ciezarowki(il_ciezarowek, algogrod, bajtogrod, lista_ciezarowek):
    nes_x = algogrod
    nes_v = 0
    czas_etapu = 0
    czas_calkowity = 0
    for _ in range(500_000):
        czas_etapu, nes_x, nes_v, lista_ciezarowek = przeladunek(
            nes_x, nes_v, lista_ciezarowek, czas_etapu, bajtogrod
        )
        czas_calkowity += czas_etapu
        if not lista_ciezarowek:
            czas_calkowity += abs(bajtogrod - nes_x) / nes_v
            break
    return czas_calkowity


def main(data_fd):
    il_ciezarowek, algogrod, bajtogrod = map(int, data_fd.readline().strip().split())
    dtype = np.dtype([("x", np.int32), ("v", np.int32)])
    lista_ciezarowek = np.loadtxt(data_fd, dtype, max_rows=il_ciezarowek, delimiter=" ")
    wynik = ciezarowki(il_ciezarowek, algogrod, bajtogrod, lista_ciezarowek)
    return ["%.9f" % wynik]


def run():
    for line in main(sys.stdin):
        print(line)


if __name__ == "__main__":
    run()
