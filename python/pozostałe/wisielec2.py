import random
import os

rys_wis = {
    1: ('____'),
    2: (' |', ' |', ' |', ' |', '_|___'),
    3: (' ____', ' |', ' |', ' |', ' |', '_|___'),
    4: (' ____', ' |  |', ' |', ' |', ' |', '_|___'),
    5: (' ____', ' |  |', ' |  O', ' |', ' |', '_|___'),
    6: (' ____', ' |  |', ' |  O', ' | !|! ', ' |', '_|___'),
    7: (' ____', ' |  |', ' |  O', ' | !|! ', ' | / \\  ', '_|___'),
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
        slowa_do_wisielcowania = open(
            r"slowa.txt",
            encoding='utf-8'
            ).read()
        slowa_do_wisielcowania = slowa_do_wisielcowania.split()
    elif n.lower() == 'nie':
        slowa_do_wisielcowania = open(
            r"Tu wpisz położenie pliku ze słowami",
            encoding='utf-8'
            ).read()
        slowa_do_wisielcowania = slowa_do_wisielcowania.split()
    wisielcowane_slowo = random.choice(slowa_do_wisielcowania)
    bez_zgad_lit = wisielcowane_slowo.lower()
    while zle_proby_zgad < dl_gry:
        if zgadywane_litery == '':
            print('_ '*len(wisielcowane_slowo))
        if slowo == ' '.join(wisielcowane_slowo):
            print(ret('WYGRAŁEŚ', '—'))
            return ret("Wisielcowanym słowem było " + wisielcowane_slowo, '—')
        aktualnie_zgad_lit = wisielcowane_slowo
        podawana_litera = input("Zgadnij literę: ")
        podawana_litera = podawana_litera.lower()
        if podawana_litera.isalpha() == False:
            print('możesz podać tylko literę!')
        elif podawana_litera in zgadywane_litery:
            print("Ta litera już była")
        elif len(podawana_litera) > 1:
            if podawana_litera == wisielcowane_slowo:
                print(ret('WYGRAŁEŚ', '—'))
                return ret(wisielcowane_slowo, '—')
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
    print(ret('PRZEGRAŁEŚ', '—'))
    return ret("Wisielcowanym słowem było " + wisielcowane_slowo, '—')


print(wisielec())
