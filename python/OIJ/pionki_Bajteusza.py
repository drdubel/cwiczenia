def gra_bajteusza(wym_x, wym_y, il_pion, plansza_pion):
    wynik = []
    for i in range(sum([max(wym_x, wym_y)*3, wym_x, wym_y]):
        wynik.append()
    return plansza_pion, max(wynik)

def main():
    plansza_pion=[]
    poz_pion=[]
    wym_y, wym_x, il_pion=list(map(int, input().split()))
    for _ in range(il_pion):
        poz_pion.append(list(map(int, input().split())))
    for i in range(wym_y):
        plansza_pion.append([])
        for j in range(wym_x):
            if [i+1, j+1] in poz_pion:
                plansza_pion[i].append(True)
            else:
                plansza_pion[i].append(False)
    print(gra_bajteusza(wym_x, wym_y, il_pion, plansza_pion))

if __name__ == "__main__":
    main()
