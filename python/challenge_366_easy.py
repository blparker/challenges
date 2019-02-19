"""
Challenge
=========
Given two strings of letters, determine whether the second can be made from the first by removing one letter. The remaining letters must stay in the same order.

Examples
========

    funnel("leave", "eave") => true
    funnel("reset", "rest") => true
    funnel("dragoon", "dragon") => true
    funnel("eave", "leave") => false
    funnel("sleet", "lets") => false
    funnel("skiff", "ski") => false

Optional bonus 1
================
Given a string, find all words from the enable1 word list that can be made by removing one letter from the string. If there are two possible letters you can
remove to make the same word, only count it once. Ordering of the output words doesn't matter.

    bonus("dragoon") => ["dragon"]
    bonus("boats") => ["oats", "bats", "bots", "boas", "boat"]
    bonus("affidavit") => []

Optional bonus 2
================
Given an input word from enable1, the largest number of words that can be returned from bonus(word) is 5. One such input is "boats". There are 28 such inputs in
total. Find them all.

Ideally you can do this without comparing every word in the list to every other word in the list. A good time is around a second. Possibly more or less, depending
on your language and platform of choice - Python will be slower and C will be faster. The point is not to hit any specific run time, just to be much faster than
checking every pair of words.
"""

def funnel_rec(f, s, i=0):
    if i == len(f) - 1: return False
    elif f[:i] + f[i+1:] == s: return True
    else: return funnel(f, s, i + 1)

def funnel(f, s):
    return any([ f[:i] + f[i+1:] == s for i in range(len(f)) ])

print(funnel("leave", "eave"))     # => true
print(funnel("reset", "rest"))     # => true
print(funnel("dragoon", "dragon")) # => true
print(funnel("eave", "leave"))     # => false
print(funnel("sleet", "lets"))     # => false
print(funnel("skiff", "ski"))      # => false

