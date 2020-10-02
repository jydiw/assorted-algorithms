from functools import reduce
from itertools import combinations, count
from math import floor, log10

def prime_factors(n, include_n=False):
  pfs = [1]
  f = 2
  og = n
  if n in [2, 3]:
    pfs.append(n)
    return pfs
  else:
    while f**2 <= n:
      while n % f == 0:
        pfs.append(f)
        n //= f
      f += 1
      if n != 1:
        if include_n or (n != og):
          pfs.append(n)
    return pfs

def divisors(n, include_n=False):
  pfs = prime_factors(n, include_n=include_n)
  divs = [1]
  end = len(pfs)
  if end >= 2:
    for i in range(2, end):
      combs = set(combinations(pfs, i))
      for comb in combs:
        div = reduce(lambda a, b: a*b, comb)
        divs.append(div)
    if not include_n:
      divs = [d for d in divs if d != n]
  return sorted(list(set(divs)))

def primes():
  nonprimes = {}                        # dictionary to hold nonprimes
  yield 2                               # first prime number
  for i in count(3, 2):                 # all primes after 2 are odd numbers
    k = nonprimes.pop(i, None)          # try to pop from nonprimes
    if k is None:                       # if k is prime
      yield i                           # yield i
      nonprimes[i*i] = i                       # add i*2 to nonprimes
    else:                               # is k is not prime
      x = k + i                         # add next multiple of i if it is odd
      while x in nonprimes or x % 2 == 0:
        x += k
      nonprimes[x] = k

def primes_below(n):
  pr = []
  for p in primes():
    if p < n:
      pr.append(p)
    else:
      break
  return pr


def fibonaccis():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a+b

def digits(n):
  if n == 0:
    n = 1
  return floor(log10(abs(n))+1)