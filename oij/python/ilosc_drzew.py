def grafne_dzewa(il_drzew, dzielnik):
    if 1 == il_drzew:
        return il_drzew
    return il_drzew ** (il_drzew - 2) % dzielnik


def main():
    il_drzew, dzielnik = [int(i) for i in input().split()]
    print(grafne_dzewa(il_drzew, dzielnik))


if __name__ == "__main__":
    main()
