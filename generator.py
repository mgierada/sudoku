import numpy as np
import random


class Generator():
    ''' Sudoku generator class '''

    def __init__(self):
        ''' Generate a board '''
        self.board = np.zeros(81).reshape(9, 9)

    def get_board(self):
        filled_board = self.solve()
        return next(filled_board)

    def possible(self, x, y, n):
        ''' Check whether it is possible to put number n in board[x][y] == 0 '''
        if self.board[x][y] != 0:
            return False
        # cannot have the same number in each row
        for i in range(9):
            if self.board[x][i] == n:
                return False
        # cannot have the same number in each column
        for i in range(9):
            if self.board[i][y] == n:
                return False
        # cannot have the same number in each 3x3 square
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[x0 + i][y0 + j] == n:
                    return False
        return True

    def solve(self):
        ''' Try to solve Sudoku puzzle recursively '''
        for x in range(9):
            for y in range(9):
                if self.board[x][y] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers)
                    for n in numbers:
                        if self.possible(x, y, n):
                            # if self.possible(x, y, n):
                            self.board[x][y] = n
                            yield from self.solve()
                            # if failed, reset to 0
                            self.board[x][y] = 0
                    return
        yield np.matrix(self.board)
