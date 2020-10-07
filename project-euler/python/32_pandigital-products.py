'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

from functools import reduce
from itertools import combinations, permutations

def pandigital_products():
  
  digits = '123456789'
  
  def pandigital_check(a, b, p):
    string = str(a) + str(b) + str(p)
    return (reduce(lambda x, y: x+y, sorted(string)) == digits) and (a*b==p)
  
  # 1 digit * 4 digit = 4 digit
  for a in range(2, 10):
    b_digit_pool = digits.replace(str(i), '')
    b_digits = combinations(b_digit_pool, 4)
    for b in b_digits:
#     other_numbers = [''.join(p) for p in permutations(other_digits, 4)]
    
    
    

