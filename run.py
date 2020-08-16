import numpy as np
from solver import Solver
from generator import Generator

# gen = Generator()
# board = gen.get_board()
# print('Generated board:')
# print(board)

# sol = Solver(board)
# print('Solved board:')
# sol.solve()
# sol.howManySolutions()
grid = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                 [6, 0, 0, 1, 9, 5, 0, 0, 0],
                 [0, 9, 8, 0, 0, 0, 0, 6, 0],
                 [8, 0, 0, 0, 6, 0, 0, 0, 3],
                 [4, 0, 0, 8, 0, 3, 0, 0, 1],
                 [7, 0, 0, 0, 2, 0, 0, 0, 6],
                 [0, 6, 0, 0, 0, 0, 2, 8, 0],
                 [0, 0, 0, 4, 1, 9, 0, 0, 5],
                 [0, 0, 0, 0, 8, 0, 0, 1, 0]])

gen = Generator()
a = gen.find_zeros(grid)
print(a)
