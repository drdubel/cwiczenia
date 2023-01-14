import a_do_b as a
import sys

print(sys.getrecursionlimit())
drogi = {}
for i in range(199999):
    drogi.update([[i, [i + 1]]])


def test_adb0a():
    assert len(a.odAdoB({4: [1], 1: [2, 3], 2: [3]}, 4, 3)) - 1 == 2


def test_adb0b():
    assert len(a.odAdoB({1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [3, 1]}, 2, 4)) - 1 == 2


def test_adb0c():
    assert a.odAdoB({2: [1]}, 1, 2) == "niestety"


def test_adb0d():
    assert len(a.odAdoB(drogi, 42, 199199)) - 1 == 1000
