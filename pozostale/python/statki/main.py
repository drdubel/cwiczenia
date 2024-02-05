import random

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
                            print(ship[1], x, y)
                            ship[1].remove((x, y))

                            if not ship[1]:
                                print(ship[0])
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

        while self.ship_lengths1 and self.ship_lengths2:
            player1.move()
            player2.move()


class Player:
    def __init__(self, game: Game, id: int):
        self.game = game
        self.board = get_new_board()
        self.id = id

        self.place_ships()

    def place_ships(self):
        self.game.place_ship(4, 4, 5, self.id, vertical=True)
        self.game.place_ship(2, 2, 4, self.id, vertical=True)
        self.game.place_ship(3, 6, 3, self.id)
        self.game.place_ship(6, 6, 3, self.id)
        self.game.place_ship(0, 0, 2, self.id, vertical=True)

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

    def shoot_ship(self):
        x, y = random.choice(np.fromiter(zip(*np.where(self.board == 2)), dtype=tuple))

        return x, y

    def get_best_move(self):
        possibilities = self.count_possible_ships()
        x = possibilities.argmax() // 10
        y = possibilities.argmax() % 10

        return x, y

    def move(self):
        if (self.board == 2).any():
            print("Shooting ship")
            x, y = self.shoot_ship()

        else:
            x, y = self.get_best_move()

        print(f"Shooting at {x}, {y}")
        result = self.game.shoot(x, y, self.id)

        if result == "hit":
            print("Hit!")
            self.board[x, y] = 1

            if self.board[x - 1, y] == 1 or self.board[x + 1, y] == 1:
                wrong = (self.board[x - 1 : x + 2, y - 1 : y + 2] == 2)[:, ::2]
                print(wrong)
                wrong[wrong == 2] = 0

            elif self.board[x, y - 1] == 1 or self.board[x, y + 1] == 1:
                wrong = [self.board[x - 1 : x + 2, y - 1 : y + 2] == 2][::2]
                print(wrong)
                wrong[wrong == 2] = 0

            if self.board[x - 1, y] == -1:
                self.board[x - 1, y] = 2

            if self.board[x + 1, y] == -1:
                self.board[x + 1, y] = 2

            if self.board[x, y - 1] == -1:
                self.board[x, y - 1] = 2

            if self.board[x, y + 1] == -1:
                self.board[x, y + 1] = 2

            neighbors = self.board[x - 1 : x + 2, y - 1 : y + 2]
            corners = neighbors[::2, ::2]

            corners[corners == -1] = 0

            print(self.board)
            print("coś nie tak?")
            self.move()

        elif result == "sunk":
            print("Hit and sunk!")
            self.board[x, y] = 1

            neighbors = self.board[x - 1 : x + 2, y - 1 : y + 2]

            neighbors[neighbors == -1] = 0

            print(self.board)
            self.move()

        elif result == "miss":
            print("Miss!")
            print(x, y)
            self.board[x, y] = 0
            print(self.board)


def main():
    game = Game()

    game.autoplay()


if __name__ == "__main__":
    main()
