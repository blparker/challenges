"""
Computing the volume of a circle is pretty straight-forward: Pi x Radius x Radius, or 
simply Pi x r 2.

What if we wanted to computer the volume of two circles? Easy, just sum it! Yet, what about 
two intersecting circles, much like the classic Venn diagram?

Your goal is to write a program that takes two unit-circles (radius of one) at given locations, 
and compute that shape's volume. You must make sure to not double-count the intersecting 
volume! (i.e. you must not sum this red area twice).

As a starting point, check out how to compute circle segments.

Input Description
=================
On standard input you will be given four floating-point space-delimited values: x y u w. x 
and y are the first circle's position in Cartesian coordinates. The second pair u and w are 
the second circle's position.

Note that the given circles may not actually intersect. If this is the case, return the sum of 
both circles (which will always be Pi x 2 since our circles are unit-circles).

Output Description
==================
Print the summed volume of the two circles, up to an accuracy of 4 digits after the decimal place.

Sample Input
============
-0.5 0 0.5 0

Sample Output
=============
5.0548
"""
"""
theta = 2 * math.acos(0.5)
asec = (theta / 2)
trih = (math.sqrt(1 - (dist / 2) ** 2)) * 2
atri = 0.5 * (dist / 2) * trih
aseg = asec - atri
aov = aseg * 2
area_of_overlapping = (2 * math.pi) - aov
print area_of_overlapping
"""
from math import acos, sqrt, pi

distance = lambda c1, c2: (sqrt((c2[1] - c1[1]) ** 2 + (c2[0] - c1[0]) ** 2))

def run(c1, c2):
  dist = distance(c1, c2)
  if dist < 2:
    print (2 * pi) - (2 * ((2 * acos(0.5) / 2) - ((0.5 * (dist / 2)) * ((sqrt(1 - (dist / 2) ** 2)) * 2))))
  else:
    print 2 * math.pi



if __name__ == '__main__':
  run([-0.5, 0], [0.5, 0])

