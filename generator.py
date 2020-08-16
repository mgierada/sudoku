import numpy as np
import random
from solver import Solver
import sys

sys.setrecursionlimit(10**6)


class Generator():
    ''' Sudoku generator class '''

    # def __init__(self):
    #     ''' Generate a board '''
    # board = np.zeros(81).reshape(9, 9)

    def get_board(self):
        # create an empty 9x9 board, i.e. A board filled with zeros.
        board = np.zeros(81).reshape(9, 9)
        self.solve(board)
        # print(board)
        # while self.find_zeros(board):
        #     board = self.solve(board)
        #     print(board)
        # else:
        #     return board

    def find_zeros(self, board):
        ''' Return False if there are some zeros '''
        counts = np.unique(board, 0, return_counts=True)[1][0]
        if counts == 0:
            return False
        else:
            return True

    def solve(self, board):
        solver = Solver(board)
        print(board)
        for row in range(9):
            for column in range(9):
                n = np.random.randint(10)
                try:
                    while solver.possible(row, column, n) is False:
                        n = np.random.randint(10)
                    board[row][column] = n
                    print(board)
                except solver.possible(x, y, n) is False:
                    print('False')
        # for x in range(9):
        #     for y in range(9):
        #         if board[x][y] == 0:
        #             ok_number = False
        #             # n = random.sample(range(1, 10), 9):
        #             n = np.random.randint(10)
        #             while ok_number is False:
        #                 if solver.possible(x, y, n):
        #                     board[x][y] = n
        #                     self.solve(board)
        #                     ok_number = True
        #             print(board)

        # else:
        #     board[x][y] = 0
        # self.solve(board)
        # else:
        #     ok_number = False
        # return board
        # else:
        #     pass
        # print(board)
        # else:
        #     board[x][y] = 0
        #     ok_number = False
        # print(board)
        # else:
        #     #     y = y - 1
        #     #     # x = x - 1
        #     board[x][y] = 0
        #     self.solve(board)
        #     self.solve(board)
        #     ok_number = True
        # self.solve(board)
        # board[x][y] = n
        # self.solve(board)
        # ok_number = True
        # else:
        #     board[x][y] = 0
        # ok_number = True
        # print(board)

        # print(board)
        # else:
        #     self.get_board()

        # print(board)
        # return board

    # A function to check if the grid is full

    def check_grid(self, grid):
        for row in range(0, 9):
            for col in range(0, 9):
                if grid[row][col] == 0:
                    return False

        # We have a complete grid!
        return True

    def check_for_solution(self, board):
        solver = Solver(board)
        if not solver.solve():
            self.get_board()

        # rows = []
        # for _ in range(9):
        #     row = random.sample(range(1, 10), 9)
        #     rows.append(row)
        # b = np.array(rows)
        # b = np.append(np.array(row), np.array(row), axis=0)
        # print(row)

        # fill the empty board with random integers in a range 1-9
        # for row in range(9):
        #     for column in range(9):
        #         b[row, column] = np.random.randint(1, 10)
        # print(b)
        # check, whether numbers in rows and columns are possible.
        # If not, put "0" instead
        Generator.check_board(self, b)
        return b

    def check_board(self, b):
        ''' Check all rows and column to find repeted numbers that
        are not allowed in the puzzle.

        Parameters:
        ___________

        b : ndarray
            an array with numbers to be checked, i.e. a board

        '''
        for row in range(9):
            Generator.check_row(self, b, row)
        for column in range(9):
            Generator.check_column(self, b, column)
        # self.check_square(b)

    def check_row(self, b, n_row):
        ''' Check row for any impossible combination of numbers.

        Parameters:
        ___________

        b : ndarray
            an array with numbers to be checked, i.e. a board
        n_row : int
            a number of the row to be checked

        '''
        row = b[n_row, :]
        set_indices_to_zero = []
        for unique_number in np.unique(row):
            # if there are more than one occurence of the number in the array,
            # get indices of them
            how_many_occurences = np.where(row == unique_number)[0]
            # It's a 1D array, so .shape[0] acts similar like len() on lists
            if how_many_occurences.shape[0] > 1:
                # loop through all
                for idx, occurence in enumerate(how_many_occurences):
                    # skip the first value, beacouse it is a valid number
                    if idx != 0:
                        set_indices_to_zero.append(occurence)
        # setting indices equal to 0
        for index in set_indices_to_zero:
            row[index] = 0

    def check_column(self, b, n_column):
        ''' Check column for any impossible combination of numbers.

        Parameters:
        ___________

        b : ndarray
            an array with numbers to be checked, i.e. a board
        n_column : int
            a number of the column to be checked

        '''
        column = b[:, n_column]
        set_indices_to_zero = []
        for unique_number in np.unique(column):
            # if there are more than one occurence of the number in the array,
            # get indices of them
            how_many_occurences = np.where(column == unique_number)[0]
            # It's a 1D array, so .shape[0] acts similar like len() on lists
            if how_many_occurences.shape[0] > 1:
                # loop through all
                for idx, occurence in enumerate(how_many_occurences):
                    # skip the first value, beacouse it is a valid number
                    if idx != 0:
                        set_indices_to_zero.append(occurence)
        # setting indices equal to 0
        for index in set_indices_to_zero:
            column[index] = 0

    def check_square(self, b, ind_row, ind_column):
        # cannot have the same number in each 3x3 square
        #
        # ind = [0, 1, 2]
        # get the first 3x3 square by using fancy indexing
        square_b = b[:, ind_row][ind_column, :]
        square_b = square_b.reshape(9)
        set_indices_to_zero = []
        for unique_number in np.unique(square_b):
            how_many_occurences = np.where(square_b == unique_number)[0]
            if how_many_occurences.shape[0] > 1:
                for idx, occurence in enumerate(how_many_occurences):
                    # skip the first value, beacouse it is a valid number
                    if idx != 0:
                        set_indices_to_zero.append(occurence)
        for index in set_indices_to_zero:
            square_b[index] = 0
        square_b = square_b.reshape(3, 3)
        return square_b

