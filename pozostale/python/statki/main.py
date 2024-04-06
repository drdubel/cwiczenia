import random
import time

import numpy as np


def get_new_board():
    board = np.zeros((10, 10), dtype=np.int8) - 1

    return board


class Game:
    def __init__(self):
        self._board1 = get_new_board()
        self._board2 = get_new_board()
        self._ships1 = [[2, []], [3, []], [4, []], [5, []], [3, []]]
        self._ships2 = [[2, []], [3, []], [4, []], [5, []], [3, []]]
        self.ship_lengths1 = [2, 3, 3, 4, 5]
        self.ship_lengths2 = [2, 3, 3, 4, 5]

    def place_ship(self, x, y, length, player, vertical=False):
        if player == 1:
            ship_id = length - 2 if length != 3 or not self._ships1[1][1] else 4

            for i in range(length):
                self._ships1[ship_id][1].append(
                    (x + i if vertical else x, y + i if not vertical else y)
                )

            self._board1[
                x : x + length if vertical else x + 1,
                y : y + length if not vertical else y + 1,
            ] = 0

        else:
            ship_id = length - 2 if length != 3 or not self._ships2[1][1] else 4

            for i in range(length):
                self._ships2[ship_id][1].append(
                    (x + i if vertical else x, y + i if not vertical else y)
                )

            self._board2[
                x : x + length if vertical else x + 1,
                y : y + length if not vertical else y + 1,
            ] = 0

    def shoot(self, x, y, player):
        if player == 1:
            if self._board2[x, y] == 0:
                self._board2[x, y] = 1

                if player == 1:
                    for ship in self._ships2:
                        if (x, y) in ship[1]:
                            ship[1].remove((x, y))

                            if not ship[1]:
                                self.ship_lengths2.remove(ship[0])
                                return "sunk"

                return "hit"

            elif self._board2[x, y] == -1:
                self._board2[x, y] = 2
                return "miss"

            else:
                return False

    def autoplay(self):
        player1 = Player(self, 1)
        player2 = Player(self, 2)

        print(self._board1)
        while self.ship_lengths1 and self.ship_lengths2:
            player1.move()
            player2.move()

        print(player1.moves, player2.moves)


class Player:
    def __init__(self, game: Game, id: int):
        self.game = game
        self.board = get_new_board()
        self.id = id
        self.moves = 0

        self.place_ships()

    def place_ships(self):
        for ship in self.game._ships1:
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                vertical = random.choice([True, False])

                if (
                    (vertical and x + ship[0] <= 10)
                    or (not vertical and y + ship[0] <= 10)
                ) and (
                    (vertical and (self.board[x : x + ship[0], y] == -1).all())
                    or (not vertical and (self.board[x, y : y + ship[0]] == -1).all())
                ):
                    self.game.place_ship(x, y, ship[0], self.id, vertical)

                    if vertical:
                        self.board[
                            max(0, x - 1) : min(10, x + ship[0] + 1),
                            max(0, y - 1) : min(10, y + 2),
                        ] = 0

                    else:
                        self.board[
                            max(0, x - 1) : min(10, x + 2),
                            max(0, y - 1) : min(10, y + ship[0] + 1),
                        ] = 0

                    break

        self.board = get_new_board()

    def count_possible_ships(self):
        possibilities = np.zeros((10, 10), dtype=np.int8)
        for _ in range(2):
            for i in range(10):
                for j in range(9):
                    for ship_len in np.unique(
                        self.game.ship_lengths1
                        if self.id == 2
                        else self.game.ship_lengths2
                    ):
                        if 10 - j < ship_len:
                            break

                        if (self.board[i, j : j + ship_len] == -1).all():
                            possibilities[i, j : j + ship_len] += 1

            self.board = self.board.transpose()
            possibilities = possibilities.transpose()

        return possibilities

    def get_best_move(self):
        possibilities = self.count_possible_ships()
        x = possibilities.argmax() // 10
        y = possibilities.argmax() % 10

        return x, y

    def shoot_ship(self):
        x, y = random.choice(np.fromiter(zip(*np.where(self.board == 2)), dtype=tuple))

        return x, y

    def move(self):
        self.moves += 1

        if (self.board == 2).any():
            x, y = self.shoot_ship()

        else:
            x, y = self.get_best_move()

        result = self.game.shoot(x, y, self.id)

        if result == "hit":
            self.board[x, y] = 1

            if (x - 1 >= 0 and self.board[x - 1, y] == 1) or (
                x + 1 < 10 and self.board[x + 1, y] == 1
            ):
                wrong = (self.board[x - 1 : x + 2, y - 1 : y + 2] == 2)[:, ::2]
                wrong[wrong == 2] = 0

            elif (y - 1 >= 0 and self.board[x, y - 1] == 1) or (
                y + 1 < 10 and self.board[x, y + 1]
            ) == 1:
                wrong = [self.board[x - 1 : x + 2, y - 1 : y + 2] == 2][::2]
                wrong[wrong == 2] = 0

            if x - 1 < 0 or x + 2 > 10 or y - 1 < 0 or y + 2 > 10:
                print("nei działa")

            neighbors = self.board[
                max(x - 1, 0) : min(10, x + 2), max(y - 1, 0) : min(10, y + 2)
            ]
            neighbors[neighbors == -1] = 2

            if x - 1 < 0:
                corners = neighbors[1, ::2]

            if x + 1 > 10:
                corners = neighbors[0, ::2]

            if y - 1 < 0:
                corners = neighbors[::2, 1]

            if y + 1 > 10:
                corners = neighbors[::2, 0]

            corners = neighbors[::2, ::2]

            corners[corners == 2] = 0

            print(self.board)

            self.move()

        elif result == "sunk":
            self.board[x, y] = 1

            neighbors = self.board[
                max(x - 1, 0) : min(10, x + 2), max(y - 1, 0) : min(10, y + 2)
            ]

            neighbors[neighbors == -1] = 0

            self.move()

        elif result == "miss":
            self.board[x, y] = 0


def main():
    game = Game()

    game.autoplay()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
