import random
k='kamień'
p='papier'
n='nożyce'

def p_k_n():
    gra=input('co wybierasz? ')
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
    
    

while True:
    p_k_n()