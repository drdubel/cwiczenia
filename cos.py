from turtle import*
import random

def fig(katy, dl):
  r = random.randrange(-255, 255)
  g = random.randrange(-255, 255)
  b = random.randrange(-255, 255)
  for i in range(katy):
    color(r, g, b)
    fd(dl)
    lt(360/katy)
    r = random.randrange(-255, 255)
    g = random.randrange(-255, 255)
    b = random.randrange(-255, 255)

def cos(il, il2, dl):
  speed(0)
  r = 0
  g = 0
  b = 0
  for i in range(il):
    color(r, g, b)
    fig(20, dl)
    rt(360/il2)
    r = random.randrange(-255, 255)
    g = random.randrange(-255, 255)
    b = random.randrange(-255, 255)

cos(100, 100.0, 50)