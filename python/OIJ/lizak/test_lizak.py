from lizak import lizak


def test_liz0a():
    assert lizak(10, [6, 8, 4, 8, 6, 8, 8, 2, 6, 6]) == 4


def test_liz0b():
    assert lizak(5, [1, 2, 3, 4, 5]) == "NIE"


def test_liz0c():
    assert lizak(5, [1, 1, 1, 1, 1]) == 3


def test_liz0d():
    assert lizak(7, [9, 99, 999, 9, 999, 99, 9]) == 7


def test_liz0e():
    assert lizak(2000, [i for i in range(1, 2001)]) == "NIE"


def test_liz0f():
    assert lizak(500000, [1, 2]*250000) == 5
