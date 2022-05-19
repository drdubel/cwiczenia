import turtle as t
t.speed(0)


def kwadrat(dl_boku, kolor):
    t.fillcolor(kolor)
    t.begin_fill()
    for _ in range(4):
        t.fd(dl_boku)
        t.lt(90)
    t.end_fill()


def cztery_kwa(bok, kolory, i, n, dl_kwadracika, il_kwa_zro):
    for _ in range(4):
        kwadrat(bok, kolory[i % 2])
        t.pu()
        if i > 0:
            t.fd(400-dl_kwadracika*il_kwa_zro)
        else:
            t.fd(400)
        t.pd()
        t.lt(90)


def mozaika(n):
    kolory = ["green", "orange"]
    dl_kwadracika = 400/(n*2+n*(n-1))
    bok = dl_kwadracika*2
    il_kwa_zro = 0
    t.pu()
    t.goto(-200, -200)
    t.pd()
    for i in range(n-1):
        cztery_kwa(bok, kolory, i, n, dl_kwadracika, il_kwa_zro)
        x = t.pos()[0]
        y = t.pos()[1]
        t.pu()
        t.goto(x+bok/2, y+bok/2)
        t.pd()
        il_kwa_zro += bok/dl_kwadracika
        bok += 2*dl_kwadracika
    kwadrat(bok, kolory[(i+1) % 2])


mozaika(int(input()))
