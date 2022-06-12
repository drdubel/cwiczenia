import os.path
import re
import slowniki
from trzyliterowki import trzyliterowki
from dwuliterowki import dwuliterowki
from time import process_time

SLOWA_FN = os.path.join(os.path.dirname(__file__), "slowa.txt")

slowa = open(SLOWA_FN, encoding="utf-8").read()
slowa = slowa.split()
slowa_txt = "\n".join(slowa)


class ErrorReturn(Exception):
    pass


def najlepsze_slowo(slowa_z_ind_i_pol_wart, pion):
    naj_slowo = [0, ""]
    for slowo, indeksy, polozenie_teraz, wart in slowa_z_ind_i_pol_wart:
        wartosc_slowa = wycena_slowa(
            slowo, polozenie_teraz[0], polozenie_teraz[1], pion, indeksy, wart
        )
        if wartosc_slowa > naj_slowo[0]:
            naj_slowo = [wartosc_slowa, slowo]
    return naj_slowo


def wycena_slowa(litery, start_x, start_y, pion, stare, wartosc=0):
    ind = 0
    wartosc_slowa = 0
    mnoznik_slowa = 1
    dl_starych = len(stare)
    for litera in litery:
        slownik_pkt = slowniki.dct(pkt=True)
        if stare and ind != stare[0] or not stare:
            slownik_pme = slowniki.dct(pme=True)
            wart_litery = slownik_pkt[litera]
            if (start_x, start_y) in slownik_pme:
                mnozniki = slownik_pme[(start_x, start_y)]
                wart_litery *= mnozniki[1]
                mnoznik_slowa *= mnozniki[0]
            wartosc_slowa += wart_litery
        if stare and ind == stare[0]:
            wart_litery = slownik_pkt[litera]
            wartosc_slowa += wart_litery
            stare.remove(ind)
        ind += 1
        if pion:
            start_y += 1
        else:
            start_x += 1
    wartosc_slowa *= mnoznik_slowa
    wartosc_slowa += wartosc
    if len(litery) - dl_starych == 7:
        wartosc_slowa += 50
    return wartosc_slowa


def litery_gracza():
    return input()


def planszozwracacz():
    plansza = []
    for _i in range(15):
        plansza.append(input().split())
    return plansza


def sloworozpoznawacz(plansza):
    slowa = []
    slowo_szer = ""
    slowo_wys = ""
    for ind in range(15):
        i = plansza[ind]
        j_ind = 0
        for j in i:
            bylo = False
            if j == "-" and slowo_szer:
                slowa.append(slowo_szer)
                slowo_szer = ""
            elif j != "-":
                if 14 > ind > 0:
                    if (
                        plansza[ind - 1][j_ind] == "-"
                        and plansza[ind + 1][j_ind] == "-"
                    ):
                        print("szer 1 " + j)
                        slowo_szer += j
                        bylo = True
                elif ind > 0:
                    if plansza[ind - 1][j_ind] == "-":
                        print("szer 2 " + j)
                        slowo_szer += j
                        bylo = True
                elif ind < 14:
                    if plansza[ind + 1][j_ind] == "-":
                        print("szer 3 " + j)
                        slowo_szer += j
                        bylo = True
                if not bylo:
                    if j_ind < 14:
                        if i[j_ind + 1] != "-":
                            print("szer 4 " + j)
                            slowo_szer += j
                            bylo = True
                    elif j_ind > 0:
                        if i[j_ind - 1] != "-":
                            print("szer 5 " + j)
                            slowo_szer += j
                            bylo = True
            j_ind += 1
        if slowo_szer:
            slowa.append(slowo_szer)
            slowo_szer = ""
        j_ind = 0
        for szer in plansza:
            bylo = False
            lit_ter = szer[ind]
            if lit_ter == "-" and slowo_wys:
                slowa.append(slowo_wys)
                slowo_wys = ""
            elif lit_ter != "-":
                if 14 > ind > 0:
                    if szer[ind - 1] == "-" and szer[ind + 1] == "-":
                        print("wys 1 " + lit_ter)
                        slowo_szer += lit_ter
                        bylo = True
                elif ind > 0:
                    if szer[ind - 1] == "-":
                        print("wys 2 " + lit_ter)
                        slowo_szer += lit_ter
                        bylo = True
                elif ind < 14:
                    if szer[ind + 1] == "-":
                        print("wys 3 " + lit_ter)
                        slowo_szer += lit_ter
                        bylo = True
                if not bylo:
                    if j_ind < 14:
                        if plansza[j_ind + 1][ind] != "-":
                            print("wys 4 " + lit_ter)
                            slowo_szer += lit_ter
                            bylo = True
                    elif j_ind > 0:
                        if plansza[j_ind - 1][ind] != "-":
                            print("wys 5 " + lit_ter)
                            slowo_szer += lit_ter
                            bylo = True
            j_ind += 1
        if slowo_wys:
            slowa.append(slowo_wys)
            slowo_wys = ""
    return slowa


