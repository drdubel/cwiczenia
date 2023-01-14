import random
import turtle

t = turtle.Pen()
a = ("green", "blue", "red")


def losowy_kolor():
    return (random.random(), random.random(), random.random())


def cegla(wielkosc, kolor=None):
    if kolor:
        t.color("black", kolor)
        t.begin_fill()
    for i in range(2):
        t.fd(wielkosc)
        t.left(90)
        t.fd(wielkosc / 1.5)
        t.left(90)
    if kolor:
        t.end_fill()
    t.fd(wielkosc)


def piramida(wk, ile_cg):
    t.speed(0)
    for i in range(ile_cg):
        for i in range(ile_cg):
            cegla(wk, kolor=losowy_kolor())
        if ile_cg > 1:
            t.left(90)
            t.fd(wk / 1.5)
            t.left(90)
            t.fd(wk * ile_cg - wk / 2)
            t.right(180)
            ile_cg -= 1


piramida(30, 10)
