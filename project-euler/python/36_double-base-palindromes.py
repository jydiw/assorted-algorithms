'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
'''

# if no leading zeroes, that means base 2 number has to start and end with 1
# meaning the number must be odd

# brute force
def is_palindrome(n):
  n = str(n)
  return n == n[::-1]

def double_base_palindromes(n):
  sums = 0
  for i in range(1,n,2):
    if is_palindrome(i) and is_palindrome(bin(i)[2:]):
      sums += i
  return sums

double_base_palindromes(1_000_000)


