import os
import numpy as np


class Solver():
    ''' Sudoku solver class '''

    def __init__(self, grid):
        self.grid = grid

    def possible(self, x, y, n):
        ''' Check whether it is possible to put number n in grid[x][y] == 0 '''
        if self.grid[x][y] != 0:
            return False
        # cannot have the same number in each row
        for i in range(9):
            if self.grid[x][i] == n:
                return False
        # cannot have the same number in each column
        for i in range(9):
            if self.grid[i][y] == n:
                return False
        # cannot have the same number in each 3x3 square
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[x0 + i][y0 + j] == n:
                    return False
        return True

    def solve(self):
        ''' Try to solve Sudoku puzzle recursively '''
        for x in range(9):
            for y in range(9):
                if self.grid[x][y] == 0:
                    for n in range(1, 10):
                        if self.possible(x, y, n):
                            self.grid[x][y] = n
                            self.solve()
                            # if failed, reset to 0
                            self.grid[x][y] = 0
                    return
        with open('results.txt', 'a+') as f:
            f.write(str(np.matrix(self.grid)))
            f.write('\n')
        # print(np.matrix(self.grid))
        # print('')
        np.matrix(self.grid)

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


if os.path.isfile('results.txt'):
    os.remove('results.txt')
