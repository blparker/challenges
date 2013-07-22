"""
The Derpsons are having a party for all their relatives. It will be the greatest party ever held, 
with hired musicians, a great cake and a magical setting with two long tables at an old castle. 
The only problem is that some of the guests can't stand each other, and cannot be placed at the 
same table.

The Derpsons have created a list with pairs of enemies they know will start a fight if put 
together. The list is rather long so it is your mission to write a program to partition the 
guests into two tables.

Input Description
=================
The input is a list of enemies for each guest (with empty lines for guests without enemies). 
Each guest have a number which is equivalent to the line number in the list.

It is a newline-separated file (text file or standard in). Each line is a comma-separated 
(no space) list of positive integers. The first line of the input is called 1, the second 2 
and so on. This input can be mapped to an array, arr, indexed from 1 to n (for n guests) 
with lists of numbers. Each index of the array is a guest, and each number of each list is 
another guest that he or she cannot be placed with.

If a number e appears in the list arr[k], it means that e and k are sworn enemies. The lists 
are symmetric so that k will also appear in the list arr[e].

Output Description
==================
A newline-separated list (on standard out or in a file) of guest numbers to put at the first 
table, followed by an empty line and then the guests to place at the second table. You may just 
return the two lists if printing is non-trivial in your language of choice.

All guests must be placed at one of the two tables in such a way that any two people at the same 
table are not enemies.

The tables do not need to be the same size. The lists do not need to be sorted.

Additionally, if the problem is impossible to solve, just output "No solution".

Example Input
=============
2,4
1,3
2
1

Example Output
==============
1
3

4
2
"""

import sys

def run(guests):
  color = 1
  levels = [[(1, color)]]
  for i, l in enumerate(guests):
    color ^= 1
    level = []
    for j in l:
      if i < j:
        level[len(level):] = [(j, color)]
    if len(level) > 0:
      levels[len(levels):] = [level]

  return partition(levels)
  

def partition(levels):
  tables = [[], []]

  for l in levels:
    for node in l:
      tables[node[1]].append(node[0])

  return tables


def read(input):
  guests = []

  with open(input) as f:
    guests = [ map(int, l.rstrip("\n").split(",")) for l in f.readlines() ]

  return guests

def output(tables):
  print "\n".join([ str(g) for g in tables[0] ])
  print "\n"
  print "\n".join([ str(g) for g in tables[1] ])

def main():
  guests = read(sys.argv[1])
  #guests = [[2, 4], [1, 3], [2], [1]]
  output(run(guests))

main()


