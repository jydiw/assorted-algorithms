'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def pythagorean_triplet(s):
  for a in range(1, s):
    b = (s**2 - 2*a*s) // (2*s - 2*a)
    c = s - a - b
    if (a**2 + b**2) == c**2:
      return a * b * c

%timeit pythagorean_triplet(1000)