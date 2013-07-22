import sys

def M(n):
  print pln(2, n) if n <= 100 else pln(1, n)
  return M(M(n + 11)) if n <= 100 else (n - 10)

def pln(levels, n):
  return 'M(' + str(n - 10) + ') since '+ str(n) +' is greater than 100' if levels == 1 else 'M(M(' + str(n + 11) + ')) since '+ str(n) +' is less than or equal to 100'
  

print M(int(sys.argv[1]))
