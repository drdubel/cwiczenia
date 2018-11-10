import random
k='kamień'
p='papier'
n='nożyce'
            

def marceli():
    while True:
        gra = input("wybierz papier, nożyce czy kamień: ")
        if gra in (k, n, p):
            return gra
        print("źle!")


def p_k_n():
    gra=marceli()
    z=[p,k,n]
    t=random.choice(z)
    print("gracz:", gra)
    print("program:", t)
    if t==gra:
        print('remis')
    if t==p and gra==k:
        print('przegral gracz,','wygrywa komputer')
    if t==k and gra==p:
        print('wygrywa gracz,','przegrywa komputer')
    if t==k and gra==n:
        print('przegral gracz,','wygrywa komputer')
    if t==n and gra==k:
        print('wygrywa gracz','przegrywa komputer')
    if t==n and gra==p:
        print('przegral gracz,','wygrywa komputer')
    if t==p and gra==n:
        print('wygrywa gracz,','przegrywa komputer')
        
    
    

for i in range(3):
    p_k_n()