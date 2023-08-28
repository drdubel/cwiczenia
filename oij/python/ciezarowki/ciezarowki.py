import sys
import numpy as np


def ciezarowki(il_ciezarowek, algogrod, bajtogrod, lista_ciezarowek):
    nes_v = 0
    eta = 2**31 - 1
    czas_do_konca = 0
    for _ in range(il_ciezarowek):
        wybor = [
            lista_ciezarowek["x"] / (lista_ciezarowek["v"] + nes_v),
            -lista_ciezarowek["x"] / (lista_ciezarowek["v"] - nes_v),
        ]
        warunki = [lista_ciezarowek["x"] > 0, lista_ciezarowek["x"] < 0]
        lista_ciezarowek["t"] = np.select(warunki, wybor, 0)
        czas_do_nesesera, _, nes_v2 = lista_ciezarowek[lista_ciezarowek["t"].argmin()]
        if eta <= czas_do_nesesera:
            return czas_do_konca + eta
        czas_do_konca += czas_do_nesesera
        lista_ciezarowek["x"] -= (
            lista_ciezarowek["v"]
            * czas_do_nesesera
            * lista_ciezarowek["x"]
            / abs(lista_ciezarowek["x"])
            + nes_v * czas_do_nesesera
        )
        bajtogrod -= nes_v * czas_do_nesesera
        eta = bajtogrod / nes_v2
        warunek = lista_ciezarowek["v"] > nes_v2
        lista_ciezarowek = np.extract(warunek, lista_ciezarowek)
        if len(lista_ciezarowek) == 0:
            return czas_do_konca + eta
        nes_v = nes_v2


def main(data_fd):
    il_ciezarowek, algogrod, bajtogrod = map(int, data_fd.readline().strip().split())
    lista_ciezarowek = np.zeros(
        il_ciezarowek, dtype=[("t", np.float64), ("x", np.float64), ("v", np.int32)]
    )
    if algogrod > bajtogrod:
        znak = -1
    else:
        znak = 1
    for slot, line in zip(lista_ciezarowek, data_fd):
        sx, sv = line[:-1].split()
        slot[1] = (int(sx) - algogrod) * znak
        slot[2] = int(sv)
    wynik = ciezarowki(
        il_ciezarowek, 0, (bajtogrod - algogrod) * znak, lista_ciezarowek
    )
    return ["%.9f" % wynik]


def run():
    for line in main(sys.stdin):
        print(line)


if __name__ == "__main__":
    run()