def czy_wystarczy_liter(z_liter, litery_gracza, slowa_z_indeksami):
    dobre_slowa_z_indeksami = []
    for slowo, indeks, polozenie in slowa_z_indeksami:
        nadmiar_liter = slowo
        for litera in z_liter:
            nadmiar_liter = nadmiar_liter.replace(litera, "", 1)
        if not nadmiar_liter:
            continue
        for litera_gracza in litery_gracza:
            nadmiar_liter = nadmiar_liter.replace(litera_gracza, "", 1)
        if nadmiar_liter:
            continue
        dobre_slowa_z_indeksami.append([slowo, indeks, polozenie])
    return dobre_slowa_z_indeksami


def czy_da_sie(pion, slowa_ind_pol, plansza):
    dobre_slowa = []
    for slowo, indeksy, polozenie in slowa_ind_pol:
        nowe_polozenie = polozenie.copy()
        slowo_dobre = True
        wart = 0
        for litera, i in zip(slowo, [j for j in range(len(slowo))]):
            if pion:
                if i not in indeksy and slowo_dobre:
                    czy_db_litera = sprawdzanie_pionowe(
                        nowe_polozenie.copy(), litera, plansza.copy()
                    )
                    wart += czy_db_litera[1]
                    if not czy_db_litera[0]:
                        slowo_dobre = False
                nowe_polozenie[0] += 1
            else:
                if i not in indeksy and slowo_dobre:
                    czy_db_litera = sprawdzanie_poziome(
                        nowe_polozenie.copy(), litera, plansza.copy()
                    )
                    wart += czy_db_litera[1]
                    if not czy_db_litera[0]:
                        slowo_dobre = False
                nowe_polozenie[1] += 1
        if slowo_dobre:
            dobre_slowa.append([slowo, indeksy, polozenie, wart])
    return dobre_slowa


def sprawdzanie_pionowe(polozenie, litera, plansza):
    polozenie_litery = polozenie.copy()
    if polozenie[1] - 1 >= 0 and polozenie[1] + 1 <= 14:
        if (
            plansza[polozenie[0]][polozenie[1] - 1] == "-"
            and plansza[polozenie[0]][polozenie[1] + 1] == "-"
        ):
            return [True, 0]
    elif polozenie[1] + 1 <= 14 and plansza[polozenie[0] + 1][polozenie[1] + 1] == "-":
        return [True, 0]
    elif polozenie[1] - 1 >= 0 and plansza[polozenie[0]][polozenie[1] - 1] == "-":
        return [True, 0]
    poczatek = False
    while not poczatek:
        if polozenie[1] == 0 or plansza[polozenie[0]][polozenie[1]] == "-":
            poczatek = polozenie.copy()
            polozenie[1] += 1
        polozenie[1] -= 1
    koniec = False
    slowo = ""
    while not koniec:
        if (
            polozenie[1] == 14
            or plansza[polozenie[0]][polozenie[1]] == "-"
            and polozenie_litery != polozenie
        ):
            koniec = True
        elif polozenie_litery == polozenie:
            slowo += litera
        else:
            slowo += plansza[polozenie[0]][polozenie[1]]
        polozenie[1] += 1
    slownik_sprawdzany = slowa
    if len(slowo) == 2:
        slownik_sprawdzany = dwuliterowki
    elif len(slowo) == 3:
        slownik_sprawdzany = trzyliterowki
    if slowo in slownik_sprawdzany:
        stare = [i for i in range(len(slowo))]
        stare.remove(polozenie_litery[1] - poczatek[1])
        return [
            True,
            wycena_slowa(slowo, poczatek[1], poczatek[0], False, stare.copy()),
        ]
    return [False, 0]


