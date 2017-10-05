"""
Make a calculator that lets the user add, subtract, multiply and divide integers. It should allow exponents too. The user 
can only enter integers and must expect the result to be integers. The twist is that YOU, the programmer, can only let the 
program calculate expressions using addition. Only addition. The user can enter 3*2 however you cannot calculate it using 
multiplication.

Basically, the programmer is not allowed to multiply, divide and subtract using the operations provided by a programming 
language. To the programmer, the only accessible direct operation is addition.

Your calculator should be able to handle addition, subtraction, division, multiplication and exponents. No modulo 
operation (to obtain the remainder for two given operands) too.

Please note that
  - You are not allowed to use any functions (other than user-defined functions) to work with exponents. Basically, don't
    cheat by allowing pre-defined functions from a library for the dirty work.
  - You can use logical operators.
  - The only binary arithmetic operator that you can use is + (addition).
  - The only unary operator that you can use is ++ (increment operator).
  - No bitwise operations are allowed.

Input Description
=================
Allow the user to enter two integers and the operation symbol.
Let's use ^ for exponents i.e. 2^3 = 23 = 8

Output description
==================
If the answer is an integer, display the answer. If the answer is not an integer, display a warning message. Handle 
errors like 1/0 appropriately.

Challenge Inputs and Outputs
============================
Input    Output
12 + 25    37
-30 + 100    70
100 - 30    70
100 - -30    130
-25 - 29    -54
-41 - -10    -31
9 * 3    27
9 * -4    -36
-4 * 8    -32
-12 * -9    108
100 / 2    50
75 / -3    -25
-75 / 3    -25
7 / 3    Non-integral answer
0 / 0    Not-defined
5 ^ 3    125
-5 ^ 3    -125
-8 ^ 3    -512
-1 ^ 1    -1
1 ^ 1    1
0 ^ 5    0
5 ^ 0    1
10 ^ -3    Non-integral answer

Bonus
=====
Modify your program such that it works with decimals (except for ^ operation) with a minimum precision of 1 decimal place.

Simple grammar
==============
Expr = Factor Op Factor
Factor = Unary | digit+
Unary = '-' digit+
digit = [0-9]
"""

from functools import partial
from itertools import takewhile

tokens = None
idx = 0

add = lambda a, b: a + b
mul = lambda a, b: a if b == 1 else add(a, mult(a, b - 1))
div = lambda a, b, c=0: c if a <= 1 else div(sub(a, b), b, c + 1)
sub = lambda a, b: add(a, -b)
lit = lambda a: a
ops = [('+', add), ('*', mul), ('/', div), ('-', sub)]

def expr():
    exp = [factor(), op(), factor()]
    return exp[1](exp[0], exp[2])

def factor(): return unary() or literal()
def op():     return next((o[1] for o in ops if match(o[0])), False)
def unary():  return match('-') and -literal()

def match(expected):
    global tokens, idx
    if tokens[idx] == expected:
        idx += 1
        return expected
    else:
        return False

def literal():
    global tokens, idx
    n = [ t for t in takewhile(lambda c: c.isdigit(), tokens[idx:]) ]
    idx += len(n)
    return int(''.join(n))

def run(input):
    global tokens, idx
    idx = 0
    tokens = [t for t in list(input) if t != ' ']
    return expr()


assert run('12 + 25') == 37
assert run('-30 + 100') == 70
assert run('100 - 30') == 70


