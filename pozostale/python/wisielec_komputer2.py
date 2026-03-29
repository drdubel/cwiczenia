import subprocess
from random import choice

import tqdm
from pyinstrument import Profiler

rys_wis = [
    [],
    ["_____"],
    [" |", " |", " |", " |", "_|___"],
    [" ____", " |", " |", " |", " |", "_|___"],
    [" ____", " |  |", " |", " |", " |", "_|___"],
    [" ____", " |  |", " |  O", " |", " |", "_|___"],
    [" ____", " |  |", " |  O", " | !|! ", " |", "_|___"],
    [" ____", " |  |", " |  O", " | !|! ", " | / \\  ", "_|___"],
]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


def build_trie(words):
    root = TrieNode()
    for word in words:
        node = root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True
    return root


def search_pattern(root, pattern, allowed_letters):
    allowed = set(allowed_letters)
    results = []

    def dfs(node, i, prefix):
        if i == len(pattern):
            if node.is_word:
                results.append(prefix)
            return

        char = pattern[i]

        if char == "_":
            for ch, child in node.children.items():
                if ch in allowed:
                    dfs(child, i + 1, prefix + ch)
        else:
            if char in node.children:
                dfs(node.children[char], i + 1, prefix + char)

    dfs(root, 0, "")
    return results


class Wisielec:
    def __init__(self, debug=False):
        self.rys_wis = [
            [],
            ["_____"],
            [" |", " |", " |", " |", "_|___"],
            [" ____", " |", " |", " |", " |", "_|___"],
            [" ____", " |  |", " |", " |", " |", "_|___"],
            [" ____", " |  |", " |  O", " |", " |", "_|___"],
            [" ____", " |  |", " |  O", " | !|! ", " |", "_|___"],
            [" ____", " |  |", " |  O", " | !|! ", " | / \\  ", "_|___"],
        ]
        self.gracz = True
        self.debug = debug

        with open("pozostale/python/slowa.txt", "r") as plik:
            self.slowa = plik.read().strip().splitlines()
        self.trie_root = build_trie(self.slowa)

    def komputer_wybiera_litere(self, slowo, zgadniete_litery):
        mozliwe_litery = [litera for litera in "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż" if litera not in zgadniete_litery]

        pasujace_slowa = search_pattern(self.trie_root, slowo, mozliwe_litery)
        wystapienia = {litera: sum(1 if litera in s else 0 for s in pasujace_slowa) for litera in mozliwe_litery}

        return max(wystapienia, key=wystapienia.get) if wystapienia else choice(mozliwe_litery)

    def podaj_litere(self, ukryte_slowo="", zgadniete_litery=set(), gracz=True):
        if gracz:
            litera = ""
            while litera not in "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż" or len(litera) != 1:
                litera = input("Podaj literę: ").lower()
        else:
            litera = self.komputer_wybiera_litere(ukryte_slowo, zgadniete_litery)

        return litera

    def sedzia(self, slowo, gracz=True):
        ukryte_slowo = "_" * len(slowo)
        proby = 7
        proba = 0
        zgadniete_litery = set()

        while proba < proby and ukryte_slowo != slowo:
            if self.debug:
                subprocess.run("clear", shell=True)
                print(*rys_wis[proba], sep="\n", end="\n" * 3) if proba > 0 else None

                print(f"Ukryte słowo: {' '.join(ukryte_slowo)}")
                print(f"Zgadnięte litery: {' '.join(sorted(zgadniete_litery))}")

            litera = self.podaj_litere(ukryte_slowo, zgadniete_litery, gracz)

            if litera in zgadniete_litery:
                if self.debug:
                    print("Już zgadłeś tę literę. Spróbuj inną.")
                continue

            zgadniete_litery.add(litera)

            if litera in slowo:
                ukryte_slowo = "".join([litera if slowo[i] == litera else ukryte_slowo[i] for i in range(len(slowo))])
                if self.debug:
                    print("Dobra robota! Trafiłeś literę.")
            else:
                proba += 1
                if self.debug:
                    print("Niestety, ta litera nie występuje w słowie.")

        if ukryte_slowo == slowo:
            if self.debug:
                print("Gratulacje! Odgadłeś słowo: " + slowo)
            return True
        else:
            if self.debug:
                print(*rys_wis[proba], sep="\n")
                print(f"Niestety, przegrałeś. Szukane słowo to: {slowo}")
            return False

    def graj(self, gracz=True):
        slowo = choice(self.slowa)
        return self.sedzia(slowo, gracz)


def main() -> None:
    wisielec = Wisielec(debug=True)
    ile = 100
    i = 0

    profiler = Profiler()
    profiler.start()
    for _ in tqdm.tqdm(range(ile), desc="Gry"):
        if wisielec.graj(gracz=False):
            i += 1

    print(f"Komputer wygrał {i} z {ile} gier ({i / ile:.2%})")
    profiler.stop()
    profiler.print()


if __name__ == "__main__":
    main()
