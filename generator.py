import numpy as np
import random


class Generator():
    ''' Sudoku generator class '''

    def board(self):
        ''' Generate a board '''
        # create an empty 9x9 board, i.e. A board filled with zeros.
        rows = []
        for _ in range(9):
            row = random.sample(range(1, 10), 9)
            rows.append(row)
        b = np.array(rows)
        # b = np.append(np.array(row), np.array(row), axis=0)
        # print(row)

        # fill the empty board with random integers in a range 1-9
        # for row in range(9):
        #     for column in range(9):
        #         b[row, column] = np.random.randint(1, 10)
        # print(b)
        # check, whether numbers in rows and columns are possible.
        # If not, put "0" instead
        # Generator.check_board(self, b)
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
        self.check_square(b)

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


gen = Generator()
board = gen.board()
print(board)
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

# new_board = np.append(small_square1, small_square2, axis=0)
# print(new_board)

# print(small_square)
