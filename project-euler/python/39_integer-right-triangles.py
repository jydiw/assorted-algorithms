'''
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

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

q = 1
r = 1
for p in range(12,1000):
  if len(pythagorean_triplet(p)) > r:
    q = p
    r = len(pythagorean_triplet(p))

print(q)

pythagorean_triplet(840)