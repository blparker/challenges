"""
Description
===========
You've been taking some classes at a local university. Unfortunately, your theory-of-under-water-basket-weaving professor is really boring. He's also
very nosy. In order to pass the time during class, you like sharing notes with your best friend sitting across the aisle. Just in case your professor
intercepts any of your notes, you've decided to encrypt them.

To make things easier for yourself, you're going to write a program which will encrypt the notes for you. You've decided a transposition cipher is probably
the best suited method for your purposes.

A transposition cipher is "a method of encryption by which the positions held by units of plaintext (which are commonly characters or groups of characters)
are shifted according to a regular system, so that the ciphertext constitutes a permutation of the plaintext" (En.wikipedia.org, 2018).

Specifically, we will be implementing a type of route cipher today. In a route cipher the text you want to encrypt is written out in a grid, and then arranged
in a given pattern. The pattern can be as simple or complex as you'd like to make it.

Task
====
For our purposes today, your program should be able to accommodate two input paramters: Grid Dimensions, and Clockwise or Counterclockwise Rotation. To make
things easier, your program need only support the Spiral route from outside to inside.

Example
=======
Take the following message as an example:

    WE ARE DISCOVERED. FLEE AT ONCE

Given inputs may include punctuation, however the encrypted text should not. Further, given text may be in all caps, all lower case, or a mix of the two.
The encrypted text must be in all caps.

You will be given dimensions in which to write out the letters in a grid. For example dimensions of:

    9, 3

Would result in 9 columns and 3 rows:

    W   E   A   R   E   D   I   S   C
    O   V   E   R   E   D   F   L   E
    E   A   T   O   N   C   E   X   X

As you can see, all punctuation and spaces have been stripped from the message.

For our cipher, text should be entered into the grid left to right, as seen above.

Encryption begins at the top right. Your route cipher must support a Spiral route around the grid from outside to the inside in either a clockwise or
counterclockwise direction.

For example, input parameters of clockwise and (9, 3) would result in the following encrypted output:

    CEXXECNOTAEOWEAREDISLFDEREV

Beginning with the C at the top right of the grid, you spiral clockwise along the outside, so the next letter is E, then X, and so on eventually yielding the
output above.

Input Description
=================
Input will be organized as follows:

    "string" (columns, rows) rotation-direction
.

Note: If the string does not fill in the rectangle of given dimensions perfectly, fill in empty spaces with an X

So,

    "This is an example" (6, 3)

becomes:

    T   H   I   S   I   S
    A   N   E   X   A   M
    P   L   E   X   X   X

Challenge Inputs
================
    "WE ARE DISCOVERED. FLEE AT ONCE" (9, 3) clockwise
    "why is this professor so boring omg" (6, 5) counter-clockwise
    "Solving challenges on r/dailyprogrammer is so much fun!!" (8, 6) counter-clockwise
    "For lunch let's have peanut-butter and bologna sandwiches" (4, 12) clockwise
    "I've even witnessed a grown man satisfy a camel" (9,5) clockwise
    "Why does it say paper jam when there is no paper jam?" (3, 14) counter-clockwise

Challenge Outputs
=================
    "CEXXECNOTAEOWEAREDISLFDEREV"
    "TSIYHWHFSNGOMGXIRORPSIEOBOROSS"
    "CGNIVLOSHSYMUCHFUNXXMMLEGNELLAOPERISSOAIADRNROGR"
    "LHSENURBGAISEHCNNOATUPHLUFORCTVABEDOSWDALNTTEAEN"
    "IGAMXXXXXXXLETRTIVEEVENWASACAYFSIONESSEDNAMNW"
    "YHWDSSPEAHTRSPEAMXJPOIENWJPYTEOIAARMEHENAR"

Bonus
=====
A bonus solution will support at least basic decryption as well as encryption.

Bonus 2
=======
Allow for different start positions and/or different routes (spiraling inside-out, zig-zag, etc.), or for entering text by a different pattern, such as
top-to-bottom.

References
En.wikipedia.org. (2018). Transposition cipher. [online] Available at: https://en.wikipedia.org/wiki/Transposition_cipher [Accessed 12 Feb. 2018].
"""



test = 'WE ARE DISCOVERED. FLEE AT ONCE'
cols, rows = (9, 3)

m = [[ 'X' for c in range(cols) ] for r in range(rows)]

#for i in range(len(test)):
    #print(i, test[i], i % rows, i % cols)

i, j = 0, 0

for c in test:
    if not c.isalpha(): continue

    #print(c, i, j % cols)
    m[i][j % cols] = c

    j += 1
    if j > 0 and j % cols == 0:
        i += 1

print(m)



tl, tr, bl, br = (0, 0), (0, 8), (2, 0), (2, 8)
i, j = tr

cipher = []

def left():
    global i, j, m
    print("Switching to left")
    while (i, j) != bl:
        cipher.append(m[i][j])
        j -= 1

def up():
    global i, j, m
    print("Switching to up")
    while (i, j) != tl:
        cipher.append(m[i][j])
        i -= 1

def right():
    global i, j, m
    print("Switching to right", tr)
    while (i, j) != tr:
        cipher.append(m[i][j])
        j += 1


def down():
    global i, j, br, cipher, m
    print("Switching to down")
    while (i, j) != br:
        cipher.append(m[i][j])
        i += 1


x = 0
n = cols * rows - 1

while len(cipher) < n:
    if (i, j) == br:
        left()
        br = (br[0] - 1, br[1] - 1)
        print('After down: ', cipher)
    elif (i, j) == bl:
        up()
        bl = (bl[0] - 1, bl[1] + 1)
        print('After up: ', cipher)
    elif (i, j) == tl:
        right()
        tl = (tl[0] + 1, tl[1] + 1)
        print('After right: ', cipher)
    elif (i, j) == tr:
        down()
        if x > 0:
            tr = (tr[0] + 1, tr[1] - 1)
        else:
            tr = (tr[0], tr[1] - 1)
        print('After down: ', cipher)
    x += 1

cipher.append(m[i][j])

print('#####')
print(''.join(cipher))

# iterate based on directions: down, left, up, right
#def down(i, j, to):
    #for x in range(i, to, -1):
        #print(i)


#down(0, 8, 0)



