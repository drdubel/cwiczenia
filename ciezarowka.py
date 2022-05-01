import numpy as np
nes_x = -10
nes_v = 0
lista_ciezarowek = np.zeros(3, dtype=[("t", np.float32), ("x", np.float32), ("v", np.int32)])
lista_ciezarowek["v"][0:] += 1
lista_ciezarowek["v"][1:] += 1
lista_ciezarowek["v"][2:] += 1
lista_ciezarowek["x"] -= 10
lista_ciezarowek["x"][0:] += 2
lista_ciezarowek["x"][1:] += 1
lista_ciezarowek["x"][2:] += 3
warunki = [nes_x < lista_ciezarowek["x"], nes_x > lista_ciezarowek["x"]]
wybor = [(lista_ciezarowek["x"] - nes_x) / (lista_ciezarowek["v"] + nes_v), (nes_x - lista_ciezarowek["x"]) / (lista_ciezarowek["v"] - nes_v)]
lista_ciezarowek["t"] = np.select(warunki, wybor, 0)
