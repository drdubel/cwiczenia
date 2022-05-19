import os
import random

def ret(text, wyp):
    return text.center(os.get_terminal_size().columns, wyp)

def rysuj(pozycje):
    print(
    f"""
    ¹    |²    |³ 
      {pozycje[0][0]}  |  {pozycje[0][1]}  |  {pozycje[0][2]}
    _____|_____|_____
    ⁴    |⁵    |⁶
      {pozycje[1][0]}  |  {pozycje[1][1]}  |  {pozycje[1][2]} 
    _____|_____|_____
    ⁷    |⁸    |⁹
      {pozycje[2][0]}  |  {pozycje[2][1]}  |  {pozycje[2][2]}
         |     |     
    """
    )

def wygral(pozycje, znak):
    for i in range(3):
        if pozycje[i].count(znak) == 3:
            return znak
    for i in range(3):
        znaki_w_kolumnie = []
        for j in range(3):
            znaki_w_kolumnie.append(pozycje[j][i])
        if znaki_w_kolumnie.count(znak) == 3:
            return znak
    if [pozycje[0][0], pozycje[1][1], pozycje[2][2]].count(znak) == 3 or [pozycje[2][0], pozycje[1][1], pozycje[0][2]].count(znak) == 3:
        return znak
    return "Nikt"
        

def kolko_z_krzyzykiem():
    print("Położenie podawaj od 1 do 9 liczone od lewej do prawej na planszy!")
    pozycje = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    znaki = ['X', 'O']
    ruchy_pozostale = 9
    i = 0
    while ruchy_pozostale:
        znak_teraz = znaki[i%2]
        rysuj(pozycje)
        miejsce = int(input(f"Na którym miejscu chcesz umiejscowić {znak_teraz}? "))
        if pozycje[(miejsce-1)//3][(miejsce-1)%3] != ' ':
            print("To miejsce jest zajęte! Podaj tym razem niezajęte.")
        else:
            pozycje[(miejsce-1)//3][(miejsce-1)%3] = znak_teraz
            i += 1
            ruchy_pozostale -= 1
            wygrana = wygral(pozycje, znak_teraz)
            if wygrana != "Nikt":
                return ret(f"WYGRAŁ GRACZ {wygrana}", '-')

    return ret("REMIS", '-')


print(kolko_z_krzyzykiem())