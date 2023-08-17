from najmniejsza_suma import najmniejsza_suma


def test_naj0a():
    assert najmniejsza_suma([0, 1, 2, 3, 3, 4, 7, 9], 3) == 380


def test_naj0b():
    assert najmniejsza_suma([4, 4, 5, 5, 6, 6, 7], 7) == 37


def test_naj0c():
    assert najmniejsza_suma([1, 2, 5, 5, 6, 9], 3) == 100


def test_naj0d():
    assert najmniejsza_suma([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == 774


def test_naj0e():
    assert najmniejsza_suma([9 for i in range(200000)], 15000) == 599999999999985000


def test_naj0f():
    assert (
        najmniejsza_suma(list(map(int, sorted("11100000" * 25000))), 60000) == 24015000
    )
