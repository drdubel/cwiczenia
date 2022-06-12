def czy_trian_pop(odcinki):
    lpsz_odc = ''
    for odcinek in odcinki:
        lpsz_odc += str()


def ploty(z, zestawy):
    pass


if __name__ == "__main__":
    z = int(input())
    zestawy = []
    for i in range(z):
        zestawy.append([])
        n = int(input())
        for _ in range(n - 2):
            zestawy[i].append([int(i) for i in input().split()])
    ploty(z, zestawy)
