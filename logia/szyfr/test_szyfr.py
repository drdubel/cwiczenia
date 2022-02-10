from szyfr import deszyfr

def test_szy0a():
    assert deszyfr([31452122]) == ["krab"]

def test_szy0b():
    assert deszyfr([232821473121, 22212252, 30212729]) == ["chatka", "baby", "jagi"]

def test_szy0c():
    assert deszyfr([332131425021, 4321412925413121]) == ["makowa", "panienka"]

# def test_szy0d():