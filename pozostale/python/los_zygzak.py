import turtle
import random

t = turtle.Pen()


def los_zygzak():
    while True:
        t.color(random.random(), random.random(), random.random())
        t.speed(0)
        t.fd(random.randrange(0, 200))
        t.right(random.randrange(0, 1000))
        if t.distance(0, 0) > 300:
            t.goto(0, 0)


los_zygzak()
