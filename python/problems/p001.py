#!/usr/bin/env python3


def is_multiple(n: int) -> bool:
    return n % 3 == 0 or n % 5 == 0


answer = sum(n for n in range(1, 1000) if is_multiple(n))
assert answer == 233168
print(answer)
