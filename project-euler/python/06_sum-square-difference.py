'''
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 == 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 == 3025

Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is:
3025 - 385 = 2640

Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.
'''

import numpy as np

# brute force
def sum_square_difference(n):
  first_n = np.arange(1, n+1)
  sum_square = np.dot(first_n, first_n)
  square_sum = np.sum(first_n) ** 2
  return square_sum - sum_square

%timeit sum_square_difference(100)

# using euler and pyramidal numbers
def sum_square_difference_2(n):
  square_sum = ((n+1) * n / 2)**2
  sum_square = n * (n+1) * (2*n+1) / 6
  return square_sum - sum_square

%timeit sum_square_difference_2(100)