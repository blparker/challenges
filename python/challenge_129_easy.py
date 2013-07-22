"""
This programming challenge is a classic interview question for software engineers: given 
a string, find the longest sub-string that contains, at most, two characters.

Input Description
=================
Through standard console input, you will be given a string to search, which only 
contains lower-case alphabet letters.

Output Description
==================
Simply print the longest sub-string of the given string that contains, at most, two 
characters. If you find multiple sub-strings that match the description, print the 
last sub-string (furthest to the right).

Sample Inputs
=============
abbccc
abcabcabcabccc
qwertyytrewq

Sample Outputs
==============
bbccc
bccc
tyyt
"""

def ss(input):
  substr = ''
  for i in range(0, len(input)):
    ch = input[i]
    for j in range(i, len(input)):
      ch2 = input[j]
      if ch2 != ch and input[j - 1] != ch2:
        print ch2
        break


ss('abbccc')

