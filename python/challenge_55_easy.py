"""
Write a program to solve the sliding window minimum problem using any of the methods possible. This could be a helpful link.


So basically you have an array/vector and a window size. Imagine you are looking through a window at your array and can only see windowSize elements of the array.

For example, if you had the array {4,3,2,1,5,7} and a windowSize of 3, you could only see {4,3,2} and then it slides along by one and you have: {3,2,1}. it then 
does this until you reach the end of the array. In this case the views would be: {4,3,2}, {3,2,1}, {2,1,5}, and {1,5,7}

For each of these 'views' through the window, find the lowest value, and add it to a new array 'r'. (For example, in {4,3,2}, 2 is the lowest). 'r' for the array 
giving above, would be {2,1,1,1}.

"""

import sys

def run():
	k = int(sys.argv[2])								# K, The window size
	vector = [int(x) for x in sys.argv[1].split(',')]	# V, Our vector of numbers
	r = []

	for i in range((len(vector) + 1) - k):	# i is the new starting point for the minimum
		current_r = None

		for j in range(i, (i + k)):
			if current_r == None:
				current_r = vector[j]
			elif vector[j] < current_r:
				current_r = vector[j]

		r.append(current_r)
	
	print r


if __name__ == '__main__':
	run()

