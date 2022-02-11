import turtle as t
t.speed(0)

def kwadrat(kolor, dl):
    t.fillcolor(kolor)
    t.begin_fill()
    for _ in range(4):
        t.fd(dl)
        t.lt(90)
    t.end_fill()


def wie(opis):
    il_wiez = 0
    maks_wys_wiez = 1
    pop_kol = ""
    for znacz_kol in opis:
        if znacz_kol != pop_kol:
            il_wiez += 1
        else:
            maks_wys_wiez += 1
        pop_kol = znacz_kol
    maks_dl = max(maks_wys_wiez, il_wiez)
    dl = 400/maks_dl
    t.goto(t.pos()[0]-dl*(il_wiez/2), 0)
    kolory = {
        "Y": "yellow",
        "G": "green",
    }
    pop_kol = opis[0]
    for znacz_kol in opis:
        if znacz_kol != pop_kol:
            t.pu()
            t.goto(t.pos()[0]+dl, 0)
            t.pd()
        kwadrat(kolory[znacz_kol], dl)
        t.goto(t.pos()[0], t.pos()[1]+dl)
        pop_kol = znacz_kol


wie("Y")
