import numpy as np
from solver import Solver
from generator import Generator

# gen = Generator()
# board = genboard()
# print('Generated board:')
# print(board)
board = np.array([[7, 5, 9, 8, 4, 3, 6, 2, 0],
                  [8, 7, 4, 0, 6, 5, 0, 0, 0],
                  [0, 0, 2, 9, 0, 0, 0, 0, 0],
                  [5, 2, 7, 0, 0, 0, 3, 9, 1],
                  [9, 4, 0, 6, 8, 0, 0, 5, 0],
                  [4, 0, 0, 3, 0, 0, 9, 8, 0],
                  [1, 0, 0, 0, 3, 0, 0, 4, 5],
                  [0, 6, 0, 4, 0, 0, 0, 0, 0],
                  [0, 0, 3, 0, 0, 0, 7, 0, 0]])
print(board)
sol = Solver(board)
print('Solved board:')
sol.solve()
# sol.howManySolutions()
