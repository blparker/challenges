"""
A Polygon is a geometric two-dimensional figure that has n-sides (line segments) that closes to 
form a loop. Polygons can be in many different shapes and have many different neat properties, 
though this challenge is about Regular Polygons (have equal angles). Our goal is to compute the 
permitter of an n-sided polygon that has equal-length sides given the circumradius. This is the 
distance between the center of the Polygon to any of its vertices; not to be confused with the 
apothem!

Input Description
=================
Input will consist of one line on standard console input. This line will contain first an integer N, 
then a floating-point number R. They will be space-delimited. The integer N is for the number of 
sides of the Polygon, which is between 3 to 100, inclusive. R will be the circumradius, which 
ranges from 0.01 to 100.0, inclusive.

Output Description
==================
Print the permitter of the given N-sided polygon that has a circumradius of R. Print up to three 
digits precision.

Sample Input 1
==============
5 3.7

Sample Output 1
===============
21.748

Sample Input 2
==============
100 1.0

Sample Output 2
===============
6.282
"""

import math
import sys
from math import sin, pi
from sys import argv

#def run(N, r):
  #print '%.3f' % ((r * (2 * math.sin(math.pi / N))) * N)


#if __name__ == '__main__':
  #run(int(sys.argv[1]), float(sys.argv[2]))

print '%.3f' % ((float(argv[2]) * (2 * sin(pi / int(argv[1])))) * int(argv[1]))


