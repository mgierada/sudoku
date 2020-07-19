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

    row1 = b[0, :]
    print(row1)
    for num in b[0, :]:
        if num in row1:
            b[0, row] = 0

    print(b)


board()


# solve(grid)
# base = 5
# side = base * base

# pattern for a baseline valid solution


# def pattern(r, c):
#     return (base * (r % base) + r // base + c) % side

# # randomize rows, columns and numbers (of valid base pattern)

# def shuffle(s):
#     return sample(s, len(s))


# rBase = range(base)
# rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
# cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
# nums = shuffle(range(1, base * base + 1))

# # produce board using randomized baseline pattern
# board = [[nums[pattern(r, c)] for c in cols] for r in rows]

# print('Solved sudoku')
# for line in board:
#     print(line)

# squares = side * side
# empties = squares * 3 // 4
# for p in sample(range(squares), empties):
#     board[p // side][p % side] = 0

# numSize = len(str(side))
# print('To be solved')
# for line in board:
#     print("[" + "  ".join(f"{n or '.':{numSize}}" for n in line) + "]")

# def expandLine(line):
#     return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]

# line0  = expandLine("╔═══╤═══╦═══╗")
# line1  = expandLine("║ . │ . ║ . ║")
# line2  = expandLine("╟───┼───╫───╢")
# line3  = expandLine("╠═══╪═══╬═══╣")
# line4  = expandLine("╚═══╧═══╩═══╝")

# symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # symbol = []
# # for i in range(1, base * base + 1):
# #     symbol.append(str(i))
# # print(symbol)

# nums   = [ [""]+[symbol[n] for n in row] for row in board ]
# print(line0)
# for r in range(1,side+1):
#     print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
#     print([line2,line3,line4][(r%side==0)+(r%base==0)])
