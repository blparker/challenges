"""
Input Description
=================
The input will be a number on each line, called n.

Output Description
==================
The format of the output will be:

  p1 < n < p2

Where p1 is the smaller prime, p2 is the larger prime and n is the input. If n already is a prime, the output will be:
  n is prime.

Challenge Input
===============
  270
  541
  993
  649

Challenge Output
================

  269 < 270 < 271
  541 is prime.
  991 < 993 < 997
  647 < 649 < 653

Bonus
=====
Write the program to work for numbers with big gaps to the nearest primes. This requires a clever solution and cannot be efficiently bruteforced.

  2010741
  1425172824437700148

"""
import math

def primes(up_to):
  p = [True] * (up_to + 1)
  for i in range(2, int(math.sqrt(up_to)) + 1):
    if p[i]:
      j = i**2
      idx = 1
      while j < (up_to + 1):
        p[j] = False
        j = i**2 + (idx * i)
        idx += 1
  return p


def main():
  ns = [270, 541, 993, 649]
  for n in ns:
    p = primes(n)
    if p[n]:
      print '{} is prime'.format(n)
    else:
      # Iterate until we find one below
      u, l = 0, 0
      i = 1
      while True:
        nn = (n - i)
        p = primes(nn)
        if p[nn]:
          l = nn
          break
        i += 1
      # Iterate until we find one above
      i = 1
      while True:
        nn = n + i
        p = primes(nn)
        if p[nn]:
          u = nn
          break
        i += 1
      print '{} < {} < {}'.format(l, n, u)

main()

