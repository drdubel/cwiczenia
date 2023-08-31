import numpy as np


def generateTests(args):
    pass


def main():
    args = []
    for i in range(int(input())):
        args.append(tuple(input.split()))
    args = np.array(
        tuple(args),
        dtype=[
            ("id", "U10"),
            ("quantity", "U10"),
            ("min", int),
            ("max", int),
            ("newline", bool),
        ],
    )


if __name__ == "__main__":
    main()
