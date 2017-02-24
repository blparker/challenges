"""
Description
===========
Scrabble is a popular word game where players remove tiles with letters on them from a bag and use them to create words on a board. The total number of tiles as well 
as the frequency of each letter does not change between games. For this challenge we will be using the tile set from the English edition, which has 100 tiles 
total. Here's a reference for the distribution and point value of each tile.

Each tile will be represented by the letter that appears on it, with the exception that blank tiles are represented by underscores _.

Input Description
=================
The tiles already in play are inputted as an uppercase string. For example, if 14 tiles have been removed from the bag and are in play, 
you would be given an input like this:

  AEERTYOXMCNB_S

Output Description
==================
You should output the tiles that are left in the bag. The list should be in descending order of the quantity of each tile left in the bag, skipping over amounts that have no tiles.
In cases where more than one letter has the same quantity remaining, output those letters in alphabetical order, with blank tiles at the end.

  10: E
  9: I
  8: A
  7: O
  5: N, R, T
  4: D, L, U
  3: G, S
  2: F, H, P, V, W
  1: B, C, J, K, M, Q, Y, Z, _
  0: X

If more tiles have been removed from the bag than possible, such as 3 Qs, you should give a helpful error message instead of printing the list.
Invalid input. More Q's have been taken from the bag than possible.

Challenge Inputs
================

  PQAREIOURSTHGWIOAE_
  LQTOONOEFFJZT
  AXHDRUIOR_XHJZUQEE

Challenge Outputs
=================

1.
  10: E
  7: A, I
  6: N, O
  5: T
  4: D, L, R
  3: S, U
  2: B, C, F, G, M, V, Y
  1: H, J, K, P, W, X, Z, _
  0: Q

2.
  11: E
  9: A, I
  6: R
  5: N, O
  4: D, S, T, U
  3: G, L
  2: B, C, H, M, P, V, W, Y, _
  1: K, X
  0: F, J, Q, Z

3.
  Invalid input. More X's have been taken from the bag than possible.

Bonus
=====
After the normal output, output the distribution of tiles in play and the total point score of both sets of tiles.
"""

"""
counts = [
  ('A', 9), ('B', 2), ('C', 2), ('D', 4), ('E', 12), ('F', 2), ('G', 3), ('H', 2), ('I', 9),
  ('J', 1), ('K', 1), ('L', 4), ('M', 2), ('N', 6), ('O', 8), ('P', 2), ('Q', 1), ('R', 6),
  ('S', 4), ('T', 6), ('U', 4), ('V', 2), ('W', 2), ('X', 1), ('Y', 2), ('Z', 1), ('_', 2)
]
"""
counts = {
  'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9,
  'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6,
  'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1, '_': 2
}

from collections import defaultdict
import sys

def run(in_play):
  c = { c: in_play.count(c) for c in set(in_play) }
  l = [ ((v - c[k] if k in c else v), k) for k, v in counts.iteritems() ]
  d = defaultdict(list)
  for k, v in l:
    if k < 0: raise ValueError('Invalid input. More '+ v +'\'s have been taken from the bag than possible.')
    d[k].append(v)

  print '\n'.join([ str(i[0]) + ': ' + ', '.join(sorted(i[1])) for i in sorted(d.items(), reverse=True) ])


#t = 'AEERTYOXMCNB_S'
#t = 'PQAREIOURSTHGWIOAE_'
t = 'LQTOONOEFFJZT'
#t = 'AXHDRUIOR_XHJZUQEE'

run(sys.argv[1])


