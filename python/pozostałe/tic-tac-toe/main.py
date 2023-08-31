from random import choice


class Board:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.empty = [i for i in range(9)]

    def insertLetter(self, letter, pos):
        self.board[pos] = letter
        self.empty.remove(pos)

    def spaceIsFree(self, pos):
        return pos in self.empty

    def printBoard(self):
        return " " + f"\n———+———+———\n ".join(
            [" | ".join(self.board[i : i + 3]) for i in range(3)]
        )

    def selectRandom(self):
        return choice(self.empty)

    def isBoardFull(self):
        return not bool(self.empty)

    def isWinner(self, letter):
        pass
