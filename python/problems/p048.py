# python abuse

base = 10**10
ans = 0
for i in range(1, 1001):
  ans += pow(i, i, base)
print(ans % base)