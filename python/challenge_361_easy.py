"""
Description
===========
5 Friends (let's call them a, b, c, d and e) are playing a game and need to keep track of the scores. Each time someone scores a point,
the letter of his name is typed in lowercase. If someone loses a point, the letter of his name is typed in uppercase. Give the resulting
score from highest to lowest.

Input Description
=================
A series of characters indicating who scored a point. Examples:

    abcde
    dbbaCEDbdAacCEAadcB

Output Description
==================
The score of every player, sorted from highest to lowest. Examples:

    a:1, b:1, c:1, d:1, e:1
    b:2, d:2, a:1, c:0, e:-2

Challenge Input
===============
    EbAAdbBEaBaaBBdAccbeebaec
"""
from collections import defaultdict

def sort(s):
    return sorted(s.iteritems(), key=lambda (k, v): v, reverse=True)

def format(s):
    return ', '.join('%s:%d' % (t[0], t[1]) for t in s)

def run(i):
    s = defaultdict(int)
    for c in i:
        s[c.lower()] += 1 if c.islower() else -1
    return format(sort(s))

print(run('abcde'))
print(run('dbbaCEDbdAacCEAadcB'))
print(run('EbAAdbBEaBaaBBdAccbeebaec'))

