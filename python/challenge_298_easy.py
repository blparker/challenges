"""
Difficulty may be higher than easy,
  (((3))) is an expression with too many parentheses.

The rule for "too many parentheses" around part of an expression is that if removing matching parentheses around a section of text still leaves that 
section enclosed by parentheses, then those parentheses should be removed as extraneous.

  (3) is the proper stripping of extra parentheses in above example.

((a((bc)(de)))f) does not have any extra parentheses. Removing any matching set of parentheses does not leave a "single" parenthesesed group that was 
previously enclosed by the parentheses in question.

Inputs
======
((a((bc)(de)))f)  
(((zbcd)(((e)fg))))
ab((c))

Outputs
=======
((a((bc)(de)))f)  
((zbcd)((e)fg))
ab(c)

Bonus
=====
A 2nd rule of too many parentheses can be that parentheses enclosing nothing are not needed, and so should be removed. A/white space would not be nothing.

Inputs
======
  ()
  ((fgh()()()))
  ()(abc())

Outputs
=======
  NULL
  (fgh)
  (abc)

"""

#s = 'ab((c))'
s = '(((zbcd)(((e)fg))))'


def parse(s):
  st = []
  ast = []

  i = 0
  while i < len(s):
    c = s[i]
    st.append(c)

    if c is ')':
      a = st.pop()
      while c != '(':
        c = st.pop()
        print 'Popped C:', c
        a += c

      a = a[::-1]
      if a != '()':
        ast.append(a)

    i += 1

  r = ''.join([ c for c in st ])
  ast.append(r)
  print ast[::-1]

print parse(s)

"""
stack = []

for char in i:
  if char == '(':

    print "Open"
  elif char == ')':
    print "Close"
  else:
    print char
"""

