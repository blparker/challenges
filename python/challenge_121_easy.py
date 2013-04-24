"""
Bytelandian Currency is made of coins with integers on them. There is a coin for each 
non-negative integer (including 0). You have access to a peculiar money changing 
machine. If you insert a N-valued coin, with N positive, It pays back 3 coins of the 
value N/2,N/3 and N/4, rounded down. For example, if you insert a 19-valued coin, you 
get three coins worth 9, 6, and 4. If you insert a 2-valued coin, you get three coins 
worth 1, 0, and 0. 0-valued coins cannot be used in this machine.

One day you're bored so you insert a 7-valued coin. You get three coins back, and you 
then insert each of these back into the machine. You continue to do this with every 
positive-valued coin you get back, until finally you're left with nothing but 0-valued 
coins. You count them up and see you have 15 coins.

How many 0-valued coins could you get starting with a single 1000-valued coin?

Input Description
=================
The value of N of the coin you start with

Output Description
==================
The number of 0-valued coins you wind up with after putting every positive-valued coin 
you have through the machine.

Example
=======
Input: 7
Output: 15
"""

import sys

def run(coin):
  return 1 if coin == 0 else (run(coin / 2) + run(coin / 3) + run(coin / 4))


print run(int(sys.argv[1]))


