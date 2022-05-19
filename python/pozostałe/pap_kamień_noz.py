import random
KA = 'kamień'
PA = 'papier'
NO = 'nożyce'
CZ = 'czarna_dz'
KO = 'komputer'
TR = 'śrut'

wygrywa = {
    KA: PA,
    PA: NO,
    NO: KA,
    KO: KA,
    PA: KO,
    NO: KO,
}

WYGRANA = 1
PRZEGRANA = -1
REMIS = 0

def sedzia(ah, oh):
    if ah == oh:
        return REMIS
    if ah == CZ:
        return WYGRANA
    if oh == CZ:
        return PRZEGRANA
    if ah == TR and oh != CZ:
        return WYGRANA
    if oh == TR and ah != CZ:
        return PRZEGRANA
    if wygrywa[ah] == oh:
        return PRZEGRANA
    else:
        return WYGRANA

def marceli(z):
    while True:
        trut = input("wybierz papier, nożyce, kamień czy czarną dziurę: ")
        if trut in z:
            return trut
        print("źle!")

def p_k_n_c(tury, pkt_b, pkt_a):
    pkt = 0
    while pkt_b <= tury or pkt_a <= tury:
        z = [PA, KA, NO, CZ, KO, TR]
        ah = marceli(z)
        oh = random.choice(z)
        koniec = sedzia(ah, oh)
        pkt += koniec
        print('komputer wybrał:', oh)
        print('gracz wybrał:', ah)
        if koniec == REMIS:
            print('remis')
            print('gracz ma', pkt_b, 'a komputer', pkt_a) 
        if koniec == WYGRANA:
            print('wygrał gracz')
            pkt_b += 1
            print('gracz ma', pkt_b, 'a komputer', pkt_a) 
        if koniec == PRZEGRANA:
            print('przegrał gracz a wygrał komputer')
            pkt_a += 1
            print('gracz ma', pkt_b, 'a komputer', pkt_a)
        if pkt_b == 3:
            if tury - pkt_a == 1:
                print('gracz wygrał', 'jednym punktem')
            else:
                print('gracz wygrał', tury - pkt_a, 'punktami')
            return
        if pkt_a == 3:
            if tury - pkt_b == 1:
                print('komputer wygrał', 'jednym punktem')
            else:
                print('komputer wygrał', tury - pkt_b, 'punktami')
            return
    


p_k_n_c(3, 0, 0)