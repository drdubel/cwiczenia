from pprint import pprint as print

import numpy as np


class Probablity:
    def __init__(self, number, square):
        self.number = number
        self.positions = [(square // 3 + i // 3, square % 3 + i % 3) for i in range(9)]

        print(self.positions)

    def __getitem__(self, key):
        return self.number[key]


class Game:
    def __init__(self, board=np.zeros([3, 3, 3, 3])):
        self.board = board

    def __getitem__(self, key):
        return self.board[key]

    def __repr__(self) -> str:
        pretty_board = """╔═════╦═════╦═════╦═════╦═════╦═════╦═════╦═════╦═════╗
║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  │
║─────┼─────┼─────╬─────┼─────┼─────╬─────┼─────┼─────┤
║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  │
║─────┼─────┼─────╬─────┼─────┼─────╬─────┼─────┼─────┤
║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  │
║═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╣
║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  │
║─────┼─────┼─────╬─────┼─────┼─────╬─────┼─────┼─────┤
║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  │
║─────┼─────┼─────╬─────┼─────┼─────╬─────┼─────┼─────┤
║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  │
║═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╬═════╣
║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  │
║─────┼─────┼─────╬─────┼─────┼─────╬─────┼─────┼─────┤
║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  │
║─────┼─────┼─────╬─────┼─────┼─────╬─────┼─────┼─────┤
║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  ║  {}  │  {}  │  {}  │
╚═════╩═════╩═════╩═════╩═════╩═════╩═════╩═════╩═════╝""".format(
            *self.board.flatten()
        )

        return pretty_board


class Player:
    def __init__(self, game):
        self.game = game

    def solve(self):
        probablities = self.get_probablities()

        print(probablities)

        for i in range(9):
            for key, value in probablities[i].items():
                if len(value) == 1:
                    self.game.board[
                        value[0][0] // 3,
                        value[0][1] // 3,
                        value[0][0] % 3,
                        value[0][1] % 3,
                    ] = key

        print(self.game)

    def get_probablities(self):
        probablities = [
            {
                j: [((i // 3) * 3 + k // 3, (i % 3) * 3 + k % 3) for k in range(9)]
                for j in range(1, 10)
            }
            for i in range(9)
        ]

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        if self.game[i][j][k][l] != 0:
                            for m in range(1, 10):
                                if probablities[i * 3 + j][m] == []:
                                    continue

                                probablities[i * 3 + j][m].remove(
                                    (i * 3 + k, j * 3 + l)
                                )

                            probablities[i * 3 + j][self.game[i][j][k][l]] = []

                            continue

                        for m in range(1, 10):
                            if probablities[i * 3 + j][m] == []:
                                continue

                            if (
                                m in self.game[i][j]
                                or m in self.game[i, :, k]
                                or m in self.game[:, j, :, l]
                            ):
                                probablities[i * 3 + j][m].remove(
                                    (i * 3 + k, j * 3 + l)
                                )

        return probablities


def main():
    game = Game(
        np.array(
            [
                [
                    [
                        [5, 3, 0],
                        [6, 0, 0],
                        [0, 9, 8],
                    ],
                    [
                        [0, 7, 0],
                        [1, 9, 5],
                        [0, 0, 0],
                    ],
                    [
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 6, 0],
                    ],
                ],
                [
                    [
                        [8, 0, 0],
                        [4, 0, 0],
                        [7, 0, 0],
                    ],
                    [
                        [0, 6, 0],
                        [8, 0, 3],
                        [0, 2, 0],
                    ],
                    [
                        [0, 0, 3],
                        [0, 0, 1],
                        [0, 0, 6],
                    ],
                ],
                [
                    [
                        [0, 6, 0],
                        [0, 0, 0],
                        [0, 0, 0],
                    ],
                    [
                        [0, 0, 0],
                        [4, 1, 9],
                        [0, 8, 0],
                    ],
                    [
                        [2, 8, 0],
                        [0, 0, 5],
                        [0, 7, 9],
                    ],
                ],
            ]
        )
    )
    player = Player(game)
    player.solve()


if __name__ == "__main__":
    main()
