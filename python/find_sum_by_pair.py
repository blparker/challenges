
l = [1, 2, 3, 9]
#l = [1, 2, 4, 4]
s = 8

def naive(l, s):
  for i in range(0, len(l)):
    for j in range(i + 1, len(l)):
      if l[i] + l[j] == s:
        return (l[i], l[j])

  return None


def linear(l, s):
  left, right = 0, len(l) - 1
  while left < right:
    t = l[left] + l[right]
    if t > s:
      right -= 1
    elif t < s:
      left += 1
    else:
      return (l[left], l[right])

  return None


print linear(l, s)

