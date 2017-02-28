"""
Description
===========
You will be given a sequence that of letters and you must match with a dictionary. The sequence is a pattern of equal letters that you must find.

E.G.
Pattern:
XXYY means that you have a word that contains a sequence of 2 of the same letters followed by again 2 of the same letts

succeed <- matches
succes <- no match

XYYX means we have a word with at least for letters where you have a sequence of a letter, followed by 2 letters that are the same and then again 
the first letter

narrate <- matches
hodor <- no match

Input description
=================

Input 1
=======
XXYY

Input 2
=======
XXYYZZ

Input 3
=======
XXYYX

Output description
==================

The words that match in the dictionary

Output 1
========
aarrgh
aarrghh
addressee
addressees
allee
allees
allottee
allottees
appellee
appellees
arrowwood
arrowwoods
balloon
ballooned
ballooning
balloonings
balloonist
balloonists
balloons
barroom
barrooms
bassoon
bassoonist
bassoonists
bassoons
belleek
belleeks
...

Output 2
========
bookkeeper
bookkeepers
bookkeeping
bookkeepings

Output 3
========
addressees
betweenness
betweennesses
colessees
fricassees
greenness
greennesses
heelless
keelless
keenness
keennesses
lessees
wheelless

Output can vary if you use a different dictionary

"""

i1 = 'XXYY'
i2 = 'XXYYZZ'
i3 = 'XXYYX'

seen = {}
i = 1
p = []
for c in i3:
  if c not in seen:
    seen[c] = i
    i += 1

  p.append(seen[c])

print p

