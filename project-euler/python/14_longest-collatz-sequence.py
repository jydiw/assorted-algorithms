'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def collatz(n):
  yield n
  while True:
    if n <= 1:
      break
    elif n % 2 == 0:
      n //= 2
      yield n
    else:
      n = 3*n + 1
      yield n

def longest_collatz_sequence(n):
  l = 1
  c = 1
  n = int(n)
  for i in range(2, n):
    lc = len(list(collatz(i)))
    if lc > l:
      l = lc
      c = i
  return c

longest_collatz_sequence(1e6)