import turtle as t
t.speed(0)


def wielokat(ile_katow):
    for i in range(ile_katow):
        t.forward(600/ile_katow)
        t.left(360/ile_katow)


def kwiatek(ile_platkow, ile_katow):
    for i in range(ile_platkow):
        wielokat(ile_katow)
        t.left(360/ile_platkow) 


def kwiat(ile_platkow):
    for i in range(ile_platkow):
        wielokat(ile_platkow)
        t.forward(600/ile_platkow)
        t.rt(360/ile_platkow)


def lodyga(dlugosc_lodygi):
    t.rt(90)
    t.fd(dlugosc_lodygi)
    t.rt(180)
    t.fd(dlugosc_lodygi + 200)
    t.rt(90)
    
lodyga(int(input()))
for i in range(3, 11):
    kwiatek(i, i)




input('nacisnij enter')
