'''
2520 is the smallest number that can be divided by each of the numbers from 1 
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?
'''

def prime_factors(n):
  f = 2
  factors = []
  while f**2 <= n:
    count = 0
    while n % f == 0:
      n //= f
      count += 1
    if count > 0:
      factors.append([f, count])
    f += 1
  if n != 1:
    factors.append([n, 1])
  return factors

def smallest_multiple(n):
  factors = []
  for i in range(2,n+1):
    factors.extend(prime_factors(i))
  factors = dict(sorted(factors, key=lambda x: x[1]))
  product = 1
  for k, v in factors.items():
    product *= k**v
  return product

%timeit smallest_multiple(20)