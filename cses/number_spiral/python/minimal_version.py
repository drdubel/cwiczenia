import sys


def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        y, x = map(int, sys.stdin.readline().split())
        m = max(y, x)
        print(m * (m - 1) + 1 + (y - x) * (m % 2 * -2 + 1))


if __name__ == "__main__":
    main()
