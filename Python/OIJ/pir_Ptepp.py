def ile_spos(il_pol, dzielnik, lista_pol):
    wynik = []
    for i in range(2, il_pol+1):
        if lista_pol[i] == 0:
            wynik.append(0)
        else:
            
    return wynik[len(wynik)-1]%dzielnik

def main():
    il_pol, dzielnik = list(map(int, input().split()))
    list_pol = int(input())
    print(ile_spos(il_pol, dzielnik, list_pol))

if __name__ == "__main__":
    main()