from zygzad import zygzak


def test_zyg0a():
    assert zygzak('PGGG') == '3/1'


def test_zyg0b():
    assert zygzak('PPGPG') == '2/3'


def test_zyg0c():
    assert zygzak('PPGPPGPG') == '3/5'


def test_zyg0d():    
    assert zygzak('PPGPPGPPGPPG') == '1/2'


def test_zyg0e():
    assert zygzak('PPGPPGGP') == 'NIE'


def test_zyg0f():
    assert zygzak('PPPPPGGG') == 'NIE'


def test_zyg0g():
    assert zygzak('PPPG'*50) == '1/3'


def test_zyg0h():
    assert zygzak('PGP'*300000) == 'NIE'


def test_zyg0i():
    assert zygzak('PG'*50000000) == '1/1'
