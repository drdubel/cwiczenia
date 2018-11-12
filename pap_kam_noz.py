import random
k='kamień'
p='papier'
n='nożyce'
c='czarna_dz'

def marceli():
    while True:
        gra = input("wybierz papier, nożyce, kamień czy czarną dziurę: ")
        if gra in (k, n, p, c):
            return gra
        print("źle!")


def p_k_n_c(grw, trw):
    while grw or trw<3:
        gra=marceli()
        z=[p,k,n,c]
        t=random.choice(z)
        print("gracz:", gra)
        print("program:", t)
        if t==gra:
            print('remis')
            print('gracz ma:', grw, 'a komputer:', trw)
        if t==p and gra==k:
            print('przegral gracz,','wygrywa komputer')
            trw+=1
            print('gracz ma:', grw, 'a komputer:', trw)
        if t==k and gra==p:
            r=print('wygrywa gracz,','przegrywa komputer')
            grw+=1
            print('gracz ma:', grw, 'a komputer:', trw)
        if t==k and gra==n:
            g=print('przegral gracz,','wygrywa komputer')
            trw+=1
            print('gracz ma:', grw, 'a komputer:', trw)
        if t==n and gra==k:
            print('wygrywa gracz,','przegrywa komputer')
            grw+=1
            print('gracz ma:', grw, 'a komputer:', trw)
        if t==n and gra==p:
            print('przegral gracz,','wygrywa komputer')
            trw+=1
            print('gracz ma:', grw, 'a komputer:', trw)
        if t==p and gra==n:
            print('wygrywa gracz,','przegrywa komputer')
            grw+=1
            print('gracz ma:', grw, 'a komputer:', trw)
        if t==c and gra != c:
            print('przegral gracz,','wygrywa komputer')
            trw+=1
            print('gracz ma:', grw, 'a komputer:', trw)
        if t!=c and gra == c:
            print('wygrywa gracz,','przegrywa komputer')
            grw+=1
            print('gracz ma:', grw, 'a komputer:', trw)
        if grw==3:
            print('gracz wygrywa ',3-trw, 'punktami')
            return
        if trw==3:
            print('komputer wygrywa ',3-grw, 'punktami')
            return
            


p_k_n_c(0 ,0)
    