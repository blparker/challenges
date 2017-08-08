"""
Description

In computational complexity theory, the 3SUM problem asks if a given set of n real numbers contains three elements that sum to zero. A naive
solution works in O(N^2) time, and research efforts have been exploring the lower complexity bound for some time now.

Input Example

You will be given a list of integers, one set per line. Example:
  9 -6 -5 9 8 3 -4 8 1 7 -4 9 -9 1 9 -9 9 4 -6 -8

Output Example

  Your program should emit triplets of numbers that sum to 0. Example:
    -9 1 8
    -8 1 7
    -5 -4 9
    -5 1 4
    -4 1 3
    -4 -4 8

Challenge Input

    4 5 -1 -2 -7 2 -5 -3 -7 -3 1
    -1 -6 -3 -7 5 -8 2 -8 1
    -5 -1 -4 2 9 -9 -6 -1 -7

Challenge Output

    -7 2 5
    -5 1 4
    -3 -2 5
    -3 -1 4
    -3 1 2

    -7 2 5
    -6 1 5
    -3 1 2

    -5 -4 9
    -1 -1 2
"""

import sys

nums = [ 9, -6, -5, 9, 8, 3, -4, 8, 1, 7, -4, 9, -9, 1, 9, -9, 9, 4, -6, -8 ]
#nums = [ 4, 5, -1, -2, -7, 2, -5, -3, -7, -3, 1 ]
nums = sorted(set(nums))
#nums = sorted(nums)

for i in range(0, len(nums)):
  for j in range(i + 1, len(nums)):
    for k in range(j + 1, len(nums)):
      s = nums[i] + nums[j] + nums[k]
      if s == 0:
        print nums[i], nums[j], nums[k], ' = ', s

