import numpy as np
from solver import Solver
from generator import Generator

gen = Generator()
board = gen.board()
print('Generated board:')
print(board)

sol = Solver(board)
print('Solved board:')
sol.solve()
# sol.howManySolutions()
