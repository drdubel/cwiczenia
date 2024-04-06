def main():
    slowo1 = list(input())
    slowo2 = list(input())

    for char in slowo1.copy():
        if char in slowo2:
            slowo1.remove(char)
            slowo2.remove(char)

    if len(slowo1) == 1 and not slowo2:
        print(f"tak nadmiar {slowo1[0]}")

    elif len(slowo2) == 1 and not slowo1:
        print(f"tak brak {slowo2[0]}")

    elif len(slowo1) == 1 and len(slowo2) == 1:
        print(f"tak {slowo1[0]} na {slowo2[0]}")

    else:
        print("nie")


if __name__ == "__main__":
    main()
