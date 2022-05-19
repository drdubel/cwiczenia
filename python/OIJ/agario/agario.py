import sys


def agario(il_przeciwnikow, przeciwnicy):
    wynik = 2
    przeciwnicy = sorted(przeciwnicy, reverse=True)
    if przeciwnicy[-1] >= wynik:
        return ["NIE"]
    najwiekszy = przeciwnicy[0]
    czas = 0
    mniejsi = []
    while wynik < najwiekszy:
        while przeciwnicy[-1] < wynik:
            mniejsi.append(przeciwnicy.pop())
        try:
            wynik += mniejsi.pop()
            czas += 1
        except IndexError:
            return ["NIE"]
    return czas


def main(indata):
    il_przeciwnikow = int(next(indata))
    przeciwnicy = map(int, next(indata).split())
    return [agario(il_przeciwnikow, przeciwnicy)]


def run():
    for line in main((line[:-1] for line in sys.stdin)):
        print(line)


if __name__ == '__main__':
    run()
