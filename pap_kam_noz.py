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
        if t == gra:
            print("remis")
        if (gra != t and gra == k and t == p
                or gra == p and t == n
                or gra == n and t == k
                or gra != c and t == c):
            print('przegral gracz,','wygrywa komputer')
            trw+=1
            print('gracz ma:', grw, 'a komputer:', trw)
        elif gra!=t:
            print('wygrywa gracz,', 'przegral komputer')
            grw+=1
            print('gracz ma:', grw, 'a komputer:', trw)
        if grw==3:
            if 3-trw==1:
                print('gracz wygrywa ',3-trw, 'punktem')
            else:
                print('gracz wygrywa ',3-trw, 'punktami')
            return
        if trw==3:
            if 3-grw==1:
                print('komputer wygrywa ',3-grw, 'punktem')
            else:
                print('komputer wygrywa ',3-grw, 'punktami')
            return
            


p_k_n_c(0, 0)
    