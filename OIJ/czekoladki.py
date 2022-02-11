def ile_kostek(wym_czekolad):
    wynik = 0
    wynik += wym_czekolad[0]*wym_czekolad[1]+wym_czekolad[2]*wym_czekolad[3]
    return wynik

def main():
    wym_czekolad = list(map(int, input().split()))
    print(ile_kostek(wym_czekolad))

if __name__ == "__main__":
    main()