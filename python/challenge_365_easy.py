"""
Description
===========
We were all taught addition, multiplication, and exponentiation in our early years of math. You can view addition as repeated
succession. Similarly, you can view multiplication as repeated addition. And finally, you can view exponentiation as repeated
multiplication. But why stop there? Knuth's up-arrow notation takes this idea a step further. The notation is used to represent
repeated operations.

In this notation a single ↑ operator corresponds to iterated multiplication. For example:

    2 ↑ 4 = ?
    = 2 * (2 * (2 * 2)) 
    = 2^4
    = 16

While two ↑ operators correspond to iterated exponentiation. For example:

    2 ↑↑ 4 = ?
    = 2 ↑ (2 ↑ (2 ↑ 2))
    = 2^2^2^2
    = 65536

Using recursion, the following is decomposed into:

    2 ↑↑ 4 = ?
    = 2 ↑ (2 ↑↑ 3)
    = 2 ↑ (2 ↑ (2 ↑ 2))
    = 2 ↑ (2 ↑ (2 ^ 2))
    = 2 ↑ (2 ^ 4)
    = 2 ^ 16

Consider how you would evaluate three ↑ operators. For example:

    2 ↑↑↑ 3 = ?
    = 2 ↑↑ (2 ↑↑ 2)
    = 2 ↑↑ (2 ↑ 2)
    = 2 ↑↑ (2 ^ 2)
    = 2 ↑↑ 4
    = 2 ↑ (2 ↑ (2 ↑ 2))
    = 2 ^ 2 ^ 2 ^ 2
    = 65536

In today's challenge, we are given an expression in Kuth's up-arrow notation to evalute.

    5 ↑↑↑↑ 5
    7 ↑↑↑↑↑ 3
    -1 ↑↑↑ 3
    1 ↑ 0
    1 ↑↑ 0
    12 ↑↑↑↑↑↑↑↑↑↑↑ 25
"""
import re

def calc(l, r, n):
    if n == 1:
        return l ** r
    elif n >= 1 and r == 0:
        return 1
    else:
        return calc(l, calc(l, r - 1, n), n - 1)

def parse(input):
    m = re.search('^(\d+) (↑+) (\d+)$', input)
    l, r, n = int(m.group(1)), int(m.group(3)), len(m.group(2))
    return l, r, n

print(calc(*parse('2 ↑ 4')))


