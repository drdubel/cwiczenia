import turtle
t = turtle.Pen()
t.speed(0)

class MalformedTile(Exception):
    pass

def kwadrat():
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(4):
        t.fd(24)
        t.lt(90)
    t.end_fill()

def kafelki2():
    t.lt(30)
    kwadrat()
    t.fd(24)
    t.pu()
    t.sety(t.ycor()+(24**2 - 12**2)**(1/2))
    t.setx(t.xcor()-12)
    t.lt(30)
    t.pd()
    kwadrat()

def kafelki4():
    kafelki2()
    t.fd(24)
    t.rt(30)
    t.fd(24)
    t.lt(180)
    kwadrat()
    t.pu()
    t.fd(24)
    t.sety(t.ycor()-(24**2 - 12**2)**(1/2))
    t.setx(t.xcor()+12)
    t.lt(30)
    t.pd()
    kwadrat()
    t.fd(24)
    t.lt(90)
    t.fd(24)
    t.lt(30)
    t.pu()
    t.fd(24)
    t.pd()

def posadzka(n):
    if n < 2:
        raise MalformedTile("za mało kafelków, nie mniej niż 2")
    if n > 12:
        raise MalformedTile("za dużo kafelków, nie więcej niż 12")
    if n%2 != 0:
        raise MalformedTile("liczba jest nieparszysta, musi być parzysta")
    for i in range(n//2):
        for i in range(n-2):
            kafelki4()
        t.pu()
        t.sety(t.ycor()+24+(24**2 - 12**2)**(1/2)*2)
        t.setx(0)
        t.pd()


posadzka(12)
