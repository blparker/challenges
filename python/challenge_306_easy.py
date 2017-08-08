
l = [0, 1, 2, 3]

#for i in range(0, len(l)):
"""
i = 0
c = l[:]
f = i
print c
for j in range(i + 1, len(l) - 1):
  c[j], c[j + 1] = c[j + 1], c[j]
  print c
"""
c = [0] * len(l)
print l

for i in range(0, len(l)):
  if c[i] < i:
    if i % 2 == 0:
      l[0], l[i] = l[i], l[0]
    else:
      l[c[i]], l[i] = l[i], l[c[i]]
    print l
    c[i] += 1
    i = 0
  else:
    c[i] = 0
    i += 1


