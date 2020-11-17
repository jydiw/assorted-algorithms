'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
'''

import re
from functools import reduce
from itertools import count
from string import ascii_lowercase

def triangle_numbers():
  for i in count(1, 1):
    yield i * (i+1) / 2

def is_triangle(n):
  for t in triangle_numbers():
    if t == n:
      return True
    elif t > n:
      return False

def nth_triangle(n):
  if n < 1:
    return None
  for i, t in enumerate(triangle_numbers(), 1):
    if i == n:
      return int(t)

def parse_word(word):
  sub = [ascii_lowercase.index(c)+1 for c in word.lower()]
  return is_triangle(reduce(lambda a, b: a+b, sub))


words = open('../files/p042_words.txt', 'r')
words = words.read()
words = re.findall('\w+', words)

print(sum([parse_word(word) for word in words]))