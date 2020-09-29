'''
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

import numpy as np
from itertools import product

# brute force
def lattice_paths_brute_force(n):

  paths = [p for p in product([(0,1),(1,0)], repeat=2*n) if any(np.sum(p, axis=0)==[n,n])]

  return len(paths)

lattice_paths(6)