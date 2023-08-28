def rozklad(n, znak):
    wzor = ""
    do_odjecia = 1
    czynniki = []
    while n:
        pop_do_odjecia = do_odjecia
        for i in range(9, 1, -1):
            if do_odjecia * i <= n:
                do_odjecia *= i
                wzor += f"{i}["
                czynniki.append(i)
        if n == 1:
            return wzor + znak
        if do_odjecia == pop_do_odjecia:
            if wzor[-1] == "[":
                wzor += znak
                n -= do_odjecia
            if czynniki:
                wzor += "]"
                do_odjecia //= czynniki.pop()
            else:
                wzor += znak
                n -= 1
    return wzor


def trojkaty(n):
    wzor = ""
    wzor += rozklad(n, "F") + rozklad(n, "B")
    for i in range(n - 1, 0, -1):
        wzor += "D" + rozklad(i, "E") + rozklad(i, "AC")
    return wzor + "D"


def main():
    n = int(input())
    # print(trojkaty(n))
    print(rozklad(140, "BF"))


if __name__ == "__main__":
    main()
