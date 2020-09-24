import turtle

t = turtle.Pen()


class MalformedEar(Exception):
    pass


def kls(il_ziaren):
    t.speed(0)
    if il_ziaren > 10:
        raise MalformedEar("za dużo ziaren, nie więcej niż 10")
    if il_ziaren < 2:
        raise MalformedEar("za mało ziaren, nie mniej niż 2")
    a = 250 /(2*il_ziaren)


    def ziarno():
        t.fillcolor("yellow")
        t.begin_fill()
        for i in range(2):
            t.fd(a)
            t.lt(45)
            t.fd(2 * a)
            t.lt(45)
            t.fd(a)
            if i == 0:
                t.rt(45)
                t.fd(a)
                t.bk(a)
                t.lt(45)
            t.lt(90)
        t.end_fill()

    t.fd(250)
    for i in range(il_ziaren):
        ziarno()
        t.rt(90)
        ziarno()
        t.lt(90)
        t.fd(2 * a)
    t.rt(45)
    ziarno()


try:
    kls(100)
except MalformedEar:
    kls(3)
