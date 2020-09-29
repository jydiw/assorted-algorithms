'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

from functools import reduce
import re

names = open('../files/p022_names.txt', 'r')
names = names.read()
names = re.findall('\w+', names)
names = sorted(names)

def name_scorer(name):
  l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  s = range(1,27)
  score = dict(zip(letters, scores))
  return reduce(lambda a, b: a+b, [score[c] for c in name])

def names_scores(names):
  return reduce(
    lambda a, b: a+b,
    [(i+1)*name_scorer(name) for i, name in enumerate(names)]
  )

names_scores(names)