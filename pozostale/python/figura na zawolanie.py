import turtle

t = turtle.Pen()


def marceli():
    while True:
        odp = input("Ile kątów: ")
        trut = int(odp)
        if trut > 2 and trut < 11:
            return trut
        print("źle!")


def figura_na_zawolanie():
    trut = marceli()
    for i in range(trut):
        t.forward(150 / trut)
        t.left(360 / trut)


figura_na_zawolanie()
