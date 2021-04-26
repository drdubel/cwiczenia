import random
import os
import pickle

rys_wis = {
    1: ('____'),
    2: (' |', ' |', ' |', ' |', '_|___'),
    3: (' ____', ' |', ' |', ' |', ' |', '_|___'),
    4: (' ____', ' |  |', ' |', ' |', ' |', '_|___'),
    5: (' ____', ' |  |', ' |  \1', ' |', ' |', '_|___'),
    6: (' ____', ' |  |', ' |  \1', ' | !|! ', ' |', '_|___'),
    7: (' ____', ' |  |', ' |  \1', ' | !|! ', ' | / \\  ', '_|___'),
}

def ret(text, wyp):
    return text.center(os.get_terminal_size().columns, wyp)

def wisielec():
    dl_gry = 7
    dobrze_zgadniete_litery = ''
    zle_proby_zgad = 0
    slowo = ''
    zgadywane_litery = ''
    n = input('Chcesz z odmianami czy nie? ')
    if n.lower() == 'tak':
        slowa_do_wisielcowania = open(r"/home/antek/Katalog_Antka/cwiczenia/pozostałe/slowa.txt", encoding='utf-8').read()
        slowa_do_wisielcowania = slowa_do_wisielcowania.split()
    elif n.lower() == 'nie':
        slowa_do_wisielcowania = open(r"~/wisielecslowa.txt", encoding='utf-8').read()
        slowa_do_wisielcowania = slowa_do_wisielcowania.split()
    wisielcowane_slowo = random.choice(slowa_do_wisielcowania)
    if len(wisielcowane_slowo) < 4:
        podp_il = 1
    else:
        podp_il = len(wisielcowane_slowo)//4
    bez_zgad_lit = wisielcowane_slowo.lower()
    while zle_proby_zgad < dl_gry:
        if zgadywane_litery == '':
            print('_ '*len(wisielcowane_slowo))
        if slowo == ' '.join(wisielcowane_slowo):
            print(ret('WYGRAŁEŚ', '–'))
            return ret("Wisielcowanym słowem było " + wisielcowane_slowo, '–')
        aktualnie_zgad_lit = wisielcowane_slowo
        if podp_il == 0:
            print('NIE MASZ JUŻ PODPOWIEDZI')
        elif podp_il == 1:
            print(f'ZOSTAŁA CI {podp_il} PODPOWIEDŹ')
        elif podp_il > 1:
            print(f'ZOSTAŁY CI {podp_il} PODPOWIEDZI')
        podawana_litera = input("Zgadnij literę: ")
        if podawana_litera == 'podpowiedź':
            podawana_litera = random.choice(bez_zgad_lit)
            podp_il -= 1
        podawana_litera = podawana_litera.lower()
        if podawana_litera.isalpha() == False:
            print('możesz podać tylko literę!')
        elif podawana_litera in zgadywane_litery:
            print("Ta litera już była")
        elif len(podawana_litera) > 1:
            if podawana_litera == wisielcowane_slowo:
                print(ret('WYGRAŁEŚ', '–'))
                return ret(wisielcowane_slowo, '–')
            else:
                zle_proby_zgad += 3
        else:
            if podawana_litera in wisielcowane_slowo:
                bez_zgad_lit = bez_zgad_lit.replace(podawana_litera, '')
                dobrze_zgadniete_litery += podawana_litera
                zgadywane_litery += podawana_litera
            else:
                zle_proby_zgad += 1
                zgadywane_litery += podawana_litera
            for litera in bez_zgad_lit:
                aktualnie_zgad_lit = aktualnie_zgad_lit.replace(litera, '_')
            slowo = ' '.join(aktualnie_zgad_lit)
            print(zle_proby_zgad, slowo, ', '.join(zgadywane_litery), sep='\n')
            if zle_proby_zgad > 1:
                print('\n'.join(rys_wis[zle_proby_zgad]))
            elif zle_proby_zgad == 1:
                print(rys_wis[zle_proby_zgad])
    print(ret('PRZEGRAŁEŚ', '–'))
    return ret("Wisielcowanym słowem było " + wisielcowane_slowo, '–') 

print(wisielec())