
import sys

def run(input):
  print input

def parse(input):
  input = [ j for j in (i.split(' ') for i in input.split('\n')) ]
  return input


run(parse('A 3 4\nB 4 5\nC 1 2\nD 2 3'))

