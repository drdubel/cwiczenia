def blekitne_marchwie(wymiary, pole):
    wynik = 1
    polozenie = []
    for szer in range(wymiary[1]):
        for wys in range(wymiary[0]):
            if pole[wys][szer] == 'x':
                polozenie.append([szer, wys])
    for szer in range(wymiary[1]):
        
    return polozenie

def main():
    wymiary = [int(i) for i in input().split()]
    pole = []
    for _ in range(wymiary[0]):
        pole.append(input())
        assert len(pole[len(pole)-1]) == wymiary[1]
    print(blekitne_marchwie(wymiary, pole))

if __name__ == "__main__":
    main()