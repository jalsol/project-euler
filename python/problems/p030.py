ans = 0

for a in range(10):
  for b in range(10):
    for c in range(10):
      for d in range(10):
        for e in range(10):
          for f in range(10):
            ds = [a, b, c, d, e, f]
            n = 10**5 * a + 10**4 * b + 10**3 * c + 10**2 * d + 10 * e + f

            if sum([1 if x != 0 else 0 for x in ds]) == 1:
              print("skipping", n)
              continue

            if sum([x**5 for x in ds]) == n:
              ans += n

print(ans)