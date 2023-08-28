def plu(n, ciag_n):
    pkt_wiez = []
    ind = 0
    odw_ind = len(ciag_n) - 1
    for wys in ciag_n:
        pkt_wiez.append(wys - ind + wys - odw_ind)
        ind += 1
        odw_ind -= 1
    srdk_krzyza = pkt_wiez.index(max(pkt_wiez))
    wys_krzyza = ciag_n[srdk_krzyza]
    wys_prop = 1
    i = 0
    while i <= wys_krzyza >= wys_prop:
        for j in range(1, i + 1):
            if (
                wys_prop - (wys_prop - 1) // 2 > ciag_n[srdk_krzyza + j]
                and wys_prop - (wys_prop - 1) // 2 > ciag_n[srdk_krzyza - j]
            ):
                return (wys_prop - 1) // 2
        if wys_krzyza >= wys_prop + 2:
            wys_prop += 2
            i += 1
        else:
            return (wys_prop - 1) // 2


if __name__ == "__main__":
    n = int(input())
    ciag_n = [int(i) for i in input().split()]
    print(plu(n, ciag_n))
