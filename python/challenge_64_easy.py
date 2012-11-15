"""
The divisors of a number are those numbers that divide it evenly; for example, the divisors of 60 
are 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, and 60. The sum of the divisors of 60 is 168, and the number of 
divisors of 60 is 12.

The totatives of a number are those numbers less than the given number and coprime to it; two numbers 
are coprime if they have no common factors other than 1. The number of totatives of a given number is 
called its totient. For example, the totatives of 30 are 1, 7, 11, 13, 17, 19, 23, and 29, and the 
totient of 30 is 8.

Your task is to write a small library of five functions that compute the divisors of a number, the sum and 
number of its divisors, the totatives of a number, and its totient.
"""

import sys
import math

def run(num):
	print divisors(num)
	print num_divisors(num)
	print sum_divisors(num)
	print totatives(num)
	print totient(num)


def divisors(num):
	return [x for x in range(1, (num + 1)) if num % x == 0]

def sum_divisors(num):
	return sum(divisors(num))

def num_divisors(num):
	return len(divisors(num))

def totatives(num):
	return [x for x in range(1, num) if _gcd(x, num) == 1]

def totient(num):
	return len(totatives(num))

def _gcd(a, b):
	return a if b == 0 else _gcd(b, a % b)


run(int(sys.argv[1]))

