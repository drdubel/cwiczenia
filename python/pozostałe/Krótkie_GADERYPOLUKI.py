Szyfrarka = {
    "g": "a",
    "a": "g",
    "d": "e",
    "e": "d",
    "r": "y",
    "y": "r",
    "p": "o",
    "o": "p",
    "l": "u",
    "u": "l",
    "k": "i",
    "i": "k",
}
slowo = input("Co chcesz zaszyfrować: ")
zaszyfrowane_slowo = ""
for litera in slowo:
    if litera.isupper():
        litera = litera.lower()
    try:
        zaszyfrowane_slowo += Szyfrarka[litera]
    except KeyError:
        zaszyfrowane_slowo += litera
print(zaszyfrowane_slowo)
