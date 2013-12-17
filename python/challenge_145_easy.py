"""
Your goal is to draw a tree given the base-width of the tree (the number of characters on the 
bottom-most row of the triangle section). This "tree" must be drawn through ASCII art-style 
graphics on standard console output. It will consist of a 1x3 trunk on the bottom, and a 
triangle shape on the top. The tree must be centered, with the leaves growing from a base of 
N-characters, up to a top-layer of 1 character. Each layer reduces by 2 character, so the 
bottom might be 7, while shrinks to 5, 3, and 1 on top layers. See example output.

Input Description
=================
You will be given one line of text on standard-console input: an integer and two characters, 
all space-delimited. The integer, N, will range inclusively from 3 to 21 and always be odd. The 
next character will be your trunk character. The next character will be your leaves character. 
Draw the trunk and leaves components with these characters, respectively.

Output Description
==================
Given the three input arguments, draw a centered-tree. It should follow this pattern: (this 
is the smallest tree possible, with a base of 3)
   *
  ***
  ###

Here's a much larger tree, of base 7:

   *
  ***
 *****
*******
  ###

Sample Input 1
==============
3 # *

Sample Output 1
===============
   *
  ***
  ###

Sample Input 2
==============
13 = +

Sample Output 2
===============
      +
     +++
    +++++
   +++++++
  +++++++++
 +++++++++++
+++++++++++++
     ===
"""

def run(N, t, l):
  median = int(round(N / 2.0))
  print '\n'.join([''.join([ l if (i in range(median-1-j, median+j)) else ' ' for i in xrange(len([' '] * N)) ]) for j in xrange(median) ])
  print ''.join([ t if i in range(median-2, median+1) else ' ' for i in xrange(N) ])


if __name__ == '__main__':
  N, t, l = raw_input().split()
  #run(5, '=', '+')
  #run(13, '=', '+')
  run(int(N), t, l)


