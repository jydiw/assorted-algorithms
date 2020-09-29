'''
A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

from itertools import combinations

def largest_palindrome(n):
  nums = range(10**(n-1), 10**(n))
  prods = sorted(
    list(set([p[0]*p[1] for p in combinations(nums, 2)])), 
    reverse=True
  )
  for p in prods:
    if is_palindrome(p):
      return p

def is_palindrome(p):
  return str(p) == str(p)[::-1]

%timeit print(largest_palindrome(3))