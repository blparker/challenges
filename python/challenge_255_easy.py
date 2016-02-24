"""
When you were a little kid, was indiscriminately flicking light switches super fun? I know it was for me. Let's tap into that and try to recall that 
feeling with today's challenge.

Imagine a row of N light switches, each attached to a light bulb. All the bulbs are off to start with. You are going to release your inner child 
so they can run back and forth along this row of light switches, flipping bunches of switches from on to off or vice versa. The challenge will be to figure 
out the state of the lights after this fun happens.

Input Description
=================
The input will have two parts. First, the number of switches/bulbs (N) is specified. On the remaining lines, there will be pairs of integers indicating ranges 
of switches that your inner child toggles as they run back and forth. These ranges are inclusive (both their end points, along with everything between them is 
included), and the positions of switches are zero-indexed (so the possible positions range from 0 to N-1).

Example input
=============
  10
  3 6
  0 4
  7 3
  9 9

There is a more thorough explanation of what happens below.

Output description
==================

The output is a single number: the number of switches that are on after all the running around.

Example output
==============
  7

"""
import sys

def run(N, ranges):
  s = [False] * N
  for r in ranges:
    r = make_range(r)
    s[r[0]:r[len(r) - 1]] = [ not s[i] for i in r ]

  return s.count(True)


def get_input(fname):
  with open(fname) as f:
    N = int(f.readline().rstrip('\n'))
    ranges = [ map(int, l.rstrip('\n').split(' ')) for l in f.readlines() ]
    return (N, ranges)


def make_range(r):
  r[0], r[1] = min(r), max(r)
  return range(r[0], r[1] + 1)


i = get_input(sys.argv[1])
print run(i[0], i[1])


