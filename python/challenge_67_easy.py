"""
As we all know, when computers do calculations or store numbers, they don't use decimal notation like we do, they 
use binary notation. So for instance, when a computer stores the number 13, it doesn't store "1" and "3", it 
stores "1101", which is 13 in binary.

But more than that, when we instruct it to store an integer, we usually tell it to store it in a certain 
datatype with a certain length. For (relatively small) integers, that length is usually as 32 bits, or four 
bytes (also called "one word" on 32-bit processors). So 13 isn't really stored as "1101", it's stored as 
"00000000000000000000000000001101".

If we were to reverse that bit pattern, we would get "10110000000000000000000000000000", which written in decimal 
becomes "2952790016".

Write a program that can do this "32-bit reverse" operation, so when given the number 13, it will return 2952790016.

Note: just to be clear, for all numbers in this problem, we are using unsigned 32 bit integers.
"""

import sys
import math

def run(num):
	numBits = int(math.floor(math.log(num, 2)) + 1)
	print bin(num)
	rev = ((num << 8) | (num >> 8)) & 0xFFFF
	print bin(rev)
	#num = num << 32 - numBits
	#print bin(num)


run(int(sys.argv[1]))

