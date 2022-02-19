from usuzad import usuzad

def test_usu0a():
    assert usuzad(7, [4, 1, 5, 2, 4, 1, 3]) == 2

def test_usu0b():
    assert usuzad(5, [1, 1, 1, 1, 1]) == 3

def test_usu0c():
    assert usuzad(5, [4, 4, 4, 4, 4]) == 1

def test_usu0d():
    assert usuzad(6, [0, 0, 0, 0, 0, 0]) == 6

def test_usu0e():
    assert usuzad(16, [199, 5, 3, 2, 432, 42, 32, 432, 43, 43, 234, 42, 534, 5363, 23, 1]) == 1

def test_usu0f():
    assert usuzad(200000, [int(i) for i in ("1 0 "*100000).split()]) == 100000

def test_usu0g():
    assert usuzad(200000, [int(i) for i in ("4 1 "*100000).split()]) == 99998
