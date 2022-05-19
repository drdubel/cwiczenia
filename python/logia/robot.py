from turtle import*

def zkwa():
    color("green")
    begin_fill()
    for i in range(4):
        fd(30)
        rt(90)
    end_fill()

def pkwa():
    color("yellow")
    begin_fill()
    for i in range(4):
        fd(30)
        rt(90)
    end_fill()

def noga_1():
    zkwa()
    bk(30)
    zkwa()
    for i in range(5):
        lt(90)
        fd(30)
        rt(90)
        pkwa()

def brzuch():
    for i in range(5):
        lt(90)
        fd(30)
        rt(90)
        for i in range(3):
            pkwa()
            fd(30)
        bk(90) 

def reka_1():
    for i in range(3):
        bk(30)
        pkwa()
    for i in range(3):
        rt(90)
        fd(30)
        lt(90)
        pkwa()
    zkwa()

def glowa():
    lt(90)
    pu()
    fd(120)
    rt(90)
    fd(120)
    pkwa()
    for i in range(3):
        bk(30)
        lt(90)
        fd(30)
        rt(90)
        for i in range(3):
            pkwa()
            fd(30)
        bk(60)
    fd(60)
    rt(90)
    fd(30)
    lt(90)
    zkwa()

def reka_2():
    rt(90)
    pu()
    fd(90)
    lt(90)
    for i in range(3):
        pkwa()
        fd(30)
    bk(30)
    for i in range(3):
        lt(90)
        fd(30)
        rt(90)
        pkwa()
    zkwa()

def noga_2():
    rt(90)
    fd(240)
    lt(90)
    bk(90)
    for i in range(3):
        pkwa()
        fd(30)
    bk(30)
    for i in range(3):
        rt(90)
        fd(30)
        lt(90)
        pkwa()
    zkwa()
    fd(30)
    zkwa()

def robot():
    speed(0)
    shape("turtle")
    noga_1()
    brzuch()
    reka_1()
    glowa()
    reka_2()
    noga_2()

robot()
