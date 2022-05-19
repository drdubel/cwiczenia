def zes(n, lvle_zaw):
    il_zesp = 0
    wyk = 0
    if lvle_zaw.count(lvle_zaw[0]) == len(lvle_zaw):
        return len(lvle_zaw)//3
    for lvl in lvle_zaw:
        il_tak_sam = lvle_zaw.count(lvl)
        ile_tak_mniej = lvle_zaw.count(lvl-1)
        ile_tak_wiek = lvle_zaw.count(lvl+1)
        if il_tak_sam > 1:
            if il_tak_sam >= 3:
                for i in range(3):
                    lvle_zaw.remove(lvl)
                il_zesp += 1
            elif ile_tak_mniej >= 1:
                for i in range(2):
                    lvle_zaw.remove(lvl)
                lvle_zaw.remove(lvl-1)
                il_zesp += 1
            elif ile_tak_wiek >= 1:
                for i in range(2):
                    lvle_zaw.remove(lvl)
                lvle_zaw.remove(lvl+1)
                il_zesp += 1
        elif ile_tak_mniej > 1:
            for i in range(2):
                lvle_zaw.remove(lvl-1)
            lvle_zaw.remove(lvl)
            il_zesp += 1
        elif ile_tak_wiek > 1:
            for i in range(2):
                lvle_zaw.remove(lvl+1)
            lvle_zaw.remove(lvl)
            il_zesp += 1
        wyk += 1
    return il_zesp

            

if __name__ == "__main__":
    n = int(input())
    lvle_zaw = [int(i) for i in input().split()]
    print(zes(n, lvle_zaw))