'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

from euler import primes, primes_between

def pandigital_primes(n):
  upper = int(str(n)*n)
  allowed = '123456789'[:n]
  ndp = primes_between(10**(n-1), upper)
  for p in ndp[::-1]:
    if ''.join(sorted(str(p))) == allowed:
      return p

pandigital_primes(7)