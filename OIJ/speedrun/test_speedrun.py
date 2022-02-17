from speedrun import speedrun

def test_spe0a():
    assert speedrun([4,1,1,3,4,1,6,9,10,10]) == 8

def test_spe0b():
    assert speedrun([2,3,1,4,6,5]) == 4

def test_spe0c():
    assert speedrun([5,4,1,2,3,7,6]) == 6

def test_spe0d():
    assert speedrun(list(range(20,0,-1))) == 1