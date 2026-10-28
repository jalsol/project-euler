# 1e7 numbers, a few seconds on python

fact = [1] * 10
for i in range(2, 10):
  fact[i] = fact[i - 1] * i

def calc(num):
  sum = 0
  while num > 0:
    sum += fact[num % 10]
    num //= 10
  return sum

ans = 0
for num in range(3, 10**7):
  if num == calc(num):
    ans += num

print(ans)