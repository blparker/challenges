"""
Write a program that given two strings, finds out if the second string is contained in the first, and if it is, 
where it is.

I.e. given the strings "Double, double, toil and trouble" and "il an" will return 18, because the second 
substring is embedded in the first, starting on position 18.

NOTE: Pretty much every language have this functionality built in for their strings, sometimes called find() 
(as in Python) or indexOf() (as in Java). But the point of this problem is to write the program yourself, 
so you are not allowed to use functions like this!
"""

import sys

def run():
	str = sys.argv[1]
	find = sys.argv[2]
	fndPtr = 0

	for i in range(0, len(str)):
		if str[i] == find[fndPtr]:
			print 'Found starting at:', i
			fndPtr += 1
		else:
			fndPtr = -1
	
	if fndPtr > 0:
		print "FOUND"
	else:
		print "NOT FOUND"


if __name__ == '__main__':
	run()

