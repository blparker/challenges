"""
As a crude form of hashing function, Lars wants to sum the digits of a number. Then 
he wants to sum the digits of the result, and repeat until he have only one digit left. 
He learnt that this is called the digital root of a number, but the Wikipedia article 
is just confusing him.

Can you help him implement this problem in your favourite programming language?

It is possible to treat the number as a string and work with each character at a time. 
This is pretty slow on big numbers, though, so Lars wants you to at least try solving 
it with only integer calculations (the modulo operator may prove to be useful!).

Example
=======
Input: 31337
Output: 8, because 3+1+3+3+7=17 and 1+7=8

Challenge Input: 1073741824

"""

import sys

def main(input):
  total = 0
  print doWork(input)

def doWork(input):
  total = reduce(lambda x, y: x+y, [int(input[i]) for i in range(0, len(input))])
  return doWork(str(total)) if(total >= 10) else total


main(sys.argv[1])

