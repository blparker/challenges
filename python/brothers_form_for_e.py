

import math

num = 20
print sum([(float(2 * n + 2) / math.factorial(2 * n + 1)) for n in range(0, num + 1)])
