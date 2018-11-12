import turtle
t=turtle.Pen()
kratka = 7

def puzel():
    t.speed(0)
    t.down()
    t.color('black', 'red')
    t.begin_fill()
    for i in range(4):
        t.fd(kratka*2)
        t.left(90)
        t.fd(kratka)
        t.right(90)
        t.fd(kratka)
        t.right(90)
        t.fd(kratka)
        t.left(90)
        t.fd(kratka*2)
        t.left(90)
    t.end_fill()
    t.up()


def laczenie(kolor):
    t.down()
    t.color('black', kolor)
    t.begin_fill()
    t.fd(kratka*2)
    t.right(90)
    t.fd(kratka)
    t.right(90)
    t.fd(kratka*3)
    t.right(90)
    t.fd(kratka)
    t.right(90)
    t.fd(kratka*2)
    t.end_fill()
    t.up()


def rzad_puzli(ile):
    for i in range(ile):
        puzel()
        if i>0:
            t.fd(kratka*5)
            t.left(90)
            t.fd(kratka*3)
            t.right(90)
            laczenie('green')
            t.right(90)
            t.fd(kratka*3)
            t.left(90)
            puzel()
 
    
def puzelzlaczeniem():
    puzel()
    t.fd(kratka*3)
    t.right(90)
    laczenie('yellow')
    t.bk(kratka)
    t.left(90)
    t.bk(kratka*3)


def rzadzlaczeniem(ile):
    puzelzlaczeniem()
    if ile>0:
        for i in range(ile):
            t.fd(kratka*5)
            t.left(90)
            t.fd(kratka*3)
            t.right(90)
            laczenie('green')
            t.right(90)
            t.fd(kratka*3)
            t.left(90)
            puzelzlaczeniem()


def piramida(ile):
    rzad_puzli(ile)
    if ile==2:
        t.left(90)
        t.fd(kratka*6)
        t.right(90)
        puzelzlaczeniem()
    if ile>2:
        ile-=1
        while ile>0:
            ile=ile-1
            t.left(90)
            t.fd(kratka*6)
            t.left(90)
            t.fd(kratka*ile*6)
            t.left(180)
            rzadzlaczeniem(ile)