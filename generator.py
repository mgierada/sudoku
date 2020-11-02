import numpy as np
from solver import Solver
import random


class Generator():
    ''' Sudoku generator class '''

    # def __init__(self):
    #     ''' Generate a board '''
    #     self.board = np.zeros(81).reshape(9, 9)

    def get_board(self):
        self.board = np.zeros(81).reshape(9, 9)
        next(self.solve())
        self.remove()
        # self.check_solution()
        # self.howManySolutions()
        checking = Solver(self.board)
        checking.solve()
        checking.howManySolutions()
        return self.board

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

    def remove(self):
        zeros = 0
        while zeros <= 40:
            row, col = random.randint(0, 8), random.randint(0, 8)
            self.board[row][col] = 0
            zeros = len(np.where(self.board == 0.)[0])
        return self.board

    def check_solution(self):
        ''' Try to solve Sudoku puzzle recursively '''
        for x in range(9):
            for y in range(9):
                if self.board[x][y] == 0:
                    for n in range(1, 10):
                        if self.possible(x, y, n):
                            self.board[x][y] = n
                            self.solve()
                            # if failed, reset to 0
                            self.board[x][y] = 0
                    return
        with open('results.txt', 'a+') as f:
            f.write(str(np.matrix(self.board)))
            f.write('\n')

    def howManySolutions(self):
        nsoltmp = []
        with open('results.txt', 'r') as f:
            for line in f.readlines():
                if '[[' in line:
                    nsoltmp.append(line[:2])
        nsol = len(nsoltmp)
        if nsol == 1:
            print('There is {} solution'.format(nsol))
            return nsol
        else:
            print('There are {} solutions'.format(nsol))
            return nsol
