n = 600851475143

d = 3
ans = 1

while d * d <= n:
  if n % d == 0:
    while n % d == 0:
      n //= d
    ans = d
  d += 2

if n > 2:
  ans = n

print(ans)