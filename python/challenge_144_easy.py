"""
You have just been hired at a local home improvement store to help compute the proper costs 
of inventory. The current prices are out of date and wrong; you have to figure out which 
items need to be re-labeled with the correct price.

You will be first given a list of item-names and their current price. You will then be given 
another list of the same item-names but with the correct price. You must then print a list of 
items that have changed, and by how much.

Input Description
=================
The first line of input will be an integer N, which is for the number of rows in each list. 
Each list has N-lines of two space-delimited strings: the first string will be the unique 
item name (without spaces), the second string will be the price (in whole-integer cents). The 
second list, following the same format, will have the same unique item-names, but with the 
correct price. Note that the lists may not be in the same order!

Output Description
==================
For each item that has had its price changed, print a row with the item name and the price 
difference (in cents). Print the sign of the change (e.g. '+' for a growth in price, or '-' 
for a loss in price). Order does not matter for output.

Sample Input 1
==============
4
CarriageBolt 45
Eyebolt 50
Washer 120
Rivet 10
CarriageBolt 45
Eyebolt 45
Washer 140
Rivet 10

Sample Output 1
===============
Eyebolt -5
Washer +20

Sample Input 2
==============
3
2DNail 3
4DNail 5
8DNail 10
8DNail 11
4DNail 5
2DNail 2

Sample Output 2
===============
2DNail -1
8DNail +1
"""

def run(orig, new):
  t = { k: ((new[k] - orig[k]), '+' if new[k] > orig[k] else '-') for k in new }
  print '\n'.join(['%s %s%s' % (k, v[1], abs(v[0])) for (k, v) in t.items() if v[0] != 0])


def pi(i):
  return { i[n].split(' ')[0]: int(i[n].split(' ')[1]) for n in range(0, len(i)) }


if __name__ == '__main__':
  n = input()
  d1 = pi([raw_input() for x in xrange(n)])
  d2 = pi([raw_input() for x in xrange(n)])
  """
  d1 = "CarriageBolt 45\n\
Eyebolt 50\n\
Washer 120\n\
Rivet 10"
  d2 = "CarriageBolt 45\n\
Eyebolt 45\n\
Washer 140\n\
Rivet 10"
  """
  run(d1, d2)

