from zad_prob_a import roznorodnosc


def test_roz0a():
    assert roznorodnosc(7, [3, 2, 2, 2, 4, 4, 4]) == 5


def test_roz0b():
    assert roznorodnosc(5, [0, 0, 5, 1, 1]) == 5


def test_roz0c():
    assert roznorodnosc(14, [1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7, 7, 7]) == 9


def test_roz0d():
    roz0d = open("/home/antek/Pobrane/roz0d.txt").read()
    roz0d = [int(j) for j in roz0d.split()]
    assert roznorodnosc(1000, roz0d) == 1000


def test_roz0e():
    roz0e = open("/home/antek/Pobrane/roz0e.txt").read()
    roz0e = [int(i) for i in roz0e.split()]
    assert roznorodnosc(1000000, roz0e) == 311982
