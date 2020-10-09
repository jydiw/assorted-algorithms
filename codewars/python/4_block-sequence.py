'''
Consider the following array:

[1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789,
12345678910, 1234567891011...]

If we join these blocks of numbers, we come up with an infinite sequence which
starts with 112123123412345123456.... The list is infinite.

You will be given an number (n) and your task will be to return the element at
that index in the sequence, where 1 ≤ n ≤ 10^18. Assume the indexes start with
1, not 0. For example:

solve(1) = 1, because the first character in the sequence is 1. There is no
index 0.
solve(2) = 1, because the second character is also 1.
solve(3) = 2, because the third character is 2.
More examples in the test cases. Good luck!
'''
from math import floor, log10, sqrt

'''
# brute force method
def solve(n):
  k = n
  i = 0
  a = ''
  while n >= 0:
    i += 1
    a += str(i)
    n -= len(a)
  return a[n-1]
'''


def solve(n):
  k = 1
  i = 1
  while i < n:
    i = int(sqrt(2*k + 0.25) - 0.5)
    k += 1
  # k = i*(i+1) / 2
  return k

def triangular_number(n):



solve(31000)
floor(log10(999))