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
        with open('res_file.txt', 'a+') as f:
            f.write(str(np.matrix(self.grid)))
            f.write('\n')
        print(np.matrix(self.grid))
        print('')
        np.matrix(self.grid)

    def howManySolutions(self):
        nsoltmp = []
        with open('res_file.txt', 'r') as f:
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


if os.path.isfile('res_file.txt'):
    os.remove('res_file.txt')

###
# tests

# grid = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
#                  [6, 0, 0, 1, 9, 5, 0, 0, 0],
#                  [0, 9, 8, 0, 0, 0, 0, 6, 0],
#                  [8, 0, 0, 0, 6, 0, 0, 0, 3],
#                  [4, 0, 0, 8, 0, 3, 0, 0, 1],
#                  [7, 0, 0, 0, 2, 0, 0, 0, 6],
#                  [0, 6, 0, 0, 0, 0, 2, 8, 0],
#                  [0, 0, 0, 4, 1, 9, 0, 0, 5],
#                  [0, 0, 0, 0, 8, 0, 0, 1, 0]])

# grid = np.array([[5, 3, 4, 6, 7, 8, 1, 9, 2],
#                  [6, 7, 2, 1, 9, 5, 3, 4, 8],
#                  [1, 9, 8, 3, 4, 2, 5, 6, 7],
#                  [8, 5, 9, 7, 6, 1, 4, 2, 3],
#                  [4, 2, 6, 8, 5, 3, 9, 7, 1],
#                  [7, 1, 3, 9, 2, 4, 8, 5, 6],
#                  [9, 6, 1, 5, 3, 7, 2, 8, 4],
#                  [2, 8, 7, 4, 1, 9, 6, 3, 5],
#                  [3, 4, 5, 2, 8, 6, 7, 1, 9]])
# grid = np.zeros(81).reshape(9, 9)
# print(grid)
# print('-------')
# print(a)
# sol = Solver(grid)
# sol.solve()
# sol.howManySolutions()
