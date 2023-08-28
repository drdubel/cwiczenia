import random
import os

WYGRANA = 1
PRZEGRANA = -1

pkn = {
    "pistolet": r"""
 _ __________________,
  \@([____]__________)
  _/\|--[___]
 /     /(()
/______|
\_____/
""",
    "kamień": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "papier": """
    ________
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "nożyce": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
}

KA = "kamień"
PA = "papier"
NO = "nożyce"
PT = "pistolet"

mozliwosci = ["kamień", "papier", "nożyce", "pistolet"]

wygrana = {
    PA: KA,
    NO: PA,
    KA: NO,
}
przegrana = {
    KA: PA,
    PA: NO,
    NO: KA,
}


class GraczChytry:
    def __init__(self, do_ilu_gramy):
        self.tury = do_ilu_gramy
        self.poprzedni = None

    def wybierz(self):
        if self.poprzedni:
            if self.poprzedni == PT:
                return KA
            else:
                print(przegrana[self.poprzedni])
                print(wygrana[self.poprzedni])
                return przegrana[self.poprzedni]
        else:
            return random.choice(mozliwosci)

    def wynik(self, token, wygrana):
        self.tury -= 1
        self.poprzedni = token


def smart_input(prompt, validator):
    while True:
        val = input(prompt)
        try:
            if validator(val):
                return val
        except ValueError:
            pass


def ret(text, wyp):
    return text.center(os.get_terminal_size().columns, wyp)


def sedzia(komputer, gracz, sztuczny):
    if komputer == PT and gracz != KA and gracz != PT:
        sztuczny.wynik(gracz, True)
        return PRZEGRANA
    elif komputer == PT and gracz == KA:
        sztuczny.wynik(gracz, False)
        return WYGRANA
    elif gracz == PT and komputer != KA and komputer != PT:
        sztuczny.wynik(gracz, False)
        return WYGRANA
    elif gracz == PT and komputer == KA:
        sztuczny.wynik(gracz, True)
        return PRZEGRANA
    elif wygrana[komputer] == gracz:
        sztuczny.wynik(gracz, True)
        return PRZEGRANA
    elif wygrana[gracz] == komputer:
        sztuczny.wynik(gracz, False)
        return WYGRANA


def nowe_p_k_n():
    gameLength = int(smart_input("Gramy do: ", int))
    sztuczny = GraczChytry(gameLength)
    wynik_gracza = 0
    wynik_komputera = 0
    while wynik_gracza < gameLength or wynik_komputera < gameLength:
        gracz = smart_input("co wybierasz: ", lambda x: x in mozliwosci)
        komputer = sztuczny.wybierz()
        wyniki = sedzia(komputer, gracz, sztuczny)
        if wyniki == PRZEGRANA:
            wynik_komputera += 1
        elif wyniki == WYGRANA:
            wynik_gracza += 1
        print("GRACZ: ", pkn[gracz], "KOMPUTER: ", pkn[komputer], sep="\n")
        wynik = "wynik_komputera to " + str(wynik_komputera), "wynik_gracza to " + str(
            wynik_gracza
        )
        wynik = " a ".join(wynik).upper()
        print(ret(wynik, "–"))
        if wynik_komputera == gameLength:
            print("\n", ret("WYGRAŁ KOMPUTER", "–"), sep="")
            break
        if wynik_gracza == gameLength:
            print("\n", ret("WYGRAŁ GRACZ", "–"), sep="")
            break


nowe_p_k_n()
