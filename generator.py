import numpy as np


class Generator():
    ''' Sudoku generator class '''

    def board(self):
        ''' Generate a board '''
        # create an empty 9x9 board, i.e. A board filled with zeros.
        b = np.zeros(81).reshape(9, 9)
        # fill the empty board with random integers in a range 1-9
        for row in range(9):
            for column in range(9):
                b[row, column] = np.random.randint(1, 10)
        # check, whether numbers in rows and columns are possible.
        # If not, put "0" instead
        Generator.check_board(self, b)
        print(b)

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
        indices_to_set_zero = []
        for unique_number in np.unique(row):
            # if there are more than one occurence of the number in the array,
            # get indices of them
            how_many_occurences = np.where(row == unique_number)[0]
            # It's a 1D array, so .shape[0] acts similar like len() on lists
            if how_many_occurences.shape[0] > 1:
                # loop through all
                for i in np.where(row == unique_number)[0]:
                    index = np.where(row == unique_number)[0][1]
                    indices_to_set_zero.append(index)
            # setting indices equal to 0
            for index in indices_to_set_zero:
                row[index] = 0

    def check_column(self, b, n_column):
        ''' Check row for any impossible combination of numbers.

        Parameters:
        ___________

        b : ndarray
            an array with numbers to be checked, i.e. a board
        n_column : int
            a number of the column to be checked        

        '''
        column = b[:, n_column]
        indices_to_set_zero = []
        for unique_number in np.unique(column):
            # if there are more than one occurence of the number in the array,
            # get indices of them
            how_many_occurences = np.where(column == unique_number)[0]
            # It's a 1D array, so .shape[0] acts similar like len() on lists
            if how_many_occurences.shape[0] > 1:
                # loop through all
                for i in np.where(column == unique_number)[0]:
                    index = np.where(column == unique_number)[0][1]
                    indices_to_set_zero.append(index)
            # setting indices equal to 0
            for index in indices_to_set_zero:
                column[index] = 0


gen = Generator()
gen.board()
