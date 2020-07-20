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
        check_board(b)
        print(b)

    def check_board(b):
        ''' Check all rows and column to find repeted numbers that
        are not allowed in the puzzle 

        Parameters:
        ___________

        b : ndarray
            an array with numbers to be checked, i.e. a board

        '''
        for row in range(9):
            check_row(b, row)
        for column in range(9):
            check_column(b, column)

    def check_row(b, n_row):
        row = b[n_row, :]
        # print(row)
        indices_to_be_removed = []
        for unique_number in np.unique(row):
            how_many_occurences = np.where(row == unique_number)[0]
            # if there is more than one occurence of the number,
            if how_many_occurences.shape[0] > 1:
                # index = np.where(row == unique_number)[0][1]
                # print('Without mask')
                # print(unique_number, np.where(row == unique_number)[0])
                for i in np.where(row == unique_number)[0]:
                    # print(i)
                    # print('With mask')
                    # print(unique_number, mask(np.where(row == unique_number)))
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
