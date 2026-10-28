# 1 million very quick

def eq_rev(s):
  return s == s[::-1]

def check(num):
  return eq_rev(str(num)) and eq_rev(bin(num)[2:])

print(sum([num * check(num) for num in range(1, 1_000_000)]))