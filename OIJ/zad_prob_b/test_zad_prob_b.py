from zad_prob_b import czekolada

def test_cze0a():
    assert czekolada('3 9 2 10') == 'NIE'

def test_cze0b():
    assert czekolada("5 4 2 6") == 'TAK'

def test_cze0c():
    assert czekolada("400 600 903 180") == 'TAK'

def test_cze0d():
    assert czekolada("235439 137399 353527 729943") == 'NIE'

def test_cze0e():
    assert czekolada(f"{10**9} {10**8} {10**8+5} {10**8+1}") == 'TAK'
