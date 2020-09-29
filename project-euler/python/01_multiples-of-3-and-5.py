'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def sum_multiples(n, a=3, b=5):
  return sum([i for i in range(1, n) if i%a==0 or i%b==0])

print(sum_multiples(1000))