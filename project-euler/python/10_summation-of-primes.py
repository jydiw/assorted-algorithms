'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from itertools import count

# sieve of eratosthenes generator
def primes():
  np = {}                               # dictionary to hold nonprimes
  yield 2                               # first prime number
  for i in count(3, 2):                 # all primes after 2 are odd numbers
    k = np.pop(i, None)                 # try to pop from nonprimes
    if k is None:                       # if k is prime
      yield i                           # yield i
      np[i*i] = i                       # add i*2 to nonprimes
    else:                               # is k is not prime
      x = k + i                         # add next multiple of i if it is odd
      while x in np or x % 2 == 0:
        x += k
      np[x] = k

def primes_below(n):
  pr = []
  for p in primes():
    if p < n:
      pr.append(p)
    else:
      break
  return pr

print(sum(primes_below(2e6)))
%timeit sum(primes_below(2e6))