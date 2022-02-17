from dzielniki import dzielniki


def test_dzie0a():
    assert dzielniki(2, 6) == 1


def test_dzie0b():
    assert dzielniki(80000, 90000) == 2


def test_dzie0c():
    assert dzielniki(4, 25) == 3


def test_dzie0d():
    assert dzielniki(2, 100) == 4

    
def test_dzie0e():
    assert dzielniki(111, 999) == 7

    
def test_dzie0f():
    assert dzielniki(1, 1000000) == 168


def test_dzie0g():
    assert dzielniki(1, 3) == 0


def test_dzie0h():
    assert dzielniki(1, 8) == 1
