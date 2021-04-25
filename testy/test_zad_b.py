from zesp import zes

def test_zes0a():
    assert zes(11, [13, 8, 7, 10, 8, 20, 18, 1, 7, 19, 20]) == 2

def test_zes0b():
    assert zes(1000, [i for i in range(1000)]) == 0

def test_zes0c():
    assert zes(500000, [1000000000]*500000) == ''

