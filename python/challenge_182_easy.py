"""
Text formatting is big business. Every day we read information in one of several formats. Scientific publications often have their text split 
into two columns, like this. Websites are often bearing one major column and a sidebar column, such as Reddit itself. Newspapers very often 
have three to five columns. You've been commisioned by some bloke you met in Asda to write a program which, given some input text and some 
numbers, will split the data into the appropriate number of columns.

Formal Inputs and Outputs
=========================
Input Description
=================
To start, you will be given 3 numbers on one line:

  <number of columns> <column width> <space width>

  - number of columns: The number of columns to collect the text into.
  - column width: The width, in characters, of each column.
  - space width: The width, in spaces, of the space between each column.

After that first line, the rest of the input will be the text to format.

Output Description
==================
You will print the text formatted into the appropriate style.
You do not need to account for words and spaces. If you wish, cut a word into two, so as to keep the column width constant.

Sample Inputs and Outputs
=========================
Sample Input
============
Input file is available here. (NB: I promise this input actually works this time, haha.)

Sample Output
=============
Output, according to my solution, is available here. I completed the Extension challenge too - you do not have to account for longer words 
if you don't want to, or don't know how.

Extension
=========
Split words correctly, like in my sample output.
"""
import sys
import math

def split(text, n, cols, width, spaces):
  j = 0
  print n

  while j < n:
    i = j
    #print 'j=',i,
    while i < len(text):
      #sys.stdout.write('i=' + str(i) + ':')
      sys.stdout.write(text[i])
      #sys.stdout.write(' ')
      i += 1
      if i % width == 0:
        #print 'I = ', i,
        i += n - width
        sys.stdout.write(' ' * spaces)
    j += width
    print ''


text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
#split(text, 2, 20, 2)
text = 'foo bar biz baz'
cols = 2.
width = 4
spaces = 2
n = int(math.ceil(len(text) / cols))
split(text, n, cols, width, spaces)

