from duze_liczby import liczba


def test_duz0a():
    assert liczba(1024, 2) == 32


def test_duz0b():
    assert liczba(899, 2) == 29


def test_duz0c():
    assert liczba(11000, 3) == 22


def test_duz0d():
    assert liczba(1024, 2) == 32
