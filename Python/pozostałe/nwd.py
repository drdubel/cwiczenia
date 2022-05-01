def najw_wspol_dziel(lic_1, lic_2):
    while lic_2 != 0:
        resz_dziel = lic_1%lic_2
        lic_1 = lic_2
        lic_2 = resz_dziel
    return lic_1

if __name__ == '__main__':
    print(najw_wspol_dziel(27, 1960))
