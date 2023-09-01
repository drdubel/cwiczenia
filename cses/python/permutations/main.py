a = int(input())
print(
    "NO SOLUTION"
    if 1 < a < 4
    else " ".join(
        [" ".join(map(str, range(j, a + (a - j + 1) % 2, 2))) for j in range(2, 0, -1)]
    )
)
