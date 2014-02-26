"""
In this week's Easy challenge, series of words were disemvoweled into vowels, and non-vowel letters. 
Spaces were also removed. Your task today is, given the two strings produced via disemvowelment, 
output one possibility for the original string.

Your output must be such that if you put it through the solution to this week's Easy challenge, 
you'll recover exactly the input you were given.

You don't need to output the same string as the one that was originally disemvoweled, just some 
string that disemvowels to your input.

Use the Enable word list, or some other reasonable English word list. Every word in your output 
must appear in your word list.

For the sample inputs, all words in originally disemvoweled strings appear in Enable. In particular, 
I'm not using any words with punctuation, and I'm not using the word "a".

As before, ignore punctuation and capitalization.

Input description
=================
Two strings, one containing only non-vowel letters, and one containing only vowels.

Output description
==================
A space-separated series of words that could be disemvoweled into the input, each word of which must appear in your word list.

Sample Input 1
==============
wwllfndffthstrds
eieoeaeoi

Sample Output 1
===============
There are, in general, many correct outputs. Any of these is valid output for the sample input 
(using the Enable word list to verify words):

we wile lo fen daff et host rids 
we wile lo fend aff eths tor ids 
we wile lo fen daff the sot rids 
we will fend off eths tare do si 
we will fend off the asteroids

Sample Input 2
==============
bbsrshpdlkftbllsndhvmrbndblbnsthndlts
aieaeaeieooaaaeoeeaeoeaau

Sample Outputs 2
================
ab bise ars he ae pi ed look fa tab all sned hove me ar bend blob ens than adults 
ai be base rash pe die look fat bal la sned hove me ar bend blob ens than adults 
babies ae rash pe die loo ka fat balls end ho vee mar bend blob ens than adults 
babies rash pedal kef tie bolls nod aah ave omer bendable bones than adults 
babies are shaped like footballs and have more bendable bones than adults

Sample Input 3
==============
llfyrbsshvtsmpntbncnfrmdbyncdt
aoouiaeaeaoeoieeoieaeoe
"""
def load_words():
  with open('challenge_150_inter_word_list.txt') as f:
    words = { line.strip():0 for line in f.readlines() }
    f.close()
    return words


def run():
  consts = 'wwllfndffthstrds'
  vowels = 'eieoeaeoi'

  words = load_words()
  print words['we']

  for c in consts:
    for i, e in reversed(list(enumerate(vowels))):
      potential = c + vowels[0:i + 1]
      if potential in words:
        print "### ", potential
        break

if __name__ == '__main__':
  run()



