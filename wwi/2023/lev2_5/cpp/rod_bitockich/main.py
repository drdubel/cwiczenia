from random import randrange


def generate(x=1, nmax=10, mmax=40):
    n = randrange(2, nmax + 1)
    d = " ".join([str(randrange(0, n)) for _ in range(n - 1)])
    m = randrange(1, n + 1)
    ab = "\n".join([" ".join([str(randrange(1, n)), str(randrange(1, n))]) for _ in range(m)])
    return "\n".join([str(n), d, str(m), ab])


def main():
    print(generate())


if __name__ == "__main__":
    main()
