import os
import numpy as np
# import random
# from random import sample


# print('')


class Solver():
    ''' Sudoku solver class '''

    def __init__(self, grid):
        self.grid = grid

    def possible(self, x, y, n):
        ''' Check whether it is possible to put number n in grid[x][y] == 0 '''
        print(type(self.grid))
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
                        if Solver.possible(self.grid, x, y, n):
                            self.grid[x][y] = n
                            Solver.solve(self.grid)
                            # if failed, reset to 0
                            self.grid[x][y] = 0
                    return
        with open('res_file.txt', 'a+') as f:
            f.write(str(np.matrix(self.grid)))
            f.write('\n')
        f.close()
        print(np.matrix(self.grid))
        print('')

    def howManySolutions(self):
        nsoltmp = []
        with open('res_file.txt', 'r') as f:
            for line in f.readlines():
                if '[[' in line:
                    nsoltmp.append(line[:2])
        nsol = len(nsoltmp)
        print('There are {} solutions'.format(nsol))
        return nsol


if os.path.isfile('res_file.txt'):
    os.remove('res_file.txt')

grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 0, 0]
]

grid = np.matrix(grid)


sol = Solver(grid)
print(grid)
sol.solve()
# sol.howManySolutions()

# # def mask(array):
# #     a = list(array[0])
# #     # print(a)
# #     a_mask = []
# #     for i in range(len(array)):
# #         if i == 0:
# #             a_mask.append(True)
# #         else:
# #             a_mask.append(False)
# #     for i, bool in zip(a, a_mask):
# #         if bool == False:
# #             return i
# # print(a)
# # print(a_mask)


# def board():
#     b = np.zeros(81).reshape(9, 9)
#     for row in range(9):
#         for column in range(9):
#             b[row, column] = np.random.randint(1, 10)
#     check_row(b, 0)
#     # check_board(b)
#     # print(b)


# def check_board(b):
#     for row in range(9):
#         check_row(b, row)
#     for column in range(9):
#         check_column(b, column)


# def check_row(b, n_row):
#     row = b[n_row, :]
#     print(row)
#     indices_to_be_removed = []
#     for unique_number in np.unique(row):
#         how_many_occurences = np.where(row == unique_number)[0]
#         # if there is more than one occurence of the number,
#         if how_many_occurences.shape[0] > 1:
#             # index = np.where(row == unique_number)[0][1]
#             # print('Without mask')
#             # print(unique_number, how_many_occurences)
#             for num, i in enumerate(how_many_occurences):
#                 # print(i)
#                 # print('With mask')
#                 # print(unique_number, mask(np.where(row == unique_number)))
#                 # index = np.where(row == unique_number)[0][1]
#                 # print(index)
#                 # if index == 0:
#                 #     break
#                 if num != 0:
#                     indices_to_be_removed.append(i)
#     # print(indices_to_be_removed)
#     # setting indices equal to 0
#     for index in indices_to_be_removed:
#         row[index] = 0
#     print(row)


# def check_column(b, n_column):
#     column = b[:, n_column]
#     indices_to_be_removed = []
#     for unique_number in np.unique(column):
#         how_many_occurences = np.where(column == unique_number)[0]
#         # if there is more than one occurence of the number,
#         if how_many_occurences.shape[0] > 1:
#             index = np.where(column == unique_number)[0][1]
#             indices_to_be_removed.append(index)
#         # setting indices equal to 0
#         for index in indices_to_be_removed:
#             column[index] = 0


# board()
