def co_dalej(polozenie, plansza, wymiar):
    dol = False
    prawo = False
    dol1 = False
    prawo1 = False
    polozenie[1] += 1
    if polozenie[1] >= wymiar[0]:
        dol = plansza[polozenie[0]+1][polozenie[1]]
    elif polozenie[1] < wymiar[0]:
        prawo = plansza[polozenie[0]][polozenie[1]+1]
    if polozenie[0] >= wymiar[1]:
        prawo = plansza[polozenie[0]][polozenie[1]+1]
    elif polozenie[0] < wymiar[1]:
        dol = plansza[polozenie[0]+1][polozenie[1]]
    polozenie[1] -= 1
    polozenie[0] += 1
    if polozenie[1] >= wymiar[0]:
        dol1 = plansza[polozenie[0]+1][polozenie[1]]
    elif polozenie[1] < wymiar[0]:
        prawo1 = plansza[polozenie[0]][polozenie[1]+1]
    if polozenie[0] >= wymiar[1]:
        prawo1 = plansza[polozenie[0]][polozenie[1]+1]
    elif polozenie[0] < wymiar[1]:
        dol1 = plansza[polozenie[0]+1][polozenie[1]]
    polozenie[0] -= 1
    return dol, prawo, dol1, prawo1

def poruszanie_sie(polozenie, wymiar, plansza, diam, ruchy):
    odw_pol = list(reversed(polozenie))
    while odw_pol[0] < wymiar[0] or odw_pol[1] < wymiar[1]:
        if polozenie[1] >= wymiar[0]:
            polozenie[0] += 1
            ruchy += 'v'
            if polozenie[0] <= wymiar[1] and plansza[polozenie[0]][polozenie[1]] == 1:
                diam += 1
        elif polozenie[0] >= wymiar[1]:
            polozenie[1] += 1
            ruchy += '>'
            if polozenie[0] <= wymiar[1] and plansza[polozenie[0]][polozenie[1]] == 1:
                diam += 1
        else:
            prawo = plansza[polozenie[0]][polozenie[1]+1]
            dol = plansza[polozenie[0]+1][polozenie[1]]
            if prawo == dol:
                prawodol, prawoprawo, doldol, dolprawo = co_dalej(polozenie, plansza, wymiar)
                if plansza[polozenie[0]+1][polozenie[1]] == 1:
                    diam += 1
                if sum([prawodol, prawoprawo, doldol, dolprawo]) == 1:
                    if prawoprawo:
                        diam += 1
                        polozenie[1] += 2
                        ruchy += '>>'
                    elif prawodol:
                        diam += 1
                        polozenie[1] += 1
                        polozenie[0] += 1
                        ruchy += '>v'
                    elif dolprawo:
                        diam += 1
                        polozenie[1] += 1
                        polozenie[0] += 1
                        ruchy += 'v>'
                    elif doldol:
                        diam += 1
                        polozenie[0] += 2
                        ruchy += 'vv'
                else:
                    wynik1 = (0, '')
                    wynik2 = (0, '')
                    wynik3 = (0, '')
                    wynik4 = (0, '')
                    if type(prawoprawo) == int:
                        wynik1 = poruszanie_sie([polozenie[0], polozenie[1]+2], wymiar, plansza, diam+prawoprawo, ruchy+'>>')
                    if type(prawodol) == int:
                        wynik2 = poruszanie_sie([polozenie[0]+1, polozenie[1]+1], wymiar, plansza, diam+prawodol, ruchy+'>v')
                    if type(dolprawo) == int:
                        wynik3 = poruszanie_sie([polozenie[0]+1, polozenie[1]+1], wymiar, plansza, diam+dolprawo, ruchy+'v>')
                    if type(doldol) == int:
                        wynik4 = poruszanie_sie([polozenie[0]+2, polozenie[1]], wymiar, plansza, diam+doldol, ruchy+'vv')
                    return max([
                        wynik1,
                        wynik2,
                        wynik3,
                        wynik4,
                    ])
            elif prawo:
                diam += 1
                polozenie[1] += 1
                ruchy += '>'
            elif dol:
                diam += 1
                polozenie[0] += 1
                ruchy += 'v'
        odw_pol = list(reversed(polozenie))
    return diam, ruchy
        

def diamenty(il_zestawow, wymiary, plansze):
    wynik = []
    for plansza, wymiar in zip(plansze, wymiary):
        diam = 0
        ruchy = ''
        polozenie = [0, 0]
        wymiar[0] -= 1
        wymiar[1] -= 1
        if plansza[polozenie[0]][polozenie[1]] == 1:
            diam += 1
        diam, ruchy = poruszanie_sie(polozenie, wymiar, plansza, diam, ruchy)
        wynik.append(f'{str(diam)} {ruchy}')
    return wynik

def main():
    il_zestawow = int(input())
    wymiary = []
    plansze = []
    for i in range(il_zestawow):
        wymiary.append(list(map(int, input().split())))
        plansze.append([])
        for _ in range(wymiary[i][1]):
            plansze[i].append(list(map(int, input().split())))
    wyniki = diamenty(il_zestawow, wymiary, plansze)
    for wynik in wyniki:
        print(wynik)

if __name__ == "__main__":
    main()