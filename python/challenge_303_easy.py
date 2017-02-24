"""
Start with a grid h units high by w units wide. Set a point particle in motion from the upper-left corner of the grid, 45 degrees from the horizontal, 
so that it crosses from one corner of each unit square to the other. When the particle reaches the bounds of the grid, it ricochets and continues until 
it reaches another corner.

Given the size of the grid (h and w), and the velocity (v) of the particle in unit squares per second, determine C: the corner where the particle will 
stop, b: how many times the particle ricocheted off the bounds of the grid, and t: the time it took for the particle to reach C.

Constraints
===========
The particle always starts from the upper-left corner of the grid (and will therefore always end up in one of the other corners).

Since we'll be working with unit squares, h and w are always integers.

Input Description
=================
The input will be an arbitrary number of lines containing h, w, and v, each separated by spaces:
  8 3 1
  15 4 2

Output Description
==================
For each line of input, your program should output a line containing C, b, and t, where C can be UR, LR, or LL depending on where the particle ends up:
  LL 9 24
  UR 17 30

Bonus
=====
Instead of a particle, determine the behavior of a rectangle m units high by n units wide. Input should be as follows: h w m n v. So for a 10 by 7 grid with a 3 by 2 rectangle, the input would be:
  10 7 3 2 1

The output format is the same:
  LR 10 35

"""

h, w, v = 8, 3, 1
#h, w, v = 15, 4, 2

def run(w, h, v):
  i, j, b, t = 0, 0, 0, 0
  ti, tj = 1, 1

  while True:
    i += ti
    j += tj

    t += 1

    if i == 0 and j == 0:   return ('UL', b, t / v)
    elif i == 0 and j == w: return ('UR', b, t / v)
    elif i == h and j == 0: return ('LL', b, t / v)
    elif i == h and j == w: return ('LR', b, t / v)

    if j == 0 or j == w:
      tj *= -1
      b += 1
    if i == 0 or i == h:
      ti *= -1
      b += 1

print run(w, h, v)

