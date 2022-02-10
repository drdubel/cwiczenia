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
    return najw_lit
