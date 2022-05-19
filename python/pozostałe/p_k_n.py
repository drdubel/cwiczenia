import random
import os

class MalformedGameLength(Exception):
    pass

def ret(text, wyp):
    return text.center(os.get_terminal_size().columns, wyp)

def nowe_p_k_n():
    gameLength = input("Gramy do: ")
    try:
        gameLength = int(gameLength)       
    except ValueError:
        raise MalformedGameLength("musisz podać liczbę, nie słowo")
    mozliwosci = ['kamień', 'papier', 'nożyce']
    wynik_gracza = 0
    wynik_komputera = 0   
    while wynik_gracza < gameLength or wynik_komputera < gameLength:
        zle = 0
        gracz = input("co wybierasz: ")
        komputer = random.choice(mozliwosci)
        for mozliwosc in mozliwosci:
            if mozliwosc != gracz:
                zle += 1
            if zle == 3:
                print(ret("Żle", '–'))
        if gracz == "nożyce":
            if komputer == "papier":
                wynik_gracza += 1
            if komputer == "kamień":
                wynik_komputera += 1
        elif gracz == "kamień":
            if komputer == "nożyce":
                wynik_gracza += 1
            if komputer == "papier":
                wynik_komputera += 1
        elif gracz == "papier":
            if komputer == "kamień":
                wynik_gracza += 1
            if komputer == "nożyce":
                wynik_komputera += 1
        wynik = 'wynik_komputera to '+str(wynik_komputera), 'wynik_gracza to '+str(wynik_gracza)
        wynik = ' a '.join(wynik).upper()
        print(ret(wynik, '–'))
        if wynik_komputera == gameLength:
            print(ret('', ' '))
            print(ret("WYGRAŁ KOMPUTER", '–'))
            return
        if wynik_gracza == gameLength:
            print(ret('', ' '))
            print(ret("WYGRAŁ GRACZ", '–'))
            return

nowe_p_k_n()