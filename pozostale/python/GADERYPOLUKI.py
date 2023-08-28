def gaderypoluki():
    slowo = input("Podaj Słowo Do Zaszyfrowania: ")
    zaszyfrowaneSlowo = ""
    for litera in slowo:
        if litera.capitalize() == "G":
            zaszyfrowaneSlowo += "a"
        if litera.capitalize() == "A":
            zaszyfrowaneSlowo += "g"
        if litera.capitalize() == "D":
            zaszyfrowaneSlowo += "e"
        if litera.capitalize() == "E":
            zaszyfrowaneSlowo += "d"
        if litera.capitalize() == "R":
            zaszyfrowaneSlowo += "y"
        if litera.capitalize() == "Y":
            zaszyfrowaneSlowo += "r"
        if litera.capitalize() == "P":
            zaszyfrowaneSlowo += "o"
        if litera.capitalize() == "O":
            zaszyfrowaneSlowo += "p"
        if litera.capitalize() == "L":
            zaszyfrowaneSlowo += "u"
        if litera.capitalize() == "U":
            zaszyfrowaneSlowo += "l"
        if litera.capitalize() == "K":
            zaszyfrowaneSlowo += "i"
        if litera.capitalize() == "I":
            zaszyfrowaneSlowo += "k"
    return zaszyfrowaneSlowo


print(gaderypoluki())