def sprawdzanie_poziome(polozenie, litera, plansza):
    polozenie_litery = polozenie.copy()
    polozenie_litery = polozenie.copy()
    if polozenie[0] - 1 >= 0 and polozenie[0] + 1 <= 14:
        if (
            plansza[polozenie[0] - 1][polozenie[1]] == "-"
            and plansza[polozenie[0] + 1][polozenie[1]] == "-"
        ):
            return [True, 0]
    elif polozenie[0] + 1 <= 14 and plansza[polozenie[0] + 1][polozenie[1]] == "-":
        return [True, 0]
    elif polozenie[0] - 1 >= 0 and plansza[polozenie[0] - 1][polozenie[1]] == "-":
        return [True, 0]
    poczatek = False
    while not poczatek:
        if polozenie[0] == 0 or plansza[polozenie[0]][polozenie[1]] == "-":
            poczatek = polozenie.copy()
        polozenie[0] -= 1
    koniec = False
    slowo = ""
    while not koniec:
        if (
            polozenie[0] == 14
            or plansza[polozenie[0]][polozenie[1]] == "-"
            and polozenie_litery != polozenie
        ):
            koniec = True
        elif polozenie_litery == polozenie:
            slowo += litera
        else:
            slowo += plansza[polozenie[0]][polozenie[1]]
        polozenie[0] += 1
    slownik_sprawdzany = slowa
    if len(slowo) == 2:
        slownik_sprawdzany = dwuliterowki
    elif len(slowo) == 3:
        slownik_sprawdzany = trzyliterowki
    if slowo in slownik_sprawdzany:
        stare = [i for i in range(len(slowo))]
        stare.remove(polozenie_litery[0] - poczatek[0])
        return [True, wycena_slowa(slowo, poczatek[1], poczatek[0], True, stare.copy())]
    return [False, 0]


def znajdz_slowa(litery_gracza, litery_do_slowa, slowa, polozenie, pion):
    do_szukania = "^("
    il_pustych = 0
    czy_byla_litera = False
    if litery_do_slowa.isspace():
        wzorzec = []
        do_szukania += (
            ")({l}" + "".join(f"{{{set([1, len(litery_do_slowa)])}}}".split()) + ")$"
        )
    else:
        wzorzec = [0]
        for znak in litery_do_slowa:
            czy_spacje = False
            if znak == " ":
                il_pustych += 1
            elif znak != " " and il_pustych:
                if not czy_byla_litera:
                    do_szukania += (
                        "{l}" + "".join(f"{{{set([0, il_pustych])}}}".split()) + ")("
                    )
                    czy_byla_litera = True
                else:
                    do_szukania += "{l}" + f"{{{{{il_pustych}}}}}"
                    wzorzec.append(il_pustych + 1 + wzorzec[len(wzorzec) - 1])
                czy_spacje = True
                il_pustych = 0
            if znak != " ":
                if not czy_byla_litera:
                    do_szukania += ")("
                    czy_byla_litera = True
                if not czy_spacje:
                    wzorzec.append(il_pustych + 1 + wzorzec[len(wzorzec) - 1])
                do_szukania += znak
        if il_pustych:
            do_szukania += ")({l}" + f"{{{set([0, il_pustych])}}}".replace(" ", "")
        else:
            do_szukania += ")("
        do_szukania += ")$"
    slowa_oddzielone = re.findall(
        do_szukania.format(l=f"[{litery_gracza}]"), slowa, re.M
    )
    slowa_zlaczone = []
    indeksy = []
    polozenia = []
    for slowo in slowa_oddzielone:
        indeksy_starych = []
        for do_dodania in wzorzec:
            indeksy_starych.append(len(slowo[0]) + do_dodania)
        slowa_zlaczone.append(slowo[0] + slowo[1] + slowo[2])
        indeksy.append(indeksy_starych)
        if litery_do_slowa.isspace():
            if pion:
                polozenia.append([polozenie[0], polozenie[1]])
            else:
                polozenia.append([polozenie[0], polozenie[1]])
        elif pion:
            polozenia.append(
                [
                    polozenie[0]
                    + len(litery_do_slowa)
                    - len(slowo[0] + slowo[1])
                    - il_pustych,
                    polozenie[1],
                ]
            )
        else:
            polozenia.append(
                [
                    polozenie[0],
                    polozenie[1]
                    + len(litery_do_slowa)
                    - len(slowo[0] + slowo[1])
                    - il_pustych,
                ]
            )
    return czy_wystarczy_liter(
        litery_do_slowa.replace(" ", ""),
        litery_gracza,
        zip(slowa_zlaczone, indeksy, polozenia),
    )


