#include <cassert>
#include <cstdio>

auto main() -> int {
  int sum = 0;
  for (int n = 1; n < 1000; ++n)
    if (n % 3 == 0 || n % 5 == 0) sum += n;
  assert(sum == 233168);
  std::printf("%d\n", sum);
}
