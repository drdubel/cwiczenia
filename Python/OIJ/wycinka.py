def wyc_drzew(il_drzew, od_wym, miejsca_drzew, wysokosci_drzew):
    pass


def main():
    il_drzew, od_wym = list(map(int, input().split()))
    miejsca_drzew = list(map(int, input().split()))
    wysokosci_drzew = list(map(int, input().split()))
    print(wyc_drzew(il_drzew, od_wym, miejsca_drzew, wysokosci_drzew))


if __name__ == "__main__":
    main()
