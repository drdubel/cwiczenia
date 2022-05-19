def lic_skar(skarpety):
    il_par_c = skarpety.count("C")//2
    il_par_b = skarpety.count("B")//2
    return il_par_b + il_par_c


def main():
    skarpety = input()
    print(lic_skar(skarpety))


if __name__ == "__main__":
    main()
