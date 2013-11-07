"""
Given a wordlist of your choosing, make a program to unscramble scrambled words from that list. For sanity and brevity, 
disregard any words which have ambiguous unscramlings, such as "dgo" unscrambling to both "dog" and "god."

Input
=====
A file which contains scrambled words and a wordlist to match it against

Output
======
The unscrambled words which match the scrambled ones
"""
import sys

def ld(s1, s2):
  if len(s1) == 0: return len(s1)
  if len(s2) == 0: return len(s2)

  d = 0
  if s1[len(s1) - 1] == s2[len(s2) - 1]: d = 0
  else: d = 1

  return min(ld(s1[0:len(s1) - 1], s2) + 1, ld(s1, s2[0:len(s2) - 1]) + 1, ld(s1[0:len(s1) - 1], s2[0:len(s2) - 1]) + d)

def run(s, w):
  input = open(s).read().splitlines()
  words = open(w).read().splitlines()

  best = []
  for i in range(0, len(input)):
    best.append(len(input[i]))
    for j in range(0, len(words)):
      d = ld(input[i], words[j])
      if d < best[-1]: best[-1] = j

  print '\n'.join([ (input[b] + ' -> ' + words[best[b]]) for b in range(0, len(best)) ])



run(sys.argv[1], sys.argv[2])

