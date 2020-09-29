'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

def largest_prime_factor(n):
  f = 2
  while f**2 <= n:
    while n % f == 0:
      n //= f
    f += 1
  return max(f-1, n)

print(largest_prime_factor(600851475143))