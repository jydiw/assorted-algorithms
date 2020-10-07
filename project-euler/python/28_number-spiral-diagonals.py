'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

def spiral_diagonal_sum(n):
  _sum = 0
  for side in range(1, n-1, 2):
    step = (side+2) - 1
    _sum += sum(range(side**2, (side+2)**2, step))
  return _sum + n**2

spiral_diagonal_sum(1001)
