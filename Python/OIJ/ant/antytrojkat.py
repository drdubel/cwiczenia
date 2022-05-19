import sys


def antytrojkat(il_patyczkow, najdluzszy, patyczki):
    pass


def main(indata):
    il_patyczkow, najdluzszy = map(int, next(indata).split())
    patyczki = list(map(int, next(indata).split()))
    return antytrojkat(il_patyczkow, najdluzszy, patyczki)


def run():
    for line in main((line.rstrip() for line in sys.stdin)):
        print(line)


if __name__ == '__main__':
    run()
