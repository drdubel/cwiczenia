def notzad(il_dni, notow, lic_zap, zap):
    for i in range(lic_zap):
        for i in

def main():
    il_dni = int(input())
    notow = [int(i) for i in input().split()]
    assert il_dni == len(notow)
    lic_zap = int(input())
    zap = []
    for i in range(lic_zap):
        zap.append(int(input()))
    print(notzad(il_dni, notow, lic_zap, zap))

if __name__ == "__main__":
    main()