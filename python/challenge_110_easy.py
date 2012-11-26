"""
Description:
You and a friend are working on a very important, bleeding-edge, research paper: "Computational Complexity 
of Sorting Pictures of Cats with Funny Text on the Web". The catch though is your friend wrote his part 
of the paper with his hands shifted to the right, meaning the top row of keys he used weren't "QWERTYUIOP" 
(regular US keyboard), but instead "WERTYUIOP{".

Your goal is to take what your friend wrote, and convert it from his broken shifted text back into regular 
english!

Formal Inputs & Outputs:
Input Description:

String ShiftedText - The shifted text in question. The only chracters you have to deal with are letters, in 
both cases, and the following symbols: '{', '[', ':', ';', '<', ','. The space character may be present, 
but you do not have to shift that.

Output Description:
Print the correct text.

Sample Inputs & Outputs:

The string "Jr;;p ept;f" should shift back, through your function, into "Hello World". Another example 
is: "Lmiyj od ,u jrtp", which corrects to "Knuth is my hero"
"""

import sys

def main(input):
	print shift(input)


def shift(input):
	qwerty = ['q','w','e','r','t','y','u','i','o','p','{','[','a','s','d','f','g','h','j','k','l',':',
			  ';','z','x','c','v','b','n','m','<',',']
	ret = []
	for i in range(len(input)):
		if input[i].lower() in qwerty:
			if input[i].isupper():
				ret.append(qwerty[qwerty.index(input[i].lower()) - 1].upper())
			else:
				ret.append(qwerty[qwerty.index(input[i]) - 1])
		else:
			ret.append(input[i])
	print ret
	#print [ qwerty[qwerty.index(input[i].lower()) - 1] for i in range(len(input)) if input[i] in qwerty ]
	return ''


main(sys.argv[1])

