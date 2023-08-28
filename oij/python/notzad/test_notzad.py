from notzad import notzad


def test_not0a():
    assert (
        notzad(10, [4, 3, 5, 6, 7, 7, 4, 5, 6, 4], 5, [2, 3, 1, 4, 5]) == "5 4 10 1 0"
    )


def test_not0b():
    assert notzad(5, [1, 2, 3, 4, 5], 5, [5, 4, 3, 2, 1]) == "1 2 3 4 5"


def test_not0c():
    assert notzad(10, [1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 4, [3, 4, 2, 10, 1]) == "0 4 0 10"


def test_not0d():
    assert notzad(10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 4, [1, 10, 5, 2]) == "10 0 0 0"


def test_not0e():
    assert (
        notzad(10, [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], 5, [3, 2, 5, 10, 4]) == "6 8 2 0 4"
    )


# def test_not0f():
#    assert notzad(200000, [int(i) for i in ("1 0 "*100000).split()]) == 100000
