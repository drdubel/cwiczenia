def odAdoB(start, drogi, koniec):
    poziomy = {0: [start]}
    poziom = 0
    byly = [start]
    while poziom in poziomy:
        for numer in poziomy[poziom]:
            #print(poziomy, drogi[numer], numer)
            if drogi[numer]:
                numery_teraz = drogi[numer]
                if poziom+1 in poziomy:
                    poziomy[poziom+1].append(numery_teraz)
                else:
                    poziomy.update([[poziom+1, numery_teraz]])
                for numer_sprawdz in numery_teraz:
                    if numer_sprawdz in byly:
                        #print(numer_sprawdz, byly, poziomy[poziom+1], numer)
                        poziomy[poziom+1].remove(numer_sprawdz)
                    else:
                        byly.append(numer_sprawdz)
        poziom += 1
    lista_wyn = {}
    for i in poziomy:
        for j in poziomy[i]:
            lista_wyn[j] = i
    return lista_wyn[koniec]

def main():
    il_miast, il_autos = list(map(int, input().split()))
    skad, dokad = list(map(int, input().split()))
    drogi = {}
    for i in range(1, il_miast+1):
        drogi.update([[i, []]])
    for _ in range(il_autos):
        droga = list(map(int, input().split()))
        drogi[droga[0]].append(droga[1])
    if skad == dokad:
        return 0
    return odAdoB(skad, drogi, dokad)

if __name__ == "__main__":
    print(main())
