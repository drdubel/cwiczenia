import turtle
t = turtle.Pen()
t.speed(0)

def kwadrat(wyp, dl):
    if wyp:
        t.fillcolor("grey")
        t.begin_fill()
    for i in range(4):
        t.fd(dl)
        t.lt(90)
    if wyp:
        t.end_fill()
    y = t.ycor()
    t.sety(y+dl)
    t.fillcolor("white")

def tabela(litera, dl):
    cyf = ord(litera)-97 
    if cyf == -65:
        t.pu()
        t.fd(dl*2)
        t.pd()
    else:
        for i in range(13):
            if cyf == i:
                kwadrat(True, dl) 
            else:
                kwadrat(False, dl)
        y = t.ycor()
        t.sety(y-dl*13)
        t.fd(dl)
        for i in range(13, 0, -1):
            if cyf == i+12:
                kwadrat(True, dl) 
            else:
                kwadrat(False, dl)
        t.fd(dl)
        y = t.ycor()
        t.sety(y-dl*13)

def koduj(napis):
    for litera in napis:
        tabela(litera, 20)

koduj("tata madry jest")