"""
Description
===========
A number is input in computer then a new no should get printed by adding one to each of its digit. If you encounter a 9, insert a 10
(don't carry over, just shift things around).

For example, 998 becomes 10109.

Bonus
=====
This challenge is trivial to do if you map it to a string to iterate over the input, operate, and then cast it back. Instead, try doing it
without casting it as a string at any point, keep it numeric (int, float if you need it) only.
"""
import math

def run(n):
    return ''.join(map(str, [d + 1 for d in map(int, str(n))]))

def run_bonus(n):
    nd = math.ceil(math.log10(n))
    new_num, off = 0, 0
    for i in range(0, nd):
        dig = (n // (10 ** (i))) % 10
        new_num += (dig + 1) * (10 ** (i + off))

        if dig == 9: off += 1
    return new_num

def test(n, expected):
    res = run_bonus(n)
    print('%d -> %d = %d == %d? %s' % (n, res, res, expected, res == expected))

#print(run(998))
test(998, 10109)
test(9898, 109109)
test(444, 555)
test(944, 1055)

