def czydrzewo(il_drzew, il_kraw, kraw):
    if il_drzew-2 > il_kraw:
        return "niedrzewo", kraw
    return "drzewo"


def main():
    il_drzew, il_kraw = list(map(int, input().split()))
    kraw = {}
    for i in range(il_kraw):
