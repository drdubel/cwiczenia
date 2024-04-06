import turtle


def main():
    t = turtle.Pen()
    t.speed(1)

    polecenia = input() + " "
    odleglosc = 0

    for char in polecenia:
        if char.isdigit():
            odleglosc = odleglosc * 10 + int(char)

        else:
            t.fd(odleglosc * 10)
            odleglosc = 0

        match char:
            case "G":
                t.setheading(90)

            case "D":
                t.setheading(270)

            case "P":
                t.setheading(0)

            case "L":
                t.setheading(180)


if __name__ == "__main__":
    main()
