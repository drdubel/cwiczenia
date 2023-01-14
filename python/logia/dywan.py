import turtle as t

t.speed(0)
t.pencolor("black")
t.pu()
t.goto(-160, -200)
t.pd()


def strzalka():
    przekatna = (40**2 + 40**2) ** 0.5 / 2
    t.fillcolor("green")
    t.begin_fill()
    t.fd(80)
    t.rt(90)
    t.fd(80)
    t.rt(135)
    t.fd(przekatna)
    t.lt(90)
    t.fd(przekatna)
    t.rt(90)
    t.fd(przekatna * 2)
    t.rt(90)
    t.fd(przekatna)
    t.lt(90)
    t.fd(przekatna)
    t.rt(225)
    t.end_fill()


def prostokat(ksztalt):
    t.lt(90)
    bok_2 = 40 * ksztalt
    t.fillcolor("red")
    t.begin_fill()
    for _ in range(2):
        t.fd(bok_2)
        t.lt(90)
        t.fd(40)
        t.lt(90)
    t.end_fill()


def kwadrat():
    for _ in range(4):
        prostokat(2)
        strzalka()
        t.fd(160)
        t.lt(90)
        t.fd(40)
    t.fd(80)
    t.lt(90)
    t.fd(120)
    prostokat(1)
    t.rt(90)
    t.bk(120)
    t.rt(90)
    t.fd(80)
    t.pu()
    t.fd(40)
    t.pd()


kwadrat()
kwadrat()
t.pu()
t.goto(-160, 0)
t.pd()
kwadrat()
kwadrat()
