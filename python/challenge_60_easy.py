"""
A number is polite if it can be written as the sum of two or more consecutive numbers; for instance, 7 is polite 
because it can be written at 3 + 4. Some numbers can be written as the sum of two or more consecutive numbers 
in more than one way; for instance, 15 = 1 + 2 + 3 + 4 + 5 = 4 + 5 + 6 = 7 + 8. The number of ways that a number 
can be written as the sum of two or more consecutive numbers is its politeness. Any number that is a power of 2 
cannot be written as the sum of two or more consecutive numbers; such a number has a politeness of 0, and is 
thus impolite.

Here is an article helping in understanding Polite numbers

Your task is to write a program that calculates all the ways that a number can be written as the sum of two 
or more consecutive numbers.
"""
import sys

def polite(num):
	polites = []

	for i in range(1, num):
		sum = 0
		currentRange = []
		for j in range(i, num):
			sum += j
			currentRange.append(j)
			if sum == num:
				polites.append(currentRange)
				break
	
	print polites


polite(int(sys.argv[1]))

