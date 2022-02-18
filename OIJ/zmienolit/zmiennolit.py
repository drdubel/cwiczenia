def zmiennolit(slowo):
    wynik = 0
    pop_lit = ''
    for litera in slowo:
        if litera == pop_lit:
            wynik += 1
        pop_lit = litera
    return wynik


if __name__ == "__main__":
    print(zmiennolit('mammamia'*100000))