def sprawdz_linijke(nr_linijki, linijka, litery_gracza, plansza):
    wart_naj_slo = [0, "", [0, 0]]
    polozenie = [nr_linijki, 0]
    polozenie[1] = 0
    wzorzec_slowa = ""
    bylo_slowo = False
    for znak in linijka:
        # print(znak, linijka)
        if wzorzec_slowa.islower():
            if bylo_slowo and znak != "-":
                wzorzec_slowa = wzorzec_slowa[::-1].replace(" ", "", 1)[::-1]
                wart_slo = najlepsze_slowo(
                    czy_da_sie(
                        False,
                        znajdz_slowa(
                            litery_gracza,
                            wzorzec_slowa,
                            slowa_txt,
                            [
                                polozenie[0],
                                polozenie.copy()[1] - 1 - len(wzorzec_slowa),
                            ],
                            False,
                        ),
                        plansza.copy(),
                    ),
                    False,
                )
                if wart_slo[0] > wart_naj_slo[0]:
                    wart_naj_slo = wart_slo
                    wart_naj_slo.append(
                        [polozenie[0], polozenie.copy()[1] - 1 - len(wzorzec_slowa)]
                    )
                bylo_slowo = False
                wzorzec_slowa += " "
            if znak == "-":
                bylo_slowo = True
        if znak == "-":
            wzorzec_slowa += " "
        else:
            wzorzec_slowa += znak
        polozenie[1] += 1
    return wart_naj_slo


def planszoprzejezdzacz(litery_gracza, plansza):
    wart_naj_slo = [0, "", [0, 0]]
    nr_linii = 0
    for linijka in plansza:
        wart_slo = sprawdz_linijke(
            nr_linii, linijka.copy(), litery_gracza, plansza.copy()
        )
        if wart_slo[0] > wart_naj_slo[0]:
            wart_naj_slo = wart_slo
        nr_linii += 1
    return wart_naj_slo


t1_start = process_time()
print(
   planszoprzejezdzacz(
       litery_gracza(),
       planszozwracacz()
   )
)
t1_stop = process_time()
print(t1_stop-t1_start)

# print(czy_da_sie(False, [["rak", [0], [1, 0]]], planszozwracacz()))

plansze = [
    """
- - - - - - - - - - - - - - -
- - - - - - - - - - - - - - -
- - - - - - - - - - - - - - -
- - - - - - - - - - - - - - -
- - - - t - m - - - - - - - -
- - - - c - a - - - - - - - -
- - - - h a m u l e c - - - -
- - - - ó - a - o - i - - - -
- g w a r - - - d - a - - - -
- - - - z - - m y d ł o - - -
- - - - - - - - - - o - - - -
- - - - - - - - - - - - - - -
- - - - - - - - - - - - - - -
- - - - - - - - - - - - - - -
- - - - - - - - - - - - - - -
""",
    """
t r o m t a d r a c j a - - -
r - - - - - o - - - a r k o m
o l a ł y - m - - - s - - - u
m - - a - - a - - - k - c - r
t o - d - - t - - - i - m - o
a - - n - - o r a n e g o - m
d o m y - - r o k - r - k - -
r - - m - - - k r a - - a - -
a - - i - o n i - r - o m e n
c o ś - - d - e - y - d - - -
j - m - - y - m - - - c - - -
o - i - - - - - - - - z - - -
m - a - - - - o d c z y n y -
- - ł - - - - n - - - n - - -
- - a r b u z i e - - u - - -
""",
]
slowa_do_planszy2 = [
    "tromtadracja",
    "arkom",
    "olały",
    "to",
    "oranego",
    "domy",
    "rok",
    "kra",
    "oni",
    "omen",
    "coś",
    "odczyny",
    "arbuzie",
    "tromtadracjom",
    "śmiała",
    "ładnymi",
    "ody",
    "domator",
    "rokiem",
    "oni",
    "akr",
    "ary",
    "jaskier",
    "ar",
    "odczynu",
    "cmokam",
    "murom",
]
