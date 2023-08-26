def main():
    n = int(input())
    brakujaca = (n * (n + 1)) / 2 - sum(map(int, input().split()))
    print(int(brakujaca))


if __name__ == "__main__":
    main()
