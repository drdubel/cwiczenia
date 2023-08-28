import turtle
import math

t = turtle.Pen()
t.speed(0)
t.lt(90)


def red_propeller(a):
    b = a / 10
    t.fd(b * 4)
    t.fillcolor("red")
    t.begin_fill()
    t.rt(60)
    for i in range(3):
        t.fd(b)
        t.lt(120)
    t.lt(60)
    t.end_fill()
    t.fd(b)
    t.begin_fill()
    t.lt(90)
    t.fd(2 * b)
    t.rt(135)
    t.fd(math.sqrt((2 * b) ** 2 * 2))
    t.end_fill()
    t.begin_fill()
    t.fd(math.sqrt((3 * b) ** 2 * 2))
    t.lt(135)
    t.fd(3 * b)
    t.lt(90)
    t.fd(a)
    t.end_fill()
    t.lt(180)


def green_propeller(a):
    b = a / 10
    t.fd(b * 4)
    t.fillcolor("green")
    t.begin_fill()
    t.lt(60)
    for i in range(3):
        t.fd(b)
        t.rt(120)
    t.rt(60)
    t.end_fill()
    t.fd(b)
    t.begin_fill()
    t.rt(90)
    t.fd(2 * b)
    t.lt(135)
    t.fd(math.sqrt((2 * b) ** 2 * 2))
    t.end_fill()
    t.begin_fill()
    t.fd(math.sqrt((3 * b) ** 2 * 2))
    t.rt(135)
    t.fd(3 * b)
    t.rt(90)
    t.fd(a)
    t.end_fill()
    t.rt(180)


def wiatrak():
    for i in range(6):
        red_propeller(250)
        t.left(30)
        green_propeller(125)
        t.left(30)


wiatrak()
