
"""
Since many did not like the previous challenge because it was quite unsatisfactory here is a new challenge ...
Given a sequence of integers, both positive and negative, find the contiguous subsequence with the maximum sum.
For instance, given the sequence 31, -41, 59, 26, -53, 58, 97, -93, -23, 84, the maximum sum subsequence is 59, 26, -53, 58, 97, which sums to 187.
"""

import sys

def run(input):
	nums = [int(x) for x in input.split(',')]

	largest = 0
	
	for i in range(0, len(nums)):
		for j in range(i + 2, len(nums)):
			sum = 0
			for x in range(i, j):
				sum += nums[x]

			if sum > largest:
				largest = sum

	print 'Largest = ', largest

if __name__ == '__main__':
	run(sys.argv[1])

