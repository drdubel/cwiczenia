def main():
    il_pudelek = int(input())
    for _ in range(il_pudelek):
        wymiary_puzli = list(map(int, input().split()))
        puzle = [[], []]
        for i in range(2):
            for _ in range(wymiary_puzli[0]):
                puzle[i].append(
        print()


if __name__ == "__main__":
    main()
