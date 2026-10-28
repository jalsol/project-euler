lim = 150000

sieve = [True] * lim

i = 3
while i * i < lim:
  if sieve[i]:
    j = i * i
    while j < lim:
      sieve[j] = False
      j += i
  i += 2

cnt = 1
i = 3
while i < lim:
  if sieve[i]:
    cnt += 1
  if cnt == 10_001:
    print(i)
    break
  i += 2