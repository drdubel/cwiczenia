def main():
    n = int(input())
    m = 0
    while n:
        n //= 5
        m += n
    print(m)


if __name__ == "__main__":
    main()
