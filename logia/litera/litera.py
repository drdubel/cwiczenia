def litera(lista):
    alfabet = 'abcdefghjiklmnopqrstuvwxyz'
    slowa = ''.join(lista)
    maks_lit = 0
    najw_lit = []
    for litera in alfabet:
        il = slowa.count(litera)
        if maks_lit < il:
            maks_lit = il
            najw_lit = [litera]
        if maks_lit == il and litera not in najw_lit:
            najw_lit.append(litera)
    if len(najw_lit) == 1:
        return najw_lit[0]
    return sorted(najw_lit)


def litera2(lista):
    czestosc_liter = {}
    for slowo in lista:
        for litera in slowo:
            # czestosc_liter[litera] = czestosc_liter.get(litera, 0) + 1
            try:
                czestosc_liter[litera] += 1
            except KeyError:
                czestosc_liter[litera] = 1
    maks_lit = max(czestosc_liter.values())
    litery = sorted(k for k, v in czestosc_liter.items() if v == maks_lit)
    if len(litery) == 1:
        return litery[0]
    return litery
