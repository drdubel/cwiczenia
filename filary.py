import turtle 
import math
t = turtle.Pen()
t.shape("turtle")
t.lt(90)
t.speed(0)

class Klasa(Exception):
    pass

def filar(a):
    t.lt(45)
    t.fd(a)
    t.lt(45)
    t.fd(a*(2/3))
    t.lt(45)
    t.fillcolor("green")
    t.begin_fill()
    for i in range(4):
        t.fd(a)
        t.lt(90)
    t.end_fill()
    t.rt(90)
    t.bk(a)
    t.rt(135)
    t.fd(a*(2/3))
    for i in range(2):
        t.rt(135)
        t.fd(a)
        t.rt(45)
        t.fd(a*(2/3))

def filary2(a):
    przekatna = math.sqrt(a**2*2)
    t.pu()
    x = t.xcor()
    print(x)
    t.setx(x-2/3*a)
    y = t.ycor()
    t.sety(y-przekatna)
    t.pd()
    t.rt(90)
    filar(a)
    t.pu()
    t.fd(4/3*a)
    t.pd()
    t.rt(90)
    filar(a)
    t.pu()
    t.fd(2/3*a)
    t.rt(90)
    t.bk(przekatna)
    t.lt(90)
    t.pd()
    t.rt(90)
    filar(a)
    t.rt(90)
    filar(a)

    

def filary(x, y):
    a = int(input("podaj wielkość filarów: "))
    print(t.pos())
    if x > 12 or x < 2 or x % 2 > 0:
        raise Klasa("zła liczba filarów, może być od 2 do 12 i musi być parzysta!")
    if y > 11 or y < 1 or y % 2 == 0:
        raise Klasa("zła liczba filarów, może być od 1 do 11 i musi być nieparzysta!")
    filar(a)
    t.rt(90)
    filar(a)
    for i in range(y//2):
        filary2(a)
    if x > 1:
        for i in range(x//2-1):
            t.pu()
            t.bk(5.55*a)
            t.rt(90)
            t.fd(42.5/30*a*(y-1))
            t.pd()
            filar(a)
            t.rt(90)
            filar(a)
            for i in range(y//2):
                filary2(a)

filary(4, 5)