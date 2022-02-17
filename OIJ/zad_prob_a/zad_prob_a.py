def roznorodnosc(il_boh, poziomy):
    wyk = 0
    pop = []
    for poziom in poziomy:
        if poziom-1 not in pop:
            poziomy[wyk] -= 1
            pop.append(poziom-1)
        elif poziom not in pop:
            pop.append(poziom)
        elif poziom+1 not in pop:
            poziomy[wyk] += 1
            pop.append(poziom+1)
    return len(pop)

def main():
    n = int(input())
    p = [int(i) for i in input().split()].sort()
    assert n == len(p)
    print(roznorodnosc(n, p))

if __name__ == "__main__":
    main()
