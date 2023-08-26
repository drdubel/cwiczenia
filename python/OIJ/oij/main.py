def main():
    word = input()
    wanted = "oij"
    i = 0
    for char in word:
        if char == wanted[i % 3]:
            i += 1
    return i // 3 if i // 3 else "NIE"


if __name__ == "__main__":
    print(main())
