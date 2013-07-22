"""
Imagine you are an engineer working on some legacy code that has some odd constraints: you're 
being asked to implement a new function, which basically merges and sorts one list of integers 
into another list of integers, where you cannot allocate any other structures apart from 
simple temporary variables (such as an index or counter variable).

You will be given two lists, list A and B, where the elements are positive integers from 1 to 
2147483647; the integer '0' is reserved as "buffer space". List A will not be pre-sorted, 
though list B will be pre-sorted and will start with a series of '0' values. These '0' 
values are simply reserved space in list B which is the same number of elements that list A 
has. You cannot modify list A in any way, though list B is fair game. Your goal is to return 
a merged and sorted list of elements of list A into list B, where you cannot allocate any 
extra space other than simple / trivial local variables for your function.

Input Description
=================
You will be given two lists, list A and B, of integers from 1 to 2147483647. List A will be 
unsorted, while list B will be sorted. List B has extra elements in the start of the list 
that are all '0' value: this is buffered space for you to work with when merging and sorting 
list A into B. These two lists will be space-delimited and on separate lines.

Output Description
==================
Simply print the contents of list B, after it has had the contents of A merged & sorted within 
it.

Example Input
=============
692 1 32
0 0 0 14 15 123 2431

Example Output
==============
1 14 15 32 123 692 2431

Note
====
Please note that the real challenge here is respecting the premise of the challenge: you must 
implement your sort / merge function inline into list B! If you do not understand the premise, 
please do ask questions and we will gladly answer. Good luck, and have fun!
"""
import random
import sys

def generate(size):
  #MAX_INT = 2147483647
  MAX_INT = 100
  return [ random.randint(1, MAX_INT) for x in range(0, size) ]


def swap(arr, f, t):
  temp = arr[f]
  arr[f] = arr[t]
  arr[t] = temp


def partition(arr, left, right, pi):
  pv = arr[pi]
  swap(arr, pi, right)
  si = left

  for i in range(left, right):
    if arr[i] <= pv:
      swap(arr, i, si)
      si = si + 1
  
  swap(arr, si, right)
  return si


def quicksort(arr, left, right):
  if left < right:
    pi = left + (right - left) / 2
    pni = partition(arr, left, right, pi)
    quicksort(arr, left, pni - 1)
    quicksort(arr, pni + 1, right)


def main():
  A = generate(10)
  #B = ([0] * len(A)) + generate(10)
  B = A + generate(10)
  quicksort(B, 0, len(B) - 1)
  print B


main()

