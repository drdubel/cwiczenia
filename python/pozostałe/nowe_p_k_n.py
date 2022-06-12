import random
import os
PRZEGRANA = -1
WYGRANA = 1

pkn = {
"pistolet":
r"""
 _ __________________,
  \@([____]__________)
  _/\|--[___]
 /     /(()
/______|
\_____/
""",
"kamień":
"""
    _______
---"   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", 
"papier":
"""
    ________
---"    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"nożyce":
"""
    _______
---"   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

KA = "kamień"
PA = "papier"
NO = "nożyce"
PT = "pistolet"

mozliwosci = ["kamień", "papier", "nożyce", "pistolet"]

wygrana = {
    PA: KA,
    NO: PA,
    KA: NO
}
wygrana2 = {
    PT: PA,
    KA: PT,
    NO: PT
}


def madry_komputer(z_gracza, pop_z_gracza, pop_z_gracza2):
    if pop_z_gracza2 == pop_z_gracza and pop_z_gracza != "":
        if pop_z_gracza == PT:
            print("return KA")
            return KA
        else:
            print("wygrana[wygrana[pop_z_gracza]]1")
            return wygrana[wygrana[pop_z_gracza]]
    elif pop_z_gracza2 == KA and pop_z_gracza == PA:
        return PT
    elif pop_z_gracza2 == KA and pop_z_gracza == PT:
        return PT
    elif pop_z_gracza2 == NO and pop_z_gracza == PA:
        return KA
    elif pop_z_gracza2 == KA and pop_z_gracza == NO:
        return PT
    elif pop_z_gracza2 == NO and pop_z_gracza == PT:
        return PA
    elif pop_z_gracza2 == PT and pop_z_gracza == PA:
        return KA
    else:
        if pop_z_gracza != "" and pop_z_gracza != PT:
            print("wygrana[wygrana[pop_z_gracza]]2")
            return wygrana[wygrana[pop_z_gracza]]
        elif pop_z_gracza == PT:
            print("wygrana2[wygrana2[pop_z_gracza]]3")
            return wygrana[wygrana2[pop_z_gracza]]
        else:
            print("random.choice(mozliwosci)")
            return random.choice(mozliwosci)


def ret(text, wyp):
    return text.center(os.get_terminal_size().columns, wyp)


def sedzia(komputer, gracz):
    if komputer == PT and gracz != KA and gracz != PT:
        return PRZEGRANA
    if komputer == PT and gracz == KA:
        return WYGRANA
    if gracz == PT and komputer != KA and komputer != PT:
        return WYGRANA
    if gracz == PT and komputer == KA:
        return PRZEGRANA
    if wygrana[komputer] == gracz:
        return PRZEGRANA
    if wygrana[gracz] == komputer:
        return WYGRANA


def nowe_p_k_n():
    pop_z_gracza = ""
    pop_z_gracza2 = ""
    game_length = int(input("Gramy do: "))
    wynik_gracza = 0
    wynik_komputera = 0
    while wynik_gracza < game_length or wynik_komputera < game_length:
        gracz = input("co wybierasz: ")
        if gracz in mozliwosci:
            komputer = madry_komputer(gracz, pop_z_gracza, pop_z_gracza2)
            a = sedzia(komputer, gracz)
            if a == PRZEGRANA:
                wynik_komputera += 1
            elif a == WYGRANA:
                wynik_gracza += 1
            print("GRACZ: ", pkn[gracz], "KOMPUTER: ", pkn[komputer], sep="\n")
            wynik = "wynik_komputera to " + str(wynik_komputera), "wynik_gracza to " + str(wynik_gracza)
            wynik = " a ".join(wynik).upper()
            print(ret(wynik, "–"))
            if wynik_komputera == game_length:
                print("\n", ret("WYGRAŁ KOMPUTER", "–"), sep="")
                break
            if wynik_gracza == game_length:
                print("\n", ret("WYGRAŁ GRACZ", "–"), sep="")
                break
            pop_z_gracza2 = pop_z_gracza
            pop_z_gracza = gracz
        else:
            print(ret("Nie Ma Takiego Znaku", "–"))


nowe_p_k_n()
