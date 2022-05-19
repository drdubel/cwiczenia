def najw_wspol_dziel(lic_1, lic_2):
    while lic_2 != 0:
        resz_dziel = lic_1%lic_2
        lic_1 = lic_2
        lic_2 = resz_dziel
    return lic_1

def najm_wspol_wiel(lic_1, lic_2):
    return lic_1*lic_2//najw_wspol_dziel(lic_1, lic_2)

def malpko_skacz(il_klat, ile_klat_skczy):
    return najm_wspol_wiel(il_klat, ile_klat_skczy)//ile_klat_skczy

def main():
    il_klat, ile_klat_skczy = [int(i) for i in input().split()]
    print(malpko_skacz(il_klat, ile_klat_skczy))

if __name__ == "__main__":
    main()