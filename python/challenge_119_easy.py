import sys
import math

def run(num):
  change = []
  num = num * 100

  q = int(math.floor(num / 25))
  change.append(q)
  num -= (q * 25)

  d = int(math.floor(num / 10))
  change.append(d)
  num -= (d * 10)

  n = int(math.floor(num / 5))
  change.append(n)
  num -= (d * 5)

  change.append(int(num))

  print change

def run2(num):
  num *= 100
  values = [ 25, 10, 5, 1 ]
  change = []
  ret = [(int(math.floor(num / values[v])); num -= int(math.floor(num / values[v])) * values[v]) for v in range(0, len(values))]
  print ret


run2(float(sys.argv[1]))