# checked_board = gen.check_for_solution()
# print(checked_board)
# TODO I need a way to do it in a more pythonic way
# small_square1 = gen.check_square(board, [0, 1, 2], [0, 1, 2])
# small_square2 = gen.check_square(board, [0, 1, 2], [3, 4, 5])
# small_square3 = gen.check_square(board, [0, 1, 2], [6, 7, 8])
# small_square4 = gen.check_square(board, [3, 4, 5], [0, 1, 2])
# small_square5 = gen.check_square(board, [3, 4, 5], [3, 4, 5])
# small_square6 = gen.check_square(board, [3, 4, 5], [6, 7, 8])
# small_square7 = gen.check_square(board, [6, 7, 8], [0, 1, 2])
# small_square8 = gen.check_square(board, [6, 7, 8], [3, 4, 5])
# small_square9 = gen.check_square(board, [6, 6, 8], [6, 7, 8])

# column1 = np.concatenate((small_square1, small_square2, small_square3), axis=0)
# column2 = np.concatenate((small_square4, small_square5, small_square6), axis=0)
# column3 = np.concatenate((small_square7, small_square8, small_square9), axis=0)
# new_board = np.concatenate((column1, column2, column3), axis=1)
# print(new_board)

# sol = Solver(new_board)
# print('Solved board:')
# while sol.solve() is None:
#     gen = Generator()
#     board = gen.board()
#     print(board)
#     # TODO I need a way to do it in a more pythonic way
#     small_square1 = gen.check_square(board, [0, 1, 2], [0, 1, 2])
#     small_square2 = gen.check_square(board, [0, 1, 2], [3, 4, 5])
#     small_square3 = gen.check_square(board, [0, 1, 2], [6, 7, 8])
#     small_square4 = gen.check_square(board, [3, 4, 5], [0, 1, 2])
#     small_square5 = gen.check_square(board, [3, 4, 5], [3, 4, 5])
#     small_square6 = gen.check_square(board, [3, 4, 5], [6, 7, 8])
#     small_square7 = gen.check_square(board, [6, 7, 8], [0, 1, 2])
#     small_square8 = gen.check_square(board, [6, 7, 8], [3, 4, 5])
#     small_square9 = gen.check_square(board, [6, 6, 8], [6, 7, 8])

#     column1 = np.concatenate((small_square1, small_square2, small_square3), axis=0)
#     column2 = np.concatenate((small_square4, small_square5, small_square6), axis=0)
#     column3 = np.concatenate((small_square7, small_square8, small_square9), axis=0)
#     new_board = np.concatenate((column1, column2, column3), axis=1)
#     print(new_board)

#     sol = Solver(new_board)G


gen = Generator()
board = gen.get_board()
# print(board)
