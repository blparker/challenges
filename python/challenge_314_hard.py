"""

"""

def read_data():
  with open('challenge_314_hard_in.txt') as f:
    return [ l.rstrip('\n') for l in f.readlines() ]


def parse(data):
  parsed = [[ False if c == ' ' else True for c in l ] for l in data ]
  for idx, l in enumerate(parsed):
    d = 80 - len(l)
    parsed[idx] = l + d * [False]

  return parsed


def run(data):
  #print '\n'.join(data)
  data = [data[0]]
  encoded = [0] * 80
  i = 1
  for idx, r in enumerate(data):
    for jdx, c in enumerate(r):
      #print have_neighbor(data, idx, jdx)
      if c:
        encoded[jdx] = i

  print encoded


def have_neighbor(data, i, j):
  if not data[i][j]: return False

  if data[i - 1][j] or data[i + 1][j] or data[i][j - 1] or data[i][j + 1]:
    return True
  else:
    return False

data = parse(read_data())
run(data)

