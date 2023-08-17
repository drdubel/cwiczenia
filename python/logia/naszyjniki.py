def naszyjniki(liczba):
    liczba = int(liczba)
    slo_kolor = {
        "1": "czerwony",
        "2": "niebieski",
        "3": "zielony",
        "4": "niebieski",
        "5": "bialy",
        "6": "zielony",
        "7": "czerwony",
        "8": "zielony",
        "9": "niebieski",
        "czerwony": "1",
        "zielony": "3",
        "niebieski": "2",
        "bialy": "5",
    }
    poz_najw = len(str(liczba))
    kolory = []
    for cyfra in str(liczba):
        kolory.append(slo_kolor[cyfra])
    for i in range(len(str(liczba)) // 2):
        if kolory[i] != kolory[len(kolory) - i - 1]:
            while kolory[i] != kolory[len(kolory) - i - 1]:
                poz_najw = len(kolory) - i - 1
                liczba += 1 * (10**i)
                kolory = []
                for cyfra in str(liczba):
                    kolory.append(slo_kolor[cyfra])
    liczba_poprawiona = str(liczba)[: poz_najw + 1]
    for j in range(poz_najw + 1, len(kolory)):
        liczba_poprawiona += slo_kolor[kolory[j]]
    return liczba_poprawiona


if __name__ == "__main__":
    print(naszyjniki(input()))
