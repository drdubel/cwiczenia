import sys


def przestawianie(gabloty):
    for gablota in gabloty:
        


def main(indata):
    il_gablot = int(indata.readline().strip().split())
    przestawienia = 0
    gabloty = []
    for gablota in indata:
        gablota = list(map(int, gablota))
        gabloty.append(gablota)
        pozadany_produkt = max(gablota)
        if pozadany_produkt == 0:
            
    print(przestawienia)


def run():
    for line in main(sys.stdin):
        print(line)


if __name__ == '__main__':
    main()
