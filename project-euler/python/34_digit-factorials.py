'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''

from functools import reduce
from math import factorial
from euler import digits
import matplotlib.pyplot as plt


def simple(n, check=True):
  ns = [factorial(int(c)) for c in str(n)]
  sums = reduce(lambda a, b: a+b, ns)
  if check:
    return n == sums
  return sums

def digit_factorials(limit=2540161):
  # naive upper limit is 9_999_999, since 7 * 9! is 2540160
  facts = []
  for i in range(3, limit):
    if simple(i):
      facts.append(i)
  return facts