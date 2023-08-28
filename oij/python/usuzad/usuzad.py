def usuzad(il_kloc, klocki):
    ind = 1
    il_ruch = 0
    while ind <= il_kloc:
        if klocki[ind - 1] == 0:
            naj_spraw = ind + klocki[ind - 1]
            najw_kloc = 0
            ind += 1
        else:
            naj_spraw = ind + 1 + klocki[ind - 1]
            if naj_spraw > il_kloc:
                naj_spraw = il_kloc
            najw_kloc = max(klocki[ind:naj_spraw])
            ind += klocki[ind:naj_spraw].index(max(klocki[ind:naj_spraw])) + 1
        il_ruch += 1
        if naj_spraw == il_kloc:
            return il_ruch
    return il_ruch


if __name__ == "__main__":
    il_kloc = int(input())
    klocki = [int(i) for i in input().split()]
    assert il_kloc == len(klocki)
    print(usuzad(il_kloc, klocki))
