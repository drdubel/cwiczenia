def main(n=int(input())):
    s = (n + 1) * n / 2
    if not s % 2:
        print("YES")
        i = n
        s2 = int(s / 2)
        while s2 > i:
            s2 -= i
            i -= 1
        print(n - i + 1)
        print(s2, *[j for j in range(i + 1, n + 1)])
        print(i - 1)
        print(*[j for j in range(1, i + 1) if j != s2])
    else:
        print("NO")


if __name__ == "__main__":
    main()
