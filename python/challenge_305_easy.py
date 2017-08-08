"""
There may be an actual name to this base system (let us/me know in comments), and there is a math insight that makes this problem even easier, but it 
is still pretty easy with no math insight.

For "permutation base 2", the indexes and values start with:

index  value
-----  -----
0      0
1      1
2      00
3      01
4      10
5      11
6      000
7      001
8      010
9      011

Sample Challenge
================
  - what is the base-value for index 54?
  - what is the index-value for base 111000111

Solutions
=========
permbase2 54
1 1 0 0 0

permbase2 inv 1 1 1 0 0 0 1 1 1
965

challenge index inputs (some are 64 bit+ inputs)
================================================
234234234
234234234234234
234234234234234234234234

challenge value inputs
======================
000111000111111000111111000111111000111
11111111000111000111111000111111000111111000111

bonus
=====
Extend the function to work with any base. Base 10 index value 10 is 00. index value 109 is 99
"""
import math

p = []
n = 3
def bv(i):
  for x in range(1, n + 1):
    t = pow(2, x)
    q = 1
    for j in range(0, t):
      print bin(q << 1)
    print '---'


#bv(54)
#print p

"""
n = 0
m = 1
while n & m:
  n = n ^ m
  m <<= 1
n = n ^ m
print n
"""
  #n = n << 1
  #print bin(n)


n = int(math.floor(math.log(9, 2)))
l = [0] * n

idx = 0
while sum(l) < n:
  print l
  if l[-1] == 1:
    for i in range(1, len(l)):
      l[i - 1] = l[i]
  else:
    l[-1] = 1

print l

