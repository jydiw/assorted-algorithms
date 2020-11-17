from functools import reduce
from itertools import combinations, count
from math import floor, log10

### GENERATORS ###

def primes():
  nonprimes = {}
  yield 2
  # all primes after 2 are odd numbers
  for i in count(3, 2):
    # try to pop from nonprimes
    k = nonprimes.pop(i, None)
    # yield i if not in nonprimes
    if k is None:
      yield i
      nonprimes[i*i] = i
    # add next odd multiple of i
    else:
      x = k + i
      while x in nonprimes or x % 2 == 0:
        x += k
      nonprimes[x] = k


def fibonaccis():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a+b


def triangle_numbers():
  for i in count(1, 1):
    yield i * (i+1) / 2


### FACTORIZATION UTILITIES ###

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


### OTHER TOOLS ###

def primes_below(n):
  pr = []
  for p in primes():
    if p < n:
      pr.append(p)
    else:
      break
  return pr


def primes_between(a, b):
  pr = []
  for p in primes():
    if p > a:
      if p < b:
        pr.append(p)
      else:
        break
  return pr


def integer_digits(n):
  if n == 0:
    n = 1
  return floor(log10(abs(n))+1)


def pythagorean_triplet(p):
  triplets = []
  for a in range(1, p//2 + 1):
    b = (p**2 - 2*a*p) // (2*p - 2*a)
    if b < a:
      continue
    c = p - a - b
    if (a**2 + b**2) == c**2:
      triplets.append((a,b,c))
  return triplets