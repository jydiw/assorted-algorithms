'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and
b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from common import divisors, primes_below

def amicable_numbers(n):
  pb = primes_below(n)
  ans = []
  for i in [i for i in range(2,n) if i not in pb]:
    p = sum(divisors(i))
    if (sum(divisors(p)) == i) and (i < p):
      print(f'i is {i}')
      print(f'p is sum({divisors(i)})')
      ans.extend((i, p))
  return sum(set(ans))

amicable_numbers(10000)