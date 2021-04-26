import random
import os
import pickle
import string

class MalformedHangman(Exception):
    pass

n = input('Chcesz z odmianami? ')
if n.lower() == 'tak':
    slowa_do_wisielcowania = open(r"/home/antek/Katalog_Antka/cwiczenia/pozostałe/slowa.txt", encoding='utf-8').read()
    slowa_do_wisielcowania = slowa_do_wisielcowania.split()
elif n.lower() == 'nie':
    slowa_do_wisielcowania = open(r"c:/Users/antek/wisielecslowa.txt", encoding='utf-8').read()
    slowa_do_wisielcowania = slowa_do_wisielcowania.split()
else:
    raise MalformedHangman('musisz podać tak albo nie')

rys_wis = {
    1: ('_____'),
    2: (' |', ' |', ' |', ' |', '_|___'),
    3: (' ____', ' |', ' |', ' |', ' |', '_|___'),
    4: (' ____', ' |  |', ' |', ' |', ' |', '_|___'),
    5: (' ____', ' |  |', ' |  O', ' |', ' |', '_|___'),
    6: (' ____', ' |  |', ' |  O', ' | !|! ', ' |', '_|___'),
    7: (' ____', ' |  |', ' |  O', ' | !|! ', ' | / \\  ', '_|___'),
}

def ret(text, wyp):
    return text.center(os.get_terminal_size().columns, wyp)

def roz_wisielca(w_s, z_p_z, ils, lit_val, il, slowa, slow, dzl, podp_il):
    l = len(w_s)
    a = []
    if z_p_z == 6:
        if podp_il > 0:
            return 'podpowiedź'
        for slowo in slowa:
            if len(slowo) == l:
                a.append(slowo)
        for slowo2 in a:
            e = 0
            for i in range(len(slowo2)):
                if slow[i] == '_' or slow[i] == slowo2[i]:
                    e += 1
                if e == len(slowo2):
                    return slowo2
    else:
        return ils[il[lit_val]]

def wisielec(slowa_do_wisielcowania):
    slow = ''
    lit_val = 0
    dl_gry = 7
    dobrze_zgadniete_litery = ''
    zle_proby_zgad = 0
    slowo = ''
    zgadywane_litery = ''
    wisielcowane_slowo = random.choice(slowa_do_wisielcowania)
    slowaw = []
    dl_wisielcowanego = len(wisielcowane_slowo)
    for slowo_dl in slowa_do_wisielcowania:
        if len(slowo_dl) == dl_wisielcowanego:
            slowaw.append(slowo_dl)
    slowa_do_wisielcowania = ''.join(slowa_do_wisielcowania)
    il_lit = []
    string.ascii_lowercase += 'śąńźżęłó'
    for litera in string.ascii_lowercase:
        il_lit.append(slowa_do_wisielcowania.count(litera))
    il_lit_slow = dict(zip(il_lit, string.ascii_lowercase))
    il_lit.sort(reverse=True)
    podp_il = 0
    #if len(wisielcowane_slowo) < 4:
        #podp_il = 1
    #else:
        #podp_il = len(wisielcowane_slowo)//4
    bez_zgad_lit = wisielcowane_slowo.lower()
    while zle_proby_zgad < dl_gry:
        if zgadywane_litery == '':
            pass
        if slowo == ' '.join(wisielcowane_slowo):
            print(ret("Wisielcowanym słowem było " + wisielcowane_slowo, '–'))
            return ret('WYGRAŁEŚ', '–')
        aktualnie_zgad_lit = wisielcowane_slowo
        podawana_litera = podawana_litera = roz_wisielca(wisielcowane_slowo, zle_proby_zgad, il_lit_slow, lit_val, il_lit, slowaw, slow, dobrze_zgadniete_litery, podp_il)
        if podawana_litera == 'podpowiedź':
            podawana_litera = random.choice(bez_zgad_lit)
            podp_il -= 1
            if podp_il == 0:
                print('NIE MASZ JUŻ PODPOWIEDZI')
            elif podp_il == 1:
                print(f'ZOSTAŁA CI {podp_il} PODPOWIEDŹ')
            elif podp_il > 1:
                print(f'ZOSTAŁY CI {podp_il} PODPOWIEDZI')
        lit_val += 1
        podawana_litera.isalpha()
        if podawana_litera in zgadywane_litery:
            continue
        elif len(podawana_litera) > 1:
            if podawana_litera == wisielcowane_slowo:
                print(ret("Wisielcowanym słowem było " + wisielcowane_slowo, '–'))
                return ret('WYGRAŁEŚ', '–')
            else:
                zle_proby_zgad += 3
        else:
            podawana_litera = podawana_litera.lower()
            if podawana_litera in wisielcowane_slowo:
                bez_zgad_lit = bez_zgad_lit.replace(podawana_litera, '')
                dobrze_zgadniete_litery += podawana_litera
                zgadywane_litery += podawana_litera
            else:
                zle_proby_zgad += 1
                zgadywane_litery += podawana_litera
            for litera in bez_zgad_lit:
                aktualnie_zgad_lit = aktualnie_zgad_lit.replace(litera, '_')
            slow = aktualnie_zgad_lit
            slowo = ' '.join(aktualnie_zgad_lit)
            print(zle_proby_zgad, slowo, ', '.join(zgadywane_litery), sep='\n')
            if zle_proby_zgad > 1:
                print('\n'.join(rys_wis[zle_proby_zgad]))
            elif zle_proby_zgad == 1:
                print(rys_wis[zle_proby_zgad])
    print(ret("Wisielcowanym słowem było " + wisielcowane_slowo, '–'))
    return ret('PRZEGRAŁEŚ', '–')

#proby = 10
#wynik = 0
#for i in range(proby):
#    if wisielec(slowa_do_wisielcowania) == ret('WYGRAŁEŚ', '–'):
#        wynik += 1
#    i += proby//100
#    print('Loading'+'#'*(i//(proby//100)), f'{i/(proby/100)}%', end="\r")

#print('\n', f'{wynik}/{proby}', sep='')

print(wisielec(slowa_do_wisielcowania))