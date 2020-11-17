def multiples(f):
  ms = []
  for m in range(f, 1000, f):
    if unique_digits(f"{m:03d}"):
      ms.append(f"{m:03d}")
  return ms

def unique_digits(n):
  return len(list(set(n))) == len(n)

def leftover(n):
  digits = set('0123456789')
  for d in n:
    digits.remove(d)
  return str(list(digits)[0])

def substringdiv():
  divs = [17, 13, 11, 7, 5, 3, 2]
  ms = multiples(divs[0])
  for i in range(1, len(divs)):
    nms = []
    for a in ms:
      for b in multiples(divs[i]):
        if b[1:3] == a[:2]:
          nms.append(b[0] + a)
    ms = nms
  ms = [leftover(m)+m for m in ms if unique_digits(m)]
  return sum([int(m) for m in ms])

%timeit substringdiv()

# ref = set([m[:2] for m in multiples(17)])
# ms = []
# for a in multiples(13):
#   if a[1:] in ref:
#     ms.append(a)
# print(ms)