import os
import numpy as np
# import random
from random import sample

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

# print(np.matrix(grid))
# print('')


def possible(grid, x, y, n):
    # global grid
    if grid[x][y] != 0:
        return False
    # cannot have the same number in each row
    for i in range(9):
        # print(grid[0][i])
        if grid[x][i] == n:
            return False
    # cannot have the same number in each column
    for i in range(9):
        # print(grid[i][0])
        if grid[i][y] == n:
            return False
    # cannot have the same number in each 3x3 square
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[x0 + i][y0 + j] == n:
                return False
    return True

# print(possible(grid, 0, 0, 9))


def solve(grid):
    # global grid
    # a = []
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1, 10):
                    if possible(grid, x, y, n):
                        grid[x][y] = n
                        solve(grid)
                        grid[x][y] = 0
                        # return[]
                return
    with open('res_file.txt', 'a+') as f:
        f.write(str(np.matrix(grid)))
        f.write('\n')
    f.close()
    print(np.matrix(grid))
    print('')
    # a = len(np.array(grid))
    # print(a)
    # nsol.append(np.matrix(grid))

    # input('Is it more:')
    # print(grid)


def howManySolutions():
    nsoltmp = []
    with open('res_file.txt', 'r') as f:
        for line in f.readlines():
            if '[[' in line:
                nsoltmp.append(line[:2])
    nsol = len(nsoltmp)
    print(lnsol)
    return nsol


def board():
    b = np.zeros(81).reshape(9, 9)
    for row in range(9):
        for column in range(9):
            b[row, column] = np.random.randint(1, 10)
    for row in range(9):
        check_row(b, row)
    for column in range(9):
        check_column(b, column)
    print(b)


def check_row(b, n_row):
    row = b[n_row, :]
    indices_to_be_removed = []
    for unique_number in np.unique(row):
        how_many_occurences = np.where(row == unique_number)[0]
        # if there is more than one occurence of the number,
        if how_many_occurences.shape[0] > 1:
            index = np.where(row == unique_number)[0][1]
            indices_to_be_removed.append(index)
        # setting indices equal to 0
        for index in indices_to_be_removed:
            row[index] = 0


def check_column(b, n_column):
    column = b[:, n_column]
    indices_to_be_removed = []
    for unique_number in np.unique(column):
        how_many_occurences = np.where(column == unique_number)[0]
        # if there is more than one occurence of the number,
        if how_many_occurences.shape[0] > 1:
            index = np.where(column == unique_number)[0][1]
            indices_to_be_removed.append(index)
        # setting indices equal to 0
        for index in indices_to_be_removed:
            column[index] = 0


board()
