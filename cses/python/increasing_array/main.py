def main():
    _ = int(input())
    numbers = list(map(int, input().split()))
    min_moves = 0
    change = 0
    for i, j in zip(numbers[:-1], numbers[1:]):
        change = max(0, i - j + change)
        min_moves += change
    return min_moves


if __name__ == "__main__":
    print(main())
