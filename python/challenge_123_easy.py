"""
A newline character is a special character in text for computers: though it is not a visual 
(e.g. renderable) character, it is a control character, informing the reader (whatever program 
that is) that the following text should be on a new line (hence "newline character").

As is the case with many computer standards, newline characters (and their rendering behavior) 
were not uniform across systems until much later. Some character-encoding standards (such as 
ASCII) would encode the character as hex 0x0A (dec. 10), while Unicode has a handful of 
subtly-different newline characters. Some systems even define newline characters as a set 
of characters: Windows-style new-line is done through two bytes: CR+LF (carriage-return and 
then the ASCII newline character).

Your goal is to read ASCII-encoding text files and "fix" them for the encoding you want. You 
may be given a Windows-style text file that you want to convert to UNIX-style, or vice-versa.

Input Description
=================
On standard input, you will be given two strings in quotes: the first will be the text file 
location, with the second being which format you want it output to. Note that this second 
string will always either be "Windows" or "Unix".

Windows line endings will always be CR+LF (carriage-return and then newline), while Unix endings 
will always be just the LF (newline character).


Output Description
==================
Simply echo the text file read back off onto standard output, with all line endings corrected.

"""

import sys

def mode(input):
  return 0 if input.lower() == "windows" else 1 if input.lower() == "unix" else -1


def run(input, mode):
  with open(input) as f:
    lines = [ l.rstrip("\r\n") + ["\r\n", "\n"][mode] for l in f.readlines() ] 
    print lines


run(sys.argv[1], mode(sys.argv[2]))


