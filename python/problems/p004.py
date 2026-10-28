# 3 digits
# 890 * 890 very quick

def palin(num):
  s = str(num)
  return s == s[::-1]

ans = 0
for a in range(100, 1000):
  for b in range(100, 1000):
    prod = a * b
    if palin(prod) and ans < prod:
      ans = prod

print(ans)