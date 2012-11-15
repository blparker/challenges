"""
Description:
Website URLs, or Uniform Resource Locators, sometimes embed important data or arguments to be used by the server. This entire string, which is a 
URL with a Query String at the end, is used to "GET#Request_methods)" data from a web server.

A classic example are URLs that declare which page or service you want to access. The Wikipedia log-in URL is the following:

    http://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page

Note how the URL has the Query String "?title=..", where the value "title" is "Special:UserLogin" and "returnto" is "Main+Page"?

Your goal is to, given a website URL, validate if the URL is well-formed, and if so, print a simple list of the key-value pairs! Note that URLs 
only allow specific characters (listed here) and that a Query String must always be of the form "<base-URL>[?key1=value1[&key2=value2[etc...]]]"

Formal Inputs & Outputs:
Input Description:
String GivenURL - A given URL that may or may not be well-formed.

Output Description:
If the given URl is invalid, simply print "The given URL is invalid". If the given URL is valid, print all key-value pairs in the following format:

    key1: "value1"
    key2: "value2"
    key3: "value3"
    etc...

Sample Inputs & Outputs:
    Given "http://en.wikipedia.org/w/index.php?title=Main_Page&action=edit", your program should print the following:
    title: "Main_Page"
    action: "edit"

Given "http://en.wikipedia.org/w/index.php?title= hello world!&action={invalid_char}", your program should print the following:

    The given URL is invalid

(To help, the last example is considered invalid because space-characters and unicode characters are not valid URL characters)

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
a b c d e f g h i j k l m n o p q r s t u v w x y z
0 1 2 3 4 5 6 7 8 9 - _ . ~
Reserved
Have to be encoded sometimes
! * ' ( ) ; : @ & = + $ , / ? % # [ ]

"""

import sys

def main(url):
    if is_valid(url) == False:
        print 'The given URL is invalid'
        sys.exit()

    key_pairs = dict([ p.split('=') for p in (url.split('?')[1]).split('&') ])
    for key, value in key_pairs.iteritems():
        print key + ': "' + value + '"'


def is_valid(url):
    chars = [ chr(c) for c in range(48, 58) + range(65, 123) + range(33, 48) if c != 34 ] + \
            [ ':', ';', '=', '?', '@', '[', ']', '_', '~' ]

    return reduce(lambda x, y: x and y, [ url[i] in chars for i in range(len(url)) ])


main(sys.argv[1])

