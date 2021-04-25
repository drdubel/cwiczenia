DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def dec2cos(integer, radix=2):
    assert 2 <= radix <= len(DIGITS)
    digits = []
    a = integer
    while a > 0:
        a, reminder = divmod(a, radix)
        digits.append(DIGITS[reminder])
    digits.reverse()
    return "".join(digits)

def cos2dec(liczba, system=2):
    liczba = str(liczba)[::-1]
    wykonanie = 0
    wynik = 0
    for cyfra in liczba:
        wynik += system**wykonanie*int(DIGITS.index(cyfra))
        wykonanie += 1
    return wynik

def main():
    sys = input()
    if sys == "na dziesiatkowy":
        print(cos2dec(int(input())))
    else:
        print(dec2cos(int(input())))

if __name__ == '__main__':
    main()