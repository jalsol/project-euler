lim = 2_000_000

sieve = [True] * lim

i = 3
while i * i < lim:
  if sieve[i]:
    j = i * i
    while j < lim:
      sieve[j] = False
      j += i
  i += 2

ans = 2
i = 3
while i < lim:
  if sieve[i]:
    ans += i
  i += 2

print(ans)