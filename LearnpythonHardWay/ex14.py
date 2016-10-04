#Exercise 14: Prompting and Passing

from sys import argv
script, name = argv
prompt = '> '

print "Hi %s, I'm the %s script." %(name,script)
print "I'd like to ask you a few questions."

print "Do you like me %s" %name
likes = raw_input(prompt)

print "Where do you live %s" %name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, So you said %r about liking me.
You live in %r . Not sure where it is.
And you have %r kind of computer.
""" %(likes,lives,computer)

