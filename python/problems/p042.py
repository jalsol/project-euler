import math

with open("/tmp/0042_words.txt", "r") as f:
  def calc(s):
    return sum([ord(c) - ord('A') + 1 for c in s])
  def tri(x):
    n = math.floor(math.sqrt(2*x))
    return 2*x == n*(n+1)

  s = f.read().split(',')
  s = [x.lstrip('"').rstrip('"') for x in s]
  s = [calc(x) for x in s]
  s = sum([1 if tri(x) else 0 for x in s])
  print(s)