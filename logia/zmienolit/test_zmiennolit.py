from zmiennolit import zmiennolit


def test_zmie0a():
    assert zmiennolit("shellless") == 3


def test_zmie0b():
    assert zmiennolit("bajtazar") == 0


def test_zmie0c():
    assert zmiennolit("zwolennikrozwiazanoptymalnych") == 1


def test_zmie0d():
    assert zmiennolit("xxxxxxxxxxx") == 10


def test_zmie0e():
    assert zmiennolit("a"*500000+"b"*500000) == 999998


def test_zmie0f():
    assert zmiennolit("mammamia"*100000) == 100000


def test_zmie1a():
    assert zmiennolit("abbaabbaabbaabbaabba") == 9


def test_zmie1b():
    assert zmiennolit("bbbabbbabbbabbbabbba") == 10


def test_zmie1c():
    assert zmiennolit("babaababaababaababaa") == 4


def test_zmie1d():
    assert zmiennolit("aabaabaabaabaabaab") == 6


def test_zmie2a():
    assert zmiennolit("bbaabaaaaaaaa") == 9


def test_zmie2b():
    assert zmiennolit("aababaaabaaaaa") == 7


def test_zmie2c():
    assert zmiennolit("abbaabbbbbbaab") == 8


def test_zmie2d():
    assert zmiennolit("aaaaaaabbabaabaabb") == 10


def test_zmie2e():
    assert zmiennolit("aabaaabaabaaabaaaa") == 9
