total = 1
num = 1
step = 2

for _ in range((1001 - 1) // 2):
  for _ in range(4):
    num += step
    total += num
  step += 2

print(total)
