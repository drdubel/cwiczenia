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


class BadInputError(Exception):
    pass


def litery_gracza():
    """
    Funkcja mająca za zadanie zwrócić litery gracza.

    Zwraca:
        string: litery gracza.
    """
    return input("Podaj swoje litery!\n").replace(" ", "")


def planszozwracacz():
    """
    Funkcja mająca za zadanie zwrócić aktualne ułożenie planszy.

    Zwraca:
        list[list]: plansza w postaci listy złożonej z list.
    """
    plansza = []
    for _ in range(15):
        plansza.append(input().split())
    return plansza


def poprawnosc_liter(wejscie):
    """
    Funkcja mająca za zadanie zweryfikować czy to co podał gracz może być jego literami.

    Argumenty:
        wejscie (string, opcjonalnie): litery gracza

    Zgłasza:
        BadInputError: Nie wszystkie znaki są literami.
        BadInputError: Jest za dużo liter.

    Zwraca:
        string: Zwraca litery podane na początku, jeśli były one podane prawidłowo.
    """
    if not wejscie.isalpha():
        raise BadInputError("Możesz podać jedynie litery!")
    if len(wejscie) > 7:
        raise BadInputError("Za dużo liter!")
    return wejscie


def najlepsze_slowo(litery):
    """
    Funkcja mająca za zadanie zwrócić najlepsze słowo jakie można umieścić na planszy, a także jego położenie

    Argumenty:
        litery (string): litery gracza
    """
    print(litery)


if __name__ == "__main__":
    najlepsze_slowo(poprawnosc_liter(litery_gracza()))
