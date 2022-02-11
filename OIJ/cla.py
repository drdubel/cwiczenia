def clo(il_miast, il_drog, drogi):
    pass

def main():
    il_miast, il_drog = list(map(int, input().split()))
    drogi = {}
    for _ in range(il_drog):
        skad, dokad = list(map(int, input().split()))
        if skad in drogi:
            drogi[skad].append(dokad)
        else:
            drogi[skad] = [dokad]
    print(clo(il_miast, il_drog, drogi))

if __name__ == "__main__":
    main()