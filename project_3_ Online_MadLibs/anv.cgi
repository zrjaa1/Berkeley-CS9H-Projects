# Script overview: this is a mad lib scrit which will interface with the web, get 2 nouns and 1 verb. Based on the template written in the file, it generates different interesting sentences.
# Input: login: http://inst.eecs.berkeley.edu/~cs199dru/index.html     
# Output: A funny sentence, refresh the page will cause a new sentence.

#!/usr/bin/python

import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

import random
a = random.randint(1,7)

x1 = form['adjectvie'].value
x2 = form['noun'].value
y = form['verb'].value

print 'Content-Type: text/html'
print

with open('template.dat','r') as f:
	sentence = f.readlines()

print sentence[a] %(x1,y,x2)  
